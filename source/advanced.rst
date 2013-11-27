===============
Advanced Topics
===============

:Page Status: Incomplete
:Last Reviewed: 2013-11-26


.. _`pip vs easy_install`:

pip vs easy_install
===================

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
=========================

::

   FIXME


.. _`Wheel vs Egg`:

Wheel vs Egg
============

::

   FIXME



.. _`Installing on Debian/Ubuntu`:

Installing on Debian/Ubuntu
===========================

::

   FIXME

   cover 'dist-packages' and it's /usr and /usr/local schemes


.. _`Installing on CentOS/RedHat`:

Installing on CentOS/RedHat
===========================

::

   FIXME


.. _`Installing on Windows`:

Installing on Windows
=====================

::

   FIXME


.. _`Installing on OSX`:

Installing on OSX
=================

::

   FIXME


.. _`Building RPMs for Python projects`:

Building RPMs for Python projects
=================================

::

   FIXME


.. _`Building debs for Python projects`:

Building debs for Python projects
=================================

::

   FIXME

