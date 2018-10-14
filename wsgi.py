#!/usr/bin/env python
# coding=utf-8
# Stan 2016-04-24

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

import logging
logging.basicConfig(level=logging.INFO)

from flask_tutorial_02.main import app


if __name__ == '__main__':
    app.run(host='0.0.0.0')
