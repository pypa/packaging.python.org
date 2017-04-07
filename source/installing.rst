===================
Installing Packages
===================

:Page Status: Complete
:Last Reviewed: 2016-06-24

This section covers the basics of how to install Python :term:`packages
<Distribution Package>`.

It's important to note that the term "package" in this context is being used as
a synonym for a :term:`distribution <Distribution Package>` (i.e. a bundle of
software to be installed), not to refer to the kind of :term:`package <Import
Package>` that you import in your Python source code (i.e. a container of
modules). It is common in the Python community to refer to a :term:`distribution
<Distribution Package>` using the term "package".  Using the term "distribution"
is often not preferred, because it can easily be confused with a Linux
distribution, or another larger software distribution like Python itself.


.. contents:: Contents
   :local:


.. _installing_requirements:

Requirements for Installing Packages
====================================

This section describes the steps to follow before installing other Python
packages.

Install pip, setuptools, and wheel
----------------------------------

* If you have Python 2 >=2.7.9 or Python 3 >=3.4 installed from `python.org
  <https://www.python.org>`_, you will already have :ref:`pip` and
  :ref:`setuptools`, but will need to upgrade to the latest version:

  On Linux or OS X:

  ::

    pip install -U pip setuptools


  On Windows:

  ::

    python -m pip install -U pip setuptools

* If you're using a Python install on Linux that's managed by the system package
  manager (e.g "yum", "apt-get" etc...), and you want to use the system package
  manager to install or upgrade pip, then see :ref:`Installing
  pip/setuptools/wheel with Linux Package Managers`

* Otherwise:

 * Securely Download `get-pip.py
   <https://bootstrap.pypa.io/get-pip.py>`_ [1]_

 * Run ``python get-pip.py``. [2]_  This will install or upgrade pip.
   Additionally, it will install :ref:`setuptools` and :ref:`wheel` if they're
   not installed already.

   .. warning::

      Be cautious if you're using a Python install that's managed by your
      operating system or another package manager. get-pip.py does not
      coordinate with those tools, and may leave your system in an
      inconsistent state. You can use ``python get-pip.py --prefix=/usr/local/``
      to install in ``/usr/local`` which is designed for locally-installed
      software.


Optionally, Create a virtual environment
----------------------------------------

See :ref:`section below <Creating and using Virtual Environments>` for details,
but here's the basic commands:

   Using :ref:`virtualenv`:

   ::

    pip install virtualenv
    virtualenv <DIR>
    source <DIR>/bin/activate

   Using `venv`_: [3]_

   ::

    python3 -m venv <DIR>
    source <DIR>/bin/activate


.. _`Creating and using Virtual Environments`:

Creating Virtual Environments
=============================

Python "Virtual Environments" allow Python :term:`packages <Distribution
Package>` to be installed in an isolated location for a particular application,
rather than being installed globally.

Imagine you have an application that needs version 1 of LibFoo, but another
application requires version 2. How can you use both these applications? If you
install everything into /usr/lib/python2.7/site-packages (or whatever your
platform’s standard location is), it’s easy to end up in a situation where you
unintentionally upgrade an application that shouldn’t be upgraded.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you can’t install :term:`packages <Distribution Package>` into the
global site-packages directory? For instance, on a shared host.

In all these cases, virtual environments can help you. They have their own
installation directories and they don’t share libraries with other virtual
environments.

Currently, there are two viable tools for creating Python virtual environments:

* `venv`_ is available by default in Python 3.3 and later, and installs
  :ref:`pip` and :ref:`setuptools` into created virtual environments in
  Python 3.4 and later.
* :ref:`virtualenv` needs to be installed separately, but supports Python 2.6+
  and Python 3.3+, and :ref:`pip`, :ref:`setuptools` and :ref:`wheel` are
  always installed into created virtual environments by default (regardless of
  Python version).

The basic usage is like so:

Using :ref:`virtualenv`:

::

 virtualenv <DIR>
 source <DIR>/bin/activate


Using `venv`_:

::

 python3 -m venv <DIR>
 source <DIR>/bin/activate


For more information, see the `virtualenv <http://virtualenv.pypa.io>`_ docs or
the `venv`_ docs.


Use pip for Installing
======================

:ref:`pip` is the recommended installer.  Below, we'll cover the most common
usage scenarios. For more detail, see the `pip docs <https://pip.pypa.io>`_,
which includes a complete `Reference Guide
<https://pip.pypa.io/en/latest/reference/index.html>`_.

There are a few cases where you might want to use `easy_install
<https://pip.pypa.io/en/latest/reference/index.html>`_ instead of pip.  For
details, see the the :ref:`pip vs easy_install` breakdown in the :doc:`Advanced
Topics <additional>` section.


Installing from PyPI
====================

