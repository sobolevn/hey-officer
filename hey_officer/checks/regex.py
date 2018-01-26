# -*- coding: utf-8 -*-
# TODO(@sobolevn): implement checks for certificates and general secrets

import re

from hey_officer.error_codes import ApiKeyError, OAuthTokenError
from hey_officer.plugin import Plugin


def _word_query(identity, query):
    pattern = r'(\b|[A-Z0-9_]*_){}(_[A-Z0-9_]*|\b)\s*=\s*[\'"]{}[\'"]'.format(
        identity,
        query,
    )
    return re.compile(pattern)

OAUTH_CHECKS = (
    re.compile(r'facebook.*[\'"][0-9a-f]{32}[\'"]', re.I),
    re.compile(r'twitter.*[\'"][0-9a-z]{35,44}[\'"]', re.I),
    re.compile(r'github.*[\'"][0-9a-z]{35,40}[\'"]', re.I),
)

API_KEYS_CHECKS = (
    re.compile(r'heroku.*[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}', re.I),
    re.compile(r'akia[0-9a-z]{16}', re.I),  # Amazon
    re.compile(r'xox[pboa]-([0-9]{12}-){3}[a-z0-9]{32}', re.I),  # Slack
)


class RegexPlugin(Plugin):
    def run_checks(self):
        for check in OAUTH_CHECKS:
            found = check.search(self.contents)
            if found:
                yield OAuthTokenError(found)

        for check in API_KEYS_CHECKS:
            found = check.search(self.contents)
            if found:
                yield ApiKeyError(found)
