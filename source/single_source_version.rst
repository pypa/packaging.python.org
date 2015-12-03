.. _`Single sourcing the version`:

===================================
Single-sourcing the Project Version
===================================

:Page Status: Complete
:Last Reviewed: 2015-12-03


There are many techniques to maintain a single source of truth for the version
number of your project:

#.  Read the file in ``setup.py`` and parse the version with a regex. Example (
    from `pip setup.py <https://github.com/pypa/pip/blob/1.5.6/setup.py#L33>`_)::

        import os.path
        import re

        def find_version(*file_paths):
            with open(os.path.join(os.path.dirname(__file__), *file_paths), 'rb') as f:
                match = re.search(br"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
            if match:
                return match.group(1)
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
    `bumpversion <https://pypi.python.org/pypi/bumpversion>`_,
    `changes <https://pypi.python.org/pypi/changes>`_, `zest.releaser <https://pypi.python.org/pypi/zest.releaser>`_.


#.  Set the value to a ``__version__`` global variable in a dedicated module in
    your project (e.g. ``version.py``), then have ``setup.py`` read and ``exec`` the
    value into a variable::

        import os.path

        base_dir = os.path.dirname(__file__)
        version = {}
        with open(os.path.join(base_dir, "module_name", "version.py"), 'rb') as fp:
            exec(fp.read(), version)

        setup(
           ...
           version=version['__version__']
           ...
        )

    Example using this technique: `warehouse <https://github.com/pypa/warehouse/blob/master/warehouse/__about__.py>`_.

#.  Place the value in a simple ``VERSION`` text file and have both ``setup.py``
    and the project code read it.

    ::

        with open(os.path.join(mypackage_root_dir, 'VERSION')) as version_file:
            version = version_file.read().strip()

    An advantage with this technique is that it's not specific to Python.  Any
    tool can read the version.

    .. warning::

        With this approach you must make sure that the ``VERSION`` file is included in
        all your source and binary distributions.

#.  Set the value in ``setup.py``, and have the project code use the
    ``pkg_resources`` API.

    ::

        import pkg_resources
        assert pkg_resources.get_distribution('pip').version == '1.2.0'

    Be aware that the ``pkg_resources`` API only knows about what's in the
    installation metadata, which is not necessarily the code that's currently
    imported.


#.  Set the value to ``__version__`` in ``sample/__init__.py`` and import
    ``sample`` in ``setup.py``.

    ::

        import sample
        setup(
            ...
            version=sample.__version__
            ...
        )

    Although this technique is common, beware that it will fail if
    ``sample/__init__.py`` imports packages from ``install_requires``
    dependencies, which will very likely not be installed yet when ``setup.py``
    is run.


#.  Keep the version number in the tags of a version control system (Git, Mercurial, etc)
    instead of in the code, and automatically extract it from there using
    `setuptools_scm <https://pypi.python.org/pypi/setuptools_scm>`_.
