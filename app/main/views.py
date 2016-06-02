# -*- coding:utf-8 -*-

from flask import render_template, session, redirect, url_for
from . import main
from .. import models
import untils
@main.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@main.route('/coding')
def coding():
    articles = models.ArticleDataBase.query.all()
    return render_template('coding.html', articles = articles)

@main.route('/photos')
def photos():
    cover = untils.Untils.get_albums()
    list_cover = []
    for item in cover:
        list_cover.append({'path':item, 'album':item[14:item.find('/', 15)]})   
    return render_template('photos.html', albums_cover=list_cover)

@main.route('/coding/<id>/')
def show_article(id):
    article_fill = models.ArticleDataBase.query.filter_by(id = id).first()
    return render_template('show_article.html', article_fill = article_fill)

@main.route('/photos/<album>')
def show_album(album):
    photos_in_album = untils.Untils.get_photos_in_album(album)
    return render_template('show_album.html')
