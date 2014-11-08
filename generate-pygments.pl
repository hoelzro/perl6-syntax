#!/usr/bin/env perl6

use v6;
use Template::Mustache;

constant @KEYWORDS = <
    BEGIN CATCH CHECK CONTROL END ENTER FIRST INIT
    KEEP LAST LEAVE NEXT POST PRE START TEMP
    UNDO as assoc async augment binary break but
    cached category class constant contend continue
    copy deep default defequiv defer die do else
    elsif enum equiv exit export fail fatal for
    gather given goto grammar handles has if inline
    irs is last leave let lift loop looser macro
    make maybe method module multi my next of
    ofs only oo ors our package parsed prec
    proto readonly redo ref regex reparsed repeat
    require required return returns role rule rw
    self slang state sub submethod subset supersede
    take temp tighter token trusts try unary
    unless until use warn when where while will
>;

constant @BUILTIN_FUNCTIONS = <
    ACCEPTS HOW REJECTS VAR WHAT WHENCE WHERE WHICH
    WHO abs acos acosec acosech acosh acotan acotanh
    all any approx arity asec asech asin asinh
    assuming atan atan2 atanh attr bless body by
    bytes caller callsame callwith can capitalize cat
    ceiling chars chmod chomp chop chr chroot
    circumfix cis classify clone close cmp_ok codes
    comb connect contains context cos cosec cosech
    cosh cotan cotanh count defined delete diag
    dies_ok does e each eager elems end eof eval
    eval_dies_ok eval_elsewhere eval_lives_ok evalfile exists
    exp first flip floor flunk flush fmt force_todo
    fork from getc gethost getlogin getpeername getpw
    gmtime graphs grep hints hyper im index infix
    invert is_approx is_deeply isa isa_ok isnt iterator
    join key keys kill kv lastcall lazy lc lcfirst
    like lines link lives_ok localtime log log10 map
    max min minmax name new nextsame nextwith nfc
    nfd nfkc nfkd nok_error nonce none normalize not
    nothing ok once one open opendir operator ord
    p5chomp p5chop pack pair pairs pass perl pi
    pick plan plan_ok polar pop pos postcircumfix
    postfix pred prefix print printf push quasi
    quotemeta rand re read readdir readline reduce
    reverse rewind rewinddir rindex roots round
    roundrobin run runinstead sameaccent samecase say
    sec sech sech seek shape shift sign signature
    sin sinh skip skip_rest sleep slurp sort splice
    split sprintf sqrt srand strand subst substr succ
    sum symlink tan tanh throws_ok time times to
    todo trim trim_end trim_start true truncate uc
    ucfirst undef undefine uniq unlike unlink unpack
    unpolar unshift unwrap use_ok value values vec
    version_lt void wait want wrap write zip
>;

constant @BUILTIN_CLASSES = <
    Abstraction Any AnyChar Array Associative Bag Bit
    Blob Block Bool Buf Byte Callable Capture Char Class
    Code Codepoint Comparator Complex Decreasing Exception
    Failure False Grammar Grapheme Hash IO Increasing
    Int Junction KeyBag KeyExtractor KeyHash KeySet
    KitchenSink List Macro Mapping Match Matcher Method
    Module Num Object Ordered Ordering OrderingPair
    Package Pair Positional Proxy Range Rat Regex
    Role Routine Scalar Seq Set Signature Str StrLen
    StrPos Sub Submethod True UInt Undef Version Void
    Whatever bit bool buf buf1 buf16 buf2 buf32
    buf4 buf64 buf8 complex int int1 int16 int2
    int32 int4 int64 int8 num rat rat1 rat16 rat2
    rat32 rat4 rat64 rat8 uint uint1 uint16 uint2
    uint32 uint4 uint64 uint8 utf16 utf32 utf8
>;

constant @BUILTIN_OPERATORS = (
    'X', 'Z', 'after', 'also', 'and', 'andthen', 'before', 'cmp', 'div',
    'eq', 'eqv', 'extra', 'ff', 'fff', 'ge', 'gt', 'le', 'leg', 'lt', 'm',
    'mm', 'mod', 'ne', 'or', 'orelse', 'rx', 's', 'tr', 'x', 'xor', 'xx',
    '++', '--', '**', '!', '+', '-', '~', '?', '|', '||', '+^', '~^', '?^',
    '^', '*', '/', '%', '%%', '+&', '+<', '+>', '~&', '~<', '~>', '?&',
    'gcd', 'lcm', '+', '-', '+|', '+^', '~|', '~^', '?|', '?^',
    '~', '&', '^', 'but', 'does', '<=>', '..', '..^', '^..', '^..^',
    '!=', '==', '<', '<=', '>', '>=', '~~', '===', '!eqv',
    '&&', '||', '^^', '//', 'min', 'max', '??', '!!', 'ff', 'fff', 'so',
    'not', '<==', '==>', '<<==', '==>>',
);

constant $INDENT          = 8;
constant $MAX-LINE-LENGTH = 79;

sub python-list(@values) {
    my $indent = ' ' x 8;
    my @lines  = '';

    for @values -> $value {
        my $quoted-value = "'$value'";
        my $current-line := @lines[*-1];
        if chars($indent ~ $current-line ~ $quoted-value ~ ',') > $MAX-LINE-LENGTH {
            @lines.push: '';
            $current-line := @lines[*-1];
        }
        $current-line ~= $quoted-value ~ ', ';
    }

    @lines[1 .. *] .= map($indent ~ *);
    @lines.map(*.trim-trailing).join("\n") ~ "\n"
}

my $template = slurp 'pygments-template.py';

print Template::Mustache.render($template, {
    KEYWORDS          => python-list(@KEYWORDS),
    BUILTIN_FUNCTIONS => python-list(@BUILTIN_FUNCTIONS),
    BUILTIN_CLASSES   => python-list(@BUILTIN_CLASSES),
    BUILTIN_OPERATORS => python-list(@BUILTIN_OPERATORS),
});
