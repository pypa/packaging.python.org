.. _`Single sourcing the version`:

===================================
Single-sourcing the package version
===================================

.. todo:: Update this page for build backends other than setuptools.

There are many techniques to maintain a single source of truth for the version
number of your project:

#.  Read the file in :file:`setup.py` and get the version. Example (from `pip setup.py
    <https://github.com/pypa/pip/blob/main/setup.py>`_)::

        import codecs
        import os.path

        def read(rel_path):
            here = os.path.abspath(os.path.dirname(__file__))
            with codecs.open(os.path.join(here, rel_path), 'r') as fp:
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

    .. note::

       As of the release of setuptools 46.4.0, one can accomplish the same
       thing by instead placing the following in the project's
       :file:`setup.cfg` file (replacing "package" with the import name of the
       package):

       .. code-block:: ini

           [metadata]
           version = attr: package.__version__

       As of the release of setuptools 61.0.0, one can specify the
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

#.  Use an external build tool that either manages updating both locations, or
    offers an API that both locations can use.

    Few tools you could use, in no particular order, and not necessarily complete:
    `bump2version <https://pypi.org/project/bump2version>`_,
    `changes <https://pypi.org/project/changes>`_,
    `commitizen <https://pypi.org/project/commitizen>`_,
    `zest.releaser <https://pypi.org/project/zest.releaser>`_.


#.  Set the value to a ``__version__`` global variable in a dedicated module in
    your project (e.g. :file:`version.py`), then have :file:`setup.py` read and
    ``exec`` the value into a variable.

    ::

        version = {}
        with open("...sample/version.py") as fp:
            exec(fp.read(), version)
        # later on we use: version['__version__']

    Example using this technique: `warehouse <https://github.com/pypa/warehouse/blob/64ca42e42d5613c8339b3ec5e1cb7765c6b23083/warehouse/__about__.py>`_.

#.  Place the value in a simple ``VERSION`` text file and have both
    :file:`setup.py` and the project code read it.

    ::

        with open(os.path.join(mypackage_root_dir, 'VERSION')) as version_file:
            version = version_file.read().strip()

    An advantage with this technique is that it's not specific to Python.  Any
    tool can read the version.

    .. warning::

        With this approach you must make sure that the ``VERSION`` file is included in
        all your source and binary distributions (e.g. add ``include VERSION`` to your
        :file:`MANIFEST.in`).

#.  Set the value in :file:`setup.py`, and have the project code use the
    ``importlib.metadata`` API to fetch the value at runtime.
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

    If a project uses this method to fetch its version at runtime, then its
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

        Although this technique is common, beware that it will fail if
        ``sample/__init__.py`` imports packages from ``install_requires``
        dependencies, which will very likely not be installed yet when
        :file:`setup.py` is run.


#.  Keep the version number in the tags of a version control system (Git, Mercurial, etc)
    instead of in the code, and automatically extract it from there using
    `setuptools_scm <https://pypi.org/project/setuptools-scm/>`_.
