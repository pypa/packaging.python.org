
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

A string stating the markup syntax (if any) used in the distribution's
description, so that tools can intelligently render the description.

Historically, PyPI supported descriptions in plain text and `reStructuredText
(reST) <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_,
and could render reST into HTML. However, it is common for distribution
authors to write the description in `Markdown
<https://daringfireball.net/projects/markdown/>`_ (`RFC 7763
<https://tools.ietf.org/html/rfc7763>`_) as many code hosting sites render
Markdown READMEs, and authors would reuse the file for the description. PyPI
didn't recognize the format and so could not render the description correctly.
This resulted in many packages on PyPI with poorly-rendered descriptions when
Markdown is left as plain text, or worse, was attempted to be rendered as reST.
This field allows the distribution author to specify the format of their
description, opening up the possibility for PyPI and other tools to be able to
render Markdown and other formats.

The format of this field is the same as the ``Content-Type`` header in HTTP
(i.e.:
`RFC 1341 <https://www.w3.org/Protocols/rfc1341/4_Content-Type.html>`_).
Briefly, this means that it has a ``type/subtype`` part and then it can
optionally have a number of parameters:

Format::

    Description-Content-Type: <type>/<subtype>; charset=<charset>[; <param_name>=<param value> ...]

The ``type/subtype`` part has only a few legal values:

- ``text/plain``
- ``text/x-rst``
- ``text/markdown``

The ``charset`` parameter can be used to specify the character encoding of 
the description. The only legal value is ``UTF-8``. If omitted, it is assumed to 
be ``UTF-8``.

Other parameters might be specific to the chosen subtype. For example, for the
``markdown`` subtype, there is an optional ``variant`` parameter that allows
specifying the variant of Markdown in use (defaults to ``CommonMark`` if not
specified). Currently, the only value that is recognized is:

- ``CommonMark`` for `CommonMark
  <https://tools.ietf.org/html/rfc7764#section-3.5>`_

Example::

    Description-Content-Type: text/plain; charset=UTF-8

Example::

    Description-Content-Type: text/x-rst; charset=UTF-8

Example::

    Description-Content-Type: text/markdown; charset=UTF-8; variant=CommonMark

Example::

    Description-Content-Type: text/markdown

If a ``Description-Content-Type`` is not specified, then applications should
attempt to render it as ``text/x-rst; charset=UTF-8`` and fall back to
``text/plain`` if it is not valid rst.

If a ``Description-Content-Type`` is an unrecognized value, then the assumed
content type is ``text/plain`` (Although PyPI will probably reject anything
with an unrecognized value).

If the ``Description-Content-Type`` is ``text/markdown`` and ``variant`` is not
specified or is set to an unrecognized value, then the assumed ``variant`` is
``CommonMark``.

So for the last example above, the ``charset`` defaults to ``UTF-8`` and the
``variant`` defaults to ``CommonMark`` and thus it is equivalent to the example
before it.


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
