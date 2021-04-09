#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card
from flask_json import json_response


@flash_card.route('/test', methods=['GET'])
def get_card_test():
    return json_response(data={'token': "123456"})
    pass


