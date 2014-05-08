import sys
import os

if sys.version_info.major != 2:
    raise Exception('Python 2 is required to run the pygments tests')

sys.path.insert(0, 'pygments')

from perl6 import Perl6Lexer
import pygments
import pygments.formatters

def file_list():
    for dirpath, _, filenames in os.walk('corpus'):
        for name in filenames:
            yield os.path.join(dirpath, name)

def generate():
    lexer     = Perl6Lexer()
    formatter = pygments.formatters.get_formatter_by_name('html')

    for path in file_list():
        code        = open(path, 'r').read()
        highlighted = pygments.highlight(code, lexer, formatter)
        # XXX stick highlighted somewhere...

