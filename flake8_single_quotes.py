import sys
import tokenize

__version__ = '0.1.0'

NOQA = 'noqa'


class QuoteChecker(object):
    name = __name__
    version = __version__

    def __init__(self, tree, filename='(none)', builtins=None):
        self.file = (filename == 'stdin' and sys.stdin) or filename

    def run(self):
        if self.file is sys.stdin:
            lines = self.file
        else:
            with open(self.file, 'r') as f:
                lines = f.readlines()

        noqa_line_numbers = get_noqa_lines(lines)
        errors = get_double_quotes_errors(lines)

        for error in errors:
            if error.get('line') not in noqa_line_numbers:
                line = error.get('line')
                col = error.get('col')
                message = error.get('message')
                yield (line, col, message, type(self))


def get_noqa_lines(lines):
    tokens = []
    for t in tokenize.generate_tokens(lambda l=iter(lines): next(l)):
        tokens.append(Token(t))

    lines = []
    for t in tokens:
        noqa = t.string.lower().endswith(NOQA)
        if t.type == tokenize.COMMENT and noqa:
            lines.append(t.start_row)

    return lines


def get_double_quotes_errors(lines):
    tokens = []
    for t in tokenize.generate_tokens(lambda l=iter(lines): next(l)):
        tokens.append(Token(t))

    for t in tokens:
        # Ignore non-strings.
        if t.type != tokenize.STRING:
            continue

        # Ignore strings that don't start with double quotes.
        if not t.string.startswith('"'):
            continue

        # Ignore single quotes wrapped in double quotes.
        if "'" in t.string:
            continue

        start_row, start_col = t.start
        yield {'message': 'Q000 Strings should use single quotes.',
               'line': start_row,
               'col': start_col}


class Token(object):
    def __init__(self, token):
        self.token = token

    @property
    def type(self):
        return self.token[0]

    @property
    def string(self):
        return self.token[1]

    @property
    def start(self):
        return self.token[2]

    @property
    def start_row(self):
        return self.token[2][0]

    @property
    def start_col(self):
        return self.token[2][1]
