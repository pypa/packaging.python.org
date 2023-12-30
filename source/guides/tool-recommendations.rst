.. _`Tool Recommendations`:

====================
Tool recommendations
====================

The Python packaging landscape consists of many different tools. For many tasks,
the Python Packaging Authority (PyPA, the umbrella organization which
encompasses many packaging tools and maintains this guide) purposefully does not
make a blanket recommendation; for example, the reason there exist many build
backends is that the landscape was opened in order to enable the development of
new backends serving certain users' needs better than the previously unique
backend, setuptools. This guide does point to some tools that are widely
recognized, and also makes some recommendations of tools that you should *not*
use because they are deprecated or insecure.


Virtual environments
====================

The standard tools to create and use virtual environments manually are
:ref:`virtualenv` (PyPA project) and :doc:`venv <python:library/venv>` (part of
the Python standard library, though missing some features of virtualenv).


Installing packages
===================

:ref:`Pip` is a standard tool to install packages from :term:`PyPI <Python
Package Index (PyPI)>`. It can install into the global environment or into
virtual environments. You may want to read pip's recommendations for
:doc:`secure installs <pip:topics/secure-installs>`. Pip is available by default
in most Python installations.

Alternatively, for installing Python command line applications specifically,
consider :ref:`pipx`, which is a wrapper around pip that installs each
application into a dedicated virtual environment in order to avoid conflicts
with other applications and, on Linux, conflicts with the system.

For scientific software specifically, consider :ref:`Conda` or :ref:`Spack`.

.. todo:: Write a "pip vs. Conda" comparison, here or in a new discussion.

Do **not** use ``easy_install`` (part of :ref:`setuptools`), which is deprecated
in favor of pip (see :ref:`pip vs easy_install` for details). Likewise, do
**not** use ``python setup.py install`` or ``python setup.py develop``, which
are also deprecated (see :ref:`setup-py-deprecated` for background and
:ref:`modernize-setup-py-project` for migration advice).


Lock files
==========

:ref:`pip-tools` and :ref:`Pipenv` are two recognized tools to create lock
files, which contain the exact versions of all packages installed into an
environment, for reproducibility purposes.


Build backends
==============

Popular :term:`build backends <build backend>` for pure-Python packages include:

- Hatchling, which is part of :ref:`Hatch` (but can be used without
  Hatch as well). Hatchling is extensible through a plugin system.

- :ref:`setuptools`, the historical build backend. It can be configured
  programmatically through the :file:`setup.py` file.

  If you use setuptools, please be aware that it contains many deprecated
  features which are currently kept for compatibility, but should not be used.
  For example, do not use ``python setup.py`` invocations
  (cf. :ref:`setup-py-deprecated`), the ``python_requires`` argument to
  ``setup()`` (use the :ref:`[build-system] table
  <pyproject-guide-build-system-table>` of :file:`pyproject.toml` instead), or
  the ``easy_install`` command (cf. :ref:`pip vs easy_install`).

- Flit-core, part of :ref:`Flit` (but usable standalone). It is meant to be a
  minimal and opinionated build backend. It is not extensible.

- PDM-backend_, part of :ref:`PDM` (but usable standalone). It provides build
  hooks for extensibility.

- Poetry-core, part of :ref:`Poetry` (but usable standalone). It is extensible
  through plugins.

Do **not** use distutils, which is deprecated, and has been removed from the
standard library in Python 3.12, although it still remains available from
setuptools.

For packages with :term:`extension modules <extension module>`, you may use
setuptools, but consider using a build system dedicated to the language the
extension is written in, such as Meson or CMake for C/C++, or Cargo for Rust,
and bridging this build system to Python using a dedicated build backend:

- :ref:`meson-python` for Meson,

- :ref:`scikit-build-core` for CMake,

- :ref:`maturin` for Cargo.


Building distributions
======================

The standard tool to build :term:`source distributions <source distribution (or
"sdist")>` and :term:`wheels <wheel>` for uploading to PyPI is :ref:`build`.  It
will invoke whichever build backend you :ref:`declared
<pyproject-guide-build-system-table>` in :file:`pyproject.toml`.

Do **not** use ``python setup.py sdist`` and ``python setup.py bdist_wheel`` for
this task. All direct invocations of :file:`setup.py` are :ref:`deprecated
<setup-py-deprecated>`.

If you have :term:`extension modules <extension module>` and want to distribute
wheels for multiple platforms, use :ref:`cibuildwheel` as part of your CI setup
to build distributable wheels.


Uploading to PyPI
=================

The standard tool for this task is :ref:`twine`.

**Never** use ``python setup.py upload`` for this task. In addition to being
:ref:`deprecated <setup-py-deprecated>`, it is insecure.


Integrated workflow tools
=========================

These are tools that combine many features in one command line application, such
as automatically managing virtual environments for a project, building
distributions, uploading to PyPI, or creating and using lock files.

- :ref:`Hatch`,
- :ref:`Flit`,
- :ref:`PDM`,
- :ref:`Poetry`.



.. _pdm-backend: https://backend.pdm-project.org
