
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

`Issues <https://github.com/pypa/bandersnatch/issues>`__ |
`GitHub <https://github.com/pypa/bandersnatch>`__ |
`PyPI <https://pypi.org/project/bandersnatch>`__

``bandersnatch`` is a PyPI mirroring client designed to efficiently
create a complete mirror of the contents of PyPI. Organizations thus
save bandwidth and latency on package downloads (especially in the
context of automated tests) and to prevent heavily loading PyPI's
Content Delivery Network (CDN).


.. _build:

build
=====

`Docs <build:index>` |
`Issues <https://github.com/pypa/build/issues>`__ |
`GitHub <https://github.com/pypa/build>`__ |
`PyPI <https://pypi.org/project/build>`__

``build`` is a :pep:`517` compatible Python package builder. It provides a CLI to
build packages, as well as a Python API.


.. _cibuildwheel:

cibuildwheel
============

`Docs <https://cibuildwheel.readthedocs.io/>`__ |
`Issues <https://github.com/pypa/cibuildwheel/issues>`__ |
`GitHub <https://github.com/pypa/cibuildwheel>`__ |
`PyPI <https://pypi.org/project/cibuildwheel>`__ |
`Discussions <https://github.com/pypa/cibuildwheel/discussions>`__ |
`Discord #cibuildwheel <https://discord.com/invite/pypa>`__

``cibuildwheel`` is a Python package that builds :term:`wheels <Wheel>` for all common
platforms and Python versions on most CI systems. Also see :ref:`multibuild`.

.. _distlib:

distlib
=======

:doc:`Docs <distlib:index>` |
`Issues <https://bitbucket.org/pypa/distlib/issues?status=new&status=open>`__ |
`Bitbucket <https://bitbucket.org/pypa/distlib>`__ |
`PyPI <https://pypi.org/project/distlib>`__

``distlib`` is a library which implements low-level functions that
relate to packaging and distribution of Python software.  ``distlib``
implements several relevant PEPs (Python Enhancement Proposal
standards) and is useful for developers of third-party packaging tools
to make and upload binary and source :term:`distributions
<Distribution Package>`, achieve interoperability, resolve
dependencies, manage package resources, and do other similar
functions.

Unlike the stricter :ref:`packaging` project (below), which
specifically implements modern Python packaging interoperability
standards, ``distlib`` also attempts to provide reasonable fallback
behaviours when asked to handle legacy packages and metadata that
predate the modern interoperability standards and fall into the subset
of packages that are incompatible with those standards.

.. _flit:

flit
====

`Docs <https://flit.readthedocs.io/en/latest/>`__ |
`Issues <https://github.com/pypa/flit/issues>`__ |
`PyPI <https://pypi.org/project/flit>`__

Flit provides a simple way to create and upload pure Python packages and
modules to PyPI.  It focuses on `making the easy things easy <flit-rationale_>`_
for packaging.  Flit can generate a configuration file to quickly set up a
simple project, build source distributions and wheels, and upload them to PyPI.

Flit uses ``pyproject.toml`` to configure a project. Flit does not rely on tools
such as :ref:`setuptools` to build distributions, or :ref:`twine` to upload them
to PyPI. Flit requires Python 3, but you can use it to distribute modules for
Python 2, so long as they can be imported on Python 3.

.. _flit-rationale: https://flit.readthedocs.io/en/latest/rationale.html

.. _hatch:

hatch
=====

`Docs <https://hatch.pypa.io/latest/>`__ |
`GitHub <https://github.com/pypa/hatch>`__ |
`PyPI <https://pypi.org/project/hatch>`__

Hatch is a unified command-line tool meant to conveniently manage
dependencies and environment isolation for Python developers. Python
package developers use Hatch and its build backend Hatchling to
configure, version, specify dependencies for, and publish packages
to PyPI. Its plugin system allows for easily extending functionality.

.. _packaging:

packaging
=========

:doc:`Docs <packaging:index>` |
`Issues <https://github.com/pypa/packaging/issues>`__ |
`GitHub <https://github.com/pypa/packaging>`__ |
`PyPI <https://pypi.org/project/packaging>`__

Core utilities for Python packaging used by :ref:`pip` and :ref:`setuptools`.

The core utilities in the packaging library handle version handling,
specifiers, markers, requirements, tags, and similar attributes and
tasks for Python packages. Most Python users rely on this library
without needing to explicitly call it; developers of the other Python
packaging, distribution, and installation tools listed here often use
its functionality to parse, discover, and otherwise handle dependency
attributes.

