#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup


# Package meta-data.
NAME = "example_mlem_get_started"
DESCRIPTION = ""
VERSION = "0.0.0"
URL = ""
EMAIL = ""
AUTHOR = ""
REQUIRES_PYTHON = "==3.8.10"


def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(
    name=NAME,
    description=DESCRIPTION,
    version=VERSION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    **{}
)