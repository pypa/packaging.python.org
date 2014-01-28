===================
Concepts & Analyses
===================

:Page Status: Incomplete
:Last Reviewed: 2014-01-22

This section covers various packaging concepts and analyses.


Packaging Formats
=================

::

   FIXME

   1) sdist and wheel are the most relevant currently
   2) what defines an sdist? (sdist 2.0 is coming)


Installation Schemes
====================

::

   FIXME

   1. distutils/sysconfig schemes
   2. global vs user installs
   3. virtual environments


.. _`Requirements files vs setup.py`:

Requirements files vs setup.py
==============================


::

   FIXME

   - cover 3 distinctions
    - abstract vs concrete requirements (https://caremad.io/blog/setup-vs-requirement/)
    - minimally defined vs exhaustive or frozen (http://stackoverflow.com/a/7085000)
    - library vs app/environment requirements.
   - mention pip's breakdown of the use cases for requirements files
      (http://www.pip-installer.org/en/latest/cookbook.html#requirements-files)
   - boil it down to a set of rules
      (e.g. see the end of http://blog.miguelgrinberg.com/post/the-package-dependency-blues)


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

.. [1] http://pythonhosted.org/setuptools/easy_install.html#natural-script-launcher


.. _pylauncher support: https://bitbucket.org/pypa/pylauncher

.. _`easy_install and sys.path`:

easy_install and sys.path
=========================

::

   FIXME

   - global easy_install'd packages override --user installs


.. _`Wheel vs Egg`:

Wheel vs Egg
============

::

   FIXME



.. _`Multi-version Installs`:

Multi-version Installs
======================

easy_install allows simultaneous installation of different versions of the same
package into a single environment shared by multiple programs which must
``require`` the appropriate version of the package at run time (using
``pkg_resources``).

For many use cases, virtual environments address this need without the
complication of the ``require`` directive. However, the advantage of
parallel installations within the same environment is that it works for an
environment shared by multiple applications, such as the system Python in a
Linux distribution.

The major limitation of ``pkg_resources`` based parallel installation is
that as soon as you import ``pkg_resources`` it locks in the *default*
version of everything which is already available on sys.path. This can
cause problems, since ``setuptools`` created command line scripts
use ``pkg_resources`` to find the entry point to execute. This means that,
for example, you can't use ``require`` tests invoked through ``nose`` or a
WSGI application invoked through ``gunicorn`` if your application needs a
non-default version of anything that is available on the standard
``sys.path`` - the script wrapper for the main application will lock in the
version that is available by default, so the subsequent ``require`` call
in your own code fails with a spurious version conflict.

This can be worked around by setting all dependencies in
``__main__.__requires__`` before importing ``pkg_resources`` for the first
time, but that approach does mean that standard command line invocations of
the affected tools can't be used - it's necessary to write a custom
wrapper script or use ``python -c '<commmand>'`` to invoke the application's
main entry point directly.

Refer to the `pkg_resources documentation
<http://pythonhosted.org/setuptools/pkg_resources.html#workingset-objects>`__
for more details.


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
      - conficting dependencies within the dep tree of one argument `
      - conflicts across arguments: ``pip|easy_install  OnePackage TwoPackage``
      - conflicts with what's already installed



.. _`Supporting multiple Python versions`:

Supporting multiple Python versions
===================================

::

  FIXME

  Useful projects/resources to reference:

  - six
  - tox
  - Travis and Shining Panda CI
  - Ned Batchelder's What's in Which version pages
    - http://nedbatchelder.com/blog/201310/whats_in_which_python_3.html
      - http://nedbatchelder.com/blog/201109/whats_in_which_python.html
  - Lennart Regebro's "Porting to Python 3"
  - the Python 3 porting how to in the main docs
  - cross reference to the stable ABI discussion
    in the binary extensions topic (once that exists)
  - mention version classifiers for distribution metadata


.. _`Local PyPI indexes and caches`:

Local PyPI indexes and caches
=============================

::

  FIXME

  - local --find-links
  - tools like https://pypi.python.org/pypi/devpi-server