The most common usage of :ref:`pip` is to install from the :term:`Python Package
Index <Python Package Index (PyPI)>` using a :term:`requirement specifier
<Requirement Specifier>`. Generally speaking, a requirement specifier is
composed of a project name followed by an optional :term:`version specifier
<Version Specifier>`.  :pep:`440` contains a :pep:`full
specification <440#version-specifiers>`
of the currently supported specifiers. Below are some examples.

To install the latest version of "SomeProject":

::

 pip install 'SomeProject'


To install a specific version:

::

 pip install 'SomeProject==1.4'


To install greater than or equal to one version and less than another:

::

 pip install 'SomeProject>=1,<2'


To install a version that's :pep:`"compatible" <440#compatible-release>`
with a certain version: [4]_

::

 pip install 'SomeProject~=1.4.2'

In this case, this means to install any version "==1.4.*" version that's also
">=1.4.2".


Source Distributions vs Wheels
==============================

:ref:`pip` can install from either :term:`Source Distributions (sdist) <Source
Distribution (or "sdist")>` or :term:`Wheels <Wheel>`, but if both are present
on PyPI, pip will prefer a compatible :term:`wheel <Wheel>`.

:term:`Wheels <Wheel>` are a pre-built :term:`distribution <Distribution
Package>` format that provides faster installation compared to :term:`Source
Distributions (sdist) <Source Distribution (or "sdist")>`, especially when a
project contains compiled extensions.

If :ref:`pip` does not find a wheel to install, it will locally build a wheel
and cache it for future installs, instead of rebuilding the source distribution
in the future.


Upgrading packages
==================

Upgrade an already installed `SomeProject` to the latest from PyPI.

::

 pip install --upgrade SomeProject



Installing to the User Site
===========================

To install :term:`packages <Distribution Package>` that are isolated to the
current user, use the ``--user`` flag:

::

  pip install --user SomeProject


For more information see the `User Installs
<https://pip.readthedocs.io/en/latest/user_guide.html#user-installs>`_ section
from the pip docs.


Requirements files
==================

Install a list of requirements specified in a :ref:`Requirements File
<pip:Requirements Files>`.

::

 pip install -r requirements.txt


Installing from VCS
===================

Install a project from VCS in "editable" mode.  For a full breakdown of the
syntax, see pip's section on :ref:`VCS Support <pip:VCS Support>`.

::

 pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject          # from git
 pip install -e hg+https://hg.repo/some_pkg.git#egg=SomeProject            # from mercurial
 pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomeProject         # from svn
 pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomeProject  # from a branch


Installing from other Indexes
=============================

Install from an alternate index

::

 pip install --index-url http://my.package.repo/simple/ SomeProject


Search an additional index during install, in addition to :term:`PyPI <Python
Package Index (PyPI)>`

::

 pip install --extra-index-url http://my.package.repo/simple SomeProject



Installing from a local src tree
================================


Installing from local src in `Development Mode
<https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode>`_,
i.e. in such a way that the project appears to be installed, but yet is
still editable from the src tree.

::

 pip install -e <path>


You can also install normally from src

::

 pip install <path>


Installing from local archives
==============================

Install a particular source archive file.

::

 pip install ./downloads/SomeProject-1.0.4.tar.gz


Install from a local directory containing archives (and don't check :term:`PyPI
<Python Package Index (PyPI)>`)

::

 pip install --no-index --find-links=file:///local/dir/ SomeProject
 pip install --no-index --find-links=/local/dir/ SomeProject
 pip install --no-index --find-links=relative/dir/ SomeProject


Installing from other sources
=============================

To install from other data sources (for example Amazon S3 storage) you can
create a helper application that presents the data in a :pep:`503` compliant
index format, and use the ``--extra-index-url`` flag to direct pip to use
that index.

::

 ./s3helper --port=7777
 pip install --extra-index-url http://localhost:7777 SomeProject


Installing Prereleases
======================

Find pre-release and development versions, in addition to stable versions.  By
default, pip only finds stable versions.

::

 pip install --pre SomeProject


Installing Setuptools "Extras"
==============================

Install `setuptools extras`_.

::

  $ pip install SomePackage[PDF]
  $ pip install SomePackage[PDF]==3.0
  $ pip install -e .[PDF]==3.0  # editable project in current directory



----

.. [1] "Secure" in this context means using a modern browser or a
       tool like `curl` that verifies SSL certificates when downloading from
       https URLs.

.. [2] Depending on your platform, this may require root or Administrator
       access. :ref:`pip` is currently considering changing this by `making user
       installs the default behavior
       <https://github.com/pypa/pip/issues/1668>`_.

.. [3] Beginning with Python 3.4, ``venv`` (a stdlib alternative to
       :ref:`virtualenv`) will create virtualenv environments with ``pip``
       pre-installed, thereby making it an equal alternative to
       :ref:`virtualenv`.

.. [4] The compatible release specifier was accepted in :pep:`440`
       and support was released in :ref:`setuptools` v8.0 and
       :ref:`pip` v6.0

.. _venv: https://docs.python.org/3/library/venv.html
.. _setuptools extras: https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies
