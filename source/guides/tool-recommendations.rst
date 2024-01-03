.. _`Tool Recommendations`:

====================
Tool recommendations
====================

The Python packaging landscape consists of many different tools. For many tasks,
the :term:`Python Packaging Authority <Python Packaging Authority (PyPA)>`
(PyPA, the working group which encompasses many packaging tools and
maintains this guide) purposefully does not make a blanket recommendation; for
example, the reason there are many build backends is that the landscape was
opened up in order to enable the development of new backends serving certain users'
needs better than the previously unique backend, setuptools. This guide does
point to some tools that are widely recognized, and also makes some
recommendations of tools that you should *not* use because they are deprecated
or insecure.


Virtual environments
====================

The standard tools to create and use virtual environments manually are
:ref:`virtualenv` (PyPA project) and :doc:`venv <python:library/venv>` (part of
the Python standard library, though missing some features of virtualenv).


Installing packages
===================

:ref:`Pip` is the standard tool to install packages from :term:`PyPI <Python
Package Index (PyPI)>`. It can install into the global environment or into
virtual environments. You may want to read pip's recommendations for
:doc:`secure installs <pip:topics/secure-installs>`. Pip is available by default
in most Python installations through the standard library package
:doc:`ensurepip <python:library/ensurepip>`.

Alternatively, consider :ref:`pipx` for the specific use case of installing Python
command line applications that are distributed through PyPI.
Pipx is a wrapper around pip and venv that installs each
application into a dedicated virtual environment. This avoids conflicts between
the dependencies of different applications, and also with the system
(especially on Linux).

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

Popular :term:`build backends <build backend>` for pure-Python packages include,
in alphabetical order:

- Flit-core_ (developed with but separate from :ref:`Flit`). It is meant to be a
  minimal and opinionated build backend. It is not extensible.

- Hatchling_, which is developed along with :ref:`Hatch`, but is separate and can
  be used without Hatch. Hatchling is extensible through a plugin system.

- PDM-backend_ (developed with but separate from :ref:`PDM`). It provides build
  hooks for extensibility.

- Poetry-core_ (developed with but separate from :ref:`Poetry`). It is extensible
  through plugins.

- :ref:`setuptools` (which used to be the only build backend). It can be configured
  using modern standards like `pyproject.toml`, but can also be extended
  and supports customisation via `setup.py`.
  programmatically through the :file:`setup.py` file (but for basic metadata,
  :file:`pyproject.toml` is preferred).

  If you use setuptools, please be aware that it contains many deprecated
  features which are currently kept for compatibility, but should not be used.
  For example, do **not** use ``python setup.py`` invocations
  (cf. :ref:`setup-py-deprecated`), the ``setup_requires`` argument to
  ``setup()`` (use the :ref:`[build-system] table
  <pyproject-guide-build-system-table>` of :file:`pyproject.toml` instead), or
  the ``easy_install`` command (cf. :ref:`pip vs easy_install`).

Do **not** use :ref:`distutils`, which is deprecated, and has been removed from
the standard library in Python 3.12, although it still remains available from
setuptools.

For packages with :term:`extension modules <extension module>`, you may use
a build system with dedicated support for the language the extension is written in,
for example:

- :ref:`setuptools` - natively supports C/C++ (with 3rd-party plugins for Go and Rust);
- :ref:`meson-python` - C, C++, Fortran, and Rust and other languages supported by Meson;
- :ref:`scikit-build-core` - C, C++, Fortran and other languages supported by CMake;
- :ref:`maturin` - Rust, via Cargo.

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
distributions, uploading to PyPI, or creating and using (tool-specific) lock
files. They often call the tools mentioned above under the hood. In alphabetical
order:

- :ref:`Flit`,
- :ref:`Hatch`,
- :ref:`PDM`,
- :ref:`Pipenv`,
- :ref:`Poetry`.


.. _flit-core: https://pypi.org/project/flit-core/
.. _hatchling: https://pypi.org/project/hatchling/
.. _pdm-backend: https://backend.pdm-project.org
.. _poetry-core: https://pypi.org/project/poetry-core/
