#!/usr/bin/env python

from app import db
from .user import Users


class FlashCardBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # user = db.relationship('Users', backref=db.backref('posts', lazy=True))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class FlashCards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(10))
    # user = db.relationship('Users', backref=db.backref('posts', lazy=True))
    book_id = db.Column(db.Integer, db.ForeignKey('flash_card_books.id'), nullable=False)
    book = db.relationship('FlashCardBooks', backref=db.backref('posts', lazy=True))
    front = db.Column(db.String(255))
    back = db.Column(db.Text)
    known = db.Column(db.Integer, nullable=False)
    known_time = db.Column(db.Integer, nullable=False)
    check_time = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class CheckRecords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('flash_cards.id'), nullable=False)
    result = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    front = db.Column(db.Text)
    back = db.Column(db.Text)





