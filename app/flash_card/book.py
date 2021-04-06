#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import FlashCard
from app.middleware.auth.jwt import login_required


# Book list interface
@FlashCard.route("book")
@login_required
def book_list():
    pass


# Book info interface
@FlashCard.route("book/info")
@login_required
def book_info():
    pass
