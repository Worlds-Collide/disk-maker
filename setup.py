#!/usr/bin/env python
import sys
import os


try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup


setup(name='diskmaker',
      version=0.1,
      description='Create disks of planetesimals and embryos',
      author='Tom Barclay, Elisa Quintana',
      author_email='tom@tombarclay.com',
      url='https://github.com/Worlds-Collide/disk-maker',
      packages=['diskmaker'],
      install_requires=["numpy>=1.8"],
      )