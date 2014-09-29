.. _`NumPy and the Science Stack`:

===================================
Installing Scientific Distributions
===================================

:Page Status: Incomplete
:Last Reviewed: 2014-07-24


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

Mac OS X installers and package managers
----------------------------------------

Similar to the situation on Windows, many projects (including NumPy) publish
Mac OS X installers that are compatible with the Mac OS X CPython binaries
published on python.org.

Mac OS X users also have access to Linux distribution style package managers
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
