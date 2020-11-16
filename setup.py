#!/usr/bin/env python

from setuptools import setup
from Cython.Build import cythonize

setup(
    name='TheBB-TestPackage',
    version='1.0.0',
    maintainer='Eivind Fonn',
    maintainer_email='evfonn@gmail.com',
    packages=['thebb_testpackage'],
    ext_modules=cythonize('thebb_testextension.pyx'),
)
