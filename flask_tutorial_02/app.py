#!/usr/bin/env python
# coding=utf-8
# Stan 2016-06-07

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from . import config


app = Flask(__name__, static_url_path='')

app.config.from_object(config)
# app.config.from_pyfile('app.cfg')

db = SQLAlchemy(app)
