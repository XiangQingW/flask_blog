#!/usr/bin/env python
# -*- coding:utf-8 -*-

# start from this file

import os

from app import create_app, db
from app.models import ArticlDataBase
from flask.ext.script import Manger, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manger(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app = app, db = db, ArticlDataBase = ArticlDataBase)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
