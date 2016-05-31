# -*- coding:utf-8 -*-
from . import db

class ArticleDataBase(db.Model):
    __tablename__ = 'article_info'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(256))
    content = db.Column(db.String(10000))
    written_time = db.Column(db.String(32))
