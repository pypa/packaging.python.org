#!/usr/bin/env python

import io

from setuptools import setup

# README into long description
with io.open('README.rst', encoding='utf-8') as readme_file:
    long_description = readme_file.read()


setup(
    name='pypa-theme',
    version='0.0.1',
    description='The Sphinx theme for PyPA projects',
    long_description=long_description,
    author='PyPA',
    author_email='distutils-sig@python.org',
    url='https://pypa.io',
    packages=['pypa_theme'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'pypa_theme = pypa_theme',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
