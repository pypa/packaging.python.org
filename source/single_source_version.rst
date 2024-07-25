.. _`Single sourcing the version`:

===================================
Single-sourcing the Project Version
===================================

:Page Status: Complete
:Last Reviewed: 2015-09-08

One of the challenges in building packages is that the version string can be required in multiple places.

* It needs to be specified when building the package (e.g. in :file:`pyproject.toml`)
   - That will assure that it is properly assigned in the distribution file name, and in teh installed package.

* Some projects require that there be a version string available as an attribute in the importable module, e.g::

    import a_package
    print(a_package.__version__)

While different projects have different needs, it's important to make sure that there is a single source of truth for the version number.

In general, the options are:

1) If the code is in a version control system (VCS), e.g. git, then the version can be extracted from the VCS.

2) The version can be hard-coded into the `pyproject.toml` file -- and the build system can copy it into other locations it may be required.

3) The version string can be hard-coded into the source code -- either in a special purpose file, such as `_version.txt`, or as a attribute in the `__init__.py`, and the build system can extract it at build time.

If the version string is not in the source, it can be extracted at runtime with code in `__init__.py`, such as::

    import importlib.metadata
    __version__ = importlib.metadata.version('the_distribution_name')


Consult your build system documentation for how to implement your preferred method.

Put links in to build system docs?
-- I have no idea which are currently robust and maintained -- do we want to get into seeming endorsing particular tools in this doc?


* setuptools:

* hatch:

* poetry:

* PyBuilder:

* Others?

