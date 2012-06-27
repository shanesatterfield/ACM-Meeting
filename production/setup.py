#!/usr/bin/env python

from distutils.core import setup

setup(name='acm@thebeach',
      version='1.0',
      description='ACM Meeting Scripts',
      author='Shane Satterfield',
      author_email='dustyplant@gmail.com',
      url='http://csulb.acm.org',
      packages=['acm', 'acm.secret', 'acm.util', 'acm.model' ],
     )