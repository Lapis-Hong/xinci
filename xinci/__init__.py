#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/18
"""This package contains interfaces and functionality to xinci. """
# from __future__ import absolute_import
from __future__ import unicode_literals

from .dictionary import Dictionary
from .word_extraction import extract


__version__ = '1.2.0'

__all__ = [Dictionary, extract]


# if len(logger.handlers) == 0:  # To ensure reload() doesn't add another one
#     logger.addHandler(logging.NullHandler())






