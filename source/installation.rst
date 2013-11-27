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

:ref:`virtualenv` and :ref:`pip`

::

   FIXME

   What to cover:

   1) Why virtualenv (what about pyenv? buildout?)
   2) Why pip (compare pip vs easy_install in detail); use rationale from PEP453
   3) When to use easy_install ([multi-version] eggs)


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


pip vs easy_install
-------------------

`easy_install` was released in 2004, as part of :ref:`setuptools`.  It was
notable at the time for installing :term:`distributions <Distribution>` from
:term:`PyPI <Python Package Index (PyPI)>` using requirement specifiers, and
automatically installing dependencies.

:ref:`pip` came later in 2008, as alternative to `easy_install`, although still
largely built on top of :ref:`setuptools` components.  It was notable at the
time for *not* installing packages as :term:`Eggs <Egg>` or from :term:`Eggs <Egg>` (but
rather simply as 'flat' packages from :term:`sdists <Source Distribution (or
"sdist")>`), and introducing the idea of :ref:`Requirements Files
<pip:Requirements Files>`, which gave users the power to easily replicate
environments.

Here's a breakdown if the important differences between pip and easy_install now:

+-----------------------------+----------------------------------+-------------------------------+
|                             | **pip**                          | **easy_install**              |
+-----------------------------+----------------------------------+-------------------------------+
|Installs from :term:`Wheels  |Yes                               |No                             |
|<Wheel>`                     |                                  |                               |
+-----------------------------+----------------------------------+-------------------------------+
|Uninstall Packages           |Yes (``pip uninstall``)           |No                             |
+-----------------------------+----------------------------------+-------------------------------+
|Dependency Overrides         |Yes (:ref:`Requirements Files     |No                             |
|                             |<pip:Requirements Files>`)        |                               |
+-----------------------------+----------------------------------+-------------------------------+
|List Installed Packages      |Yes (``pip list`` and ``pip       |No                             |
|                             |freeze``)                         |                               |
+-----------------------------+----------------------------------+-------------------------------+
|:ref:`PEP438 <PEP438s>`      |Yes                               |No                             |
|Support                      |                                  |                               |
+-----------------------------+----------------------------------+-------------------------------+
|Installation format          |'Flat' packages with `egg-info`   | Encapsulated Egg format       |
|                             |metadata.                         |                               |
+-----------------------------+----------------------------------+-------------------------------+
|sys.path modification        |No                                |:ref:`Yes <easy_install and    |
|                             |                                  |sys.path>`                     |
|                             |                                  |                               |
+-----------------------------+----------------------------------+-------------------------------+
|Installs from :term:`Eggs    |No                                |Yes                            |
|<Egg>`                       |                                  |                               |
+-----------------------------+----------------------------------+-------------------------------+
|Multi-version Installs       |No                                |Yes                            |
|                             |                                  |                               |
+-----------------------------+----------------------------------+-------------------------------+


.. _`easy_install and sys.path`:

easy_install and sys.path
-------------------------



Installing on Debian/Ubuntu
---------------------------

::

   FIXME

   cover 'dist-packages' and it's /usr and /usr/local schemes


Installing on CentOS/RedHat
---------------------------

::

   FIXME


Installing on Windows
---------------------

::

   FIXME


Installing on OSX
-----------------

::

   FIXME



