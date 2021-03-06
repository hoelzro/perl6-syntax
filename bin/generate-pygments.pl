#!/usr/bin/env perl6

use v6;
use Template::Mustache;

my %stash := OUTER::OUTER::;

my @KEYWORDS = <
    BEGIN CATCH CHECK CONTROL END ENTER FIRST INIT
    KEEP LAST LEAVE NEXT POST PRE START TEMP
    UNDO as assoc async augment binary break but
    cached category class constant contend continue
    copy deep default defequiv defer die do done else
    elsif emit enum equiv exit export fail fatal for
    gather given goto grammar handles has if inline
    irs is last leave let loop looser macro
    make maybe method module multi my next of
    ofs only oo ors our package parsed prec
    proto quit readonly redo ref regex reparsed repeat
    require required return returns role rule rw
    self slang state sub submethod subset supersede
    take temp tighter token trusts try unary
    unless until use wait warn when where while will
>;

my @BUILTIN_FUNCTIONS = %stash.keys\
    .grep(/^ '&'/)\
    .grep(-> $name { $name !~~ /":<" .*? ">"/})\
    .grep(/<[a..z]>/)\
    .map(*.substr(1))\
    .sort;

my $BLACKLIST = Set.new(<
    ContainerDescriptor
    MethodDispatcher
    MultiDispatcher
    WrapDispatcher
    NQPCursorRole
    Rational
    Scheduler
>);

my @BUILTIN_CLASSES = %stash.keys\
    .grep(/^ \w+ $/)\
    .grep({ $BLACKLIST{$_} || %stash{$_}.WHICH eqv %stash{$_}.WHAT.WHICH })\
    .sort;

my @BUILTIN_OPERATORS = %stash.keys\
    .grep(/^ '&'/)\
    .grep(-> $name { $name ~~ /infix|prefix|postfix/})\
    .map({ /":<" <( .*? )> ">"$/; ~$/ })\
    .sort;

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

my $template = slurp 'templates/pygments.py';

print Template::Mustache.render($template, {
    KEYWORDS          => python-list(@KEYWORDS),
    BUILTIN_FUNCTIONS => python-list(@BUILTIN_FUNCTIONS),
    BUILTIN_CLASSES   => python-list(@BUILTIN_CLASSES),
    BUILTIN_OPERATORS => python-list(@BUILTIN_OPERATORS),
});
