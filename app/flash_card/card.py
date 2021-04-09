#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required, current_identity
from app.model.flash_card import FlashCards
from flask import request


@flash_card.route('/card')
@jwt_required
def card_list():
    data = request.get_json()
    page = data.get('page', 1)
    per_page = 10
    user_id = current_identity.id
    cards = FlashCards.query.\
        filter(user_id=user_id).\
        order_by(FlashCards.created_at.desc()).\
        paginate(page, per_page)
    print(cards)
    pass


@flash_card.route('/card/<card_id>', methods=['GET'])
@jwt_required
def card_info(card_id):
    print(card_id)
    pass


@flash_card.route('/card', methods=['POST'])
@jwt_required
def add_card():
    pass


@flash_card.route('/card/<card_id>', methods=['POST'])
@jwt_required()
def update_card(card_id):
    print(card_id)


@flash_card.route("/card/<card_id>", methods=['DELETE'])
@jwt_required()
def delete_card(card_id):
    print(card_id)
    pass


