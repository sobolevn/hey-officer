#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

REQUIRED = []

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is
# present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='hey-officer',
    version='0.0.1',
    description=(
        'Customs officer detects secret values inside your files '
        'and prevents secrets from being leaked'
    ),
    long_description=long_description,
    author='Nikita Sobolev',
    author_email='mail@sobolenv.me',
    url='https://github.com/sobolevn/hey-officer',

    packages=find_packages(exclude=('tests', )),

    install_requires=REQUIRED,
    include_package_data=True,

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='',

    entry_points={
        'console_scripts': [
            'hey-officer=hey_officer.cli:main',
        ],
    },
)
