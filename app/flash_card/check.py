#!/usr/bin/env python

from app.flash_card import flash_card
from flask_jwt import jwt_required, current_identity
from flask import request
from flask_json import json_response
from app.model.flash_card import FlashCardBooks, FlashCards, CheckRecords
from app import redis_client, db
import json
import time


@flash_card.route("/check/init", methods=['POST'])
@jwt_required()
def check_init():
    data = request.get_json()
    book_id = data.get("book_id")
    user_id = current_identity.id
    book = FlashCardBooks.query.filter_by(id=book_id, user_id=user_id).first()
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")
    init_check(book)
    # card = get_next_card(book)
    return json_response()


# can abandon
@flash_card.route("/check", methods=['GET'])
@jwt_required()
def flash_card_item():
    book_id = request.args.get('book_id')
    user_id = current_identity.id
    book = FlashCardBooks.query.filter_by(id=book_id, user_id=user_id).first()
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")
    card = get_next_card(book)
    return json_response(data=card)


@flash_card.route('/check/<card_id>', methods=['POST'])
@jwt_required()
def check_flask_card(card_id):
    data = request.get_json()
    result = data.get("result")  # known:  unknown:
    user_id = current_identity.id

    card = FlashCards.query.filter_by(id=card_id).first()
    if card is None:
        return json_response(status=404, msg="抽记卡未找到，可能已经被删除了哦")
    check_card(card, result)
    # next_card = get_next_card(user_id)
    return json_response()


def init_check(book: FlashCardBooks):
    book_id = book.id
    user_id = book.user_id
    cards = FlashCards.query.filter_by(book_id=book_id).order_by(
        FlashCards.check_time.asc(),
        FlashCards.known_time.asc(),
        FlashCards.known.asc()
    ).limit(20).all()
    if cards is None:
        return False

    redis_key = get_redis_key(user_id)
    redis_client.ltrim(redis_key, 1, 0)
    print(cards)
    for card in cards:
        card_data = json.dumps({
            "id": card.id,
            "front": card.front,
            "back": card.back
        })
        redis_client.rpush(redis_key, card_data)
    return True


def get_next_card(book: FlashCardBooks):
    user_id = book.user_id
    redis_key = get_redis_key(user_id)
    card_data = redis_client.lpop(redis_key)
    if card_data is None:
        return None
    card = json.loads(card_data)
    return card


def check_card(card: FlashCards, result: str):
    card_id = card.id
    user_id = card.user_id

    if result == "known":
        old_known = card.known
        card.known = old_known + 1
        card.known_time = int(time.time())
    else:
        redis_key = get_redis_key(user_id)
        card_data = json.dumps({
            "id": card.id,
            "front": card.front,
            "back": card.back
        })
        redis_client.rpush(redis_key, card_data)
    card.check_time = int(time.time())
    record = CheckRecords(user_id=user_id, card_id=card_id, result=result)
    db.session.add(record)
    db.session.commit()


def get_redis_key(user_id):
    return f"flash_card:{str(user_id)}:check"
