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
Package Index (PyPI)>`. You may want to read pip's recommendations for
:doc:`secure installs <pip:topics/secure-installs>`. Pip is available by default
in most Python installations through the standard library package
:doc:`ensurepip <python:library/ensurepip>`.

Alternatively, consider :ref:`pipx` for the specific use case of installing Python
applications that are distributed through PyPI and run from the command line.
Pipx is a wrapper around pip and venv that installs each
application into a dedicated virtual environment. This avoids conflicts between
the dependencies of different applications, and also with system-wide applications
making use of the same Python interpreter (especially on Linux).

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

.. important::

   Please, remember: this document does not seek to steer the reader towards
   a particular tool, only to enumerate common tools. Different use cases often
   need specialized workflows.

Popular :term:`build backends <build backend>` for pure-Python packages include,
in alphabetical order:

- :doc:`Flit-core <flit:pyproject_toml>` -- developed with but separate from :ref:`Flit`.
  A minimal and opinionated build backend. It does not support plugins.

- Hatchling_ -- developed with but separate from :ref:`Hatch`. Supports plugins.

- PDM-backend_ -- developed with but separate from :ref:`PDM`. Supports plugins.

- Poetry-core_ -- developed with but separate from :ref:`Poetry`. Supports
  plugins.

  Unlike other backends on this list, Poetry-core does not support the standard
  :ref:`[project] table <writing-pyproject-toml>` (it uses a different format,
  in the ``[tool.poetry]`` table).

- :ref:`setuptools`, which used to be the only build backend. Supports plugins.

  .. caution::

     If you use setuptools, please be aware that some features that predate
     standardisation efforts are now deprecated and only *temporarily kept*
     for compatibility.

     In particular, do **not** use direct ``python setup.py`` invocations. On the
     other hand, configuring setuptools with a :file:`setup.py` file is still fully
     supported, although it is recommended to use the modern :ref:`[project] table
     in pyproject.toml <writing-pyproject-toml>` (or :file:`setup.cfg`) whenever possible and keep
     :file:`setup.py` only if programmatic configuration is needed. See
     :ref:`setup-py-deprecated`.

     Other examples of deprecated features you should **not** use include the
     ``setup_requires`` argument to ``setup()`` (use the :ref:`[build-system] table
     <pyproject-guide-build-system-table>` in :file:`pyproject.toml` instead), and
     the ``easy_install`` command (cf. :ref:`pip vs easy_install`).

Do **not** use :ref:`distutils`, which is deprecated, and has been removed from
the standard library in Python 3.12, although it still remains available from
setuptools.

For packages with :term:`extension modules <extension module>`, it is best to use
a build system with dedicated support for the language the extension is written in,
for example:

- :ref:`setuptools` -- natively supports C and C++ (with third-party plugins for Go and Rust),
- :ref:`meson-python` -- C, C++, Fortran, Rust, and other languages supported by Meson,
- :ref:`scikit-build-core` -- C, C++, Fortran, and other languages supported by CMake,
- :ref:`maturin` -- Rust, via Cargo.


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

For projects hosted on or published via supported CI/CD platforms, it is
recommended to use the :ref:`Trusted Publishing <trusted-publishing>`, which
allows the package to be securely uploaded to PyPI from a CI/CD workflow
without a manually configured API token.

As of November 2024, PyPI supports the following platforms as Trusted Publishing
providers:

* GitHub Actions (on ``https://github.com``)
* GitLab CI/CD (on ``https://gitlab.com``)
* ActiveState
* Google Cloud

The other available method is to upload the package manually using :ref:`twine`.

.. danger::

    **Never** use ``python setup.py upload`` for this task. In addition to being
    :ref:`deprecated <setup-py-deprecated>`, it is insecure.


Workflow tools
==============

These tools are environment managers that automatically manage virtual
environments for a project. They also act as "task runners", allowing you to
define and invoke tasks such as running tests, compiling documentation,
regenerating some files, etc. Some of them provide shortcuts for building
distributions and uploading to PyPI, and some support lock files for
applications. They often call the tools mentioned above under the hood. In
alphabetical order:

- :ref:`Flit`,
- :ref:`Hatch`,
- :doc:`nox <nox:index>`,
- :ref:`PDM`,
- :ref:`Pipenv`,
- :ref:`Poetry`,
- :doc:`tox <tox:index>`.


.. _hatchling: https://pypi.org/project/hatchling/
.. _pdm-backend: https://backend.pdm-project.org
.. _poetry-core: https://pypi.org/project/poetry-core/
