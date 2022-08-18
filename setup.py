#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="webprobe",
    install_requires=[

        "cryptography>=2.8",
        "PySocks>=1.6.8",
        "cffi>=1.14.0",
        "quo>=2022.6",
        "Jinja2>=3.0.0",
        "certifi>=2017.4.17",
        "urllib3>=1.21.1",
        "cryptography>=2.8",
        "cffi>=1.14.0",
        "defusedxml>=0.7.0",
        "markupsafe>=2.0.0",
        "pyopenssl>=21.0.0",
        "idna>=2.5",
        "chardet>=3.0.2",
        "charset_normalizer~=2.0.0",
        "requests_ntlm>=1.1.0",
        "colorama>=0.4.4",
        "ntlm_auth>=1.5.0",
        "pyparsing>=2.4.7",
    ],

    package_data={

        # If any package contains *.txt files, include them:
        "webprobe": ["db/*.txt"]},
)
