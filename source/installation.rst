==================
Installation Guide
==================

:Page Status: Incomplete
:Last Reviewed: 2013-11-03


A guide to installing python :term:`distributions <Distribution>` from
:term:`PyPI <Python Package Index (PyPI)>` and other sources.


What is "installation"?
=======================

::

   FIXME

   What to cover:

   1. distutils/sysconfig schemes
   2. global vs user installs
   3. virtual environments


Introduction to PyPI
====================

::

   FIXME


What tools to use
=================

The PyPA recommends the use of :ref:`pip` for package installation and
:ref:`virtualenv` for virtual environments.

Advantages of pip over easy_install:

  - Uninstall support.
  - Addresses [unspecified] bugs that easy_install cannot address due to
    backward-compatibilty constraints.
  - Decoupled from packaging tools.

::

   FIXME

   What to cover:

   1) Why virtualenv (what about pyenv? buildout?)
   2) What easy_install bugs mentioned in PEP453 does pip address?

Alternatives
------------

:ref:`setuptools` provides the ``easy_install`` command for installation.
``easy_install`` is preferred by some for the features it offers not offered
by pip:

  - Multi-version installs: easy_install allows simultaneous installation of
    different versions of the same package inte a single environment shared by
    multiple programs which must ``require`` the appropriate version of the
    package at run time. In general, virtual environments fulfill this need
    without the complication of the ``require`` directive.
  - Natural egg support: Although pip can install as eggs using the ``--egg``
    parameter for installing eggs, easy_install provides additional control
    over how eggs are installed (i.e. zipped or unzipped).
  - Rigorous version management: easy_install will raise an error if
    mutually-incompatible versions of a dependency tree are installed.
  - Better console script support on Windows: ``easy_install`` is currently
    the only installer that supports the `launching of natural scripts
    <http://pythonhosted.org/setuptools/easy_install.html#natural-script-launcher>`_
    using `PyLauncher <https://bitbucket.org/pypa/pylauncher>`.

Getting started with virtualenv
===============================

::

   FIXME


Getting started with pip
========================

::

   FIXME

   What to cover:

   1. link to:
      - pip's quickstart (which needs improvement)
      - pip's feature overview (which doesn't exist atm)
      - pip's cookbook
      - pip's guide on "wheel caching"
      - pip's usage (which needs better subcommand descriptions and more examples)


Advanced Topics
===============

* :ref:`pip vs easy_install`
* :ref:`easy_install and sys.path`
* :ref:`Installing on Debian/Ubuntu`
* :ref:`Installing on CentOS/RedHat`
* :ref:`Installing on Windows`
* :ref:`Installing on OSX`
