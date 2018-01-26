# -*- coding: utf-8 -*-
# TODO(@sobolevn): implement filename plugin to check for filenames like:
# .crt, .key, .pem, id_rsa, .pub


regexes = {
    #"Internal subdomain": re.compile('([a-z0-9]+[.]*supersecretinternal[.]com)'),
    "Slack Token": re.compile('(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})'),
    "RSA private key": re.compile('-----BEGIN RSA PRIVATE KEY-----'),
    "SSH (OPENSSH) private key": re.compile('-----BEGIN OPENSSH PRIVATE KEY-----'),
    "SSH (DSA) private key": re.compile('-----BEGIN DSA PRIVATE KEY-----'),
    "SSH (EC) private key": re.compile('-----BEGIN EC PRIVATE KEY-----'),
    "PGP private key block": re.compile('-----BEGIN PGP PRIVATE KEY BLOCK-----'),
    "Certificate": '-----BEGIN CERTIFICATE-----',
    "AWS API Key": '',
    "Heroku API Key": '',
    "Generic Secret": re.compile('[s|S][e|E][c|C][r|R][e|E][t|T].*[\'|"][0-9a-zA-Z]{32,45}[\'|"]'),
}

STRING_VALS = (
    (
        'aws_secret_key',
        'Amazon Web Services secret key',
        (
            re.compile(r'(\'|")[A-Za-z0-9\\\+]{40}(\'|")'),
            re.compile(r'(\b|_)AWS(\b|_)', re.IGNORECASE)
        ),
        all
    ),
)

LINE_VALS = (
    (
        'diff',
        'Possible SCM diff in code',
        (
            re.compile(r'^<<<<<<< .*$'),
            re.compile(r'^>>>>>>> .*$')
        ),
    ),
    (
        'ssh_rsa_private_key',
        'Possible SSH private key',
        re.compile(r'^-{5}(BEGIN|END)\s+RSA\s+PRIVATE\s+KEY-{5}$')
    ),
    (
        'ssh_rsa_public_key',
        'Possible SSH public key',
        re.compile(r'^ssh-rsa\s+AAAA[0-9A-Za-z+/]+[=]{0,3}\s*([^@]+@[^@]+)?$')
    ),
)

t = r'(\b|[A-Z0-9_]*_)(SECRET|PASSWORD)(_[A-Z0-9_]*|\b)\s*=\s[\'"][^\'"]+[\'"]'
VAR_NAMES = (
    (
        'password',
        'Possible hardcoded password',
        re.compile(r'(\b|[A-Z0-9_]*_)PASSWORD(_[A-Z0-9_]*|\b)\s*=\s(\'|")[^\'"]+(\'|")')
    ),
    (
        'secret',
        'Possible hardcoded secret key',
        re.compile(r'')
    ),
)
