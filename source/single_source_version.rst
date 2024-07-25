.. _`Single sourcing the version`:

===================================
Single-sourcing the Project Version
===================================

:Page Status: Complete
:Last Reviewed: 2015-09-08

One of the challenges in building packages is that the version string can be required in multiple places.

* It needs to be specified when building the package (e.g. in :file:`pyproject.toml`)
   - That will assure that it is properly assigned in the distribution file name, and in the installed package.

* Some projects prefer that there be a version string available as an attribute in the importable module, e.g::

    import a_package
    print(a_package.__version__)

* In the metadata of the artifacts for each of the packaging ecosystems    

While different projects have different needs, it's important to make sure that there is a single source of truth for the version number.

In general, the options are:

1) If the code is in a version control system (VCS), e.g. git, then the version can be extracted from the VCS.

2) The version can be hard-coded into the `pyproject.toml` file -- and the build system can copy it into other locations it may be required.

3) The version string can be hard-coded into the source code -- either in a special purpose file, such as `_version.txt`, or as a attribute in the `__init__.py`, and the build system can extract it at build time.

If the version string is not in the source, it can be extracted at runtime with code in `__init__.py`, such as::

    import importlib.metadata
    __version__ = importlib.metadata.version('the_distribution_name')


Consult your build system documentation for how to implement your preferred method.

Here are the common ones:

* `Hatch <https://hatch.pypa.io/1.9/version/>`_

* `Setuptools <https://setuptools.pypa.io/en/latest/userguide/distribution.html#specifying-your-project-s-version>`_

  -  `setuptools_scm <https://setuptools-scm.readthedocs.io/en/latest/>`_

* `Flit <https://flit.pypa.io/en/stable/>`_

* `PDM <https://pdm-project.org/en/latest/reference/pep621/#__tabbed_1_2>`_

