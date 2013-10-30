==================
Installation Guide
==================

:Page Status: Incomplete [1]_
:Last Reviewed: 10-29-2013

This page explains how to install python packages, which you will normally
find on `PyPI <https://pypi.python.org/pypi>`__.

Note that if you ever plan on working on multiple python projects, it is
usually worth setting up a :ref:`virtualenv` environment in which to install
packages for a particular project. In this way, different projects'
package and runtime requirements can be isolated from each other.

Installing from PyPI
====================

::

  $ pip install SomePackage             # latest version
  $ pip install SomePackage==1.0.4      # specific version
  $ pip install 'SomePackage>=1.0.4'    # minimum version


Installing from other indexes
=============================

This can be handy when installing packages from a local PyPI mirror, or
similar situations where one might wish to use a personal repository of
packages, rather than the official one.

::

  $ pip install --index-url=https://my.package.repo/simple SomePackage

One can also install directly from a file system, or archive::

  $ pip install --no-index /path/to/package
  $ pip install --no-index /path/to/SomePackage-1.0.4.zip


Installing from VCS
===================

pip supports installing python projects (that have distutils or setuptools
`setup.py`) directly from version control.

::

  $ pip install -e git+https://git.repo/some_pkg.git#egg=SomePackage          # from git
  $ pip install -e hg+https://hg.repo/some_pkg.git#egg=SomePackage            # from mercurial
  $ pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomePackage         # from svn
  $ pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomePackage  # from 'feature' branch

Note the ``#egg=SomePackage`` fragment on the end, that is used to help
indicate to pip the name of the package being installed, but is not part
of the url used to retreive the package.

For a full breakdown of the forms pip supports, see the `VCS Support
<http://www.pip-installer.org/en/latest/logic.html#vcs-support>`_ section in the
pip docs.

Installing from a requirements file
===================================

A project may sometimes contain a :file:`requirements.txt` or
:file:`dev-requirements.txt` file (or both) which lists all the packages needed
to respectively install, or help develop that project. Pip can read this file
to install all the listed requirements.

::

  $ pip install -r requirements.txt

One can also generate this file quite easily from the current set of installed
packages, on a unix shell::

  $ pip freeze > requirements.txt

.. note::

   this will generate the requirements with exact version numbers. This can,
   for instance, be useful for replicating an install environment.

Installing your project in edit mode
====================================

This allows you to continue working on a project in progress even as
python will then consider it 'installed' - the installation is not 'static'.

using ``.`` will install the project in your current directory.

::

  $ pip install -e .


Upgrading
=========

::

  $ pip install --upgrade SomePackage

Listing installed packages
==========================

::

  $ pip freeze

Uninstalling
============

::

  $ pip uninstall SomePackage
  Uninstalling SomePackage:
    /my/env/lib/pythonx.x/site-packages/somepackage
  Proceed (y/n)? y
  Successfully uninstalled SomePackage


User Installs
=============

With Python 2.6 came the `"user scheme" for installation
<http://docs.python.org/install/index.html#alternate-installation-the-user-scheme>`_,
which means that all Python distributions support an alternative install
location that is specific to a user.  The default location for each OS is
explained in the python documentation for the `site.USER_BASE
<http://docs.python.org/library/site.html#site.USER_BASE>`_ variable.  This mode
of installation can be turned on by specifying the `--user` option to ``pip
install``.

::

  $ pip install --user SomePackage

Moreover, the "user scheme" can be customized by setting the ``PYTHONUSERBASE``
environment variable, which updates the value of ``site.USER_BASE``. To install
"SomePackage" into an environment with site.USER_BASE customized to '/myappenv',
do the following::

  $ export PYTHONUSERBASE=/myappenv
  $ pip install --user SomePackage


.. _page_status:

Where to get more details
=========================

The :ref:`pip` `docs <http://pip-installer.org>`_ have a `usage section
<http://www.pip-installer.org/en/latest/usage.html>`_ that exhausts all the
subcommands and options, with many examples, and a `cookbook section
<http://www.pip-installer.org/en/latest/cookbook.html>`_ that covers many of the
practical issues users deal with.


.. [1] This page will likely be revamped. See `Issue #23
       <https://bitbucket.org/pypa/python-packaging-user-guide/issue/23/stop-recreating-the-pip-setuptools-docs-in>`_.
