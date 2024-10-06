.. _single-source-version:

===================================
Single-sourcing the Project Version
===================================

:Page Status: Complete
:Last Reviewed: 2024-10-02

Many Python :term:`distribution packages <Distribution Package>` publish a single
Python :term:`import package <Import Package>` where it is desired that the runtime
``__version__`` attribute on the import package report the same version specifier
as ``importlib.metadata.version`` reports for the distribution package
(as described in :ref:`runtime-version-access`).

It is also frequently desired that this version information be derived from a version
control system *tag* (such as ``v1.2.3``) rather than being manually updated in the
source code.

To ensure that version numbers do not get out of sync, it may be sufficient to add
an automated test case that ensure ``package.__version__`` and
``importlib.metadata.version("package")`` report the same value.

Alternatively, a project's chosen build system mar offer a way to define a single
source of truth for the version number.

In general, the options are:

1) If the code is in a version control system (VCS), e.g. Git, then the version can be extracted from the VCS.

2) The version can be hard-coded into the :file:`pyproject.toml` file -- and the build system can copy it
   into other locations it may be required.

3) The version string can be hard-coded into the source code -- either in a special purpose file,
   such as :file:`_version.txt`, or as an attribute in a module, such as :file:`__init__.py`, and the build
   system can extract it at build time.

Consult your build system's documentation for their recommended method.

.. _Build system version handling:

Build System Version Handling
-----------------------------

The following are links to some build system's documentation for handling version strings.

* `Flit <https://flit.pypa.io/en/stable/>`_

* `Hatchling <https://hatch.pypa.io/1.9/version/>`_

* `PDM <https://pdm-project.org/en/latest/reference/pep621/#__tabbed_1_2>`_

* `Setuptools <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#dynamic-metadata>`_

  -  `setuptools_scm <https://setuptools-scm.readthedocs.io/en/latest/>`_
