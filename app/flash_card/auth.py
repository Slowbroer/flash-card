#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.flash_card import flash_card


@flash_card.route('/auth/logout')
def logout():
    pass
