#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Config(object):

    APP_ENV = ''
    DEBUG = False
    JWT_AUTH_USERNAME_KEY = 'code'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # JWT_AUTH_URL_RULE = None
    WE_CHAT_APP_ID = os.environ.get('WE_CHAT_APP_ID')
    WE_CHAT_SECRET = os.environ.get('WE_CHAT_SECRET')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_URL')
