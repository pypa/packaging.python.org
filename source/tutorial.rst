=================================
Installation & Packaging Tutorial
=================================

:Page Status: Incomplete
:Last Reviewed: 2014-03-10

.. contents::

Installing the Tools
====================

For Installation or Packaging, you'll minimally want :ref:`pip` and
:ref:`setuptools`, and in most cases, :ref:`virtualenv` (unless you're using
`pyvenv`_).

Additionally, for building wheels, you'll need :ref:`wheel`, and for uploading
to :term:`PyPI <Python Package Index (PyPI)>`, you'll need :ref:`twine`.

We recommend the following installation sequence:

1. Install :ref:`pip` and :ref:`setuptools`:

   If you have Python 3.4:

   * Your distribution will likely already have the ``pip`` command available
     by default (and setuptools will be installed as well).  If ``pip`` is not
     available, run: ``python -m ensurepip --upgrade``, which will install pip
     and setuptools.

   If you have less than Python 3.4:

   * Securely Download `get-pip.py
     <https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_ [1]_

   * Run ``python get-pip.py``.  This will install or upgrade pip.
     Additionally, it will install setuptools if it's not installed already. To
     upgrade an existing setuptools, run ``pip install -U setuptools`` [2]_ [3]_

2. Optionally, Create a virtual environment (See :ref:`section below <Creating
   and using Virtual Environments>` for details):

   Using :ref:`virtualenv`:

   ::

    pip install virtualenv
    virtualenv <DIR>
    source <DIR>/bin/activate

   Using `pyvenv`_: [5]_

   ::

    pyvenv <DIR>
    source <DIR>/bin/activate


3. For building wheels: ``pip install wheel`` [2]_

4. For uploading distributions: ``pip install twine`` [2]_


.. _`Creating and using Virtual Environments`:

Creating and using Virtual Environments
=======================================

Currently, there are two viable tools for creating Python virtual environments:
:ref:`virtualenv` and `pyvenv`_. `pyvenv`_ is only available in Python 3.3 &
3.4, and only in Python 3.4, is :ref:`pip` & :ref:`setuptools` installed into
environments by default, whereas :ref:`virtualenv` supports Python 2.6 thru
Python 3.4 and :ref:`pip` & :ref:`setuptools` are installed by default in every
version.

The basic problem being addressed with virtual environments is one of
dependencies and versions, and indirectly permissions. Imagine you have an
application that needs version 1 of LibFoo, but another application requires
version 2. How can you use both these applications? If you install everything
into /usr/lib/python2.7/site-packages (or whatever your platform’s standard
location is), it’s easy to end up in a situation where you unintentionally
upgrade an application that shouldn’t be upgraded.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you can’t install packages into the global site-packages
directory? For instance, on a shared host.

In all these cases, virtualenv can help you. It creates an environment that has
its own installation directories, that doesn’t share libraries with other
virtualenv environments (and optionally doesn’t access the globally installed
libraries either).

The basic usage is like so:

Using :ref:`virtualenv`:

::

 virtualenv <DIR>
 source <DIR>/bin/activate


Using `pyvenv`_:

::

 pyvenv <DIR>
 source <DIR>/bin/activate


For more information, see the `virtualenv <http://www.virtualenv.org>`_ docs or
the `pyvenv`_ docs.

Note that in some cases, the `user installation scheme
<http://docs.python.org/install/index.html#alternate-installation-the-user-scheme>`_
can offer similar benefits as Virtual Environments. For more information see the
`User Installs
<https://pip.readthedocs.org/en/latest/user_guide.html#user-installs>`_ section
from the pip docs.


Installing Python packages
==========================

:ref:`pip` is the recommended installer, and supports various requirement forms
and options.  For details, see the `pip docs
<http://www.pip-installer.org/en/latest/>`_.

Below are the most common use cases:

