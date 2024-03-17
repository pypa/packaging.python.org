.. _package-formats:

===============
Package Formats
===============

This page discusses the file formats that are used to distribute Python packages
and the differences between them.

You will find files in two formats on package indices such as PyPI_: **source
distributions**, or **sdists** for short, and **binary distributions**, commonly
called **wheels**.  For example, the `PyPI page for pip 23.3.1 <pip-pypi_>`_
lets you download two files, ``pip-23.3.1.tar.gz`` and
``pip-23.3.1-py3-none-any.whl``.  The former is an sdist, the latter is a
wheel. As explained below, these serve different purposes. When publishing a
package on PyPI (or elsewhere), you should always upload both an sdist and one
or more wheel.


What is a source distribution?
==============================

Conceptually, a source distribution is an archive of the source code in raw
form. Concretely, an sdist is a ``.tar.gz`` archive containing the source code
plus an additional special file called ``PKG-INFO``, which holds the project
metadata. The presence of this file helps packaging tools to be more efficient
by not needing to compute the metadata themselves. The ``PKG-INFO`` file follows
the format specified in :ref:`core-metadata` and is not intended to be written
by hand [#core-metadata-format]_.

You can thus inspect the contents of an sdist by unpacking it using standard
tools to work with tar archives, such as ``tar -xvf`` on UNIX platforms (like
Linux and macOS), or :ref:`the command line interface of Python's tarfile module
<python:tarfile-commandline>` on any platform.

Sdists serve several purposes in the packaging ecosystem. When :ref:`pip`, the
standard Python package installer, cannot find a wheel to install, it will fall
back on downloading a source distribution, compiling a wheel from it, and
installing the wheel. Furthermore, sdists are often used as the package source
by downstream packagers (such as Linux distributions, Conda, Homebrew and
MacPorts on macOS, ...), who, for various reasons, may prefer them over, e.g.,
pulling from a Git repository.

A source distribution is recognized by its file name, which has the form
:samp:`{package_name}-{version}.tar.gz`, e.g., ``pip-23.3.1.tar.gz``.

.. TODO: provide clear guidance on whether sdists should contain docs and tests.
   Discussion: https://discuss.python.org/t/should-sdists-include-docs-and-tests/14578

If you want technical details on the sdist format, read the :ref:`sdist
specification <source-distribution-format>`.


What is a wheel?
================

Conceptually, a wheel contains exactly the files that need to be copied when
installing the package.

There is a big difference between sdists and wheels for packages with
:term:`extension modules <extension module>`, written in compiled languages like
C, C++ and Rust, which need to be compiled into platform-dependent machine code.
With these packages, wheels do not contain source code (like C source files) but
compiled, executable code (like ``.so`` files on Linux or DLLs on Windows).

Furthermore, while there is only one sdist per version of a project, there may
be many wheels. Again, this is most relevant in the context of extension
modules. The compiled code of an extension module is tied to an operating system
and processor architecture, and often also to the version of the Python
interpreter (unless the :ref:`Python stable ABI <cpython-stable-abi>` is used).

For pure-Python packages, the difference between sdists and wheels is less
marked. There is normally one single wheel, for all platforms and Python
versions.  Python is an interpreted language, which does not need ahead-of-time
compilation, so wheels contain ``.py`` files just like sdists.

If you are wondering about ``.pyc`` bytecode files: they are not included in
wheels, since they are cheap to generate, and including them would unnecessarily
force a huge number of packages to distribute one wheel per Python version
instead of one single wheel. Instead, installers like :ref:`pip` generate them
while installing the package.

With that being said, there are still important differences between sdists and
wheels, even for pure Python projects. Wheels are meant to contain exactly what
is to be installed, and nothing more. In particular, wheels should never include
tests and documentation, while sdists commonly do.  Also, the wheel format is
more complex than sdist. For example, it includes a special file -- called
``RECORD`` -- that lists all files in the wheel along with a hash of their
content, as a safety check of the download's integrity.

At a glance, you might wonder if wheels are really needed for "plain and basic"
pure Python projects. Keep in mind that due to the flexibility of sdists,
installers like pip cannot install from sdists directly -- they need to first
build a wheel, by invoking the :term:`build backend` that the sdist specifies
(the build backend may do all sorts of transformations while building the wheel,
such as compiling C extensions). For this reason, even for a pure Python
project, you should always upload *both* an sdist and a wheel to PyPI or other
package indices. This makes installation much faster for your users, since a
wheel is directly installable. By only including files that must be installed,
wheels also make for smaller downloads.

On the technical level, a wheel is a ZIP archive (unlike sdists which are TAR
archives). You can inspect its contents by unpacking it as a normal ZIP archive,
e.g., using ``unzip`` on UNIX platforms like Linux and macOS, ``Expand-Archive``
in Powershell on Windows, or :ref:`the command line interface of Python's
zipfile module <python:zipfile-commandline>`. This can be very useful to check
that the wheel includes all the files you need it to.

Inside a wheel, you will find the package's files, plus an additional directory
called :samp:`{package_name}-{version}.dist-info`. This directory contains
various files, including a ``METADATA`` file which is the equivalent of
``PKG-INFO`` in sdists, as well as ``RECORD``. This can be useful to ensure no
files are missing from your wheels.

The file name of a wheel (ignoring some rarely used features) looks like this:
:samp:`{package_name}-{version}-{python_tag}-{abi_tag}-{platform_tag}.whl`.
This naming convention identifies which platforms and Python versions the wheel
is compatible with. For example, the name ``pip-23.3.1-py3-none-any.whl`` means
that:

- (``py3``) This wheel can be installed on any implementation of Python 3,
  whether CPython, the most widely used Python implementation, or an alternative
  implementation like PyPy_;
- (``none``) It does not depend on the Python version;
- (``any``) It does not depend on the platform.

The pattern ``py3-none-any`` is common for pure Python projects. Packages with
extension modules typically ship multiple wheels with more complex tags.

All technical details on the wheel format can be found in the :ref:`wheel
specification <binary-distribution-format>`.


.. _egg-format:
.. _`Wheel vs Egg`:

What about eggs?
================

"Egg" is an old package format that has been replaced with the wheel format.  It
should not be used anymore. Since August 2023, PyPI `rejects egg uploads
<pypi-eggs-deprecation_>`_.

Here's a breakdown of the important differences between wheel and egg.

* The egg format was introduced by :ref:`setuptools` in 2004, whereas the wheel
  format was introduced by :pep:`427` in 2012.

* Wheel has an :doc:`official standard specification
  </specifications/binary-distribution-format>`. Egg did not.

* Wheel is a :term:`distribution <Distribution Package>` format, i.e a packaging
  format. [#wheel-importable]_ Egg was both a distribution format and a runtime
  installation format (if left zipped), and was designed to be importable.

* Wheel archives do not include ``.pyc`` files. Therefore, when the distribution
  only contains Python files (i.e. no compiled extensions), and is compatible
  with Python 2 and 3, it's possible for a wheel to be "universal", similar to
  an :term:`sdist <Source Distribution (or "sdist")>`.

* Wheel uses standard :ref:`.dist-info directories
  <recording-installed-packages>`.  Egg used ``.egg-info``.

* Wheel has a :ref:`richer file naming convention <wheel-file-name-spec>`. A
  single wheel archive can indicate its compatibility with a number of Python
  language versions and implementations, ABIs, and system architectures.

* Wheel is versioned. Every wheel file contains the version of the wheel
  specification and the implementation that packaged it.

* Wheel is internally organized by `sysconfig path type
  <https://docs.python.org/2/library/sysconfig.html#installation-paths>`_,
  therefore making it easier to convert to other formats.

--------------------------------------------------------------------------------

.. [#core-metadata-format] This format is email-based. Although this would
   be unlikely to be chosen today, backwards compatibility considerations lead to
   it being kept as the canonical format. From the user point of view, this
   is mostly invisible, since the metadata is specified by the user in a way
   understood by the build backend, typically ``[project]`` in ``pyproject.toml``,
   and translated by the build backend into ``PKG-INFO``.

.. [#wheel-importable] Circumstantially, in some cases, wheels can be used
   as an importable runtime format, although :ref:`this is not officially supported
   at this time <binary-distribution-format-import-wheel>`.



.. _pip-pypi: https://pypi.org/project/pip/23.3.1/#files
.. _pypi: https://pypi.org
.. _pypi-eggs-deprecation: https://blog.pypi.org/posts/2023-06-26-deprecate-egg-uploads/
.. _pypy: https://pypy.org
