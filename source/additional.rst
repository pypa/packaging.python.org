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

Refer to the `pkg_resources documentation <http://pythonhosted.org/setuptools/pkg_resources.html#workingset-objects>`__
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
      - conficting dependencies within the dep tree of one argument ``pip|easy_install  OnePackage``
      - conflicts across arguments: ``pip|easy_install  OnePackage TwoPackage``
      - conflicts with what's already installed


.. _`Binary Extensions`:

Binary Extensions
=================

One of the features of the CPython reference interpreter is that, in
addition to allowing the execution of Python code, it also exposes a rich
C API for use by other software. One of the most common uses of this C API
is to create importable C extensions that allow things which aren't
always easy to achieve in pure Python code.


Use cases for binary extensions
-------------------------------

The typical use cases for binary extensions break down into just three
conventional categories:

* accelerator modules: these modules are completely self-contained, and
  are created solely to run faster than the equivalent pure Python code
  runs in CPython. Ideally, accelerator modules will always have a pure
  Python equivalent to use as a fallback if the accelerated version isn't
  available on a given system. The CPython standard library makes extensive
  use of accelerator modules.

* wrapper modules: these modules are created to expose existing C interfaces
  to Python code. They may either expose the underlying C interface directly,
  or else expose a more "Pythonic" API that makes use of Python language
  features to make the API easier to use. The CPython standard library makes
  extensive use of accelerator modules.

* low level system access: these modules are created to access lower level
  features of the CPython runtime, the operating system, or the underlying
  hardware. Through platform specific code, extension modules may achieve
  things that aren't possible in pure Python code. A number of CPython
  standard library modules are written in C in order to access interpreter
  internals that aren't exposed at the language level.

  One particularly notable feature of C extensions is that, when they don't
  need to call back into the interpreter runtime, they can release CPython's
  global interpreter lock around long-running operations (regardling of
  whether those operations are CPU or IO bound).

Not all extension modules will fit neatly into the above categories. The
extension modules included with NumPy, for example, span all three use cases
- they moves inner loops to C for speed reasons, wrap external libraries
written in C, FORTRAN and other languages, and uses low level system
interfaces for both CPython and the underlying operation system to support
concurrent execution of vectorised operations and to tightly control the
exact memory layout of created objects.


Disadvantages of using binary extensions
----------------------------------------

The main disadvantage of using binary extensions is the fact that it makes
subsequent distribution of the software more difficult. One of the
advantages of using Python is that it is largely cross platform, and the
languages used to write extension modules (typically C or C++, but really
any language that can bind to the CPython C API) typically require that
custom binaries be created for different platforms.

This means that binary extensions:

* require that end users be able to either build them from source, or else
  that someone publish pre-built binaries for common platforms

* may not be compatible with different builds of the CPython reference
  interpreter

* often will not work correctly with alternative interpreters such as PyPy,
  IronPython or Jython

* if handcoded, make maintenance more difficult by requiring that
  maintainers be familiar not only with Python, but also with the language
  used to create the binary extension, as well as with the details of the
  CPython C API.

* if a pure Python fallback implementation is provided, make maintenance
  more difficult by requiring that changes be implemented in two places,
  and introducing additional complexity in the test suite to ensure both
  versions are always executed.


Alternatives to handcoded accelerator modules
---------------------------------------------

When extension modules are just being used to make code run faster (after
profiling has identified the code where the speed increase is worth
additional maintenance effort), a number of other alternatives should
also be considered:

* look for existing optimised alternatives. The CPython standard libary
  includes a number of optimised data structures and algorithms (especially
  in the builtins and the ``collections`` and ``itertools`` modules). The
  Python Package Index also offers additional alternatives. Sometimes, the
  appropriate choice of standard library or third party module can avoid the
  need to create your own accelerator module.

