#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required
from flask import request
from flask_json import json_response
from app.model.flash_card import FlashCardBooks, FlashCards
from app import redis_client
import json


@flash_card.route("/check")
@jwt_required()
def flash_card_item():
    data = request.get_json()
    book_id = data.get("book_id")
    book = FlashCardBooks.query.filter(id=book_id).first()
    if book is None:
        return json_response(status=404, msg="the book is not found")
    # get a random card
    card_data = redis_client.lpop()
    card = json.dumps(card_data)
    return json_response(data=card)


@flash_card.route('/check/<card_id>')
@jwt_required()
def check_flask_card(card_id):
    data = request.get_json()
    result = data.get("result")  # known:  unknown:
    pass
