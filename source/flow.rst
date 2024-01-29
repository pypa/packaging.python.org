==================
The Packaging Flow
==================

The document aims to outline the flow involved in publishing/distributing a
:term:`distribution package <Distribution Package>`, usually to the `Python
Package Index (PyPI)`_. It is written for package publishers, who are assumed
to be the package author.

.. _Python Package Index (PyPI): https://pypi.org/

While the :doc:`tutorial <tutorials/packaging-projects>` walks through the
process of preparing a simple package for release, it does not fully enumerate
what steps and files are required, and for what purpose.

Publishing a package requires a flow from the author's source code to an end
user's Python environment. The steps to achieve this are:

- Have a source tree containing the package. This is typically a checkout from
  a version control system (VCS).

- Prepare a configuration file describing the package metadata (name, version
  and so forth) and how to create the build artifacts. For most packages, this
  will be a :file:`pyproject.toml` file, maintained manually in the source
  tree.

- Create build artifacts to be sent to the package distribution service
  (usually PyPI); these will normally be a
  :term:`source distribution ("sdist") <Source Distribution (or "sdist")>`
  and one or more :term:`built distributions ("wheels") <Built Distribution>`.
  These are made by a build tool using the configuration file from the
  previous step. Often there is just one generic wheel for a pure Python
  package.

- Upload the build artifacts to the package distribution service.

At that point, the package is present on the package distribution service.
To use the package, end users must:

- Download one of the package's build artifacts from the package distribution
  service.

- Install it in their Python environment, usually in its ``site-packages``
  directory. This step may involve a build/compile step which, if needed, must
  be described by the package metadata.

These last 2 steps are typically performed by :ref:`pip` when an end user runs
``pip install``.

The steps above are described in more detail below.

The source tree
===============

The source tree contains the package source code, usually a checkout from a
VCS. The particular version of the code used to create the build artifacts
will typically be a checkout based on a tag associated with the version.

The configuration file
======================

The configuration file depends on the tool used to create the build artifacts.
The standard practice is to use a :file:`pyproject.toml` file in the `TOML
format`_.

.. _TOML format: https://github.com/toml-lang/toml

At a minimum, the :file:`pyproject.toml` file needs a ``[build-system]`` table
specifying your build tool. There are many build tools available, including
but not limited to :ref:`flit`, :ref:`hatch`, :ref:`pdm`, :ref:`poetry`,
:ref:`setuptools`, `trampolim`_, and `whey`_. Each tool's documentation will
show what to put in the ``[build-system]`` table.

.. _trampolim: https://pypi.org/project/trampolim/
.. _whey: https://pypi.org/project/whey/

For example, here is a table for using :ref:`hatch`:

.. code-block:: toml

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

With such a table in the :file:`pyproject.toml` file,
a ":term:`frontend <Build Frontend>`" tool like
:ref:`build` can run your chosen
build tool's ":term:`backend <Build Backend>`"
to create the build artifacts.
Your build tool may also provide its own frontend. An install tool
like :ref:`pip` also acts as a frontend when it runs your build tool's backend
to install from a source distribution.

The particular build tool you choose dictates what additional information is
required in the :file:`pyproject.toml` file. For example, you might specify:

* a ``[project]`` table containing project
  :doc:`Core Metadata </specifications/core-metadata/>`
  (name, version, author and so forth),

* a ``[tool]`` table containing tool-specific configuration options.

Refer to the :ref:`pyproject.toml guide <writing-pyproject-toml>` for a
complete guide to ``pyproject.toml`` configuration.


Build artifacts
===============

The source distribution (sdist)
-------------------------------

A source distribution contains enough to install the package from source in an
end user's Python environment. As such, it needs the package source, and may
also include tests and documentation. These are useful for end users wanting
to develop your sources, and for end user systems where some local compilation
step is required (such as a C extension).

The :ref:`build` package knows how to invoke your build tool to create one of
these:

.. code-block:: bash

    python3 -m build --sdist source-tree-directory

Or, your build tool may provide its own interface for creating an sdist.


The built distributions (wheels)
--------------------------------

A built distribution contains only the files needed for an end user's Python
environment. No compilation steps are required during the install, and the
wheel file can simply be unpacked into the ``site-packages`` directory. This
makes the install faster and more convenient for end users.

A pure Python package typically needs only one "generic" wheel. A package with
compiled binary extensions needs a wheel for each supported combination of
Python interpreter, operating system, and CPU architecture that it supports.
If a suitable wheel file is not available, tools like :ref:`pip` will fall
back to installing the source distribution.

The :ref:`build` package knows how to invoke your build tool to create one of
these:

.. code-block:: bash

    python3 -m build --wheel source-tree-directory

Or, your build tool may provide its own interface for creating a wheel.

.. note::

  The default behaviour of :ref:`build` is to make both an sdist and a wheel
  from the source in the current directory; the above examples are
  deliberately specific.

Upload to the package distribution service
==========================================

The :ref:`twine` tool can upload build artifacts to PyPI for distribution,
using a command like:

.. code-block:: bash

    twine upload dist/package-name-version.tar.gz dist/package-name-version-py3-none-any.whl

Or, your build tool may provide its own interface for uploading.

Download and install
====================

Now that the package is published, end users can download and install the
package into their Python environment. Typically this is done with :ref:`pip`,
using a command like:

.. code-block:: bash

    python3 -m pip install package-name

End users may also use other tools like :ref:`pipenv`, :ref:`poetry`, or
:ref:`pdm`.
