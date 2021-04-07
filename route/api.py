#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import FlashCard
import requests, json
from flask import request
from manage import db
from app.model.user import User


@FlashCard.route('/')
def index():
    return "hello world"


@FlashCard.route('/auth/login')
def login():
    code = request.data['code']
    content = requests.get("https://api.weixin.qq.com/sns/jscode2session?appid=&secret=&js_code=" +
                 code + "&grant_type=authorization_code").content
    content_obj = json.loads(content)
    if content_obj['errcode'] == 0:
        union_id = content_obj['unionid']

    return "login success"


@FlashCard.route('/auth/logout')
def logout():
    return "logout success"

