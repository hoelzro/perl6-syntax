import sys
import os
import tempfile

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
        yield path, highlighted

def update():
    generated_dir = tempfile.mkdtemp()
    for path, highlighted in generate():
        parent = os.path.dirname(os.path.join(generated_dir, path))
        if not os.path.exists(parent):
            os.makedirs(parent)
        open(os.path.join(generated_dir, path + '.html'), 'w').write(highlighted)
    # XXX do something with generated_dir

def verify():
    pass

update()
