===================
Concepts & Analyses
===================

:Page Status: Incomplete
:Last Reviewed: 2014-04-09

This section covers various packaging concepts and analyses.

.. contents::


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


.. _`install_requires vs Requirements files`:

install_requires vs Requirements files
======================================

install_requires
----------------

``install_requires`` is a :ref:`setuptools` ``setup.py`` keyword that should be
used to specify what a project **minimally** needs to run correctly.  When the
project is installed by :ref:`pip`, this is the specification that is used to
install its dependencies.

For example, if the project requires A and B, your ``install_requires`` would be
like so:

::

 install_requires=[
    'A',
    'B'
 ]

Additionally, it's best practice to indicate any known lower or upper bounds.

For example, it may be known, that your project requires at least v1 of 'A', and
v2 of 'B', so it would be like so:

::

 install_requires=[
    'A>=1',
    'B>=2'
 ]

It may also be known that project A follows semantic versioning, and that v2 of
'A' will indicate a break in compatibility, so it makes sense to not allow v2:

::

 install_requires=[
    'A>=1,<2',
    'B>=2'
 ]

It is not considered best practice to use ``install_requires`` to pin
dependencies to specific versions, or to specify sub-dependencies
(i.e. dependencies of your dependencies).  This is overly-restrictive, and
prevents the user from gaining the benefit of dependency upgrades.

Lastly, it's important to understand that ``install_requires`` is a listing of
"Abstract" requirements, i.e just names and version restrictions that don't
determine where the dependencies will be fulfilled from (i.e. from what
index or source).  The where (i.e. how they are to be made "Concrete") is to
be determined at install time using :ref:`pip` options. [3]_


Requirements files
------------------

:ref:`Requirements Files <pip:Requirements Files>` described most simply, are
just a list of :ref:`pip:pip install` arguments placed into a file.

Whereas ``install_requires`` defines the dependencies for a single project,
:ref:`Requirements Files <pip:Requirements Files>` are often used to define
the requirements for a complete python environment.

Whereas ``install_requires`` requirements are minimal, requirements files
often contain an exhaustive listing of pinned versions for the purpose of
achieving :ref:`repeatable installations <pip:Repeatability>` of a complete
environment.

Whereas ``install_requires`` requirements are "Abstract", requirements files
often contain pip options like ``--index-url`` or ``--find-links`` to make
requirements "Concrete". [3]_

Whereas ``install_requires`` metadata is automatically analyzed by pip during an
install, requirements files are not, and only are used when a user specifically
installs them using ``pip install -r``.



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
|Uninstall Distributions       |Yes (``pip uninstall``)           |No                             |
+------------------------------+----------------------------------+-------------------------------+
|Dependency Overrides          |Yes (:ref:`Requirements Files     |No                             |
|                              |<pip:Requirements Files>`)        |                               |
+------------------------------+----------------------------------+-------------------------------+
|List Installed Distributions  |Yes (``pip list`` and ``pip       |No                             |
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

   - global easy_install'd distributions override --user installs


.. _`Wheel vs Egg`:

Wheel vs Egg
============

* :term:`Wheel` has an :ref:`official PEP <PEP427s>`. :term:`Egg` did not.

* :term:`Wheel` is a :term:`distribution <Distribution>` format, i.e a packaging
  format. [2]_ :term:`Egg` was both a distribution format and a runtime
  installation format (if left zipped), and was designed to be importable.

* :term:`Wheel` archives do not include .pyc files. Therefore, when the
  distribution only contains python files (i.e. no compiled extensions), and is
  compatible with Python 2 and 3, it's possible for a wheel to be "universal",
  similar to an :term:`sdist <Source Distribution (or "sdist")>`.

* :term:`Wheel` uses :ref:`PEP376-compliant <PEP376s>` ``.dist-info``
  directories. Egg used ``.egg-info``.

* :term:`Wheel` has a :ref:`richer file naming convention <PEP425s>`. A single
  wheel archive can indicate its compatibility with a number of Python language
  versions and implementations, ABIs, and system architectures.

* :term:`Wheel` is versioned. Every wheel file contains the version of the wheel
  specification and the implementation that packaged it.

* :term:`Wheel` is internally organized by `sysconfig path type
  <http://docs.python.org/2/library/sysconfig.html#installation-paths>`_,
  therefore making it easier to convert to other formats.


.. _`Multi-version Installs`:

Multi-version Installs
======================

easy_install allows simultaneous installation of different versions of the same
project into a single environment shared by multiple programs which must
``require`` the appropriate version of the project at run time (using
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
      - conflicts across arguments: ``pip|easy_install  OneProject TwoProject``
      - conflicts with what's already installed


----

.. [2] Circumstantially, in some cases, wheels can be used as an importable
       runtime format, although `this is not officially supported at this time
       <http://www.python.org/dev/peps/pep-0427/#is-it-possible-to-import-python-code-directly-from-a-wheel-file>`_.

.. [3] For more on "Abstract" vs "Concrete" requirements, see
       https://caremad.io/blog/setup-vs-requirement.

