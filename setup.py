# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ssirc-website',
    version='0.1',
    description='SSiRC website',
    author='Landon Rieger',
    author_email='landon.rieger@usask.ca',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask', 'bibtexparser'],
)
