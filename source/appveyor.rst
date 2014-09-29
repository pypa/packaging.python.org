=================================================
Building Binary Wheels for Windows using Appveyor
=================================================

:Page Status: Incomplete
:Last Reviewed: 2014-09-27

This section covers how to use the free `Appveyor`_ continuous integration
service to build Windows-targeted binary wheels for your project.

.. contents::


Background
==========

Windows users typically do not have access to a C compiler, and therefore are
reliant on projects that use C extensions distributing binary wheels on PyPI in
order for the distribution to be installable via ``pip install dist```.
However, it is often the case that projects which are intended to be
cross-platform are developed on Unix, and so the project developers *also* have
the problem of lack of access to a Windows compiler.

The Appveyor service is a continuous integration service, much like the
better-known `Travis`_ service that is commonly used for testing by projects
hosted on `Github`_. However, unlike Travis, the build workers on Appveyor are
Windows hosts and have the necessary compilers installed to build Python
extensions.

Setting Up
==========

In order to use Appveyor to build Windows wheels for your project, you must
have an account on the service. Instructions on setting up an account are given
in `the Appveyor documentation <http://www.appveyor.com/docs>`__. The free tier
of account is perfectly adequate for open source projects.

Appveyor provides integration with `Github`_ and `Bitbucket`_, so as long as
your project is hosted on one of those two services, setting up Appveyor
integration is straightforward.

Once you have set up your Appveyor account and added your project, Appveyor will
automatically build your project each time a commit occurs. This behaviour will
be familiar to users of Travis.

Adding Appveyor support to your project
=======================================

In order to define how Appveyor should build your project, you need to add an
``appveyor.yml`` file to your project. The full details of what can be included
in the file are covered in the Appveyor documentation. This guide will provide
the details necessary to set up wheel builds.

appveyor.yml
------------

.. literalinclude:: code/appveyor.yml
   :language: yaml
   :linenos:

This file can be downloaded from `here <https://raw.githubusercontent.com/pypa/python-packaging-user-guide/master/source/code/appveyor.yml>`__.

The ``appveyor.yml`` file must be located in the root directory of your
project. It is in ``YAML`` format, and consists of a number of sections.

The ``environment`` section is the key to defining the Python versions for
which your wheels will be created. Appveyor comes with Python 2.7, 3.3 and 3.4
installed, in both 32-bit and 64-bit builds. The example file builds for all of
these environments.

The ``install`` section installs any additional software that the project may
require. The supplied code installs ``pip`` (if needed) and ``wheel``. Projects
may wish to customise this code in certain circumstances (for example, to install
additional build packages such as ``Cython``, or test tools such as ``tox``).

The ``build`` section simply switches off builds - there is no build step needed
for Python, unlike languages like ``C#``.

The ``test_script`` section is technically not needed. The supplied file runs
your test suite using ``setup.py test``. You may wish to use another test tool
such as ``tox`` or ``py.test``. Or you could skip the test (but why would you,
unless your tests are expected to fail on Windows?) by replacing the script with
a simple ``echo Skipped`` command.

The ``after_test`` command is where the wheels are built. Assuming your project
uses the recommended tools (specifically, ``setuptools``) then the
``setup.py bdist_wheel`` command will build your wheels.

Note that wheels will only be built if your tests succeed. If you expect your
tests to fail on Windows, you can skip them as described above.


Support scripts
---------------

The ``appveyor.yml`` file relies on two support scripts. The code assumes that
these will be placed in a subdirectory named ``appveyor`` at the root of your
project.

`appveyor/run_with_compiler.cmd <https://raw.githubusercontent.com/pypa/python-packaging-user-guide/master/source/code/run_with_compiler.cmd>`__
is a Windows batch script that runs a single command in an environment with the
appropriate compiler for the selected Python version.

`appveyor/install.ps1 <https://raw.githubusercontent.com/pypa/python-packaging-user-guide/master/source/code/install.ps1>`__ is a Powershell
script that downloads and installs any missing Python versions, installs
``pip`` into the Python ``site-packages`` and downloads and installs the latest
``wheel`` distribution. Steps that are not needed are omitted, so in practice,
the Python install will never be run (it is present for advanced users who want
to install additional versions of Python not supplied by Appveyor) and the
``pip`` install will be omitted for Python 3.4, where pip is installed as
standard.

You can simply download these two files and include them in your project
unchanged.


Access to the built wheels
--------------------------

When your build completes, the built wheels will be available from the Appveyor
control panel for your project. They can be found by going to the build status
page for each build in turn. At the top of the build output there is a series
of links, one of which is "Artifacts". That page will include a list of links
to the wheels for that Python version / architecture. You can download those
wheels and upload them to PyPI as part of your release process.

Additional Notes
================

Automatically uploading wheels
------------------------------

It is possible to request Appveyor to automatically upload wheels. There is a
``deployment`` step available in ``appveyor.yml`` that can be used to (for
example) copy the built artifacts to a FTP site, or an Amazon S3 instance.
Documentation on how to do this is included in the Appveyor guides.

Alternatively, it would be possible to add a ``twine upload`` step to the
build.  The supplied ``appveyor.yml`` does not do this, as it is not clear that
uploading new wheels after every commit is desirable (although some projects
may wish to do this).

External dependencies
---------------------

The supplied scripts will successfully build any distribution that does not
rely on 3rd party external libraries for the build. It would be possible for an
individual project to add code to the ``install.ps1`` script to make external
libraries available to the build, but this is of necessity specific to
individual projects.

Should projects develop scripts showing how to do this, references will be
added to this guide at a later date.

Possible issues
---------------

The webhooks installed by Appveyor for github projects report on the build
success on the project page, in much the same way as the Travis webhooks do.
There is a limitation on the github reporting API, which means that only one
build result is currently shown for a project - so if your project uses both
Travis and Appveyor, only one will be displayed. The github team are aware of
this limitation, and are planning on fixing it. In the meantime, however, it
can sometimes be necessary to check the build results by going to the project
page in the CI system directly.

Note that failed builds are *always* reported by github, so this issue does not
mean that projects could find failures being missed.

Support scripts
---------------

For reference, the two support scripts are listed here:

``code/run_with_compiler.cmd``

.. literalinclude:: code/run_with_compiler.cmd
   :language: bat
   :linenos:

``code/install.ps1``

.. literalinclude:: code/install.ps1
   :language: powershell
   :linenos:

.. _Appveyor: http://www.appveyor.com/
.. _Travis: https://travis-ci.org/
.. _Github: https://github.org/
.. _Bitbucket: https://bitbucket.org/
