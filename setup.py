#!/usr/bin/env/ python
from setuptools import setup
import os
import sys
import subprocess

# edit setup details here
name='python-git-package'
license='GNU GPLv3'
description='description'
url=''
author='Brecht Baeten'
author_email='brecht.baeten@gmail.com'
packages=['python_git_package']
install_requires=[]
classifiers = ['Programming Language :: Python :: 2.7']
version = '0.0.0'

changelog = ''


# run the setup command
setup(
	name=name,
	version=version,
	license=license,
	description=description,
	long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
	url=url,
	author=author,
	author_email=author_email,
	packages=packages,
	install_requires=install_requires,
	classifiers=classifiers,
    entry_points={'console_scripts': [
        'python-git-package=python_git_package:execute_from_command_line',
    ]},
)

#scripts=['python-git-package.py'],
