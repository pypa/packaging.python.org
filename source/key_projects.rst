
.. _projects:

=================
Project Summaries
=================

Summaries and links for the most relevant projects in the space of Python
installation and packaging.

.. _pypa_projects:

PyPA Projects
#############

.. _bandersnatch:

bandersnatch
============

`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://github.com/pypa/bandersnatch/issues>`__ |
`Github <https://github.com/pypa/bandersnatch>`__ |
`PyPI <https://pypi.org/project/bandersnatch>`__ |
Dev irc:#bandersnatch

bandersnatch is a PyPI mirroring client designed to efficiently create a
complete mirror of the contents of PyPI.


.. _distlib:

distlib
=======

`Docs <http://pythonhosted.org/distlib/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bitbucket.org/pypa/distlib/issues?status=new&status=open>`__ |
`Bitbucket <https://bitbucket.org/pypa/distlib>`__ |
`PyPI <https://pypi.org/project/distlib>`__

Distlib is a library which implements low-level functions that relate to
packaging and distribution of Python software.  It consists in part of the
functions from the `distutils2 <https://pypi.org/project/Distutils2>`_
project, which was intended to be released as ``packaging`` in the Python 3.3
stdlib, but was removed shortly before Python 3.3 entered beta testing.


.. _packaging:

packaging
=========

`Docs <https://packaging.pypa.io>`__ |
`Dev list <http://groups.google.com/group/pypa-dev>`__ |
`Issues <https://github.com/pypa/packaging/issues>`__ |
`Github <https://github.com/pypa/packaging>`__ |
`PyPI <https://pypi.org/project/packaging>`__ |
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
`PyPI <https://pypi.org/project/pip/>`__ |
User irc:#pypa |
Dev irc:#pypa-dev

A tool for installing Python packages.


.. _Pipenv:

Pipenv
======

`Docs <https://docs.pipenv.org>`__ |
`Source <https://github.com/pypa/pipenv>`__ |
`Issues <https://github.com/pypa/pipenv/issues>`__ |
`PyPI <https://pypi.org/project/pipenv>`__

Pipenv is a project that aims to bring the best of all packaging worlds to the
Python world. It harnesses :ref:`Pipfile`, :ref:`pip`, and :ref:`virtualenv`
into one single toolchain. It features very pretty terminal colors.


.. _Pipfile:

Pipfile
=======

`Source <https://github.com/pypa/pipfile>`__

:file:`Pipfile` and its sister :file:`Pipfile.lock` are a higher-level
application-centric alternative to :ref:`pip`'s lower-level
:file:`requirements.txt` file.


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
`PyPI <https://pypi.org/project/setuptools>`__ |
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
`PyPI <https://pypi.org/project/twine>`__

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
`PyPI <https://pypi.org/project/virtualenv/>`__ |
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


The current codebase powering the :term:`Python Package Index (PyPI)`. It is
hosted at `pypi.org <https://pypi.org/>`_.


.. _wheel:

wheel
=====

`Docs <https://wheel.readthedocs.io/en/latest/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://github.com/pypa/wheel/issues>`__ |
`Github <https://github.com/pypa/wheel>`__ |
`PyPI <https://pypi.org/project/wheel>`__ |
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
`PyPI <https://pypi.org/project/bento>`__

Bento is a packaging tool solution for Python software, targeted as an
alternative to distutils, setuptools, distribute, etc....  Bento's philosophy is
reproducibility, extensibility and simplicity (in that order).

.. _buildout:

buildout
========

`Docs <http://www.buildout.org/en/latest/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bugs.launchpad.net/zc.buildout>`__ |
`PyPI <https://pypi.org/project/zc.buildout>`__ |
irc:#buildout

Buildout is a Python-based build system for creating, assembling and deploying
applications from multiple parts, some of which may be non-Python-based.  It
lets you create a buildout configuration and reproduce the same software later.

.. _conda:

conda
=====

`Docs <http://conda.pydata.org/docs/>`__

conda is the package management tool for `Anaconda
<https://docs.anaconda.com/anaconda/>`__ Python installations.
Anaconda Python is a distribution from `Anaconda, Inc
<https://www.anaconda.com/download>`__ specifically aimed at the scientific
community, and in particular on Windows where the installation of binary
extensions is often difficult.

