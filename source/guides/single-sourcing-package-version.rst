.. _`Single sourcing the version`:

===================================
Single-sourcing the package version
===================================


There are many techniques to maintain a single source of truth for the version
number of your project:

#.  Read the file with version info in :file:`setup.py` and parse version line.
    Example::

        import os

        def get_version(rel_path):
            current_dir = os.path.abspath(os.path.dirname(__file__))
            version_file = os.path.join(current_dir, rel_path)
            for line in open(version_file, 'rb'):
                # Decode to unicode for PY2/PY3 in a fail-safe way
                line = line.decode('cp437')
                if line.startswith('__version__'):
                    # __version__ = "0.9"
                    delim = '\"' if '\"' in line else '\''
                    return line.split(delim)[1]

        setup(
           ...
           version=get_version("package/__init__.py"),
           ...
        )

#.  Use an external build tool that either manages updating both locations, or
    offers an API that both locations can use.

    Few tools you could use, in no particular order, and not necessarily complete:
    `bumpversion <https://pypi.org/project/bumpversion>`_,
    `changes <https://pypi.org/project/changes>`_, `zest.releaser <https://pypi.org/project/zest.releaser>`_.


#.  Set the value to a ``__version__`` global variable in a dedicated module in
    your project (e.g. :file:`version.py`), then have :file:`setup.py` read and
    ``exec`` the value into a variable.

    Using ``execfile``:

    ::

        execfile('...sample/version.py')
        # now we have a `__version__` variable
        # later on we use: __version__

    Using ``exec``:

    ::

        version = {}
        with open("...sample/version.py") as fp:
            exec(fp.read(), version)
        # later on we use: version['__version__']

    Example using this technique: `warehouse <https://github.com/pypa/warehouse/blob/master/warehouse/__about__.py>`_.

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
    ``pkg_resources`` API.

    ::

        import pkg_resources
        assert pkg_resources.get_distribution('pip').version == '1.2.0'

    Be aware that the ``pkg_resources`` API only knows about what's in the
    installation metadata, which is not necessarily the code that's currently
    imported.


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
    `setuptools_scm <https://pypi.org/project/setuptools_scm>`_.
