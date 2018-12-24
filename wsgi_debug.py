#!/usr/bin/env python
# coding=utf-8
# Stan 2016-04-24

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

import logging
logging.basicConfig(level=logging.DEBUG)

from flask_tutorial_02.app import app

app.debug = True

from flask_tutorial_02 import main


if __name__ == '__main__':
    app.run()
#   app.run(host='0.0.0.0', ssl_context='adhoc', debug=True)
