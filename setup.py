#!/usr/bin/env python

import os.path
from setuptools import setup, find_packages


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


#
# REQUIREMENTS
#
def parse_requirements(requirements):

    return [
        r.strip()
        for r in requirements
        if (
            not r.strip().startswith('#') and
            not r.strip().startswith('-e') and
            r.strip())
    ]


with open(os.path.join(BASE_DIR, 'requirements.txt')) as f:
    requirements = parse_requirements(f.readlines())


setup(
    name='szczypiorek',
    description=(
        'Szczypiorek environment management for humans.'),
    version='1.0.10',
    url='https://github.com/cosphere-org/szczypiorek',
    author='CoSphere Tech',
    author_email='contact@cosphere.org',
    packages=find_packages(),
    data_files=[(
        '',
        [
            'requirements.txt',
            'README.md',
        ],
    )],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        szczypiorek=szczypiorek.cli:cli
    ''',
    install_requires=requirements,
    keywords=['szczypiorek', 'environment', 'secrets'],
    classifiers=[])
