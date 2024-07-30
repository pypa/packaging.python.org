.. _`Single sourcing the version`:

===================================
Single-sourcing the Project Version
===================================

:Page Status: Complete
:Last Reviewed: 2024-??

One of the challenges in building packages is that the version string can be required in multiple places.

* It needs to be specified when building the package (e.g. in :file:``pyproject.toml``)
   - That will assure that it is properly assigned in the distribution file name, and in the installed package metadata.

* A package may set a top level ``__version__`` attribute to provide runtime access to the version of the installed package. If this is done, the value of ``__version__`` attribute and that used by the build system to set the distribution's version should be kept in sync in :ref:`the build systems's recommended way <how_to_set_version_links>`.

In the cases where a package does not set a top level ``__version__`` attribute, the version may still be accessible using ``importlib.metadata.version("distribution_name")``.

To ensure that version numbers do not get out of sync, it is recommended that there is a single source of truth for the version number.

In general, the options are:

1) If the code is in a version control system (VCS), e.g. git, then the version can be extracted from the VCS.

2) The version can be hard-coded into the :file:`pyproject.toml` file -- and the build system can copy it into other locations it may be required.

3) The version string can be hard-coded into the source code -- either in a special purpose file, such as ``_version.txt``, or as a attribute in the ``__init__.py``, and the build system can extract it at build time.


Consult your build system's documentation for their recommended method.

.. _how_to_set_version_links:

Build System Version Handling
----------------------------

* `Flit <https://flit.pypa.io/en/stable/>`_

* `Hatchling <https://hatch.pypa.io/1.9/version/>`_

* `PDM <https://pdm-project.org/en/latest/reference/pep621/#__tabbed_1_2>`_

* `Setuptools <https://setuptools.pypa.io/en/latest/userguide/distribution.html#specifying-your-project-s-version>`_

  -  `setuptools_scm <https://setuptools-scm.readthedocs.io/en/latest/>`_



