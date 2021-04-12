#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_json import json_response
from app import jwt
from flask import request
from flask_jwt import JWTError
from manage import app
from app.model.user import Users


@flash_card.route('/auth')
def login():
    data = request.get_json()
    username = data.get(app.config.get('JWT_AUTH_USERNAME_KEY'), None)
    password = data.get(app.config.get('JWT_AUTH_PASSWORD_KEY'), None)
    identity = jwt.authentication_callback(username, password)
    if identity:
        token = jwt.jwt_encode_callback(identity)
        return jwt.auth_response_callback(token, identity)
    raise JWTError('Bad Request', 'Invalid credentials')


@flash_card.route('/auth/test', methods=["POST"])
def login_test():
    identity = Users.query.filter_by(id=1).first()
    if identity:
        token = jwt.jwt_encode_callback(identity)
        return jwt.auth_response_callback(token, identity)
    raise JWTError('Bad Request', 'Invalid credentials')


@flash_card.route('/auth/logout')
def logout():
    pass
