#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import FlashCard


@FlashCard.route('/card')
def card_list():
    pass


@FlashCard.route('/card/<card_id>', methods=['GET'])
def card_info(card_id):
    print(card_id)
    pass


@FlashCard.route('/card', methods=['POST'])
def add_card():
    pass


@FlashCard.route('/card/<card_id>', methods=['POST'])
def update_card(card_id):
    print(card_id)


@FlashCard.route("/card/<card_id>", methods=['DELETE'])
def delete_card(card_id):
    print(card_id)
    pass


