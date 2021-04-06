#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import FlashCard


# Book list interface
@FlashCard.route("book")
def book_list():
    pass


# Book info interface
@FlashCard.route("book/info")
def book_info():
    pass
