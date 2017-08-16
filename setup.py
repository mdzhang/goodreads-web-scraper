#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def read_requires(file):
    with open(file) as reqs_txt:
        return [line for line in reqs_txt]


requirements = read_requires('requirements.txt')
test_requirements = read_requires('requirements_dev.txt')

setup(
    name='goodreads_web_scraper',
    version='0.1.0',
    description="Web scrapers for Goodreads pages",
    long_description=readme + '\n\n' + history,
    author="Michelle D Zhang",
    author_email='zhang.michelle.d@gmail.com',
    url='https://github.com/mdzhang/goodreads-web-scraper',
    packages=['goodreads_web_scraper'],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='goodreads_web_scraper',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='goodreads_web_scraper.tests',
    tests_require=test_requirements,
)
