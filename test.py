import sys

# XXX check for python 2

sys.path.insert(0, 'pygments')

from perl6 import Perl6Lexer
import pygments
import pygments.formatters

code = '''
use lib 'lib';

use Bailador;
Bailador::import;

unless 'data'.IO ~~ :d {
    mkdir 'data'
}

get '/' => sub {
    template 'index.tt'
}

post '/new_paste' => sub {
    my $t  = time;
    my $c = request.params<content>;
    unless $c {
        return "No empty pastes please";
    }
    my $fh = open "data/$t", :w;
    $fh.print: $c;
    $fh.close;
    return "New paste available at paste/$t";
}

get /paste\/(.+)/ => sub ($tag) {
    content_type 'text/plain';
    if "data/$tag".IO.f {
        return slurp "data/$tag"
    }
    status 404;
    return "Paste does not exist";
}

baile;
'''

formatter = pygments.formatters.get_formatter_by_name('terminal256')
print pygments.highlight(code, Perl6Lexer(), formatter)
