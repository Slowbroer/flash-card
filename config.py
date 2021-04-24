#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime


class Config(object):

    APP_ENV = ''
    DEBUG = False
    JWT_AUTH_USERNAME_KEY = 'nickname'
    JWT_AUTH_PASSWORD_KEY = 'code'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # JWT_AUTH_URL_RULE = None
    WE_CHAT_APP_ID = os.environ.get('WE_CHAT_APP_ID')
    WE_CHAT_SECRET = os.environ.get('WE_CHAT_SECRET')

    JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=int(os.environ.get('JWT_TTL', 300)))

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_URL')

    REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
