:orphan:

=================================
Supporting Windows using Appveyor
=================================

:Page Status: Obsolete
:Last Reviewed: 2015-12-03

This section covers how to use the free `Appveyor`_ continuous integration
service to provide Windows support for your project. This includes testing
the code on Windows, and building Windows-targeted binaries for projects
that use C extensions.


Background
==========

Many projects are developed on Unix by default, and providing Windows support
can be a challenge, because setting up a suitable Windows test environment is
non-trivial, and may require buying software licenses.

The Appveyor service is a continuous integration service, much like the
better-known `Travis`_ service that is commonly used for testing by projects
hosted on `GitHub`_. However, unlike Travis, the build workers on Appveyor are
Windows hosts and have the necessary compilers installed to build Python
extensions.

Windows users typically do not have access to a C compiler, and therefore are
reliant on projects that use C extensions distributing binary wheels on PyPI in
order for the distribution to be installable via ``python -m pip install <dist>``. By
using Appveyor as a build service (even if not using it for testing) it is
possible for projects without a dedicated Windows environment to provide
Windows-targeted binaries.

Setting up
==========

In order to use Appveyor to build Windows wheels for your project, you must
have an account on the service. Instructions on setting up an account are given
in `the Appveyor documentation <https://www.appveyor.com/docs/>`__. The free tier
of account is perfectly adequate for open source projects.

Appveyor provides integration with `GitHub`_ and `Bitbucket`_, so as long as
your project is hosted on one of those two services, setting up Appveyor
integration is straightforward.

Once you have set up your Appveyor account and added your project, Appveyor will
automatically build your project each time a commit occurs. This behaviour will
be familiar to users of Travis.

Adding Appveyor support to your project
=======================================

In order to define how Appveyor should build your project, you need to add an
:file:`appveyor.yml` file to your project. The full details of what can be
included in the file are covered in the Appveyor documentation. This guide will
provide the details necessary to set up wheel builds.

Appveyor includes by default all of the compiler toolchains needed to build
extensions for Python. For Python 2.7, 3.5+ and 32-bit versions of 3.3 and 3.4,
the tools work out of the box. But for 64-bit versions of Python 3.3 and 3.4,
there is a small amount of additional configuration needed to let distutils
know where to find the 64-bit compilers. (From 3.5 onwards, the version of
Visual Studio used includes 64-bit compilers with no additional setup).

appveyor.yml
------------

.. literalinclude:: appveyor-sample/appveyor.yml
   :language: yaml
   :linenos:

This file can be downloaded from `here <https://raw.githubusercontent.com/pypa/python-packaging-user-guide/master/source/guides/appveyor-sample/appveyor.yml>`__.

The :file:`appveyor.yml` file must be located in the root directory of your
project. It is in ``YAML`` format, and consists of a number of sections.

The ``environment`` section is the key to defining the Python versions for
which your wheels will be created. Appveyor comes with Python 2.6, 2.7, 3.3,
3.4 and 3.5 installed, in both 32-bit and 64-bit builds. The example file
builds for all of these environments except Python 2.6. Installing for Python
2.6 is more complex, as it does not come with pip included. We don't support
2.6 in this document (as Windows users still using Python 2 are generally able
to move to Python 2.7 without too much difficulty).

The ``install`` section uses pip to install any additional software that the
project may require. The only requirement for building wheels is the ``wheel``
project, but projects may wish to customise this code in certain circumstances
(for example, to install additional build packages such as ``Cython``, or test
tools such as ``tox``).

The ``build`` section simply switches off builds - there is no build step needed
for Python, unlike languages like ``C#``.

The main sections that will need to be tailored to your project are ``test_script``
and ``after_test``.

The ``test_script`` section is where you will run your project's tests. The
supplied file runs your test suite using ``setup.py test``. If you are only
interested in building wheels, and not in running your tests on Windows, you
can replace this section with a dummy command such as ``echo Skipped Tests``.
You may wish to use another test tool, such as ``nose`` or :file:`py.test`.  Or
you may wish to use a test driver like ``tox`` - however if you are using
``tox`` there are some additional configuration changes you will need to
consider, which are described below.

The ``after_test`` runs once your tests have completed, and so is where the
wheels should be built. Assuming your project uses the recommended tools
(specifically, ``setuptools``) then the ``setup.py bdist_wheel`` command
will build your wheels.

Note that wheels will only be built if your tests succeed. If you expect your
tests to fail on Windows, you can skip them as described above.


Support script
--------------

The :file:`appveyor.yml` file relies on a single support script, which sets up
the environment to use the SDK compiler for 64-bit builds on Python 3.3 and
3.4.  For projects which do not need a compiler, or which don't support 3.3 or
3.4 on 64-bit Windows, only the :file:`appveyor.yml` file is needed.

