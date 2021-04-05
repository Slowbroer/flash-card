#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import FlashCard


@FlashCard.route('/auth/login')
def login():
    return "login success"


@FlashCard.route('/auth/logout')
def logout():
    return "logout success"

