.. _`Single sourcing the version`:

===================================
Single-sourcing the package version
===================================


There are many techniques to maintain a single source of truth for the version string of your projects:


Auto extract the version string from the source
-----------------------------------------------

One way of single sourcing is to specify the version string somewhere in the source code, e.g. ``my_package/__init__.py``. Then it can be found at runtime with ``my_package.__version__``, and that same value can be used to set the version when building the package.

#. Declare to read the version string  from the source in ``setuptools.cfg`` or ``pyproject.toml``

   With recent versions of setuptools (since 46.4.0), one can add a declaration
   to the project's :file:`setup.cfg` file (replacing "package" with the import
   name of the package):

   .. code-block:: ini

       [metadata]
       version = attr: package.__version__

   As of the release of setuptools 61.0.0, one can also specify the
   version dynamically in the project's :file:`pyproject.toml` file.

   .. code-block:: toml

        [project]
        name = "package"
        dynamic = ["version"]

        [tool.setuptools.dynamic]
        version = {attr = "package.__version__"}

   Please be aware that declarative config indicators, including the
   ``attr:`` directive, are not supported in parameters to
   :file:`setup.py`.


#.  While the modern standard is to use declarative files (such as ``setup.cfg``),
    with older versions of setuptools, you may need to add a version-reading
    function to setup.py: Example adapted from (from `pip setup.py <https://github.com/pypa/pip/blob/main/setup.py#L11>`_)::

        from pathlib import Path

        def read(rel_path):
            here = Path(__file__).parent.absolute()
            with open(here / rel_path), 'r') as fp:
                return fp.read()

        def get_version(rel_path):
            for line in read(rel_path).splitlines():
                if line.startswith('__version__'):
                    delim = '"' if '"' in line else "'"
                    return line.split(delim)[1]
            else:
                raise RuntimeError("Unable to find version string.")

        setup(
           ...
           version=get_version("package/__init__.py")
           ...
        )

Generate the version string from the SCM
----------------------------------------

Most projects use a Source Code Management System (SCM), such as git or mercurial to manage the code and also manage releases.
In order to keep the versioning of releases in sync with your package, the version string can be kept in the tags of a version control system, and automatically extracted with a tool such as
`setuptools_scm <https://pypi.org/project/setuptools-scm/>`_.

.. NOTE: maybe put in an example using setuptools_scm?

.. NOTE2: Is setuptools_scm the only one now?

Use an external version management tool
---------------------------------------

An external build tool can be used that manages the version string in both the SCM and source code, either directly or via an API:

A few tools you could use, in no particular order, and not necessarily complete:
`bump2version <https://pypi.org/project/bump2version>`_,
`changes <https://pypi.org/project/changes>`_,
`commitizen <https://pypi.org/project/commitizen>`_,
`versioneer <https://github.com/python-versioneer/python-versioneer>`_,
`zest.releaser <https://pypi.org/project/zest.releaser>`_,

.. NOTE: are these all still being maintained??

Dedicated file for the version string
-------------------------------------

Place the value in a simple ``VERSION`` text file and have both
:file:`setup.py` and the project code read it.

::

    with open(os.path.join(mypackage_root_dir, 'VERSION')) as version_file:
        version = version_file.read().strip()

An advantage with this technique is that it's not specific to Python.  Any
tool can read the version string.

.. warning::

    With this approach you must make sure that the ``VERSION`` file is included in
    all your source and binary distributions (e.g. add ``include VERSION`` to your
    :file:`MANIFEST.in`).


No longer recommend methods
---------------------------

These methods rely on importing of code during the build process, or dynamically generating the version at build time. These methods are prone to errors and security issues, but you may encounter them in older code bases.

#.  Set the value to a ``__version__`` global variable in a dedicated module in
    your project (e.g. :file:`version.py`), then have :file:`setup.py` read and
    ``exec`` the value into a variable.

    ::

        version = {}
        with open("...sample/version.py") as fp:
            exec(fp.read(), version)
        # later on we use: version['__version__']

    Example using this technique: `warehouse <https://github.com/pypa/warehouse/blob/64ca42e42d5613c8339b3ec5e1cb7765c6b23083/warehouse/__about__.py>`_.


#.  Set the value in :file:`setup.py`, and have the project code use the
    ``importlib.metadata`` API to fetch the value at build time.
    (``importlib.metadata`` was introduced in Python 3.8 and is available to
    older versions as the ``importlib-metadata`` project.)  An installed
    project's version can be fetched with the API as follows::

        import sys

        if sys.version_info >= (3, 8):
            from importlib import metadata
        else:
            import importlib_metadata as metadata

        assert metadata.version('pip') == '1.2.0'

    Be aware that the ``importlib.metadata`` API only knows about what's in the
    installation metadata, which is not necessarily the code that's currently
    imported.

    If a project uses this method to fetch its version string at build time, then its
    ``install_requires`` value needs to be edited to install
    ``importlib-metadata`` on pre-3.8 versions of Python like so::

        setup(
            ...
            install_requires=[
                ...
                'importlib-metadata >= 1.0 ; python_version < "3.8"',
                ...
            ],
            ...
        )

    An older (and less efficient) alternative to ``importlib.metadata`` is the
    ``pkg_resources`` API provided by ``setuptools``::

        import pkg_resources
        assert pkg_resources.get_distribution('pip').version == '1.2.0'

    If a project uses ``pkg_resources`` to fetch its own version at runtime,
    then ``setuptools`` must be added to the project's ``install_requires``
    list.

    Example using this technique: `setuptools <https://github.com/pypa/setuptools/blob/main/setuptools/version.py>`_.


#.  Set the value to ``__version__`` in ``sample/__init__.py`` and import
    ``sample`` in :file:`setup.py`.

    ::

        import sample
        setup(
            ...
            version=sample.__version__
            ...
        )

    .. warning::

        Although this technique used to be common, beware that it will fail if
        ``sample/__init__.py`` imports packages from ``install_requires``
        dependencies, which will very likely not be installed yet when
        :file:`setup.py` is run.
