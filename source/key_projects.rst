
.. _projects:

=================
Project Summaries
=================

:Page Status: Complete
:Last Reviewed: 2016-06-24

Summaries and links for the most relevant projects in the space of Python
installation and packaging.

.. _pypa_projects:

PyPA Projects
#############

.. _bandersnatch:

bandersnatch
============

`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bitbucket.org/pypa/bandersnatch/issues?status=new&status=open>`__ |
`Bitbucket <https://bitbucket.org/pypa/bandersnatch>`__ |
`PyPI <https://pypi.python.org/pypi/bandersnatch>`__

bandersnatch is a PyPI mirroring client designed to efficiently create a
complete mirror of the contents of PyPI.


.. _distlib:

distlib
=======

`Docs <http://pythonhosted.org/distlib/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bitbucket.org/pypa/distlib/issues?status=new&status=open>`__ |
`Bitbucket <https://bitbucket.org/pypa/distlib>`__ |
`PyPI <https://pypi.python.org/pypi/distlib>`__

Distlib is a library which implements low-level functions that relate to
packaging and distribution of Python software.  It consists in part of the
functions from the `distutils2 <https://pypi.python.org/pypi/Distutils2>`_
project, which was intended to be released as ``packaging`` in the Python 3.3
stdlib, but was removed shortly before Python 3.3 entered beta testing.


.. _packaging:

packaging
=========

`Dev list <http://groups.google.com/group/pypa-dev>`__ |
`Issues <https://github.com/pypa/packaging/issues>`__ |
`Github <https://github.com/pypa/packaging>`__ |
`PyPI <https://pypi.python.org/pypi/packaging>`__ |
User irc:#pypa |
Dev irc:#pypa-dev

Core utilities for Python packaging used by :ref:`pip` and :ref:`setuptools`.


.. _pip:

pip
===

`Docs <https://pip.pypa.io/en/stable/>`__ |
`User list <http://groups.google.com/group/python-virtualenv>`__ [1]_ |
`Dev list <http://groups.google.com/group/pypa-dev>`__ |
`Issues <https://github.com/pypa/pip/issues>`__ |
`Github <https://github.com/pypa/pip>`__ |
`PyPI <https://pypi.python.org/pypi/pip/>`__ |
User irc:#pypa |
Dev irc:#pypa-dev

A tool for installing Python packages.


Python Packaging User Guide
===========================

`Docs <https://packaging.python.org/en/latest/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ |
`Issues <https://github.com/pypa/python-packaging-user-guide/issues>`__ |
`Github <https://github.com/pypa/python-packaging-user-guide>`__ |
User irc:#pypa |
Dev irc:#pypa-dev

This guide!


.. _setuptools:
.. _easy_install:

setuptools
==========

`Docs <https://setuptools.readthedocs.io/en/latest/>`__ |
`User list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Dev list <http://groups.google.com/group/pypa-dev>`__ |
`Issues <https://github.com/pypa/setuptools/issues>`__ |
`GitHub <https://github.com/pypa/setuptools>`__ |
`PyPI <https://pypi.python.org/pypi/setuptools>`__ |
User irc:#pypa  |
Dev irc:#pypa-dev


setuptools (which includes ``easy_install``) is a collection of enhancements to
the Python distutils that allow you to more easily build and distribute Python
distributions, especially ones that have dependencies on other packages.

`distribute`_ was a fork of setuptools that was merged back into setuptools (in
v0.7), thereby making setuptools the primary choice for Python packaging.


.. _twine:

twine
=====

`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://github.com/pypa/twine/issues>`__ |
`Github <https://github.com/pypa/twine>`__ |
`PyPI <https://pypi.python.org/pypi/twine>`__

Twine is a utility for interacting with PyPI, that offers a secure replacement for
``setup.py upload``.



.. _virtualenv:

virtualenv
==========

`Docs <https://virtualenv.pypa.io/en/stable/>`__ |
`User list <http://groups.google.com/group/python-virtualenv>`__ |
`Dev list <http://groups.google.com/group/pypa-dev>`__ |
`Issues <https://github.com/pypa/virtualenv/issues>`__ |
`Github <https://github.com/pypa/virtualenv>`__ |
`PyPI <https://pypi.python.org/pypi/virtualenv/>`__ |
User irc:#pypa  |
Dev irc:#pypa-dev

A tool for creating isolated Python environments.


.. _warehouse:

Warehouse
=========

`Docs <https://warehouse.pypa.io/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://github.com/pypa/warehouse/issues>`__ |
`Github <https://github.com/pypa/warehouse>`__ |
Dev irc:#pypa-dev


The new unreleased PyPI application which can be previewed at https://pypi.org/.


.. _wheel:

wheel
=====

`Docs <https://wheel.readthedocs.io/en/latest/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bitbucket.org/pypa/wheel/issues?status=new&status=open>`__ |
`Bitbucket <https://bitbucket.org/pypa/wheel>`__ |
`PyPI <https://pypi.python.org/pypi/wheel>`__ |
User irc:#pypa  |
Dev irc:#pypa-dev


Primarily, the wheel project offers the ``bdist_wheel`` :ref:`setuptools` extension for
creating :term:`wheel distributions <Wheel>`.  Additionally, it offers its own
command line utility for creating and installing wheels.


Non-PyPA Projects
#################

.. _bento:

bento
=====

