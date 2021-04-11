#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
import requests
import json
from flask_json import FlaskJSON, JsonError, json_response, as_json
from config import Config
from flask_redis import FlaskRedis


db = SQLAlchemy()
jwt = JWT()
redis_client = FlaskRedis()


@jwt.authentication_handler
def authenticate(code, password):
    from app.model.user import Users
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
    if 'errcode' not in content_obj:
        # union_id = content_obj['unionid']
        open_id = content_obj['openid']
        user = Users.query.filter_by(open_id=open_id).first()
        if user is None:
            user = Users(open_id=open_id)
            db.session.add(user)
            db.session.commit()
        return user
    return None


@jwt.identity_handler
def identity(payload):
    from app.model.user import Users
    user_id = payload['identity']
    return Users.query.filter_by(id=user_id).first()


@jwt.auth_response_handler
def auth_response(access_token, identity_instance):
    print(access_token)
    return json_response(data={'token': bytes.decode(access_token)})


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    FlaskJSON(app)
    redis_client.init_app(app)

    from .flash_card import flash_card as flash_card_blueprint
    app.register_blueprint(flash_card_blueprint, url_prefix='/flash_card')
    return app