* for long running applications, the JIT compiled `PyPy interpreter
  <http://pypy.org/>`__ may offer a suitable alternative to the standard
  CPython runtime. The main barrier to adopting PyPy is typically reliance
  on other binary extension modules - while PyPy does emulate the CPython
  C API, modules that rely on that cause problems for the PyPy JIT, and the
  emulation layer can often expose latent defects in extension modules that
  CPython currently tolerates (frequently around reference counting errors -
  an object having one live reference instead of two often won't break
  anything, but no references instead of one is a major problem).

* `Cython <http://cython.org/>`__ is a mature static compiler that can
  compile most Python code to C extension modules. The initial compilation
  provides some speed increases (by bypassing the CPython interpreter layer),
  and Cython's optional static typing features can offer additional
  opportunities for speed increases. Using Cython still has the disadvantage
  of increasing the complexity of distributing the resulting application,
  but has the benefit of having a reduced barrier to entry for Python
  programmers (relative to other languages like C or C++).

* `Numba <http://numba.pydata.org/>`__ is a newer tool, created by members
  of the scientific Python community, that aims to leverage LLVM to allow
  selective compilation of pieces of a Python application to native
  machine code at runtime. It requires that LLVM be available on the
  system where the code is running, but can provide significant speed
  increases, especially for operations that are amenable to vectorisation.


Alternatives to handcoded wrapper modules
-----------------------------------------

The C ABI (Application Binary Interface) is a common standard for sharing
functionality between multiple applications. One of the strengths of the
CPython C API (Application Programming Interface) is allowing Python users
to tap into that functionality. However, wrapping modules by hand is quite
tedious, so a number of other alternative approaches should be considered.

The approaches described below don't simplify the distribution case at all,
but they *can* significantly reduce the maintenance burden of keeping
wrapper modules up to date.

* In addition to being useful for the creation of accelerator modules,
  `Cython <http://cython.org/>`__ is also useful for creating wrapper
  modules. It still involves wrapping the interfaces by hand, however, so
  may not be a good choice for wrapping large APIs.

* `cffi <cffi.readthedocs.org/>`__ is a project created by some of the PyPy
  developers to make it straightforward for developers that already know
  both Python and C to expose their C modules to Python applications. It
  also makes it relatively straightforward to wrap a C module based on its
  header files, even if you don't know C yourself.

  One of the key advantages of ``cffi`` is that it is compatible with the
  PyPy JIT, allowing CFFI wrapper modules to participate fully in PyPy's
  tracing JIT optimisations.

* `SWIG <http://www.swig.org/>`__ is a wrapper interface generator that
  allows a variety of programming languages, including Python, to interface
  with C *and C++* code.

* The standard library's ``ctypes`` module, while useful for getting access
  to C level interfaces when header information isn't available, suffers
  from the fact that it operates solely at the C ABI level, and thus has
  no automatic consistency checking between the interface actually being
  exported by the library and the one declared in the Python code. By
  contrast, the above alternatives are all able to operate at the C *API*
  level, using C header files to ensure consistency between the interface
  exported by the library being wrapped and the one expected by the Python
  wrapper module. While ``cffi`` *can* operate directly at the C ABI level,
  it suffers from the same interface inconsistency problems as ``ctypes``
  when it is used that way.


Alternatives for low level system access
----------------------------------------

For applications that need low level system access (regardless of the
reason), a binary extension module often *is* the best way to go about it.
This is particularly true for low level access to the CPython runtime
itself, since some operations (like releasing the Global Interpreter Lock)
are simply invalid when the interpreter is running code, even if a module
like ``ctypes`` or ``cffi`` is used to obtain access to the relevant C
API interfaces.

For cases where the extension module is manipulating the underlying
operating system or hardware (rather than the CPython runtime), it may
sometimes be better to just write an ordinary C library (or a library in
another systems programming language like C++ or Rust that can export a C
compatible ABI), and then use one of the wrapping techniques described
above to make the interface available as an importable Python module.


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
