.. _single-source-version:

===================================
Single-sourcing the Project Version
===================================

:Page Status: Complete
:Last Reviewed: 2024-10-07

Many Python :term:`distribution packages <Distribution Package>` publish a single
Python :term:`import package <Import Package>` where it is desired that the runtime
``__version__`` attribute on the import package report the same version specifier
as :func:`importlib.metadata.version` reports for the distribution package
(as described in :ref:`runtime-version-access`).

It is also frequently desired that this version information be derived from a version
control system *tag* (such as ``v1.2.3``) rather than being manually updated in the
source code.

Some projects may choose to simply live with the data entry duplication, and rely
on automated testing to ensure the different values do not diverge.

Alternatively, a project's chosen build system may offer a way to define a single
source of truth for the version number.

In general, the options are:

1) If the code is in a version control system (VCS), such as Git, then the version can be extracted from the VCS.

2) The version can be hard-coded into the :file:`pyproject.toml` file -- and the build system can copy it
   into other locations it may be required.

3) The version string can be hard-coded into the source code -- either in a special purpose file,
   such as :file:`_version.txt` (which must then be shipped as part of the project's source distribution
   package), or as an attribute in a particular module, such as :file:`__init__.py`. The build
   system can then extract it from the runtime location at build time.

Consult your build system's documentation for their recommended method.

When the intention is that a distribution package and its associated import package
share the same version, it is recommended that the project include an automated test
case that ensures ``import_name.__version__`` and ``importlib.metadata.version("dist-name")``
report the same value (note: for many projects, ``import_name`` and ``dist-name`` will
be the same name).


.. _Build system version handling:

Build System Version Handling
-----------------------------

The following are links to some build system's documentation for handling version strings.

* `Flit <https://flit.pypa.io/en/stable/>`_

* `Hatchling <https://hatch.pypa.io/1.9/version/>`_

* `PDM <https://pdm-project.org/en/latest/reference/pep621/#__tabbed_1_2>`_

* `Setuptools <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#dynamic-metadata>`_

  -  `setuptools_scm <https://setuptools-scm.readthedocs.io/en/latest/>`_
