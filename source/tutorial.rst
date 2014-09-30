====================================
Tutorial on Installing Distributions
====================================

:Page Status: Complete
:Last Reviewed: 2014-09-30

.. contents::

This tutorial covers the basics of how to install Python :term:`packages
<Package (Meaning #2)>`, which are known more formally as
:term:`distributions <Distribution>`.


.. _installing_setup:

Setup for Installing Packages
=============================

This section describes the steps to follow before installing other
Python packages.  You will want to install :ref:`pip` and
:ref:`setuptools`, and in most cases, :ref:`virtualenv` (unless you're using
`pyvenv`_).

We recommend the following installation sequence:

1. Install :ref:`pip` and :ref:`setuptools`: [3]_

   If you have a :ref:`PEP453 <PEP453s>`-compliant Python 3.4, it may already
   have the ``pip`` command available by default (and setuptools will be
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

   Using `pyvenv`_: [5]_

   ::

    pyvenv <DIR>
    source <DIR>/bin/activate


.. _`Creating and using Virtual Environments`:

Virtual Environments
====================

Python "Virtual Environments" allow Python :term:`distributions <Distribution>`
to be installed in an isolated location for a particular application, rather
than being installed globally.

Imagine you have an application that needs version 1 of LibFoo, but another
application requires version 2. How can you use both these applications? If you
install everything into /usr/lib/python2.7/site-packages (or whatever your
platform’s standard location is), it’s easy to end up in a situation where you
unintentionally upgrade an application that shouldn’t be upgraded.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you can’t install :term:`distributions <Distribution>` into the
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


Installing Python Distributions
===============================

:ref:`pip` is the recommended installer, and supports various requirement forms
and options.  For details, see the `pip docs
<https://pip.pypa.io>`_.

Examples
--------

Install `SomeProject` and its dependencies from :term:`PyPI <Python Package
Index (PyPI)>` using :ref:`pip:Requirement Specifiers`

::

 pip install SomeProject           # latest version
 pip install SomeProject==1.0.4    # specific version
 pip install 'SomeProject>=1.0.4'  # minimum version


Install a list of requirements specified in a :ref:`Requirements File
<pip:Requirements Files>`.

::

 pip install -r requirements.txt


Upgrade an already installed `SomeProject` to the latest from PyPI.

::

 pip install --upgrade SomeProject


Install a project from VCS in "editable" mode.  For a full breakdown of the
syntax, see pip's section on :ref:`VCS Support <pip:VCS Support>`.

::

 pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject          # from git
 pip install -e hg+https://hg.repo/some_pkg.git#egg=SomeProject            # from mercurial
 pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomeProject         # from svn
 pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomeProject  # from a branch


Install a particular source archive file.

::

 pip install ./downloads/SomeProject-1.0.4.tar.gz
 pip install http://my.package.repo/SomeProject-1.0.4.zip


Install from an alternate index

::

 pip install --index-url http://my.package.repo/simple/ SomeProject


Search an additional index during install, in addition to :term:`PyPI <Python
Package Index (PyPI)>`

::

 pip install --extra-index-url http://my.package.repo/simple SomeProject


Install from a local directory containing archives (and don't check :term:`PyPI
<Python Package Index (PyPI)>`)

::

 pip install --no-index --find-links=file:///local/dir/ SomeProject
 pip install --no-index --find-links=/local/dir/ SomeProject
 pip install --no-index --find-links=relative/dir/ SomeProject


Find pre-release and development versions, in addition to stable versions.  By
default, pip only finds stable versions.

::

 pip install --pre SomeProject


Wheels
------

:term:`Wheel` is a pre-built :term:`distribution <Distribution>` format that
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


User Installs
-------------

To install :term:`distributions <Distribution>` that are isolated to the current
user, use the ``-user`` flag:

::

  pip install --user SomeProject


For more information see the `User Installs
<https://pip.readthedocs.org/en/latest/user_guide.html#user-installs>`_ section
from the pip docs.



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

.. [4] For more information on creating projects, see the `Setuptools Docs
       <http://pythonhosted.org/setuptools/setuptools.html>`_

.. [5] Beginning with Python 3.4, ``pyvenv`` (a stdlib alternative to
       :ref:`virtualenv`) will create virtualenv environments with ``pip``
       pre-installed, thereby making it an equal alternative to
       :ref:`virtualenv`.

.. _pyvenv: http://docs.python.org/3.4/library/venv.html
