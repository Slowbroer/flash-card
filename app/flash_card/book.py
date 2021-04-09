#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required, current_identity
from app.model.flash_card import FlashCardBooks
from flask import request
from app import db


# Book list interface
@flash_card.route("/book", methods=['GET'])
@jwt_required()
def book_list():
    data = request.get_json()
    page = data.get('page', 1)
    per_page = 10
    user_id = current_identity.id
    # user_id = data.get('user')

    books = FlashCardBooks.query.\
        filter(user_id=user_id).\
        order_by(FlashCardBooks.created_at.desc()).\
        paginate(page, per_page)
    print(books)
    pass


# Book info interface
@flash_card.route("/book/<id>", methods=['GET'])
@jwt_required()
def book_info():
    pass


@flash_card.route("/book", methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()
    name = data.get('name')
    user_id = current_identity.id
    book = FlashCardBooks(name=name, user_id=user_id)
    db.session.add(book)
    db.session.commit()
    pass


@flash_card.route('/book/<id>', methods=['POST'])
@jwt_required()
def update_book():
    pass


@flash_card.route('/book', methods=['DELETE'])
@jwt_required()
def delete_book():
    pass
