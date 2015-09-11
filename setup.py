# -*- coding: utf-8 -*-
'''
Flake8-Single-Quotes
--------------------
A Flake8 extension to enforce single-quotes.

Links
`````
* `development version
<https://github.com/maxcountryman/flake8-single-quotes>`_
'''

from setuptools import setup

import flake8_single_quotes


ext_checker_str = 'flake8_single_quotes = flake8_single_quotes:QuoteChecker'

setup(name='flake8-single-quotes',
      author='Max Countryman',
      author_email='maxc@me.com',
      version=flake8_single_quotes.__version__,
      install_requires=['setuptools'],
      url='http://github.com/maxcountryman/flake8-single-quotes/',
      long_description=__doc__,
      description='A Flake8 extension to enforce single-quotes.',
      py_modules=['flake8_single_quotes'],
      test_suite='test',
      include_package_data=True,
      entry_points={'flake8.extension': [ext_checker_str]},
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Topic :: Software Development :: Quality Assurance'],
      zip_safe=False)
