#!/usr/bin/env python
# coding=utf-8
# Stan 2016-07-13

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

import time

from flask import request, g

from ..app import app, db
from ..models.http_request import HttpRequest


# ===== Interface =====

@app.before_request
def before_request():
    if request.endpoint not in ['static']:
        g.record = HttpRequest()
        db.session.add(g.record)
        db.session.commit()


@app.after_request
def after_request(response):
    if 'record' in g:
        g.record.duration = time.time() - g.record._start
        g.record.status = response.status_code
        db.session.commit()

    return response
