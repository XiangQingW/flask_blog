# -*- coding:utf-8 -*-

from flask import render_template, session, redirect, url_for
from . import main
import untils
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@main.route('/coding')
def coding():
    return render_template('coding.html')

@main.route('/wonderful_life')
def wonderful_life():
    cover = untils.Untils.get_albums()
    return render_template('wonderful_life.html', albums_cover=cover)
