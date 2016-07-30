
.. _specifications:

===================
PyPA Specifications
===================

:Page Status: Complete
:Last Reviewed: 2016-01-22

This is a list of currently active interoperability specifications maintained
by the Python Packaging Authority.

Package distribution metadata
#############################

Core metadata
=============

The current core metadata file format, version 1.2, is specified in :pep:`345`.

However, the version specifiers and environment markers sections of that PEP
have been superceded as described below. In addition, metadata files are
permitted to contain the following additional fields:

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

Description-Content-Type
~~~~~~~~~~~~~~~~~~~~~~~~

A string containing the format of the distribution's description, so that tools
can intelligently render the description. Historically, distribution
descriptions in plain text and in `reStructuredText (reST)
<http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_ have
been supported and PyPI knows how to render reST into HTML. It is very common
for distribution authors to write their description in `Markdown
<https://daringfireball.net/projects/markdown/>`_ (`RFC 7763
<https://tools.ietf.org/html/rfc7763>`_). Distribution authors commonly use
Markdown probably because that's the markup language that they are most
familiar with, but PyPI historically didn't know the format of the description
and thus could not know to render a description as Markdown. This results in
PyPI having many packages where the description is rendered in a very ugly way,
because the description was written in Markdown, but PyPI is rendering it as
reST. This field allows the distribution author to specify the format of their
description and thus opens up the possibility for PyPI and other tools to be
able to render Markdown and other formats.

The format of this field is same as the ``Content-Type`` header in HTTP (e.g.:
`RFC 1341 <https://www.w3.org/Protocols/rfc1341/4_Content-Type.html>`_).
Briefly, this means that it has a ``type/subtype`` part and then it can
optionally have a number of parameters:

Format::

    Description-Content-Type: <type>/<subtype>; charset=<charset>[; <param_name>=<param value> ...]

The ``type/subtype`` part has only a few legal values:

- ``text/plain``
- ``text/x-rst``
- ``text/markdown``

One parameter is called ``charset``; it can be used to specify whether the
character set in use is UTF-8, ASCII, etc. If ``charset`` is not provided, then
it is recommended that the implementation (e.g.: PyPI) treat the content as
UTF-8.

Other parameters might be specific to the chosen subtype. For example, for the
``markdown`` subtype, there is a ``variant`` parameter that allows specifying
the variant of Markdown in use, such as ``Original`` for `Gruber's original
Markdown syntax <https://tools.ietf.org/html/rfc7763#section-6.1.4>`_ or
``GFM`` for `GitHub Flavored Markdown (GFM)
<https://tools.ietf.org/html/rfc7764#section-3.2>`_.

Example::

    Description-Content-Type: text/plain; charset=UTF-8

Example::

    Description-Content-Type: text/x-rst; charset=UTF-8

Example::

    Description-Content-Type: text/markdown; charset=UTF-8; variant=Original

Example::

    Description-Content-Type: text/markdown; charset=UTF-8; variant=GFM

If a ``Description-Content-Type`` is not specified, then the assumed content type
is ``text/x-rst; charset=UTF-8``.


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
