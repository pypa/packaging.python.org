.. _`NumPy and the Science Stack`:

==============================
Installing scientific packages
==============================

.. contents:: Contents
   :local:


Scientific software tends to have more complex dependencies than most, and
it will often have multiple build options to take advantage of different
kinds of hardware, or to interoperate with different pieces of external
software.

In particular, `NumPy <http://www.numpy.org/>`__, which provides the basis
for most of the software in the `scientific Python stack
<http://www.scipy.org/stackspec.html#stackspec>`__ can be configured
to interoperate with different FORTRAN libraries, and can take advantage
of different levels of vectorised instructions available in modern CPUs.

Starting with version 1.10.4 of NumPy and version 1.0.0 of SciPy, pre-built
32-bit and 64-bit binaries in the ``wheel`` format are available for all major
operating systems (Windows, macOS, and Linux) on PyPI. Note, however, that on
Windows, NumPy binaries are linked against the `ATLAS
<http://www.netlib.org/atlas/>` BLAS/LAPACK library, restricted to SSE2
instructions, so they may not provide optimal linear algebra performance.

There are a number of alternative options for obtaining scientific Python
libraries (or any other Python libraries that require a compilation environment
to install from source and don't provide pre-built wheel files on PyPI).


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

If using versions which may be several months old is acceptable, then this is
likely to be a good option (just make sure to allow access to distributions
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

As with Linux system packages, the Windows installers will only install into a
system Python installation - they do not support installation in virtual
environments. Allowing access to distributions installed into the system Python
when using virtual environments is a common approach to working around this
limitation.

The `wheel` project also provides a `wheel convert` subcommand that can
convert a Windows `bdist_wininst` installer to a wheel.

.. preserve old links to this heading
.. _mac-os-x-installers-and-package-managers:

macOS installers and package managers
-------------------------------------

Similar to the situation on Windows, many projects (including NumPy) publish
macOS installers that are compatible with the macOS CPython binaries
published on python.org.

macOS users also have access to Linux distribution style package managers
such as ``MacPorts``. The SciPy site has more details on using MacPorts to
install the `scientific Python stack
<http://www.scipy.org/install.html#mac-packages>`__


SciPy distributions
-------------------

The SciPy site lists `several distributions
<http://www.scipy.org/install.html>`__ that provide the full SciPy stack to
end users in an easy to use and update format.

Some of these distributions may not be compatible with the standard ``pip``
and ``virtualenv`` based toolchain.

Spack
------
`Spack <https://github.com/LLNL/spack/>`_ is a flexible package manager
designed to support multiple versions, configurations, platforms, and compilers.
It was built to support the needs of large supercomputing centers and scientific
application teams, who must often build software many different ways.
Spack is not limited to Python; it can install packages for ``C``, ``C++``,
``Fortran``, ``R``, and other languages.  It is non-destructive; installing
a new version of one package does not break existing installations, so many
configurations can coexist on the same system.

Spack offers a simple but powerful syntax that allows users to specify
versions and configuration options concisely. Package files are written in
pure Python, and they are templated so that it is easy to swap compilers,
dependency implementations (like MPI), versions, and build options with a single
package file.  Spack also generates *module* files so that packages can
be loaded and unloaded from the user's environment.


The conda cross-platform package manager
----------------------------------------

`Anaconda <https://www.anaconda.com/download/>`_ is a Python distribution
published by Continuum Analytics. It is a stable collection of Open Source
packages for big data and scientific use.  As of the 5.0 release of Anaconda,
about 200 packages are installed by default, and a total of 400-500 can be
installed and updated from the Anaconda repository.

``conda`` is an open source (BSD licensed) package management system and
environment management system included in Anaconda that allows users to install
multiple versions of binary software packages and their dependencies, and
easily switch between them. It is a cross-platform tool working on Windows,
macOS, and Linux. Conda can be used to package up and distribute all kinds of
packages, it is not limited to just Python packages. It has full support for
native virtual environments. Conda makes environments first-class citizens,
making it easy to create independent environments even for C libraries. It is
written in Python, but is Python-agnostic. Conda manages Python itself as a
package, so that `conda update python` is possible, in contrast to pip, which
only manages Python packages. Conda is available in Anaconda and Miniconda (an
easy-to-install download with just Python and conda).
