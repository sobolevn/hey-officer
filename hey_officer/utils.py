# -*- coding: utf-8 -*-

import os


def normalize_path(path, parent=os.curdir):
    separator = os.path.sep
    # NOTE(sigmavirus24): os.path.altsep may be None
    alternate_separator = os.path.altsep or ''
    if separator in path or (alternate_separator and
                             alternate_separator in path):
        path = os.path.abspath(os.path.join(parent, path))
    return path.rstrip(separator + alternate_separator)
