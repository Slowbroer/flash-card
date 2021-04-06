#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def create_app():
    app = Flask(__name__)

    from .flash_card import FlashCard as FlashCardBlueprint
    app.register_blueprint(FlashCardBlueprint, url_prefix='/flash_card')
    return app
