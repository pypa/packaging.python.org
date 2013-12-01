===============
Advanced Topics
===============

:Page Status: Incomplete
:Last Reviewed: 2013-12-01


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

Here's a breakdown of the important differences between pip and easy_install now:

+------------------------------+----------------------------------+-------------------------------+
|                              | **pip**                          | **easy_install**              |
+------------------------------+----------------------------------+-------------------------------+
|Installs from :term:`Wheels   |Yes                               |No                             |
|<Wheel>`                      |                                  |                               |
+------------------------------+----------------------------------+-------------------------------+
|Uninstall Packages            |Yes (``pip uninstall``)           |No                             |
+------------------------------+----------------------------------+-------------------------------+
|Dependency Overrides          |Yes (:ref:`Requirements Files     |No                             |
|                              |<pip:Requirements Files>`)        |                               |
+------------------------------+----------------------------------+-------------------------------+
|List Installed Packages       |Yes (``pip list`` and ``pip       |No                             |
|                              |freeze``)                         |                               |
+------------------------------+----------------------------------+-------------------------------+
|:ref:`PEP438 <PEP438s>`       |Yes                               |No                             |
|Support                       |                                  |                               |
+------------------------------+----------------------------------+-------------------------------+
|Installation format           |'Flat' packages with `egg-info`   | Encapsulated Egg format       |
|                              |metadata.                         |                               |
+------------------------------+----------------------------------+-------------------------------+
|sys.path modification         |No                                |:ref:`Yes <easy_install and    |
|                              |                                  |sys.path>`                     |
|                              |                                  |                               |
+------------------------------+----------------------------------+-------------------------------+
|Installs from :term:`Eggs     |No                                |Yes                            |
|<Egg>`                        |                                  |                               |
+------------------------------+----------------------------------+-------------------------------+
|`pylauncher support`_         |No                                |Yes [1]_                       |
|                              |                                  |                               |
+------------------------------+----------------------------------+-------------------------------+
|:ref:`Dependency Resolution`  |:ref:`Kinda <Dependency           |:ref:`Kinda <Dependency        |
|                              |Resolution>`                      |Resolution>`                   |
+------------------------------+----------------------------------+-------------------------------+
|:ref:`Multi-version Installs` |No                                |Yes                            |
|                              |                                  |                               |
+------------------------------+----------------------------------+-------------------------------+


.. _pylauncher support: https://bitbucket.org/pypa/pylauncher

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


.. _`Multi-version Installs`:

Multi-version Installs
======================

::

   FIXME

easy_install allows simultaneous installation of different versions of the same
package inte a single environment shared by multiple programs which must
``require`` the appropriate version of the package at run time. In general,
virtual environments fulfill this need without the complication of the
``require`` directive.


.. _`Dependency Resolution`:

Dependency Resolution
=====================

::

   FIXME

   what to cover:
   - pip lacking a true resolver (currently, "1st found wins"; practical for overriding in requirements files)
   - easy_install will raise an error if mutually-incompatible versions of a dependency tree are installed.
   - console_scripts complaining about conflicts
   - scenarios to breakdown:
      - conficting dependencies within the dep tree of one argument ``pip|easy_install  OnePackage``
      - conflicts across arguments: ``pip|easy_install  OnePackage TwoPackage``
      - conflicts with what's already installed

.. [1] http://pythonhosted.org/setuptools/easy_install.html#natural-script-launcher
