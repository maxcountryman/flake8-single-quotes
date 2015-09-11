import os

import flake8_single_quotes as fsq


def test_get_noqa_lines():
    with open('tests/data/no_qa.py') as f:
        lines = f.readlines()
        assert fsq.get_noqa_lines(lines) == [2]


def test_wrapped():
    with open('tests/data/wrapped.py') as f:
        lines = f.readlines()
        assert list(fsq.get_double_quotes_errors(lines)) == []


def test_doubles():
    with open('tests/data/doubles.py') as f:
        lines = f.readlines()
        expected = [{'col': 24,
                     'line': 1,
                     'message': 'Q000 Strings should use single quotes.'}]
        assert list(fsq.get_double_quotes_errors(lines)) == expected


def test_noqa_doubles():
    abspath = os.path.abspath('tests/data/doubles_noqa.py')
    checker = fsq.QuoteChecker(None, abspath)
    assert list(checker.run()) == []
