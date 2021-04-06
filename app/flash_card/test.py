#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import FlashCard


@FlashCard.route('/test/', methods=['GET'])
def get_card_test():
    pass


@FlashCard.route('/test/<card_id>', methods=['POST'])
def test_card(card_id):
    pass
