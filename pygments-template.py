# -*- coding: utf-8 -*-

import re
from pygments.lexer import ExtendedRegexLexer, bygroups, default, include, using, this
from pygments.token import Comment, Keyword, Name, Text, String, Number, Operator

__all__ = ['Perl6Lexer']

class Perl6Lexer(ExtendedRegexLexer):
    """
    For `Perl 6 <http://www.perl6.org>`_ source code.

    .. versionadded:: 2.0
    """

    # This lexer was generated from the perl6/syntax project

    name = 'Perl6'
    aliases = ['perl6', 'pl6']
    filenames = ['*.pl', '*.pm', '*.nqp', '*.p6', '*.6pl', '*.p6l', '*.pl6',
                 '*.6pm', '*.p6m', '*.pm6', '*.t']
    mimetypes = ['text/x-perl6', 'application/x-perl6']
    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    PERL6_IDENTIFIER_RANGE = "['\w:-]"

    PERL6_KEYWORDS = (
        {{{KEYWORDS}}}
    )

    PERL6_BUILTINS = (
        {{BUILTIN_FUNCTIONS}}
    )

    PERL6_BUILTIN_CLASSES = (
        {{{BUILTIN_CLASSES}}}
    )

    PERL6_OPERATORS = (
        {{{BUILTIN_OPERATORS}}}
    )

    # Perl 6 has a *lot* of possible bracketing characters
    # this list was lifted from STD.pm6 (https://github.com/perl6/std)
    PERL6_BRACKETS = {
        u'\u0028': u'\u0029', u'\u003c': u'\u003e', u'\u005b': u'\u005d',
        u'\u007b': u'\u007d', u'\u00ab': u'\u00bb', u'\u0f3a': u'\u0f3b',
        u'\u0f3c': u'\u0f3d', u'\u169b': u'\u169c', u'\u2018': u'\u2019',
        u'\u201a': u'\u2019', u'\u201b': u'\u2019', u'\u201c': u'\u201d',
        u'\u201e': u'\u201d', u'\u201f': u'\u201d', u'\u2039': u'\u203a',
        u'\u2045': u'\u2046', u'\u207d': u'\u207e', u'\u208d': u'\u208e',
        u'\u2208': u'\u220b', u'\u2209': u'\u220c', u'\u220a': u'\u220d',
        u'\u2215': u'\u29f5', u'\u223c': u'\u223d', u'\u2243': u'\u22cd',
        u'\u2252': u'\u2253', u'\u2254': u'\u2255', u'\u2264': u'\u2265',
        u'\u2266': u'\u2267', u'\u2268': u'\u2269', u'\u226a': u'\u226b',
        u'\u226e': u'\u226f', u'\u2270': u'\u2271', u'\u2272': u'\u2273',
        u'\u2274': u'\u2275', u'\u2276': u'\u2277', u'\u2278': u'\u2279',
        u'\u227a': u'\u227b', u'\u227c': u'\u227d', u'\u227e': u'\u227f',
        u'\u2280': u'\u2281', u'\u2282': u'\u2283', u'\u2284': u'\u2285',
        u'\u2286': u'\u2287', u'\u2288': u'\u2289', u'\u228a': u'\u228b',
        u'\u228f': u'\u2290', u'\u2291': u'\u2292', u'\u2298': u'\u29b8',
        u'\u22a2': u'\u22a3', u'\u22a6': u'\u2ade', u'\u22a8': u'\u2ae4',
        u'\u22a9': u'\u2ae3', u'\u22ab': u'\u2ae5', u'\u22b0': u'\u22b1',
        u'\u22b2': u'\u22b3', u'\u22b4': u'\u22b5', u'\u22b6': u'\u22b7',
        u'\u22c9': u'\u22ca', u'\u22cb': u'\u22cc', u'\u22d0': u'\u22d1',
        u'\u22d6': u'\u22d7', u'\u22d8': u'\u22d9', u'\u22da': u'\u22db',
        u'\u22dc': u'\u22dd', u'\u22de': u'\u22df', u'\u22e0': u'\u22e1',
        u'\u22e2': u'\u22e3', u'\u22e4': u'\u22e5', u'\u22e6': u'\u22e7',
        u'\u22e8': u'\u22e9', u'\u22ea': u'\u22eb', u'\u22ec': u'\u22ed',
        u'\u22f0': u'\u22f1', u'\u22f2': u'\u22fa', u'\u22f3': u'\u22fb',
        u'\u22f4': u'\u22fc', u'\u22f6': u'\u22fd', u'\u22f7': u'\u22fe',
        u'\u2308': u'\u2309', u'\u230a': u'\u230b', u'\u2329': u'\u232a',
        u'\u23b4': u'\u23b5', u'\u2768': u'\u2769', u'\u276a': u'\u276b',
        u'\u276c': u'\u276d', u'\u276e': u'\u276f', u'\u2770': u'\u2771',
        u'\u2772': u'\u2773', u'\u2774': u'\u2775', u'\u27c3': u'\u27c4',
        u'\u27c5': u'\u27c6', u'\u27d5': u'\u27d6', u'\u27dd': u'\u27de',
        u'\u27e2': u'\u27e3', u'\u27e4': u'\u27e5', u'\u27e6': u'\u27e7',
        u'\u27e8': u'\u27e9', u'\u27ea': u'\u27eb', u'\u2983': u'\u2984',
        u'\u2985': u'\u2986', u'\u2987': u'\u2988', u'\u2989': u'\u298a',
        u'\u298b': u'\u298c', u'\u298d': u'\u298e', u'\u298f': u'\u2990',
        u'\u2991': u'\u2992', u'\u2993': u'\u2994', u'\u2995': u'\u2996',
        u'\u2997': u'\u2998', u'\u29c0': u'\u29c1', u'\u29c4': u'\u29c5',
        u'\u29cf': u'\u29d0', u'\u29d1': u'\u29d2', u'\u29d4': u'\u29d5',
        u'\u29d8': u'\u29d9', u'\u29da': u'\u29db', u'\u29f8': u'\u29f9',
        u'\u29fc': u'\u29fd', u'\u2a2b': u'\u2a2c', u'\u2a2d': u'\u2a2e',
        u'\u2a34': u'\u2a35', u'\u2a3c': u'\u2a3d', u'\u2a64': u'\u2a65',
        u'\u2a79': u'\u2a7a', u'\u2a7d': u'\u2a7e', u'\u2a7f': u'\u2a80',
        u'\u2a81': u'\u2a82', u'\u2a83': u'\u2a84', u'\u2a8b': u'\u2a8c',
        u'\u2a91': u'\u2a92', u'\u2a93': u'\u2a94', u'\u2a95': u'\u2a96',
        u'\u2a97': u'\u2a98', u'\u2a99': u'\u2a9a', u'\u2a9b': u'\u2a9c',
        u'\u2aa1': u'\u2aa2', u'\u2aa6': u'\u2aa7', u'\u2aa8': u'\u2aa9',
        u'\u2aaa': u'\u2aab', u'\u2aac': u'\u2aad', u'\u2aaf': u'\u2ab0',
        u'\u2ab3': u'\u2ab4', u'\u2abb': u'\u2abc', u'\u2abd': u'\u2abe',
        u'\u2abf': u'\u2ac0', u'\u2ac1': u'\u2ac2', u'\u2ac3': u'\u2ac4',
        u'\u2ac5': u'\u2ac6', u'\u2acd': u'\u2ace', u'\u2acf': u'\u2ad0',
        u'\u2ad1': u'\u2ad2', u'\u2ad3': u'\u2ad4', u'\u2ad5': u'\u2ad6',
        u'\u2aec': u'\u2aed', u'\u2af7': u'\u2af8', u'\u2af9': u'\u2afa',
        u'\u2e02': u'\u2e03', u'\u2e04': u'\u2e05', u'\u2e09': u'\u2e0a',
        u'\u2e0c': u'\u2e0d', u'\u2e1c': u'\u2e1d', u'\u2e20': u'\u2e21',
        u'\u3008': u'\u3009', u'\u300a': u'\u300b', u'\u300c': u'\u300d',
        u'\u300e': u'\u300f', u'\u3010': u'\u3011', u'\u3014': u'\u3015',
        u'\u3016': u'\u3017', u'\u3018': u'\u3019', u'\u301a': u'\u301b',
        u'\u301d': u'\u301e', u'\ufd3e': u'\ufd3f', u'\ufe17': u'\ufe18',
        u'\ufe35': u'\ufe36', u'\ufe37': u'\ufe38', u'\ufe39': u'\ufe3a',
        u'\ufe3b': u'\ufe3c', u'\ufe3d': u'\ufe3e', u'\ufe3f': u'\ufe40',
        u'\ufe41': u'\ufe42', u'\ufe43': u'\ufe44', u'\ufe47': u'\ufe48',
        u'\ufe59': u'\ufe5a', u'\ufe5b': u'\ufe5c', u'\ufe5d': u'\ufe5e',
        u'\uff08': u'\uff09', u'\uff1c': u'\uff1e', u'\uff3b': u'\uff3d',
        u'\uff5b': u'\uff5d', u'\uff5f': u'\uff60', u'\uff62': u'\uff63',
    }

    def _build_word_match(words, boundary_regex_fragment=None, prefix='', suffix=''):
        if boundary_regex_fragment is None:
            return r'\b(' + prefix + r'|'.join(re.escape(x) for x in words) + \
                suffix + r')\b'
        else:
            return r'(?<!' + boundary_regex_fragment + r')' + prefix + r'(' + \
                r'|'.join(re.escape(x) for x in words) + r')' + suffix + r'(?!' + \
                boundary_regex_fragment + r')'

    def brackets_callback(token_class):
        def callback(lexer, match, context):
            groups = match.groupdict()
            opening_chars = groups['delimiter']
            n_chars = len(opening_chars)
            adverbs = groups.get('adverbs')

            closer = Perl6Lexer.PERL6_BRACKETS.get(opening_chars[0])
            text = context.text

            if closer is None:  # it's not a mirrored character, which means we
                                # just need to look for the next occurrence

                end_pos = text.find(opening_chars, match.start('delimiter') + n_chars)
            else:   # we need to look for the corresponding closing character,
                    # keep nesting in mind
                closing_chars = closer * n_chars
                nesting_level = 1

                search_pos = match.start('delimiter')

                while nesting_level > 0:
                    next_open_pos = text.find(opening_chars, search_pos + n_chars)
                    next_close_pos = text.find(closing_chars, search_pos + n_chars)

                    if next_close_pos == -1:
                        next_close_pos = len(text)
                        nesting_level = 0
                    elif next_open_pos != -1 and next_open_pos < next_close_pos:
                        nesting_level += 1
                        search_pos = next_open_pos
                    else:  # next_close_pos < next_open_pos
                        nesting_level -= 1
                        search_pos = next_close_pos

                end_pos = next_close_pos

            if end_pos < 0:     # if we didn't find a closer, just highlight the
                                # rest of the text in this class
                end_pos = len(text)

            if adverbs is not None and re.search(r':to\b', adverbs):
                heredoc_terminator = text[match.start('delimiter') + n_chars:end_pos]
                end_heredoc = re.search(r'^\s*' + re.escape(heredoc_terminator) +
                                        r'\s*$', text[end_pos:], re.MULTILINE)

                if end_heredoc:
                    end_pos += end_heredoc.end()
                else:
                    end_pos = len(text)

            yield match.start(), token_class, text[match.start():end_pos + n_chars]
            context.pos = end_pos + n_chars

        return callback

    def opening_brace_callback(lexer, match, context):
        stack = context.stack

        yield match.start(), Text, context.text[match.start():match.end()]
        context.pos = match.end()

        # if we encounter an opening brace and we're one level
        # below a token state, it means we need to increment
        # the nesting level for braces so we know later when
        # we should return to the token rules.
        if len(stack) > 2 and stack[-2] == 'token':
            context.perl6_token_nesting_level += 1

    def closing_brace_callback(lexer, match, context):
        stack = context.stack

        yield match.start(), Text, context.text[match.start():match.end()]
        context.pos = match.end()

        # if we encounter a free closing brace and we're one level
        # below a token state, it means we need to check the nesting
        # level to see if we need to return to the token state.
        if len(stack) > 2 and stack[-2] == 'token':
            context.perl6_token_nesting_level -= 1
            if context.perl6_token_nesting_level == 0:
                stack.pop()

    def embedded_perl6_callback(lexer, match, context):
        context.perl6_token_nesting_level = 1
        yield match.start(), Text, context.text[match.start():match.end()]
        context.pos = match.end()
        context.stack.append('root')

    # If you're modifying these rules, be careful if you need to process '{' or '}'
    # characters. We have special logic for processing these characters (due to the fact
    # that you can nest Perl 6 code in regex blocks), so if you need to process one of
    # them, make sure you also process the corresponding one!
    tokens = {
        'common': [
            (r'#[`|=](?P<delimiter>(?P<first_char>[' + ''.join(PERL6_BRACKETS) + r'])(?P=first_char)*)',
             brackets_callback(Comment.Multiline)),
            (r'#[^\n]*$', Comment.Single),
            (r'^(\s*)=begin\s+(\w+)\b.*?^\1=end\s+\2', Comment.Multiline),
            (r'^(\s*)=for.*?\n\s*?\n', Comment.Multiline),
            (r'^=.*?\n\s*?\n', Comment.Multiline),
            (r'(regex|token|rule)(\s*' + PERL6_IDENTIFIER_RANGE + '+:sym)',
             bygroups(Keyword, Name), 'token-sym-brackets'),
            (r'(regex|token|rule)(?!' + PERL6_IDENTIFIER_RANGE + ')(\s*' + PERL6_IDENTIFIER_RANGE + '+)?',
             bygroups(Keyword, Name), 'pre-token'),
            # deal with a special case in the Perl 6 grammar (role q { ... })
            (r'(role)(\s+)(q)(\s*)', bygroups(Keyword, Text, Name, Text)),
            (_build_word_match(PERL6_KEYWORDS, PERL6_IDENTIFIER_RANGE), Keyword),
            (_build_word_match(PERL6_BUILTIN_CLASSES, PERL6_IDENTIFIER_RANGE, suffix='(?::[UD])?'),
             Name.Builtin),
            (_build_word_match(PERL6_BUILTINS, PERL6_IDENTIFIER_RANGE), Name.Builtin),
            # copied from PerlLexer
            (r'[$@%&][.^:?=!~]?' + PERL6_IDENTIFIER_RANGE + u'+(?:<<.*?>>|<.*?>|«.*?»)*',
             Name.Variable),
            (r'\$[!/](?:<<.*?>>|<.*?>|«.*?»)*', Name.Variable.Global),
            (r'::\?\w+', Name.Variable.Global),
            (r'[$@%&]\*' + PERL6_IDENTIFIER_RANGE + u'+(?:<<.*?>>|<.*?>|«.*?»)*',
             Name.Variable.Global),
            (r'\$(?:<.*?>)+', Name.Variable),
            (r'(?:q|qq|Q)[a-zA-Z]?\s*(?P<adverbs>:[\w\s:]+)?\s*(?P<delimiter>(?P<first_char>[^0-9a-zA-Z:\s])'
             r'(?P=first_char)*)', brackets_callback(String)),
            # copied from PerlLexer
            (r'0_?[0-7]+(_[0-7]+)*', Number.Oct),
            (r'0x[0-9A-Fa-f]+(_[0-9A-Fa-f]+)*', Number.Hex),
            (r'0b[01]+(_[01]+)*', Number.Bin),
            (r'(?i)(\d*(_\d*)*\.\d+(_\d*)*|\d+(_\d*)*\.\d+(_\d*)*)(e[+-]?\d+)?',
             Number.Float),
            (r'(?i)\d+(_\d*)*e[+-]?\d+(_\d*)*', Number.Float),
            (r'\d+(_\d+)*', Number.Integer),
            (r'(?<=~~)\s*/(?:\\\\|\\/|.)*?/', String.Regex),
            (r'(?<=[=(,])\s*/(?:\\\\|\\/|.)*?/', String.Regex),
            (r'm\w+(?=\()', Name),
            (r'(?:m|ms|rx)\s*(?P<adverbs>:[\w\s:]+)?\s*(?P<delimiter>(?P<first_char>[^\w:\s])'
             r'(?P=first_char)*)', brackets_callback(String.Regex)),
            (r'(?:s|ss|tr)\s*(?::[\w\s:]+)?\s*/(?:\\\\|\\/|.)*?/(?:\\\\|\\/|.)*?/',
             String.Regex),
            (r'<[^\s=].*?\S>', String),
            (_build_word_match(PERL6_OPERATORS), Operator),
            (r'\w' + PERL6_IDENTIFIER_RANGE + '*', Name),
            (r"'(\\\\|\\[^\\]|[^'\\])*'", String),
            (r'"(\\\\|\\[^\\]|[^"\\])*"', String),
        ],
        'root': [
            include('common'),
            (r'\{', opening_brace_callback),
            (r'\}', closing_brace_callback),
            (r'.+?', Text),
        ],
        'pre-token': [
            include('common'),
            (r'\{', Text, ('#pop', 'token')),
            (r'.+?', Text),
        ],
        'token-sym-brackets': [
            (r'(?P<delimiter>(?P<first_char>[' + ''.join(PERL6_BRACKETS) + '])(?P=first_char)*)',
             brackets_callback(Name), ('#pop', 'pre-token')),
            default(('#pop', 'pre-token')),
        ],
        'token': [
            (r'\}', Text, '#pop'),
            (r'(?<=:)(?:my|our|state|constant|temp|let).*?;', using(this)),
            # make sure that quotes in character classes aren't treated as strings
            (r'<(?:[-!?+.]\s*)?\[.*?\]>', String.Regex),
            # make sure that '#' characters in quotes aren't treated as comments
            (r"(?<!\\)'(\\\\|\\[^\\]|[^'\\])*'", String.Regex),
            (r'(?<!\\)"(\\\\|\\[^\\]|[^"\\])*"', String.Regex),
            (r'#.*?$', Comment.Single),
            (r'\{', embedded_perl6_callback),
            ('.+?', String.Regex),
        ],
    }

    def analyse_text(text):
        def strip_pod(lines):
            in_pod = False
            stripped_lines = []

            for line in lines:
                if re.match(r'^=(?:end|cut)', line):
                    in_pod = False
                elif re.match(r'^=\w+', line):
                    in_pod = True
                elif not in_pod:
                    stripped_lines.append(line)

            return stripped_lines

        # XXX handle block comments
        lines = text.splitlines()
        lines = strip_pod(lines)
        text = '\n'.join(lines)

        if shebang_matches(text, r'perl6|rakudo|niecza|pugs'):
            return True

        saw_perl_decl = False
        rating = False

        # check for my/our/has declarations
        if re.search("(?:my|our|has)\s+(?:" + Perl6Lexer.PERL6_IDENTIFIER_RANGE +
                     "+\s+)?[$@%&(]", text):
            rating = 0.8
            saw_perl_decl = True

        for line in lines:
            line = re.sub('#.*', '', line)
            if re.match('^\s*$', line):
                continue

            # match v6; use v6; use v6.0; use v6.0.0;
            if re.match('^\s*(?:use\s+)?v6(?:\.\d(?:\.\d)?)?;', line):
                return True
            # match class, module, role, enum, grammar declarations
            class_decl = re.match('^\s*(?:(?P<scope>my|our)\s+)?(?:module|class|role|enum|grammar)', line)
            if class_decl:
                if saw_perl_decl or class_decl.group('scope') is not None:
                    return True
                rating = 0.05
                continue
            break

        return rating

    def __init__(self, **options):
        super(Perl6Lexer, self).__init__(**options)
        self.encoding = options.get('encoding', 'utf-8')
