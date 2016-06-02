# -*- coding:utf-8 -*-

from app import db
from app.models import ArticleDataBase



def read_from_file(file_name):
    lines = open(file_name).readlines(2000)
    title = lines[0]
    content = ''.join(lines[1:])
    return title, content

def save_local(file_name):
    title, content = read_from_file(file_name)
    article = ArticleDataBase(title = title, content = content)
    db.session.add(article)
    db.session.commit()
    help(db.session.commit)


save_local(u'./local_file/2016_5_16_资治通鉴.data')
