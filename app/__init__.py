#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
import requests
import json
from flask_json import FlaskJSON, JsonError, json_response, as_json
from config import Config


db = SQLAlchemy()
jwt = JWT()


@jwt.authentication_handler
def authenticate(code, password):
    from app.model.user import User
    from manage import app
    app_id = app.config.get('WE_CHAT_APP_ID')
    secret = app.config.get('WE_CHAT_SECRET')

    content = requests.get(
        f"https://api.weixin.qq.com/sns/jscode2session"
        f"?appid={app_id}&secret={secret}&js_code={code}&grant_type=authorization_code"
    ).content
    app.logger.info(content)
    content_obj = json.loads(content)
    print(content_obj)
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


@jwt.identity_handler
def identity(payload):
    from app.model.user import User
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    FlaskJSON(app)

    from .flash_card import flash_card as flash_card_blueprint
    app.register_blueprint(flash_card_blueprint, url_prefix='/flash_card')
    return app