`build.cmd <https://raw.githubusercontent.com/pypa/python-packaging-user-guide/master/source/guides/appveyor-sample/build.cmd>`__
is a Windows batch script that runs a single command in an environment with the
appropriate compiler for the selected Python version. All you need to do is to
set the single environment variable ``DISTUTILS_USE_SDK`` to a value of ``1``
and the script does the rest. It sets up the SDK needed for 64-bit builds of
Python 3.3 or 3.4, so don't set the environment variable for any other builds.

You can simply download the batch file and include it in your project unchanged.


Access to the built wheels
--------------------------

When your build completes, the built wheels will be available from the Appveyor
control panel for your project. They can be found by going to the build status
page for each build in turn. At the top of the build output there is a series
of links, one of which is "Artifacts". That page will include a list of links
to the wheels for that Python version / architecture. You can download those
wheels and upload them to PyPI as part of your release process.

Additional notes
================

Testing with tox
----------------

Many projects use the :doc:`Tox <tox:index>` tool to run their tests. It ensures that tests
are run in an isolated environment using the exact files that will be distributed
by the project.

In order to use ``tox`` on Appveyor there are a couple of additional considerations
(in actual fact, these issues are not specific to Appveyor, and may well affect
other CI systems).

1. By default, ``tox`` only passes a chosen subset of environment variables to the
   test processes. Because ``distutils`` uses environment variables to control the
   compiler, this "test isolation" feature will cause the tests to use the wrong
   compiler by default.

   To force ``tox`` to pass the necessary environment variables to the subprocess,
   you need to set the ``tox`` configuration option ``passenv`` to list the additional
   environment variables to be passed to the subprocess. For the SDK compilers, you
   need

        - ``DISTUTILS_USE_SDK``
        - ``MSSdk``
        - ``INCLUDE``
        - ``LIB``

    The ``passenv`` option can be set in your :file:`tox.ini`, or if you prefer
    to avoid adding Windows-specific settings to your general project files, it
    can be set by setting the ``TOX_TESTENV_PASSENV`` environment variable. The
    supplied :file:`build.cmd` script does this by default whenever
    ``DISTUTILS_USE_SDK`` is set.

2. When used interactively, ``tox`` allows you to run your tests against multiple
   environments (often, this means multiple Python versions). This feature is not as
   useful in a CI environment like Travis or Appveyor, where all tests are run in
   isolated environments for each configuration. As a result, projects often supply
   an argument ``-e ENVNAME`` to ``tox`` to specify which environment to use (there
   are default environments for most versions of Python).

    However, this does *not* work well with a Windows CI system like Appveyor, where
    there are (for example) two installations of Python 3.4 (32-bit and 64-bit)
    available, but only one ``py34`` environment in ``tox``.

    In order to run tests using ``tox``, therefore, projects should probably use the
    default ``py`` environment in ``tox``, which uses the Python interpreter that
    was used to run ``tox``. This will ensure that when Appveyor runs the tests, they
    will be run with the configured interpreter.

    In order to support running under the ``py`` environment, it is possible that
    projects with complex ``tox`` configurations might need to modify their
    :file:`tox.ini` file. Doing so is, however, outside the scope of this
    document.

Automatically uploading wheels
------------------------------

It is possible to request Appveyor to automatically upload wheels. There is a
``deployment`` step available in :file:`appveyor.yml` that can be used to (for
example) copy the built artifacts to a FTP site, or an Amazon S3 instance.
Documentation on how to do this is included in the Appveyor guides.

Alternatively, it would be possible to add a ``twine upload`` step to the
build.  The supplied :file:`appveyor.yml` does not do this, as it is not clear
that uploading new wheels after every commit is desirable (although some
projects may wish to do this).

External dependencies
---------------------

The supplied scripts will successfully build any distribution that does not
rely on 3rd party external libraries for the build.

It is possible to add steps to the :file:`appveyor.yml` configuration
(typically in the "install" section) to download and/or build external
libraries needed by the distribution. And if needed, it is possible to add
extra configuration for the build to supply the location of these libraries to
the compiler. However, this level of configuration is beyond the scope of this
document.


Support scripts
---------------

For reference, the SDK setup support script is listed here:

``appveyor-sample/build.cmd``

.. literalinclude:: appveyor-sample/build.cmd
   :language: bat
   :linenos:

.. _Appveyor: https://www.appveyor.com/
.. _Travis: https://travis-ci.org/
.. _GitHub: https://github.com
.. _Bitbucket: https://bitbucket.org/
