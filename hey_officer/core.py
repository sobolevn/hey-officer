# -*- coding: utf-8 -*-

import codecs
import sys

from hey_officer.checks.regex import RegexPlugin


class Checker(object):
    def __init__(self, config=None):
        self.config = config

    def run(self):
        checked_files = []

        for filename in self.config:
            checker = FileChecker(filename)
            checked_files.append(checker)
            checker.check_file()

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
        return [
            RegexPlugin,
        ]

    def _output_errors(self):
        self.errors.sort(key=lambda e: e.code)

        for error in self.errors:
            print(error.pretty(self.filename))

    def has_errors(self):
        return bool(self.errors)

    def check_file(self):
        with codecs.open(self.filename, 'r', 'utf-8') as f:
            contents = f.read()

        for plugin in self._detect_plugins():
            instance = plugin(self.config, contents)
            for error in instance:
                self.errors.append(error)

        self._output_errors()
