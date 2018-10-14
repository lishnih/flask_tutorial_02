#!/usr/bin/env python
# coding=utf-8
# Stan 2018-07-09

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

import sys

from werkzeug.wsgi import DispatcherMiddleware

from ..app import app


py_version = sys.version_info[:2]
PY2 = py_version[0] == 2


if app.config["APPLICATION_ROOT"] != '/':
    def simple(env, resp):
        resp(b'200 OK', [(b'Content-Type', b'text/plain')])
        return [b'Hello WSGI World\n']

    app.wsgi_app = DispatcherMiddleware(simple, {
        app.config["APPLICATION_ROOT"]: app.wsgi_app,
    })