This project specifically focuses on implementing the modern Python
packaging interoperability standards defined at
:ref:`packaging-specifications`, and will report errors for
sufficiently old legacy packages that are incompatible with those
standards. In contrast, the :ref:`distlib` project is a more
permissive library that attempts to provide a plausible reading of
ambiguous metadata in cases where :ref:`packaging` will instead report
on error.

.. _pip:

pip
===

`Docs <https://pip.pypa.io/>`__ |
`Issues <https://github.com/pypa/pip/issues>`__ |
`GitHub <https://github.com/pypa/pip>`__ |
`PyPI <https://pypi.org/project/pip/>`__

The most popular tool for installing Python packages, and the one
included with modern versions of Python.

It provides the essential core features for finding, downloading, and
installing packages from PyPI and other Python package indexes, and can be
incorporated into a wide range of development workflows via its
command-line interface (CLI).

.. _Pipenv:

Pipenv
======

:doc:`Docs <pipenv:index>` |
`Source <https://github.com/pypa/pipenv>`__ |
`Issues <https://github.com/pypa/pipenv/issues>`__ |
`PyPI <https://pypi.org/project/pipenv>`__

Pipenv is a project that aims to bring the best of all packaging worlds to the
Python world. It harnesses :ref:`Pipfile`, :ref:`pip`, and :ref:`virtualenv`
into one single toolchain. It can autoimport ``requirements.txt`` and also
check for CVEs in `Pipfile` using `safety <https://pyup.io/safety>`_.

Pipenv aims to help users manage environments, dependencies, and
imported packages on the command line. It also works well on Windows
(which other tools often underserve), makes and checkes file hashes,
to ensure compliance with hash-locked dependency specifiers, and eases
uninstallation of packages and dependencies.

.. _Pipfile:

Pipfile
=======

`Source <https://github.com/pypa/pipfile>`__

:file:`Pipfile` and its sister :file:`Pipfile.lock` are a higher-level
application-centric alternative to :ref:`pip`'s lower-level
:file:`requirements.txt` file.

.. _pipx:

pipx
====

`Docs <https://pypa.github.io/pipx/>`__ |
`GitHub <https://github.com/pypa/pipx>`__ |
`PyPI <https://pypi.org/project/pipx/>`__

pipx is a tool to install and run Python command-line applications without
causing dependency conflicts with other packages installed on the system.


Python Packaging User Guide
===========================

:doc:`Docs <packaging.python.org:index>` |
`Issues <https://github.com/pypa/packaging.python.org/issues>`__ |
`GitHub <https://github.com/pypa/packaging.python.org>`__

This guide!

.. _readme_renderer:

readme_renderer
===============

`GitHub and docs <https://github.com/pypa/readme_renderer/>`__ |
`PyPI <https://pypi.org/project/readme-renderer/>`__

``readme_renderer`` is a library that package developers use to render
their user documentation (README) files into HTML from markup
languages such as Markdown or reStructuredText. Developers call it on
its own or via :ref:`twine`, as part of their release management
process, to check that their package descriptions will properly
display on PyPI.

.. _setuptools:
.. _easy_install:

setuptools
==========

`Docs <https://setuptools.readthedocs.io/en/latest/>`__ |
`Issues <https://github.com/pypa/setuptools/issues>`__ |
`GitHub <https://github.com/pypa/setuptools>`__ |
`PyPI <https://pypi.org/project/setuptools>`__

setuptools (which includes ``easy_install``) is a collection of
enhancements to the Python distutils that allow you to more easily
build and distribute Python :term:`distributions <Distribution
Package>`, especially ones that have dependencies on other packages.

`distribute`_ was a fork of setuptools that was merged back into setuptools (in
v0.7), thereby making setuptools the primary choice for Python packaging.


.. _trove-classifiers:

trove-classifiers
=================

`Issues <https://github.com/pypa/trove-classifiers/issues>`__ | `GitHub
<https://github.com/pypa/trove-classifiers>`__ | `PyPI
<https://pypi.org/project/trove-classifiers/>`__

trove-classifiers is the canonical source for `classifiers on PyPI
<https://pypi.org/classifiers/>`_, which project maintainers use to
`systematically describe their projects
<https://packaging.python.org/specifications/core-metadata/#classifier-multiple-use>`_
so that users can better find projects that match their needs on the PyPI.

