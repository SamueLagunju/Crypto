#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from crypto import __version__
import pathlib

here = pathlib.Path(__file__).parent.resolve()
# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


# the setup
setup(
    name='crypto',
    version=__version__,
    description='An encrypting / decrypting utility for Windows/Linux.',
    long_description=long_description,
    url='https://github.com/SamueLagunju/Crypto',
    author='Samuel Oloruntoba Lagunju',
    author_email='taofsamuel@gmail.com',
    license='MIT',
    keywords='cryptography cross-platform tutorial',
    packages=find_packages(exclude=('docs', 'tests', 'env', 'crypto-runner.py')),
    include_package_data=True,
    install_requires=[
    ],
    extras_require={
        'dev': [],
        'docs': [],
        'testing': [],
    },
    classifiers=[],
)
