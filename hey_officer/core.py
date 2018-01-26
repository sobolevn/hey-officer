# -*- coding: utf-8 -*-

import codecs
import sys
import os

from hey_officer.checks.regex import RegexPlugin
from hey_officer.utils import normalize_path


class Checker(object):
    def __init__(self, config=None):
        self.config = config

    def _files(self, paths):
        if not isinstance(paths, (tuple, list)):
            paths = (paths, )

        for path in paths:
            path = normalize_path(path)

            for root, _, files in os.walk(path):
                for filename in files:
                    yield os.path.join(root, filename)

    def run(self):
        checked_files = []

        # TODO(@sobolevn): create Config class, with fields:
        # ignore
        # paths
        # reporter
        for filename in self._files(self.config):
            # TODO(@sobolevn): use mime guessing to ignore binary files.
            checker = FileChecker(filename)
            checked_files.append(checker)
            checker.check_file()

        # TODO(@sobolevn): move to Reporter class
        if any(c.has_errors() for c in checked_files):
            print('\nFailed!')
            sys.exit(1)
        else:
            print('\nAll good!')


class FileChecker(object):
    def __init__(self, filename, config=None):
        self.config = config
        self.filename = filename
        self.errors = []

    def _detect_plugins(self):
        # TODO(@sobolevn): make these plugins auto-discoverable:
        return [
            RegexPlugin,
        ]

    def _output_errors(self):
        self.errors.sort(key=lambda e: e.code)

        for error in self.errors:
            # TODO(@sobolevn): create Reporter class to create pretty reports.
            # We would also need to support `JsonReporter`.
            print(error.pretty(self.filename))

    def has_errors(self):
        return bool(self.errors)

    def check_file(self):
        with codecs.open(self.filename, 'r', 'utf-8') as f:
            # TODO(@sobolevn): try to read file line by line
            contents = f.read()

        for plugin in self._detect_plugins():
            instance = plugin(self.config, contents)
            for error in instance:
                self.errors.append(error)

        self._output_errors()
