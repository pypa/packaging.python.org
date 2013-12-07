=================
Additional Topics
=================

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

.. [1] http://pythonhosted.org/setuptools/easy_install.html#natural-script-launcher


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

The major limitation of ``require`` is that the first time you call it, it
locks in the *default* version of everything which is available on sys.path,
and ``setuptools`` created command line scripts call it by default. This
means that, for example, you can't use ``require`` tests invoked through
``nose`` or a WSGI application invoked through ``gunicorn`` if your
application needs a non-default version of anything - the script wrapper
for the main application will lock in the version that is available by
default, so the subsequent ``require`` call fails with a spurious version
conflict.



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


.. _`Binary Extensions`:

Binary Extensions
=================

::

   FIXME

   https://bitbucket.org/pypa/python-packaging-user-guide/issue/36



.. _`NumPy and the Science Stack`:

Installing Scientific Packages
==============================

Scientific software tends to have more complex dependencies than most, and
it will often have multiple build options to take advantage of different
kinds of hardware, or to interoperate with different pieces of external
software.

In particular, `NumPy <http://www.numpy.org/>`__, which provides the basis
for most of the software in the `scientific Python stack
<http://www.scipy.org/stackspec.html#stackspec>`__ can be configured
to interoperate with different FORTRAN libraries, and can take advantage
of different levels of vectorised instructions available in modern CPUs.

Unfortunately, as of December 2013, given NumPy's current build and
distribution model, the standard tools currently aren't quite up to the
task of distributing pre-built NumPy binaries, as most users aren't going
to know which version they need, and the ``wheel`` format currently doesn't
allow the installer to make that decision on the user's behalf at install
time.

It is expected that this situation will eventually be resolved either by
future iterations of the standard tools providing full support for the
intricacies of NumPy's current build and distribution process, or by the
NumPy developers choosing one build variant as the "lowest acceptable
common denominator" and publishing that as a wheel file on PyPI.

In the meantime, however, there are a number of alternative options for
obtaining scientific Python libraries (or any other Python libraries that
require a compilation environment to install from source and don't provide
pre-built wheel files on PyPI).


Building from source
--------------------

The same complexity which makes it difficult to distribute NumPy (and many
of the projects that depend on it) as wheel files also make them difficult
to build from source yourself. However, for intrepid folks that are willing
to spend the time wrangling compilers and linkers for both C and FORTRAN,
building from source is always an option.


Linux distribution packages
---------------------------

For Linux users, the system package manager will often have pre-compiled
versions of various pieces of scientific software, including NumPy and
other parts of the scientific Python stack.

If using versions which may be several months old is acceptable, then this
is likely to be a good option (just make sure to allow access to packages
installed into the system Python when using virtual environments).


Windows installers
------------------

Many Python projects that don't (or can't) currently publish wheel files at
least publish Windows installers, either on PyPI or on their project
download page. Using these installers allows users to avoid the need to set
up a suitable environment to build extensions locally.

The extensions provided in these installers are typically compatible with
the CPython Windows installers published on python.org.

For projects which don't provide their own Windows installers (and even
some which do), Christoph Gohlke at the University of California provides
a `collection of Windows installers
<http://www.lfd.uci.edu/~gohlke/pythonlibs/>`__. Many Python users on
Windows have reported a positive experience with these prebuilt versions.

As with Linux system packages, the Windows installers will only install into
a system Python installation - they do not support installation in virtual
environments. Allowing access to packages installed into the system Python
when using virtual environments is a common approach to working around this
limitation.


Mac OS X installers and package managers
----------------------------------------

Similar to the situation on Windows, many projects (including NumPy) publish
Mac OS X installers that are compatible with the Mac OS X CPython binaries
published on python.org.

Mac OS X users also have access to Linux distribution style package managers
such as ``MacPorts``. The SciPy site has more details on using MacPorts to
install the ` scientific Python stack
<http://www.scipy.org/install.html#mac-packages>`__


SciPy distributions
-------------------

The SciPy site lists `several distributions
<http://www.scipy.org/install.html>`__ that provide the full SciPy stack to
end users in an easy to use and update format.

Some of these distributions may not be compatible with the standard ``pip``
and ``virtualenv`` based toolchain.


The conda cross-platform package manager
----------------------------------------

`Anaconda <https://store.continuum.io/cshop/anaconda/>`__ (in this context)
is a SciPy distribution published by Continuum Analytics.

``conda`` is the open source (BSD licensed) package management system that
Continuum Analytics created and published as part of Anaconda's development.
It doesn't support interoperability with system package managers the way the
standard toolchain does (as, unlike the standard toolchain, that isn't one
of conda's design goals), but it *does* support some degree of
interoperability with the standard toolchain itself. In particular,
bootstrapping conda via ``pip install conda`` and then running the
``conda init`` command provides access to all of the pre-built binaries
that Continuum Analytics have created for the free version of the
Anaconda distribution.

At time of writing (December, 2013), there are still some rough edges when
attempting to use conda to install Anaconda packages outside the Anaconda
distribution, but those issues are still likely to be simpler to resolve
or work around than building local versions of scientific Python libraries
and their external dependencies.
