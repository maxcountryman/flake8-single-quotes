# -*- coding: utf-8 -*-
'''
Flake8-Single-Quotes
--------------------
A Flake8 extension to enforce single-quotes.

Links
`````
* `development version <https://github.com/maxcountryman/flake8-single-quotes>`_
'''
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

import flake8_single_quotes

setup_requires = ['pytest', 'tox']
install_requires = ['setuptools', 'tox']
tests_requires = ['pytest-cov', 'pytest-cache']


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict',
                          '--verbose',
                          '--tb=long',
                          '--cov', 'flake8_single_quotes.py',
                          '--cov-report', 'term-missing', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


ext_checker_str = 'flake8_single_quotes = flake8_single_quotes:QuoteChecker'

setup(name='flake8-single-quotes',
      author='Max Countryman',
      author_email='maxc@me.com',
      version=flake8_single_quotes.__version__,
      url='https://github.com/maxcountryman/flake8-single-quotes/',
      description='A Flake8 extension to enforce single-quotes.',
      long_description=__doc__,
      license='MIT',
      py_modules=['flake8_single_quotes'],
      entry_points={'flake8.extension': [ext_checker_str]},
      packages=find_packages(exclude=['tests']),
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Software Development :: Quality Assurance'],
      cmdclass={'test': PyTest},
      setup_requires=setup_requires,
      install_requires=install_requires,
      tests_require=tests_requires,
      extras_require={'test': tests_requires},
      zip_safe=False)
