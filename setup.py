# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in venue_booking/__init__.py
from venue_booking import __version__ as version

setup(
	name='venue_booking',
	version=version,
	description='To book venues for events',
	author='TRidz',
	author_email='fadil@tridz',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
