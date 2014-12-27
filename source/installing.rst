===============================
Tutorial on Installing Packages
===============================

:Page Status: Incomplete
:Last Reviewed: 2014-12-24

.. contents:: Contents
   :local:

This tutorial covers the basics of how to install Python :term:`packages
<Distribution Package>`.

It's important to note that the term "package" in this context is being used as
a synonym for a :term:`distribution <Distribution Package>` (i.e. a bundle of
software to be installed), not to refer to the kind of :term:`package <Import
Package>` that you import in your Python source code (i.e. a container of
modules). It is common in the Python community to refer to a :term:`distribution
<Distribution Package>` using the term "package".  Using the term "distribution"
is often not preferred, because it can easily be confused with a Linux
distribution, or another larger software distribution like Python itself.


.. _installing_setup:

Setup for Installing Packages
=============================

This section describes the steps to follow before installing other Python
packages.

1. Install :ref:`pip` and :ref:`setuptools`: [3]_

   If you have a :ref:`PEP453 <pypa:PEP453s>`-compliant Python 3.4, it may
   already have the ``pip`` command available by default (and setuptools will be
   installed as well), or it may at least contain a working `ensurepip
   <https://docs.python.org/3.4/library/ensurepip.html>`_. To install pip (and
   setuptools) using ensurepip, run: ``python -m ensurepip --upgrade``.

   Otherwise:

   * Securely Download `get-pip.py
     <https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_ [1]_

   * Run ``python get-pip.py``.  This will install or upgrade pip.
     Additionally, it will install setuptools if it's not installed already. To
     upgrade an existing setuptools, run ``pip install -U setuptools`` [2]_

2. Optionally, Create a virtual environment (See :ref:`section below <Creating
   and using Virtual Environments>` for details):

   Using :ref:`virtualenv`:

   ::

    pip install virtualenv
    virtualenv <DIR>
    source <DIR>/bin/activate

   Using `pyvenv`_: [4]_

   ::

    pyvenv <DIR>
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
:ref:`virtualenv` and `pyvenv`_. `pyvenv`_ is only available in Python 3.3 &
3.4, and only in Python 3.4, is :ref:`pip` & :ref:`setuptools` installed into
environments by default, whereas :ref:`virtualenv` supports Python 2.6 thru
Python 3.4 and :ref:`pip` & :ref:`setuptools` are installed by default in every
version.

The basic usage is like so:

Using :ref:`virtualenv`:

::

 virtualenv <DIR>
 source <DIR>/bin/activate


Using `pyvenv`_:

::

 pyvenv <DIR>
 source <DIR>/bin/activate


For more information, see the `virtualenv <http://virtualenv.pypa.io>`_ docs or
the `pyvenv`_ docs.


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

Install `SomeProject` and its dependencies from :term:`PyPI <Python Package
Index (PyPI)>` using :ref:`pip:Requirement Specifiers`

::

 pip install SomeProject           # latest version
 pip install SomeProject==1.0.4    # specific version
 pip install 'SomeProject>=1.0.4'  # minimum version


Upgrading packages
==================

Upgrade an already installed `SomeProject` to the latest from PyPI.

::

 pip install --upgrade SomeProject


Installing Cached Wheels
========================

:term:`Wheel` is a pre-built :term:`distribution <Distribution Package>` format that
provides faster installation compared to :term:`Source Distributions (sdist)
<Source Distribution (or "sdist")>`, especially when a project contains compiled
extensions.

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


:term:`Wheel` is intended to replace :term:`Eggs <Egg>`.  For a detailed
comparison, see :ref:`Wheel vs Egg`.


Installing to the User Site
===========================

To install :term:`packages <Distribution Package>` that are isolated to the
current user, use the ``--user`` flag:

::

  pip install --user SomeProject


For more information see the `User Installs
<https://pip.readthedocs.org/en/latest/user_guide.html#user-installs>`_ section
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
 pip install -e ~/src/some_pkg                                             # from a source tree

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
<http://pythonhosted.org/setuptools/setuptools.html#development-mode>`_, i.e. in
such a way that the project appears to be installed, but yet is still editable
from the src tree.

::

 pip install -e <path>


You can also normally from src

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

.. [3] On Linux and OSX, pip and setuptools will usually be available for the system
       python from a system package manager (e.g. `yum` or `apt-get` for linux,
       or `homebrew` for OSX). Unfortunately, there is often delay in getting
       the latest version this way, so in most cases, you'll want to use these
       instructions.

.. [4] Beginning with Python 3.4, ``pyvenv`` (a stdlib alternative to
       :ref:`virtualenv`) will create virtualenv environments with ``pip``
       pre-installed, thereby making it an equal alternative to
       :ref:`virtualenv`.

.. [5]

.. _pyvenv: http://docs.python.org/3.4/library/venv.html
.. _setuptools extras: http://packages.python.org/setuptools/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies
