# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "manjaro_openapi"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Manjaro Openapi",
    author_email="oguz@manjaro.org",
    url="",
    keywords=["Swagger", "Manjaro"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['manjaro_openapi=manjaro_openapi.__main__:main']},
    long_description="""Manjaro openapi."""
)

