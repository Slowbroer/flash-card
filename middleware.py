#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import redis_client
import requests


class Middleware(object):
    def __init__(self, old):
        self.old = old

    def __call__(self, *args, **kwargs):
        print(' the operation before the request ')
        ret = self.old(*args, **kwargs)
        print(' operation after request ')
        return ret
