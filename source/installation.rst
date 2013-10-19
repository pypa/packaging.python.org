==================
Installation Guide
==================


Installing from PyPI
====================

::

  $ pip install SomePackage             # latest version
  $ pip install SomePackage==1.0.4      # specific version
  $ pip install 'SomePackage>=1.0.4'    # minimum version


Installing from other indexes
=============================

::

  $ pip install --index-url=https://my.package.repo/simple SomePackage


Installing from VCS
===================

pip supports installing python projects (that have distutils or setuptools `setup.py`) directly from version control.

::

  $ pip install -e git+https://git.repo/some_pkg.git#egg=SomePackage          # from git
  $ pip install -e hg+https://hg.repo/some_pkg.git#egg=SomePackage            # from mercurial
  $ pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomePackage         # from svn
  $ pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomePackage  # from 'feature' branch

For a full breakdown of the forms pip supports, see the `VCS Support
<http://www.pip-installer.org/en/latest/logic.html#vcs-support>`_ section in the
pip docs.

Installing your project in edit mode
====================================

::

  $ pip install -e .


Upgrading
=========

::

  $ pip install --upgrade SomePackage


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


Where to get more details
=========================

The :ref:`pip` `docs <http://pip-installer.org>`_ have a `usage section
<http://www.pip-installer.org/en/latest/usage.html>`_ that exhausts all the
subcommands and options, with many examples, and a `cookbook section
<http://www.pip-installer.org/en/latest/cookbook.html>`_ that covers many of the
practical issues users deal with.


