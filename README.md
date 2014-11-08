# Perl 6 Syntax

Files that add syntax highlighting support to editors for Perl 6.

# Building

The syntax files are generated dynamically, because they leverage a Perl 6
implementation's introspection facilities to generate lists of builtins.  So
in order to build the syntax files, you'll need the following:

  - A recent Perl 6 implementation (I recommend Rakudo)
  - Template::Mustache for Perl 6

# Testing

To run the tests, you'll need the following;

  - Perl 5 for running kate and vim tests
  - Python for running pygments tests

# Possibly supported future editors

If enough people ask for it:

  - Emacs (I'm sure this will be there)
  - Light Table
  - Atom
  - ACE
