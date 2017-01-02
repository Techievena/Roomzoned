#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

os.listdir(os.path.join('Roomzoned'))

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

from Roomzoned import release

if __name__ == "__main__":
    setup(
        name = release.name,
        version = release.__version__,
        author = release.__author__,
        author_email = release.__email__,
        description = release.__description__,
        url = release.__url__,
        download_url = release.__download_url__,
        keywords='Roomzoned Game',
        packages = ['Roomzoned'],
        scripts = ['bin/Game.py'],
        license = 'Apache License',
        entry_points = {
            'console_scripts': [
            'Roomzoned = Game:main'
            ]
        },
        install_requires = ['nose'],
        #test_suite = 'nose.collector',
        #tests_require = ['nose>=0.10.1']
    )
