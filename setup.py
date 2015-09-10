import io
from setuptools import setup
import flake8_single_quotes


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.rst')

setup(name='flake8-single-quotes',
      author='Max Countryman',
      version=flake8_quotes.__version__,
      install_requires=['setuptools'],
      url='http://github.com/maxcountryman/flake8-single-quotes/',
      long_description=long_description,
      description='Flake8 linter for enforcing single quotes.',
      py_modules=['flake8_single_quotes'],
      test_suite='test',
      include_package_data=True,
      entry_points={'flake8.extension': ['flake8_sinle_quotes = flake8_single_quotes:QuoteChecker']},
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Software Development :: Quality Assurance'])
