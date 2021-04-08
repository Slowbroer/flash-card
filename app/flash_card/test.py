#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required


@flash_card.route('/test/', methods=['GET'])
@jwt_required()
def get_card_test():
    pass


@flash_card.route('/test/<card_id>', methods=['POST'])
@jwt_required()
def test_card(card_id):
    pass
