#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_jwt import jwt_required, current_identity
from app.model.flash_card import FlashCards, FlashCardBooks
from flask import request
from flask_json import json_response
from app import db
from service.sec import SecCheck


@flash_card.route('/card')
@jwt_required()
def card_list():
    book_id = request.args.get('book_id')
    page = int(request.args.get('page', 1))  # 获取页码
    per_page = int(request.args.get('per_page', 10))  # 获取页码

    user_id = current_identity.id
    print(user_id)
    book = FlashCardBooks.query.filter_by(id=book_id, user_id=user_id).first()
    if book is None:
        return json_response(status=404, msg="抽记卡本未找到，可能已经被删除了哦")

    # per_page = 10
    user_id = current_identity.id
    cards = FlashCards.query.\
        filter_by(user_id=user_id, book_id=book_id).\
        order_by(FlashCards.id.desc()).\
        paginate(page, per_page)
        # all()
        # paginate(page, per_page)

    items = []
    for card in cards.items:
        items.append({
            'id': card.id,
            'name': card.front
        })
    return json_response(data={
        'items': items,
        'page': cards.page,
        'per_page': cards.per_page,
        'pages': cards.pages,
        'total': cards.total
    })


@flash_card.route('/card/<id>', methods=['GET'])
@jwt_required()
def card_info(id):
    user_id = current_identity.id
    card = FlashCards.query.filter_by(id=id, user_id=user_id).first()
    if card is None:
        return json_response(status=404, msg="抽记卡未找到，可能已经被删除了哦")

    return json_response(data={
        'id': card.id,
        'front': card.front,
        'back': card.back
    })


@flash_card.route('/card', methods=['POST'])
@jwt_required()
def add_card():
    user_id = current_identity.id
    data = request.get_json()
    book_id = data.get('book_id')
    front = data.get("front")
    back = data.get("back")
    if len(front) > 100:
        return json_response(status=405, msg="前面不能超过100个字")
    if len(back) > 500:
        return json_response(status=405, msg="后面不能超过500个字")
    sec = SecCheck()
    if sec.check(front) is False or sec.check(back) is False:
        return json_response(status=405, msg="填写的内容涉及敏感内容，请修改后再提交")

    book = FlashCardBooks.query.filter_by(id=book_id, user_id=user_id).first()
    if book is None:
        return json_response(status=405)
    card_count = FlashCards.query.filter_by(book_id=book_id).count()
    if card_count > 500:
        return json_response(status=405, msg="每个抽记本的抽记卡数量最多只能为500个")

    card = FlashCards(
        book_id=book.id,
        user_id=user_id,
        front=front,
        back=back,
        type="text",
        known=0,
        known_time=0,
        check_time=0
    )
    db.session.add(card)
    db.session.commit()
    return json_response()


@flash_card.route('/card/<id>', methods=['POST'])
@jwt_required()
def update_card(id):
    user_id = current_identity.id
    data = request.get_json()
    book_id = data.get('book_id')
    front = data.get("front")
    back = data.get("back")
    if len(front) > 100:
        return json_response(status=405, msg="前面不能超过100个字")
    if len(back) > 500:
        return json_response(status=405, msg="后面不能超过500个字")
    sec = SecCheck()
    if sec.check(front) is False or sec.check(back) is False:
        return json_response(status=405, msg="填写的内容涉及敏感内容，请修改后再提交")

    card = FlashCards.query.filter_by(id=id, user_id=user_id).first()
    if card is None:
        return json_response(status=404, msg="抽记卡未找到，可能已经被删除了哦")
    if book_id:
        card.book_id = book_id
    if front:
        card.front = front
    if back:
        card.back = back
    db.session.commit()
    return json_response()


@flash_card.route("/card/<id>", methods=['DELETE'])
@jwt_required()
def delete_card(id):
    user_id = current_identity.id
    card = FlashCards.query.filter_by(id=id, user_id=user_id).first()
    if card is None:
        return json_response(status=404, msg="抽记卡未找到，可能已经被删除了哦")
    db.session.delete(card)
    db.session.commit()
    return json_response()


