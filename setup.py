#!/usr/bin/env python

from setuptools import setup, find_packages

#try:
#    import setuptools_git
#except ImportError:
#    print "WARNING!"
#    print "We need the setuptools-git package to be installed for"
#    print "some of the setup.py targets to work correctly."

PACKAGE = 'jjutils'
VERSION = '0.1'

setup(
    name = PACKAGE,
    version = VERSION,
    package_dir = {'': 'src'},
    packages = find_packages('src', exclude=['jjutils.tests',
                                             'jjutils.tests.*']),
    install_requires = [ #"librsync",
                         "requests",
                         "feedparser",
                         "ijson",
                         #"pysync",
                       ],
    entry_points = {"console_scripts":
                    ['utils:utils']},
    test_suite = "utilss.tests",
)
