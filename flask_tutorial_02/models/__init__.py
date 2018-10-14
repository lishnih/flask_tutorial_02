#!/usr/bin/env python
# coding=utf-8
# Stan 2018-09-29

from __future__ import (division, absolute_import,
                        print_function, unicode_literals)

from sqlalchemy.types import TypeDecorator, String


class StrType(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        return str(value)
