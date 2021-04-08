#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    union_id = db.Column(db.String(50), unique=True, nullable=False)
    open_id = db.Column(db.String(50), unique=True, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

