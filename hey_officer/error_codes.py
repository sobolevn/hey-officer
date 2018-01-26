# -*- coding: utf-8 -*-
# TODO(@sobolevn): create errors for files and entropy


class _BaseSecurityError(Exception):
    code = None
    message = None

    def __init__(self, match):
        self.match = match

    def pretty(self):
        raise NotImplementedError('This method should be implemented')


class SecretError(_BaseSecurityError):
    code = 'ho100'


class ApiKeyError(_BaseSecurityError):
    code = 'ho101'
    message = '{code}: Found an API key at {filename}:{startpos}:{endpos}'

    def pretty(self, filename):
        return self.message.format(
            code=self.code,
            filename=filename,
            startpos=self.match.start(),
            endpos=self.match.end(),
        )


class OAuthTokenError(_BaseSecurityError):
    code = 'ho102'
    message = '{code}: Found an OAuth token at {filename}:{startpos}:{endpos}'

    def pretty(self, filename):
        return self.message.format(
            code=self.code,
            filename=filename,
            startpos=self.match.start(),
            endpos=self.match.end(),
        )


class PrivateKeyError(_BaseSecurityError):
    code = 'ho103'


class PublicKeyError(_BaseSecurityError):
    code = 'ho104'


class CertificateError(_BaseSecurityError):
    code = 'ho105'


class FilenameError(_BaseSecurityError):
    code = 'ho200'
