#!/usr/bin/env python
# coding=utf-8

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

import sys


__pkgname__ = __name__
__description__ = "Simple package based on Flask"
__version__ = "0.1"


py_version = sys.version_info[:2]
PY2 = py_version[0] == 2
