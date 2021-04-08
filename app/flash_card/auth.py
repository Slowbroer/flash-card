#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_json import json_response
from manage import app
from app import jwt
from flask import request
from flask_jwt import JWTError


@flash_card.route('/auth')
def login():
    data = request.get_json()
    username = data.get(app.config.get('JWT_AUTH_USERNAME_KEY'), None)
    password = data.get(app.config.get('JWT_AUTH_PASSWORD_KEY'), None)
    identity = jwt.authentication_callback(username, password)
    if identity:
        return jwt.auth_response_callback(identity)
    raise JWTError('Bad Request', 'Invalid credentials')


@flash_card.route('/auth/logout')
def logout():
    pass
