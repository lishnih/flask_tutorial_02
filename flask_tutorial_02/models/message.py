#!/usr/bin/env python
# coding=utf-8
# Stan 2018-10-10

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

import uuid
from datetime import datetime

from ..app import db
from . import StrType


class Message(db.Model):      # Rev. 2018-10-10
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)

    author = db.Column(db.String, nullable=False, default='')
    message = db.Column(db.String, nullable=False, default='')
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, \
        onupdate=datetime.utcnow)
    deleted = db.Column(db.Boolean, nullable=False, default=False)
