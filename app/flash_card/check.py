#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required


@flash_card.route("/check")
def flash_card_item():
    pass


@flash_card.route('/check/{card_id}')
def check_flask_card():
    pass