`Docs <http://cournape.github.io/Bento/>`__ |
`Mailing list <http://librelist.com/browser/bento>`__ |
`Issues <https://github.com/cournape/Bento/issues>`__ |
`Github <https://github.com/cournape/Bento>`__ |
`PyPI <https://pypi.python.org/pypi/bento>`__

Bento is a packaging tool solution for python software, targeted as an
alternative to distutils, setuptools, distribute, etc....  Bento's philosophy is
reproducibility, extensibility and simplicity (in that order).

.. _buildout:

buildout
========

`Docs <http://www.buildout.org/en/latest/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bugs.launchpad.net/zc.buildout>`__ |
`PyPI <https://pypi.python.org/pypi/zc.buildout>`__ |
irc:#buildout

Buildout is a Python-based build system for creating, assembling and deploying
applications from multiple parts, some of which may be non-Python-based.  It
lets you create a buildout configuration and reproduce the same software later.

.. _conda:

conda
=====

`Docs <http://conda.pydata.org/docs/>`__

conda is the package management tool for `Anaconda
<http://docs.continuum.io/anaconda/index.html>`__ Python installations.
Anaconda Python is a distribution from `Continuum Analytics
<http://continuum.io/downloads>`__ specifically aimed at the scientific
community, and in particular on Windows where the installation of binary
extensions is often difficult.

Conda is a completely separate tool to pip, virtualenv and wheel, but provides
many of their combined features in terms of package management, virtual environment
management and deployment of binary extensions.

Conda does not install packages from PyPI and can install only from
the official Continuum repositories, or anaconda.org (a place for
user-contributed *conda* packages), or a local (e.g. intranet) package server.
However, note that pip can be installed into, and work side-by-side with conda
for managing distributions from PyPI.


devpi
=====

`Docs <http://doc.devpi.net/latest/>`__ |
`Mailing List <https://groups.google.com/forum/#!forum/devpi-dev>`__ |
`Issues <https://bitbucket.org/hpk42/devpi/issues>`__ |
`PyPI <https://pypi.python.org/pypi/devpi>`__

devpi features a powerful PyPI-compatible server and PyPI proxy cache with
a complimentary command line tool to drive packaging, testing and release
activities with Python.


.. _hashdist:

Hashdist
========

`Docs <https://hashdist.readthedocs.io/en/latest/>`__ |
`Github <https://github.com/hashdist/hashdist/>`__

Hashdist is a library for building non-root software distributions. Hashdist is
trying to be “the Debian of choice for cases where Debian technology doesn’t
work”. The best way for Pythonistas to think about Hashdist may be a more
powerful hybrid of virtualenv and buildout.

.. _pex:

pex
===

`Docs <https://pex.readthedocs.io/en/latest/>`__ |
`Github <https://github.com/pantsbuild/pex/>`__ |
`PyPI <https://pypi.python.org/pypi/pex>`__

pex is both a library and tool for generating ``.pex`` (Python EXecutable)
files, standalone Python environments in the spirit of :ref:`virtualenv`.
``.pex`` files are just carefully constructed zip files with a
``#!/usr/bin/env python`` and special ``__main__.py``, and are designed to make
deployment of Python applications as simple as ``cp``.

.. _spack:

Spack
=====

`Docs <http://software.llnl.gov/spack/>`__ |
`Github <https://github.com/llnl/spack/>`__ |
`Paper <http://www.computer.org/csdl/proceedings/sc/2015/3723/00/2807623.pdf>`__ |
`Slides <https://tgamblin.github.io/files/Gamblin-Spack-SC15-Talk.pdf>`__

A flexible package manager designed to support multiple versions,
configurations, platforms, and compilers.  Spack is like homebrew, but
packages are written in Python and parameterized to allow easy
swapping of compilers, library versions, build options,
etc. Arbitrarily many versions of packages can coexist on the same
system. Spack was designed for rapidly building high performance
scientific applications on clusters and supercomputers.

Spack is not in PyPI (yet), but it requires no installation and can be
used immediately after cloning from github.


Standard Library Projects
#########################

.. _ensurepip:

ensurepip
=========

`Docs <https://docs.python.org/3/library/ensurepip.html>`__ |
`Issues <http://bugs.python.org>`__

A package in the Python Standard Library that provides support for bootstrapping
:ref:`pip` into an existing Python installation or virtual environment.  In most
cases, end users won't use this module, but rather it will be used during the
build of the Python distribution.


.. _distutils:

distutils
=========

`Docs <https://docs.python.org/3/library/distutils.html>`__ |
`User list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <http://bugs.python.org>`__ |
User irc:#pypa  |
Dev irc:#pypa-dev

A package in the Python Standard Library that has support for creating and
installing :term:`distributions <Distribution Package>`. :ref:`Setuptools`
provides enhancements to distutils, and is much more commonly used than just
using distutils by itself.


.. _venv:

venv
====

`Docs <https://docs.python.org/3/library/venv.html>`__ |
`Issues <http://bugs.python.org>`__

A package in the Python Standard Library (starting with Python 3.3) for
creating :term:`Virtual Environments <Virtual Environment>`.  For more
information, see the section on :ref:`Creating and using Virtual Environments`.


----

.. [1] pip was created by the same developer as virtualenv, and early on adopted
       the virtualenv mailing list, and it's stuck ever since.

.. [2] Multiple projects reuse the distutils-sig mailing list as their user list.


.. _distribute: https://pypi.python.org/pypi/distribute
