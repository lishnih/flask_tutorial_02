#!/usr/bin/env python
# coding=utf-8
# Stan 2016-07-13

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

import time
import json
from datetime import datetime

from flask import request

from ..app import db


class HttpRequest(db.Model):  # Rev. 2018-09-29
    __tablename__ = 'http_requests'

    id = db.Column(db.Integer, primary_key=True)
    remote_addr = db.Column(db.String)  # request property
    url = db.Column(db.String)          # request property
    method = db.Column(db.String)       # request property
    endpoint = db.Column(db.String)     # request property, sometimes is None
    status = db.Column(db.Integer)      # response property
    user = db.Column(db.Integer, nullable=False, default='0')
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Float)
    values = db.Column(db.Text, nullable=False, default='')

    def __init__(self):
        self._start = time.time()

        self.remote_addr = request.remote_addr
        self.url = request.url
        self.method = request.method
        self.endpoint = request.endpoint


db.create_all()
