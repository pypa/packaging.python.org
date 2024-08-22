.. _`Single sourcing the version`:

===================================
Single-sourcing the Project Version
===================================

:Page Status: Complete
:Last Reviewed: 2024-??

One of the challenges in building packages is that the version string can be required in multiple places.

* It needs to be specified when building the package (e.g. in :file:`pyproject.toml`)
   This will make it available in the installed package’s metadata, from where it will be accessible at runtime using ``importlib.metadata.version("distribution_name")``.

* A package may set a module attribute (e.g., ``__version__``) to provide an alternative means of runtime access to the version of the imported package. If this is done, the value of the attribute and that used by the build system to set the distribution's version should be kept in sync in :ref:`the build systems's recommended way <Build system version handling>`.

* If the code is in in a version control system (VCS), e.g. Git, the version may appear in a *tag* such as ``v1.2.3``.

To ensure that version numbers do not get out of sync, it is recommended that there is a single source of truth for the version number.

In general, the options are:

1) If the code is in a version control system (VCS), e.g. Git, then the version can be extracted from the VCS.

2) The version can be hard-coded into the :file:`pyproject.toml` file -- and the build system can copy it into other locations it may be required.

3) The version string can be hard-coded into the source code -- either in a special purpose file, such as :file:`_version.txt`, or as a attribute in a module, such as :file:`__init__.py`, and the build system can extract it at build time.


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
