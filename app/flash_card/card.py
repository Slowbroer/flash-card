#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required


@flash_card.route('/card')
@jwt_required
def card_list():
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


