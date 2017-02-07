
.. _specifications:

===================
PyPA Specifications
===================

:Page Status: Complete
:Last Reviewed: 2017-02-06

This is a list of currently active interoperability specifications maintained
by the Python Packaging Authority.

Package distribution metadata
#############################

Core metadata
=============

The current core metadata file format, version 1.2, is specified in :pep:`345`.

However, the version specifiers and environment markers sections of that PEP
have been superceded as described below. In addition, metadata files are
permitted to contain the following additional field:

Provides-Extra (multiple use)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A string containing the name of an optional feature. Must be a valid Python
identifier. May be used to make a dependency conditional on whether the
optional feature has been requested.

Example::

    Provides-Extra: pdf
    Requires-Dist: reportlab; extra == 'pdf'

A second distribution requires an optional dependency by placing it
inside square brackets, and can request multiple features by separating
them with a comma (,). The requirements are evaluated for each requested
feature and added to the set of requirements for the distribution.

Example::

    Requires-Dist: beaglevote[pdf]
    Requires-Dist: libexample[test, doc]

Two feature names `test` and `doc` are reserved to mark dependencies that
are needed for running automated tests and generating documentation,
respectively.

It is legal to specify ``Provides-Extra:`` without referencing it in any
``Requires-Dist:``.


Version Specifiers
==================

Version numbering requirements and the semantics for specifying comparisons
between versions are defined in :pep:`440`.

The version specifiers section in this PEP supersedes the version specifiers
section in :pep:`345`.

Dependency Specifiers
=====================

The dependency specifier format used to declare a dependency on another
component is defined in :pep:`508`.

The environment markers section in this PEP supersedes the environment markers
section in :pep:`345`.

Declaring Build System Dependencies
===================================

`pyproject.toml` is a build system independent file format defined in :pep:`518`
that projects may provide in order to declare any Python level dependencies that
must be installed in order to run the project's build system successfully.

Source Distribution Format
==========================

The source distribution format (``sdist``) is not currently formally defined.
Instead, its format is implicitly defined by the behaviour of the
standard library's ``distutils`` module when executing the ``setup.py sdist``
command.

Binary Distribution Format
==========================

The binary distribution format (``wheel``) is defined in :pep:`427`.

Platform Compatibility Tags
===========================

The platform compatibility tagging model used for ``wheel`` distribution is
defined in :pep:`425`.

The scheme defined in that PEP is insufficient for public distribution
of Linux wheel files (and \*nix wheel files in general), so :pep:`513` was
created to define the ``manylinux1`` tag.

Recording Installed Distributions
=================================

The format used to record installed packages and their contents is defined in
:pep:`376`.

Note that only the ``dist-info`` directory and the ``RECORD`` file format from
that PEP are currently implemented in the default packaging toolchain.


Package index interfaces
########################

Simple repository API
=====================

The current interface for querying available package versions and retrieving packages
from an index server is defined in :pep:`503`.
