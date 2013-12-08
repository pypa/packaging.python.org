====================
Installing from PyPI
====================

:Page Status: Incomplete
:Last Reviewed: 2013-12-01


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

The :term:`PyPA <Python Packaging Authority (PyPA)>` currently :doc:`recommends
<current>` :ref:`pip` for package installation and :ref:`virtualenv` for virtual
environments.

::

   FIXME

   What to cover:

   1) Why virtualenv (what about pyenv? buildout?)
   2) Why pick *one* installer to recommend?
       the rationale from PEP453
   3) why pip?
      - feature breakdown in the "pip vs easy_install" chart in the additional section weighs in pip's favor
      - Decoupled from packaging tools.
      - what easy_install bugs mentioned in PEP453 does pip address?
   4) mention easy_install for the Yes cases in the "pip vs easy_install" chart.


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


Related Additional Topics
=========================

* :ref:`pip vs easy_install`
* :ref:`easy_install and sys.path`
* :ref:`Installing on Debian/Ubuntu`
* :ref:`Installing on CentOS/RedHat`
* :ref:`Installing on Windows`
* :ref:`Installing on OSX`
* :ref:`NumPy and the Science Stack`
