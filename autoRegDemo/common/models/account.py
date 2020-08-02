# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db

class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    createTime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    remarks = db.Column(db.String(50))

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