The trove-classifiers package contains a list of valid classifiers and
deprecated classifiers (which are paired with the classifiers that replace
them).  Use this package to validate classifiers used in packages intended for
uploading to PyPI. As this list of classifiers is published as code, you
can install and import it, giving you a more convenient workflow compared to
referring to the `list published on PyPI <https://pypi.org/classifiers/>`_. The
`issue tracker <https://github.com/pypa/trove-classifiers/issues>`_ for the
project hosts discussions on proposed classifiers and requests for new
classifiers.


.. _twine:

twine
=====

`Docs <https://twine.readthedocs.io/en/latest/>`__ |
`Issues <https://github.com/pypa/twine/issues>`__ |
`GitHub <https://github.com/pypa/twine>`__ |
`PyPI <https://pypi.org/project/twine>`__

Twine is the primary tool developers use to upload packages to the
Python Package Index or other Python package indexes. It is a
command-line program that passes program files and metadata to a web
API. Developers use it because it's the official PyPI upload tool,
it's fast and secure, it's maintained, and it reliably works.


.. _virtualenv:

virtualenv
==========

:doc:`Docs <virtualenv:index>` |
`Issues <https://github.com/pypa/virtualenv/issues>`__ |
`GitHub <https://github.com/pypa/virtualenv>`__ |
`PyPI <https://pypi.org/project/virtualenv/>`__

virtualenv is a tool which uses the command-line path environment
variable to create isolated Python :term:`Virtual Environments
<Virtual Environment>`, much as :ref:`venv` does. virtualenv provides
additional functionality, compared to :ref:`venv`, by supporting Python
2.7 and by providing convenient features for configuring, maintaining,
duplicating, and troubleshooting the virtual environments. For more
information, see the section on :ref:`Creating and using Virtual
Environments`.


.. _warehouse:

Warehouse
=========

`Docs <https://warehouse.pypa.io/>`__ |
`Issues <https://github.com/pypa/warehouse/issues>`__ |
`GitHub <https://github.com/pypa/warehouse>`__

The current codebase powering the :term:`Python Package Index
(PyPI)`. It is hosted at `pypi.org <https://pypi.org/>`_. The default
source for :ref:`pip` downloads.


.. _wheel:

wheel
=====

`Docs <https://wheel.readthedocs.io/en/latest/>`__ |
`Issues <https://github.com/pypa/wheel/issues>`__ |
`GitHub <https://github.com/pypa/wheel>`__ |
`PyPI <https://pypi.org/project/wheel>`__

Primarily, the wheel project offers the ``bdist_wheel`` :ref:`setuptools` extension for
creating :term:`wheel distributions <Wheel>`.  Additionally, it offers its own
command line utility for creating and installing wheels.

See also `auditwheel <https://github.com/pypa/auditwheel>`__, a tool
that package developers use to check and fix Python packages they are
making in the binary wheel format. It provides functionality to
discover dependencies, check metadata for compliance, and repair the
wheel and metadata to properly link and include external shared
libraries in a package.


Non-PyPA Projects
#################

.. _buildout:

buildout
========

`Docs <http://www.buildout.org/en/latest/>`__ |
`Issues <https://bugs.launchpad.net/zc.buildout>`__ |
`PyPI <https://pypi.org/project/zc.buildout>`__ |
`GitHub <https://github.com/buildout/buildout/>`__

Buildout is a Python-based build system for creating, assembling and deploying
applications from multiple parts, some of which may be non-Python-based.  It
lets you create a buildout configuration and reproduce the same software later.

.. _conda:

conda
=====

:doc:`Docs <conda:index>`

conda is the package management tool for `Anaconda
<https://docs.anaconda.com/anaconda/>`__ Python installations.
Anaconda Python is a distribution from `Anaconda, Inc
<https://www.anaconda.com/products/individual>`__ specifically aimed at the scientific
community, and in particular on Windows where the installation of binary
extensions is often difficult.

Conda is a completely separate tool from :ref:`pip`, virtualenv and wheel, but provides
many of their combined features in terms of package management, virtual environment
management and deployment of binary extensions.

Conda does not install packages from PyPI and can install only from
the official Anaconda repositories, or anaconda.org (a place for
user-contributed *conda* packages), or a local (e.g. intranet) package
server.  However, note that :ref:`pip` can be installed into, and work
side-by-side with conda for managing :term:`distributions
<Distribution Package>` from PyPI. Also, `conda skeleton
<https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html>`__
is a tool to make Python packages installable by conda by first
fetching them from PyPI and modifying their metadata.

.. _devpi:

devpi
=====

`Docs <http://doc.devpi.net/latest/>`__ |
:gh:`Issues <devpi/devpi/issues>` |
`PyPI <https://pypi.org/project/devpi>`__

