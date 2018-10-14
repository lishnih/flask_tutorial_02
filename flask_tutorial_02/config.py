#!/usr/bin/env python
# coding=utf-8

import os

here = os.path.abspath(os.path.dirname(__file__))

APPLICATION_ROOT = '/'

CSRF_ENABLED = True
SECRET_KEY = 'your-secret-key'

# SQL Alchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(here, 'app.db'))
SQLALCHEMY_MIGRATE_REPO = os.path.join(here, 'db_repository')
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
