#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import FlashCard
from app.middleware.auth.jwt import login_required


@FlashCard.route('/card')
@login_required
def card_list():
    pass


@FlashCard.route('/card/<card_id>', methods=['GET'])
@login_required
def card_info(card_id):
    print(card_id)
    pass


@FlashCard.route('/card', methods=['POST'])
@login_required
def add_card():
    pass


@FlashCard.route('/card/<card_id>', methods=['POST'])
@login_required
def update_card(card_id):
    print(card_id)


@FlashCard.route("/card/<card_id>", methods=['DELETE'])
@login_required
def delete_card(card_id):
    print(card_id)
    pass


