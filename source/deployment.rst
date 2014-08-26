
========================
Development & Deployment
========================

:Page Status: Incomplete
:Last Reviewed: 2014-07-24

.. contents::


.. _`Supporting multiple Python versions`:

Supporting multiple Python versions
===================================

::

  FIXME

  Useful projects/resources to reference:

  - six
  - tox
  - Travis and Shining Panda CI
  - Ned Batchelder's What's in Which version pages
    - http://nedbatchelder.com/blog/201310/whats_in_which_python_3.html
      - http://nedbatchelder.com/blog/201109/whats_in_which_python.html
  - Lennart Regebro's "Porting to Python 3"
  - the Python 3 porting how to in the main docs
  - cross reference to the stable ABI discussion
    in the binary extensions topic (once that exists)
  - mention version classifiers for distribution metadata



Automated Testing and Continuous Integration
--------------------------------------------

Several hosted services for automated testing are available. These services
will typically monitor your source code repository (e.g. at
`Github <https://github.com>`_ or `Bitbucket <https://bitbucket.org>`_)
and run your package's test suite every time a new commit is made.

These services also offer facilities to run your package's test suite on
*multiple versions of Python*, giving rapid feedback about whether the code
will work, without the developer having to perform such tests themselves.

Wikipedia has an extensive `comparison
<http://en.wikipedia.org/wiki/Comparison_of_continuous_integration_software>`_
of many continuous-integration systems. There are two hosted services which
when used in conjunction provide automated testing across Linux, Mac and
Windows:

  - `Travis CI <https://travis-ci.org>`_ provides both a Linux and a Mac OSX
    environment. The Linux environment is Ubuntu 12.04 LTS Server Edition 64 bit
    while the OSX is 10.9.2 at the time of writing.
  - `Appveyor <http://www.appveyor.com>`_ provides a Windows environment
    (Windows Server 2012).

::

    TODO Either link to or provide example .yml files for these two
    services.

    TODO How do we keep the Travis Linux and OSX versions up-to-date in this
    document?

Both `Travis CI`_ and Appveyor_ require a `YAML
<http://www.yaml.org>`_-formatted file as specification for the instructions
for testing. If any tests fail, the output log for that specific configuration
can be inspected.

For Python packages that are intended to be deployed on both Python 2 and 3
with a single-source strategy, there are a number of options.
Supporting multiple hardware platforms
======================================

::

  FIXME

  Meaning: x86, x64, ARM, others?

  For Python-only packages, it *should* be straightforward to deploy on all
  platforms where Python can run.

  For packages with binary extensions, deployment is major headache.  Not only
  must the extensions be built on all the combinations of operating system and
  hardware platform, but they must also be tested, preferably on continuous
  integration platforms.  The issues are similar to the "multiple python
  versions" section above, not sure whether this should be a separate section.
  Even on Windows x64, both the 32 bit and 64 bit versions of Python enjoy
  significant usage.


.. _`Single sourcing the version`:

Single-sourcing the version across ``setup.py`` and your project
================================================================

There are a few techniques to store the version in your project code without duplicating the value stored in
``setup.py``:

#.  Read the file in ``setup.py`` and parse the version with a regex. Example (
    from `pip setup.py <https://github.com/pypa/pip/blob/1.5.6/setup.py#L33>`_)::

        def read(*names, **kwargs):
            return io.open(
                os.path.join(os.path.dirname(__file__), *names),
                encoding=kwargs.get("encoding", "utf8")
            ).read()

        def find_version(*file_paths):
            version_file = read(*file_paths)
            version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                      version_file, re.M)
            if version_match:
                return version_match.group(1)
            raise RuntimeError("Unable to find version string.")

        setup(
           ...
           version=find_version("package/__init__.py")
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
    your package (e.g. ``version.py``), then have ``setup.py`` read and ``exec`` the
    value into a variable.

    Using ``execfile``:

    ::

        execfile('...sample/version.py')
        assert __version__ == '1.2.0'

    Using ``exec``:

    ::

        version = {}
        with open("...sample/version.py") as fp:
            exec(fp.read(), version)
        assert version['__version__'] == '1.2.0'

    Example using this technique: `warehouse <https://github.com/pypa/warehouse/blob/master/warehouse/__about__.py>`_.

#.  Place the value in a simple ``VERSION`` text file and have both ``setup.py``
    and the project code read it.

    ::

        version_file = open(os.path.join(mypackage_root_dir, 'VERSION'))
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


.. _`PyPI mirrors and caches`:

PyPI mirrors and caches
=======================

Mirroring or caching of PyPI can be used to speed up local package
installation, allow offline work, handle corporate firewalls or just plain
Internet flakiness.

Three options are available in this area:

1. pip provides local caching options,
2. devpi provides higher-level caching option, potentially shared amongst
   many users or machines, and
3. bandersnatch provides a local complete mirror of all packages on PyPI.


Caching with pip
----------------

pip provides a number of facilities for speeding up installation by using
local cached copies of packages:

1. `Fast & local installs
   <https://pip.pypa.io/en/latest/user_guide.html#fast-local-installs>`_ by
   downloading all the requirements for a project and then pointing pip at
   those downloaded files instead of going to PyPI.
2. A variation on the above which pre-builds the installation files for
   the requirements using `pip wheel
   <http://pip.readthedocs.org/en/latest/reference/pip_wheel.html>`_::

    $ pip wheel --wheel-dir=/tmp/wheelhouse SomePackage
    $ pip install --no-index --find-links=/tmp/wheelhouse SomePackage


Caching with devpi
------------------

devpi is a caching proxy server which you run on your laptop, or some other
machine you know will always be available to you. See the `devpi
documentation for getting started`__.

__ http://doc.devpi.net/latest/quickstart-pypimirror.html


Complete mirror with bandersnatch
----------------------------------

bandersnatch will set up a complete local mirror of all packages on PyPI
(externally-hosted packages are not mirrored). See the
`bandersnatch documentation for getting that going`__.

__ https://bitbucket.org/pypa/bandersnatch/overview

A benefit of devpi is that it will create a mirror which includes packages
that are external to PyPI, unlike bandersnatch which will only cache packages
hosted on PyPI.


.. _`Patching & Forking`:

Patching & Forking
==================

::

  FIXME

  - locally patch 3rd-part projects to deal with unfixed bugs
     - old style pkg_resources "patch releases":  1.3-fork1
     - PEP440's local identifiers: http://www.python.org/dev/peps/pep-0440/#local-version-identifiers
  - fork and publish when you need to publish a project that depends on the fork
     (DONT use dependency links)



OS Packaging & Installers
=========================

::

  FIXME

  - Building rpm/debs for projects
  - Building rpms/debs for whole virtualenvs
  - Building Windows installers for Python projects
  - Building Mac OS X installers for Python projects



Application Bundles
===================

::

  FIXME

  - py2exe/py2app/PEX
  - wheels kinda/sorta


Configuration Management
========================

::

  FIXME

  puppet/salt/chef solutions



Fabric/SSH Solutions
====================

::

  FIXME
