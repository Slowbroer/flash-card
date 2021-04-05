#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)

    from .flash_card import WeChat as WeChatBlueprint
    app.register_blueprint(WeChatBlueprint, url_prefix='/WeChat')
    return app