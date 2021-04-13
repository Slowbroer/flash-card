#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required, current_identity
from app.model.flash_card import FlashCardBooks
from flask import request
from app import db
from flask_json import json_response
from flask_sqlalchemy import Pagination


# Book list interface
@flash_card.route("/book", methods=['GET'])
@jwt_required()
def book_list():
    user_id = current_identity.id
    # user_id = data.get('user')

    items = []
    books = FlashCardBooks.query.\
        filter_by(user_id=user_id).\
        order_by(FlashCardBooks.id.desc()).\
        all()
        # paginate(page, per_page)

    for book in books:
        items.append({
            'id': book.id,
            'name': book.name
        })
    return json_response(data={
        'items': items
    })


# Book info interface
@flash_card.route("/book/<id>", methods=['GET'])
@jwt_required()
def book_info(id):
    user_id = current_identity.id
    book = FlashCardBooks.query.filter_by(id=id, user_id=user_id).first()
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")

    return json_response(data={
        "id": book.id,
        "name": book.name
    })
    pass


@flash_card.route("/book", methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()
    name = data.get('name')
    user_id = current_identity.id
    # user_id = data.get('user')
    book = FlashCardBooks(name=name, user_id=user_id)
    db.session.add(book)
    db.session.commit()
    return json_response()


@flash_card.route('/book/<id>', methods=['POST'])
@jwt_required()
def update_book(id):
    book = FlashCardBooks.query.filter_by(id=id).first()
    user_id = current_identity.id
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")
    if book.user_id != user_id:
        return json_response(status=405)
    data = request.get_json()
    name = data.get('name')
    book.name = name
    db.session.commit()
    return json_response()


@flash_card.route('/book/<id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    book = FlashCardBooks.query.filter_by(id=id).first()
    user_id = current_identity.id
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")
    if book.user_id != user_id:
        return json_response(status=405)
    pass

