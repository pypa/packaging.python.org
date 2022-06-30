==================
The Packaging Flow
==================

The document aims to outline the flow involved in publishing/distributing
a :term:`distribution package <Distribution Package>`,
usually to the `Python Package Index (PyPI)`_.

.. _Python Package Index (PyPI): https://pypi.org/

While the :doc:`tutorial </tutorials/installing-packages/>`
walks through the process of preparing a simple package for release
it does not fully enumerate what steps and files are required,
and for what purpose.

This guide is aimed at package publishers, and for simplification
presumes that that is also the package author.
Also, we will use the word package to cover modules as well.

To publish a package there needs to be a flow from the author's
source code to an end user's Python installation.
The steps to achieve this are as follows:

- have a source tree containing the package and associated metadata
  describing the package (name, version and so forth), typically a checkout
  from a version control system (VCS)

- prepare a configuration file describing the package metadata and how to 
  create the build artifacts; for many packages this will be a static 
  ``pyproject.toml`` file in the source tree,
  simple and hand maintained as part of the source tree

- create build artifacts to be sent to the package distribution service 
  (usually PyPI); this will normally be a :term:`source distribution ("sdist") <Source Distribution>`
  and a number of :term:`built distributions ("wheel" files) <Built Distribution>`
  often there is just one generic wheel for a pure Python package;
  these are made by a build tool/system using the configuration file
  from the previous step

- upload the build artifacts to the package distribution service

At that point the package is present on the package distribution service.
To use the package, end users must:

- download one of the package's build artifacts from the package
  distribution service

- install it in their Python installation, usually in its ``site-packages``
  directory; this install step may involve a build/compile step which,
  if needed, must be described by the package metadata

These last 2 steps are typically performed by a tool like `pip`_.

.. _pip: https://pip.pypa.io/en/stable/

The Steps In More Detail
========================

The steps above are described in more detail below.

The Source Tree
---------------

The source tree contains the package source code, usually a checkout from a VCS.
The particular version of the code will will typically be from a checkout
based on a tag associated with the version.

The Configuration File
----------------------

The configuration file depends on the tool used to build the build artifacts.
Modern practice is a ``pyproject.toml`` file in `TOML format`_
whose contents are specified by
:pep:`517`_ and :pep:`518`_ (specifying a build system),
and :pep:`621`_ (storing project metadata in ``pyproject.toml``).

.. _TOML format: https://github.com/toml-lang/toml

At a minimum, the ``pyproject.toml`` file needs:

* a ``[build-system]`` table specifying your build tool,
  which *you* will use to create the build artifacts
  and which an *installer* such as `pip` will use
  to complete an install from a source distribution

Very frequently you might also specify in ``pyproject.toml``
(depending on the tools you use):

* a ``[project]`` table containing project :doc:`Core Metadata </specifications/core-metadata/>`
  (name, version, author and so forth);
  see :doc:`Declaring project metadata </specifications/declaring-project-metadata/>` for more detail

* a ``[tool]`` table containing tool-specific configuration options

The Build System
----------------

The build tool itself is specified by the required table ``[build-system]``.
Most build tools provide a "build frontend" such as a command line mode
for creating the build artifacts.
All can also be used via the `build`_ module
which understands the ``[build-system]`` table.

There are several choices available, including but not limited to:
`flit`_, `hatch`_, `pdm`_, `poetry`_, `setuptools`_, `trampolim`_,
`whey`_.

.. _flit: https://pypi.org/project/flit/
.. _hatch: https://github.com/ofek/hatch
.. _pdm: https://pypi.org/project/pdm/
.. _poetry: https://pypi.org/project/poetry/
.. _setuptools: https://pypi.org/project/setuptools/
.. _trampolim: https://pypi.org/project/trampolim/
.. _whey: https://pypi.org/project/whey/

For example, here is a table for using ``setuptools`` (see the `Setuptools documentation`_)::

    [build-system]
    requires = ["setuptools>=61.2""]
    build-backend = "setuptools.build_meta"

.. _Setuptools documentation: https://setuptools.pypa.io/en/latest/userguide/index.html

or for ``flit`` (see the `Flit documentation`_)::

    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

.. _Flit documentation: https://flit.pypa.io/en/latest/

With such a table in the ``pyproject.toml`` file a tool like `build`_
can run your chosen build system to create the build artifacts
and an install tool like `pip` can fetch and run the build system
when installing a source distribution.

.. _build: https://pypi.org/project/build/

The particular build system you choose dictates what additional information is required.
For example, if using ``setuptools`` you might want to add a ``setup.cfg`` file
containing package metadata and/or a small ``setup.py`` stub for backward
compatibility, for example::

    from setuptools import setup
    setup()

or equivalent (``setuptools`` is moving away from actually *running* the ``setup.py`` file directly).

Build Artifacts: the Source Distribution (sdist)
------------------------------------------------

A source distribution contains enough to install the package from source
on an end user's system.
As such it needs the package source
and may well also include tests and documentation.
These are useful for end users wanting to develop your sources
and for end user systems where some local compilation step is required,
for example for a C extension.

A build system will know how to create one of these,
and the ``build`` package knows how to invoke your build system to create one::

    python3 -m build --sdist source-tree-directory

Or, of course, you can invoke your build tool directly.

Build Artifacts: the Built Distributions (wheels)
-------------------------------------------------

A built distribution contains the completed files needed for a specific
end user system; no compilations steps are required during the install
and the wheel file can simply be unpacked into the right place.
This makes these faster and more convenient for end users;
tools like ``pip`` will fall back to the source distribtion
if a suitable wheel file is not available.
A pure Python package only needs one wheel for "generic" systems.

A build system will know how to create one of these,
and the ``build`` package knows how to invoke your build system to create one::

    python3 -m build --wheel source-tree-directory

Or, of course, you can invoke your build tool directly.

The default behaviour of ``build`` is to make both an sdist and a wheel;
the above examples are deliberately specific.

Upload to the Package Distribution Service
------------------------------------------

The `twine tool`_ can upload build artifact files to PyPI for distribution,
for example with a command like::

    twine upload dist/package-name-version.tar.gz dist/package-name-version-py3-none-any.whl

.. _twine tool: https://pypi.org/project/twine/

Some build tools will also include their own upload facilities.

Download/Install
----------------

Now that the package is published,
end users then download and install the package.
Typically this is done with ``pip``, ideally wiith a command line like::

    python3 -m pip install package-name

where ``python3`` is the python executable which is to have
``package-name`` installed.
