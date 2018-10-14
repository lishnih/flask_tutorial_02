#!/usr/bin/env python
# coding=utf-8
# Stan 2018-09-07

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

from ..app import app


app_root = app.config["APPLICATION_ROOT"]
if app_root != '/':
    @app.context_processor
    def inject_app_root():
        return dict(app_root = app.config["APPLICATION_ROOT"])
