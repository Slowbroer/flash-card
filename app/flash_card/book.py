#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required


# Book list interface
@flash_card.route("/book")
@jwt_required()
def book_list():
    pass


# Book info interface
@flash_card.route("/book/info")
@jwt_required()
def book_info():
    pass
