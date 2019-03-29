.. _`Single sourcing the version`:

===================================
Single-sourcing the package version
===================================


There are many techniques to maintain a single source of truth for the version
number of your project:

#.  Read the file in :file:`setup.py` and parse the version with a regex.
    Example ( from `pip setup.py
    <https://github.com/pypa/pip/blob/master/setup.py#L12>`_)::

        here = os.path.abspath(os.path.dirname(__file__))

        def read(*parts):
            with codecs.open(os.path.join(here, *parts), 'r') as fp:
                return fp.read()

        def find_version(*file_paths):
            version_file = read(*file_paths)
            version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                      version_file, re.M)
            if version_match:
                return version_match.group(1)
            raise RuntimeError("Unable to find version string.")

        setup(
           ...
           version=find_version("package", "__init__.py")
           ...
        )

    .. note::

        This technique has the disadvantage of having to deal with complexities of regular expressions.

#.  Use an external build tool that either manages updating both locations, or
    offers an API that both locations can use.

    Few tools you could use, in no particular order, and not necessarily complete:
    `bump2version <https://pypi.org/project/bump2version>`_,
    `changes <https://pypi.org/project/changes>`_, `zest.releaser <https://pypi.org/project/zest.releaser>`_.


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
    ``pkg_resources`` API.

    ::

        import pkg_resources
        assert pkg_resources.get_distribution('pip').version == '1.2.0'

    Be aware that the ``pkg_resources`` API only knows about what's in the
    installation metadata, which is not necessarily the code that's currently
    imported.

    Example using this technique: `setuptools <https://github.com/pypa/setuptools/blob/master/setuptools/version.py>`_.


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