Conda is a completely separate tool to pip, virtualenv and wheel, but provides
many of their combined features in terms of package management, virtual environment
management and deployment of binary extensions.

Conda does not install packages from PyPI and can install only from
the official Anaconda repositories, or anaconda.org (a place for
user-contributed *conda* packages), or a local (e.g. intranet) package server.
However, note that pip can be installed into, and work side-by-side with conda
for managing distributions from PyPI.


devpi
=====

`Docs <http://doc.devpi.net/latest/>`__ |
`Mailing List <https://groups.google.com/forum/#!forum/devpi-dev>`__ |
`Issues <https://bitbucket.org/hpk42/devpi/issues>`__ |
`PyPI <https://pypi.org/project/devpi>`__

devpi features a powerful PyPI-compatible server and PyPI proxy cache with
a complimentary command line tool to drive packaging, testing and release
activities with Python.


.. _flit:

flit
====

`Docs <https://flit.readthedocs.io/en/latest/>`__ |
`Issues <https://github.com/takluyver/flit/issues>`__ |
`PyPI <https://pypi.org/project/flit>`__

Flit is a simple way to put Python packages and modules on PyPI. Flit packages
a single importable module or package at a time, using the import name as the
name on PyPI. All subpackages and data files within a package are included
automatically. Flit requires Python 3, but you can use it to distribute modules
for Python 2, so long as they can be imported on Python 3.

enscons
=======

`Source <https://bitbucket.org/dholth/enscons/src>`__ |
`Issues <https://bitbucket.org/dholth/enscons/issues>`__ |
`PyPI <https://pypi.org/project/enscons>`__

Enscons is a Python packaging tool based on `SCons`_. It builds pip-compatible
source distributions and wheels without using distutils or setuptools,
including distributions with C extensions. Enscons has a different architecture
and philosophy than distutils. Rather than adding build features to a Python
packaging system, enscons adds Python packaging to a general purpose build
system. Enscons helps you to build sdists that can be automatically built by
pip, and wheels that are independent of enscons.

.. _SCons: http://scons.org/

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
`PyPI <https://pypi.org/project/pex>`__

pex is both a library and tool for generating :file:`.pex` (Python EXecutable)
files, standalone Python environments in the spirit of :ref:`virtualenv`.
:file:`.pex` files are just carefully constructed zip files with a
``#!/usr/bin/env python`` and special :file:`__main__.py`, and are designed to
make deployment of Python applications as simple as ``cp``.

.. _pipx:

pipx
====

`Docs <https://github.com/pipxproject/pipx>`__ |
`Github <https://github.com/pipxproject/pipx>`__ |
`PyPI <https://pypi.org/project/pipx/>`__

pipx is a tool to safely install and run Python CLI applications globally.

.. _scikit-build:

scikit-build
============

`Docs <https://scikit-build.readthedocs.io/en/latest/>`__ |
`Mailing list <https://groups.google.com/forum/#!forum/scikit-build>`__ |
`Github <https://github.com/scikit-build/scikit-build/>`__ |
`PyPI <https://pypi.org/project/scikit-build>`__

Scikit-build is an improved build system generator for CPython
C/C++/Fortran/Cython extensions that integrates with :ref:`setuptools`, :ref:`wheel`
and :ref:`pip`. It internally uses `cmake <https://pypi.org/project/cmake>`__ (available
on PyPI) to provide better support for additional compilers, build systems,
cross compilation, and locating dependencies and their associated
build requirements. To speed up and parallelize the build of large projects,
the user can install `ninja <https://pypi.org/project/ninja>`__ (also available
on PyPI).

.. _shiv:

shiv
====

`Docs <https://shiv.readthedocs.io/en/latest/>`__ |
`Github <https://github.com/linkedin/shiv>`__ |
`PyPI <https://pypi.org/project/shiv/>`__

shiv is a command line utility for building fully self contained Python zipapps as outlined in PEP
441, but with all their dependencies included. It's primary goal is making distributing Python
applications and command line tools fast & easy.

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


.. _distribute: https://pypi.org/project/distribute
