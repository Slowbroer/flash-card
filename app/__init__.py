#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
import requests, json


db = SQLAlchemy()
jwt = JWT()


def identity(payload):
    from app.model.user import User
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()


# 通过code来登陆
def authenticate(code, password):
    from app.model.user import User
    app_id = ''
    secret = ''
    print(code)
    content = requests.get(
        f"https://api.weixin.qq.com/sns/jscode2session"
        f"?appid={app_id}&secret={secret}&js_code={code}&grant_type=authorization_code"
    ).content
    content_obj = json.loads(content)
    if content_obj['errcode'] == 0:
        union_id = content_obj['unionid']
        open_id = content_obj['openid']
        user = User.query.filter_by(union_id=union_id).first()
        if user is None:
            user = User(union_id=union_id, open_id=open_id)
            db.session.add(user)
            db.session.commit()
        return user
    return None


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    jwt.identity_handler(identity)
    jwt.authentication_handler(authenticate)
    jwt.init_app(app)

    from .flash_card import flash_card as flash_card_blueprint
    app.register_blueprint(flash_card_blueprint, url_prefix='/flash_card')
    return app