devpi features a powerful PyPI-compatible server and PyPI proxy cache
with a complementary command line tool to drive packaging, testing and
release activities with Python. devpi also provides a browsable and
searchable web interface.

.. _enscons:

enscons
=======

:gh:`Source <dholth/enscons>` |
:gh:`Issues <dholth/enscons/issues>` |
`PyPI <https://pypi.org/project/enscons>`__

Enscons is a Python packaging tool based on `SCons`_. It builds
:ref:`pip`-compatible source distributions and wheels without using
distutils or setuptools, including distributions with C
extensions. Enscons has a different architecture and philosophy than
:ref:`distutils`. Rather than adding build features to a Python
packaging system, enscons adds Python packaging to a general purpose
build system. Enscons helps you to build sdists that can be
automatically built by :ref:`pip`, and wheels that are independent of
enscons.

.. _SCons: https://scons.org/

.. _hashdist:

Hashdist
========

`Docs <https://hashdist.readthedocs.io/en/latest/>`__ |
`GitHub <https://github.com/hashdist/hashdist/>`__

Hashdist is a library for building non-root software
distributions. Hashdist is trying to be “the Debian of choice for
cases where Debian technology doesn’t work”. The best way for
Pythonistas to think about Hashdist may be a more powerful hybrid of
:ref:`virtualenv` and :ref:`buildout`. It is aimed at solving the
problem of installing scientific software, and making package
distribution stateless, cached, and branchable. It is used by some
researchers but has been lacking in maintenance since 2016.

.. _multibuild:

multibuild
==========

`GitHub <https://github.com/matthew-brett/multibuild>`__

Multibuild is a set of CI scripts for building and testing Python :term:`wheels <Wheel>` for
Linux, macOS, and (less flexibly) Windows. Also see :ref:`cibuildwheel`.

.. _pdm:

pdm
===

`Docs <https://pdm.fming.dev/>`__ |
`GitHub <https://github.com/pdm-project/pdm/>`__ |
`PyPI <https://pypi.org/project/pdm>`__

PDM is a modern Python package manager with :pep:`582` support. It installs and
manages packages in a similar way to ``npm`` that doesn't need to create a
:term:`virtual environment` at all. It also uses :term:`pyproject.toml` to store
project metadata as defined in :pep:`621`.

.. _pex:

pex
===

`Docs <https://pex.readthedocs.io/en/latest/>`__ |
`GitHub <https://github.com/pantsbuild/pex/>`__ |
`PyPI <https://pypi.org/project/pex>`__

pex is both a library and tool for generating :file:`.pex` (Python EXecutable)
files, standalone Python environments in the spirit of :ref:`virtualenv`.
:file:`.pex` files are just carefully constructed zip files with a
``#!/usr/bin/env python`` and special :file:`__main__.py`, and are designed to
make deployment of Python applications as simple as ``cp``.

.. _pip-tools:

pip-tools
=========

`GitHub and Docs <https://github.com/jazzband/pip-tools/>`__ |
`PyPI <https://pypi.org/project/pip-tools/>`__

pip-tools is a suite of tools meant for Python system administrators
and release managers who particularly want to keep their builds
deterministic yet stay up to date with new versions of their
dependencies. Users can specify particular release of their
dependencies via hash, conveniently make a properly formatted list of
requirements from information in other parts of their program, update
all dependencies (a feature :ref:`pip` currently does not provide), and
create layers of constraints for the program to obey.

.. _piwheels:

piwheels
========

`Website <https://www.piwheels.org/>`__ |
:doc:`Docs <piwheels:index>` |
`GitHub <https://github.com/piwheels/piwheels/>`__

piwheels is a website, and software underpinning it, that fetches
source code distribution packages from PyPI and compiles them into
binary wheels that are optimized for installation onto Raspberry Pi
computers. Raspberry Pi OS pre-configures pip to use piwheels.org as
an additional index to PyPI.

.. _poetry:

poetry
======

`Docs <https://python-poetry.org/>`__ |
`GitHub <https://github.com/python-poetry/poetry>`__ |
`PyPI <https://pypi.org/project/poetry/>`__

poetry is a command-line tool to handle dependency installation and
isolation as well as building and packaging of Python packages. It
uses ``pyproject.toml`` and, instead of depending on the resolver
functionality within :ref:`pip`, provides its own dependency resolver.
It attempts to speed users' experience of installation and dependency
resolution by locally caching metadata about dependencies.

.. _pypiserver:

pypiserver
==========

