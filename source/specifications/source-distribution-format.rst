
.. _source-distribution-format:

==========================
Source distribution format
==========================

The current standard format of source distribution format is identified by the
presence of a :file:`pyproject.toml` file in the distribution archive.  The layout
of such a distribution was originally specified in :pep:`517` and is formally
documented here.

There is also the legacy source distribution format, implicitly defined by the
behaviour of ``distutils`` module in the standard library, when executing
:command:`setup.py sdist`. This document does not attempt to standardise this
format, except to note that if a legacy source distribution contains a
``PKG-INFO`` file using metadata version 2.2 or later, then it MUST follow
the rules applicable to source distributions defined in the metadata
specification.

Source distributions are also known as *sdists* for short.

Source trees
============

A *source tree* is a collection of files and directories -- like a version
control system checkout -- which contains a :file:`pyproject.toml` file that
can be use to build a source distribution from the contained files and
directories. :pep:`517` and :pep:`518` specify what is required to meet the
definition of what :file:`pyproject.toml` must contain for something to be
deemed a source tree.

Source distribution file name
=============================

The file name of a sdist was standardised in :pep:`625`. The file name must be in
the form ``{name}-{version}.tar.gz``, where ``{name}`` is normalised according to
the same rules as for binary distributions (see :ref:`binary-distribution-format`),
and ``{version}`` is the canonicalized form of the project version (see
:ref:`version-specifiers`).

The name and version components of the filename MUST match the values stored
in the metadata contained in the file.

Code that produces a source distribution file MUST give the file a name that matches
this specification. This includes the ``build_sdist`` hook of a build backend.

Code that processes source distribution files MAY recognise source distribution files
by the ``.tar.gz`` suffix and the presence of precisely *one* hyphen in the filename.
Code that does this may then use the distribution name and version from the filename
without further verification.

Source distribution file format
===============================

A ``.tar.gz`` source distribution (sdist) contains a single top-level directory
called ``{name}-{version}`` (e.g. ``foo-1.0``), containing the source files of
the package. The name and version MUST match the metadata stored in the file.
This directory must also contain a :file:`pyproject.toml` in the format defined in
:ref:`declaring-build-dependencies`, and a ``PKG-INFO`` file containing
metadata in the format described in the :ref:`core-metadata` specification. The
metadata MUST conform to at least version 2.2 of the metadata specification.

No other content of a sdist is required or defined. Build systems can store
whatever information they need in the sdist to build the project.

The tarball should use the modern POSIX.1-2001 pax tar format, which specifies
UTF-8 based file names. In particular, source distribution files must be readable
using the standard library tarfile module with the open flag 'r:gz'.
