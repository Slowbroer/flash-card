#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required, current_identity
from flask import request
from flask_json import json_response
from app.model.flash_card import FlashCardBooks, FlashCards, CheckRecords
from app import redis_client, db
import json


@flash_card.route("/check/init", methods=['POST'])
@jwt_required()
def check_init():
    data = request.get_json()
    book_id = data.get("book_id")
    user_id = current_identity.id
    book = FlashCardBooks.query.filter_by(id=book_id, user_id=user_id).first()
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")
    cards = FlashCards.query.filter_by(book_id=book_id).all()
    redis_key = "flask_card:" + str(user_id) + ":check"
    redis_client.ltrim(redis_key, 1, 0)
    for card in cards:
        card_data = json.dumps({
            "id": card.id,
            "front": card.front,
            "back": card.back
        })
        redis_client.rpush(redis_key, card_data)
    return json_response()


@flash_card.route("/check", methods=['GET'])
@jwt_required()
def flash_card_item():
    data = request.get_json()
    book_id = data.get("book_id")
    user_id = current_identity.id
    book = FlashCardBooks.query.filter_by(id=book_id, user_id=user_id).first()
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")
    # get a random card
    redis_key = "flask_card:" + str(user_id) + ":check"
    card_data = redis_client.lpop(redis_key)
    if card_data is None:
        return json_response(status=404)
    card = json.loads(card_data)
    return json_response(data=card)


@flash_card.route('/check/<card_id>', methods=['POST'])
@jwt_required()
def check_flask_card(card_id):
    data = request.get_json()
    result = data.get("result")  # known:  unknown:
    user_id = current_identity.id
    record = CheckRecords(user_id=user_id, card_id=card_id, result=result)
    db.session.add(record)
    db.session.commit()
    return json_response()
