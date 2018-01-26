# -*- coding: utf-8 -*-


class Plugin(object):
    def __init__(self, config, contents):
        self.config = config
        self.contents = contents

    def __iter__(self):
        return iter(self.run_checks())

    def __next__(self):
        errors = self.run_checks()
        return next(errors)

    def run_checks(self):
        raise NotImplementedError('This method should be implemented')