`Docs <https://github.com/pypiserver/pypiserver/blob/master/README.rst>`__ |
`GitHub <https://github.com/pypiserver/pypiserver>`__ |
`PyPI <https://pypi.org/project/pypiserver/>`__

pypiserver is a minimalist application that serves as a private Python
package index within organizations, implementing a simple API and
browser interface. You can upload private packages using standard
upload tools, and users can download and install them with :ref:`pip`,
without publishing them publicly. Organizations who use pypiserver
usually download packages both from pypiserver and from PyPI.

.. _pyscaffold:

PyScaffold
==========

`Docs <https://pyscaffold.org>`__ |
`GitHub <https://github.com/pyscaffold/pyscaffold>`__ |
`PyPI <https://pypi.org/project/pyscaffold/>`__

PyScaffold is a project generator for bootstrapping Python packages,
ready to be shared on PyPI and installable via :ref:`pip`.
It relies on a set of sane default configurations for established tools
(such as :ref:`setuptools`, pytest_ and Sphinx_) to provide a productive
environment so developers can start coding right away.
PyScaffold can also be used with existing projects to make packaging
easier.


.. _scikit-build:

scikit-build
============

`Docs <https://scikit-build.readthedocs.io/en/latest/>`__ |
`GitHub <https://github.com/scikit-build/scikit-build/>`__ |
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
`GitHub <https://github.com/linkedin/shiv>`__ |
`PyPI <https://pypi.org/project/shiv/>`__

shiv is a command line utility for building fully self contained
Python zipapps as outlined in :pep:`441`, but with all their
dependencies included. Its primary goal is making distributing Python
applications and command line tools fast & easy.

.. _spack:

Spack
=====

:doc:`Docs <spack:index>` |
`GitHub <https://github.com/spack/spack>`__ |
`Paper <https://www.computer.org/csdl/proceedings-article/sc/2015/2807623/12OmNBf94Xq>`__ |
`Slides <https://tgamblin.github.io/files/Gamblin-Spack-SC15-Talk.pdf>`__

A flexible package manager designed to support multiple versions,
configurations, platforms, and compilers.  Spack is like Homebrew, but
packages are written in Python and parameterized to allow easy
swapping of compilers, library versions, build options,
etc. Arbitrarily many versions of packages can coexist on the same
system. Spack was designed for rapidly building high performance
scientific applications on clusters and supercomputers.

Spack is not in PyPI (yet), but it requires no installation and can be
used immediately after cloning from GitHub.

.. _zestreleaser:

zest.releaser
=============

`Docs <https://zestreleaser.readthedocs.io/en/latest/>`__ |
`GitHub <https://github.com/zestsoftware/zest.releaser/>`__ |
`PyPI <https://pypi.org/project/zest.releaser/>`__

``zest.releaser`` is a Python package release tool providing an
abstraction layer on top of :ref:`twine`. Python developers use
``zest.releaser`` to automate incrementing package version numbers,
updating changelogs, tagging releases in source control, and uploading
new packages to PyPI.

Standard Library Projects
#########################

.. _ensurepip:

ensurepip
=========

`Docs <https://docs.python.org/3/library/ensurepip.html>`__ |
`Issues <https://bugs.python.org/>`__

A package in the Python Standard Library that provides support for bootstrapping
:ref:`pip` into an existing Python installation or virtual environment.  In most
cases, end users won't use this module, but rather it will be used during the
build of the Python distribution.


.. _distutils:

distutils
=========

`Docs <https://docs.python.org/3/library/distutils.html>`__ |
`Issues <https://bugs.python.org/>`__

The original Python packaging system, added to the standard library in
Python 2.0.

Due to the challenges of maintaining a packaging system
where feature updates are tightly coupled to language runtime updates,
direct usage of :ref:`distutils` is now actively discouraged, with
:ref:`Setuptools` being the preferred replacement. :ref:`Setuptools`
not only provides features that plain :ref:`distutils` doesn't offer
(such as dependency declarations and entry point declarations), it
also provides a consistent build interface and feature set across all
supported Python versions.


.. _venv:

venv
====

`Docs <https://docs.python.org/3/library/venv.html>`__ |
`Issues <https://github.com/python/cpython/issues>`__

A package in the Python Standard Library (starting with Python 3.3) for
creating :term:`Virtual Environments <Virtual Environment>`.  For more
information, see the section on :ref:`Creating and using Virtual Environments`.


----

.. _distribute: https://pypi.org/project/distribute
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _pytest: https://docs.pytest.org/en/stable/
