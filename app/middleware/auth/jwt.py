#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
from flask import g, request


# jwt 登陆中间件
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        pass
    return decorated_function

