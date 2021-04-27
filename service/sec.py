#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import redis_client
import requests
from manage import app
import json


class SecCheck(object):
    def __init__(self):
        self.app_id = app.config.get('WE_CHAT_APP_ID')
        self.secret = app.config.get('WE_CHAT_SECRET')

    def check(self, content):
        token = self.__token()
        if token is None:
            return False
        app.logger.info(token)
        app.logger.info(f"https://api.weixin.qq.com/wxa/msg_sec_check?access_token={token}&content={content}")
        content = requests.post(
            url=f"https://api.weixin.qq.com/wxa/msg_sec_check?access_token={token}",
            json={"content": content}
        ).content
        app.logger.info(content)
        content_obj = json.loads(content)
        if 'errcode' not in content_obj or content_obj['errcode'] == 0:
            return True
        return False

    def __token(self):
        token = redis_client.get("wc_token")
        app.logger.info(token)
        if token is None:
            content = requests.get(f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential"
                                   f"&appid={self.app_id}&secret={self.secret}").content
            app.logger.info(content)
            content_obj = json.loads(content)
            if 'errcode' not in content_obj or content_obj['errcode'] == 0:
                token = content_obj['access_token']
                redis_client.set("wc_token", token, content_obj['expires_in'])
            else:
                return None
        else:
            token = str(token, "utf-8")
        return token

