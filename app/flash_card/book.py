#!/usr/bin/env python

from app.flash_card import flash_card
from flask_jwt import jwt_required, current_identity
from app.model.flash_card import FlashCardBooks, FlashCards
from flask import request
from app import db
from flask_json import json_response
from flask_sqlalchemy import Pagination
from service.sec import SecCheck


# Book list interface
@flash_card.route("/book", methods=['GET'])
@jwt_required()
def book_list():
    user_id = current_identity.id
    page = int(request.args.get('page', 1))  # 获取页码
    per_page = int(request.args.get('per_page', 10))  # 获取页码
    # user_id = data.get('user')

    items = []
    books = FlashCardBooks.query.\
        filter_by(user_id=user_id).\
        order_by(FlashCardBooks.id.desc()). \
        paginate(page, per_page)
        # all()
        # paginate(page, per_page)

    for book in books.items:
        items.append({
            'id': book.id,
            'name': book.name
        })
    return json_response(data={
        'items': items,
        'page': books.page,
        'per_page': books.per_page,
        'pages': books.pages,
        'total': books.total
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
    if len(name) > 100:
        return json_response(status=405, msg="名字不能超过100个字")
    sec = SecCheck()
    if sec.check(name) is False:
        return json_response(status=405, msg="填写的内容涉及敏感内容，请修改后再提交")
    user_id = current_identity.id
    book_count = FlashCardBooks.query.filter_by(user_id=user_id).count()
    if book_count > 10:
        return json_response(status=405, msg="每个人的抽记本数量最多只能为10个")
    # user_id = data.get('user')
    book = FlashCardBooks(name=name, user_id=user_id)
    db.session.add(book)
    db.session.commit()
    return json_response()


@flash_card.route('/book/<id>', methods=['POST'])
@jwt_required()
def update_book(id):
    data = request.get_json()
    name = data.get('name')
    if len(name) > 100:
        return json_response(status=405, msg="名字不能超过100个字")
    sec = SecCheck()
    if sec.check(name) is False:
        return json_response(status=405, msg="填写的内容涉及敏感内容，请修改后再提交")

    book = FlashCardBooks.query.filter_by(id=id).first()
    user_id = current_identity.id
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")
    if book.user_id != user_id:
        return json_response(status=405)

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
    cards = FlashCards.query.filter_by(book_id=id).all()
    try:
        for card in cards:
            db.session.delete(card)
        db.session.delete(book)
        db.session.commit()
        return json_response()
    except Exception:
        db.session.rollback()
        return json_response(status=500)