Install `SomePackage` and it's dependencies from :term:`PyPI <Python Package
Index (PyPI)>` using :ref:`pip:Requirement Specifiers`

::

 pip install SomePackage           # latest version
 pip install SomePackage==1.0.4    # specific version
 pip install 'SomePackage>=1.0.4'  # minimum version


Install a list of requirements specified in a :ref:`Requirements File
<pip:Requirements Files>`.

::

 pip install -r requirements.txt


Upgrade an already installed `SomePackage` to the latest from PyPI.

::

 pip install --upgrade SomePackage


Install a project from VCS in "editable" mode.  For a full breakdown of the
syntax, see pip's section on :ref:`VCS Support <pip:VCS Support>`.

::

 pip install -e git+https://git.repo/some_pkg.git#egg=SomePackage          # from git
 pip install -e hg+https://hg.repo/some_pkg.git#egg=SomePackage            # from mercurial
 pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomePackage         # from svn
 pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomePackage  # from a branch


Install a particular source archive file.

::

 pip install ./downloads/SomePackage-1.0.4.tar.gz
 pip install http://my.package.repo/SomePackage-1.0.4.zip


Install from an alternate index

::

 pip install --index-url http://my.package.repo/simple/ SomePackage


Search an additional index during install, in addition to :term:`PyPI <Python
Package Index (PyPI)>`

::

 pip install --extra-index-url http://my.package.repo/simple SomePackage


Install from a local directory containing archives (and don't check :term:`PyPI
<Python Package Index (PyPI)>`)

::

 pip install --no-index --find-links=file:///local/dir/ SomePackage
 pip install --no-index --find-links=/local/dir/ SomePackage
 pip install --no-index --find-links=relative/dir/ SomePackage


Find pre-release and development versions, in addition to stable versions.  By
default, pip only finds stable versions.

::

 pip install --pre SomePackage



Installing Wheels
=================

:term:`Wheel` is a new pre-built alternative to :term:`sdist <Source
Distribution (or "sdist")>` that provides faster installation, especially when a
project contains compiled extensions.

For a detailed comparison of wheel to it's :term:`Egg` predecessor, see
:ref:`Wheel vs Egg`.

As of v1.5, :ref:`pip` prefers :term:`wheels <Wheel>` over :term:`sdists <Source
Distribution (or "sdist")>` when searching indexes.

Although wheels are `becoming more common <http://pythonwheels.com>`_ on
:term:`PyPI <Python Package Index (PyPI)>`, if you want all of your dependencies
converted to wheel, do the following (assuming you're using a :ref:`Requirements
File <pip:Requirements Files>`):

::

 pip wheel --wheel-dir=/local/wheels -r requirements.txt

And then to install those requirements just using your local directory of wheels
(and not from PyPI):

::

 pip install --no-index --find-links=/local/wheels -r requirements.txt



Creating your own Project
=========================

In the sections below, we'll reference the `PyPA sample project
<https://github.com/pypa/sampleproject>`_. which aims to exemplify best
practices for packaging Python projects using :ref:`setuptools`.


Layout
------

The critical requirement for creating projects using :ref:`setuptools` is to
have a ``setup.py``. For an example, see `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_.  We'll cover the
components of ``setup.py`` in the sections below.

Although it's not required, most projects will organize the code using a `single
top-level package <https://github.com/pypa/sampleproject/tree/master/sample>`_,
that's named the same as the project.

Additionally, most projects will contain the following files:

* A `README <https://github.com/pypa/sampleproject/blob/master/README.rst>`_ for
  explaining the project.
* A `setup.cfg <https://github.com/pypa/sampleproject/blob/master/setup.cfg>`_
  that contains option defaults for ``setup.py`` commands.
* A `MANIFEST.in
  <https://github.com/pypa/sampleproject/blob/master/MANIFEST.in>`_ that defines
  the files that will be included in the project distribution when it's
  packaged.


Name
----

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

  name = 'sample'

This will determine how your project is listed on :term:`PyPI <Python Package
Index (PyPI)>`. For details on permitted characters, see the `name
<http://legacy.python.org/dev/peps/pep-0426/#name>`_ section from :ref:`PEP426
<PEP426s>`.


Version
-------

from `sampleproject/sample/__init__.py
<https://github.com/pypa/sampleproject/blob/master/sample/__init__.py>`_

::

  __version__ = '1.2.0'

Projects should aim to comply with the `version scheme
<http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
specified in :ref:`PEP440 <PEP440s>`.

Some Examples:

::

  1.2.0.dev1  # Development release
  1.2.0a1     # Alpha Release
  1.2.0b1     # Beta Release
  1.2.0rc1    # RC Release
  1.2.0       # Final Release
  1.2.0.post1 # Post Release


Packages
--------

Metadata
--------

Dependencies
------------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

 install_requires = ['peppercorn']

"install_requires" should be used to specify what dependences a project
minimally needs to run. When the project is installed by :ref:`pip`, this is the
specification that is used to install it’s dependencies.

For more on using "install_requires" see :ref:`install_requires vs Requirements files`.

Package Data
------------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

 package_data={
     'sample': ['package_data.dat'],
 }


Often, additional files need to be installed into a package. These files are
often data that’s closely related to the package’s implementation, or text files
containing documentation that might be of interest to programmers using the
package. These files are called "package data".

The value must be a mapping from package name to a list of relative path names
that should be copied into the package. The paths are interpreted as relative to
the directory containing the package.

For more information, see `Including Data Files
<http://pythonhosted.org/setuptools/setuptools.html#including-data-files>`_ from
the `setuptools docs <http://pythonhosted.org/setuptools/setuptools.html>`_


Data Files
----------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

  data_files=[('my_data', ['data/data_file'])],

Although configuring ``package_data`` is recommended, in some cases you may need
to place data files outside of your packages.  This directive allows you to do
that.

Each (directory, files) pair in the sequence specifies the installation
directory and the files to install there. If directory is a relative path, it is
interpreted relative to the installation prefix (Python’s sys.prefix for
pure-Python packages, sys.exec_prefix for packages that contain extension
modules). Each file name in files is interpreted relative to the setup.py script
at the top of the package source distribution.

For more information see the distutils section on `Installing Additional Files
<http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files>`_.

.. note::

  :ref:`setuptools` allows absolute "data_files" paths, and pip honors them as
  absolute, when intalling from :term:`sdist <Source Distribution (or
  "sdist")>`.  This is not true, when installing from :term:`wheel`
  distributions. Wheels don't support absolute paths, and they end up being
  installed relative to "site-packages".  For discussion see `wheel Issue #92
  <https://bitbucket.org/pypa/wheel/issue/92>`_.

Manifest
--------

Scripts
-------

Universal Wheels
----------------

from `sampleproject/setup.cfg
<https://github.com/pypa/sampleproject/blob/master/setup.cfg>`_

::

 [wheel]
 universal=1

The benefit of this setting, is that ``python setup.py bdist_wheel`` will then
generate a wheel that will be installable anywhere (i.e. be "Universal"),
similar to an :term:`sdist <Source Distribution (or "sdist")>`.

Only use this setting, if:

1. Your project runs on Python 2 and 3 with no changes (i.e. it does not
   require 2to3).
2. Your project does not have any C extensions.

Beware that ``bdist_wheel`` does not currently have any checks to warn you if
use the setting inappropriately.

If your project has optional C extensions, it is recommended not to publish a
universal wheel, because pip will prefer the wheel over a source installation,
and prevent he possibility of building the extension.


Installing your project in Editable mode
========================================

To install your project in "develop" or "editable" mode (i.e. to have your
project installed, but still editable for development)

::

 cd myproject
 python setup.py develop    # the setuptools way
 pip install -e .           # the pip way



Building & Packaging your Project
=================================

Build a source distribution

::

 python setup.py sdist


Build a wheel

::

 python setup.py bdist_wheel


Note that PyPI currently only allows uploading platform-specific wheels for
Windows and Mac OS X.


Uploading your Project to PyPI
==============================

::

  FIXME:  cover registration and pypi ui


Upload your distributions with :ref:`twine`

::

 twine upload dist/*


----

.. [1] "Secure" in this context means using a modern browser or a
       tool like `curl` that verifies SSL certificates when downloading from
       https URLs.

.. [2] Depending on your platform, this may require root or Administrator access.

.. [3] On Linux and OSX, pip and setuptools will usually be available for the system
       python from a system package manager (e.g. `yum` or `apt-get` for linux,
       or `homebrew` for OSX). Unfortunately, there is often delay in getting
       the latest version this way, so in most cases, you'll want to use the
       instructions.

.. [4] For more information on creating projects, see the `Setuptools Docs
       <http://pythonhosted.org/setuptools/setuptools.html>`_

.. [5] Beginning with Python 3.4, ``pyvenv`` (a stdlib alternative to
       :ref:`virtualenv`) will create virtualenv environments with ``pip``
       pre-installed, thereby making it an equal alternative to
       :ref:`virtualenv`.


.. _pyvenv: http://docs.python.org/3.4/library/venv.html
