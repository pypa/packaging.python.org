
.. _platform-compatibility-tags:

===========================
Platform compatibility tags
===========================

Platform compatibility tags allow build tools to mark distributions as being
compatible with specific platforms, and allows installers to understand which
distributions are compatible with the system they are running on.


Overview
========

The tag format is ``{python tag}-{abi tag}-{platform tag}``.

python tag
    'py27', 'cp33'
abi tag
    'cp32dmu', 'none'
platform tag
    'linux_x86_64', 'any'

For example, the tag ``py27-none-any`` indicates compatibility with Python 2.7
(any Python 2.7 implementation) with no abi requirement, on any platform.

The ``wheel`` built package format includes these tags in its filenames,
of the form
``{distribution}-{version}(-{build tag})?-{python tag}-{abitag}-{platform tag}.whl``.
Other package formats may have their own conventions.

Any potential spaces in any tag should be replaced with ``_``.


Python Tag
==========

The Python tag indicates the implementation and version required by
a distribution.  Major implementations have abbreviated codes, initially:

* py: Generic Python (does not require implementation-specific features)
* cp: CPython
* ip: IronPython
* pp: PyPy
* jy: Jython

Other Python implementations should use :py:data:`sys.implementation.name <sys.implementation>`.

The version is ``py_version_nodot``.  CPython gets away with no dot,
but if one is needed the underscore ``_`` is used instead.  PyPy should
probably use its own versions here ``pp18``, ``pp19``.

The version can be just the major version ``2`` or ``3`` ``py2``, ``py3`` for
many pure-Python distributions.

Importantly, major-version-only tags like ``py2`` and ``py3`` are not
shorthand for ``py20`` and ``py30``.  Instead, these tags mean the packager
intentionally released a cross-version-compatible distribution.

A single-source Python 2/3 compatible distribution can use the compound
tag ``py2.py3``.  See `Compressed Tag Sets`_, below.


ABI Tag
=======

The ABI tag indicates which Python ABI is required by any included
extension modules.  For implementation-specific ABIs, the implementation
is abbreviated in the same way as the Python Tag, e.g. ``cp33d`` would be
the CPython 3.3 ABI with debugging.

The CPython stable ABI is ``abi3`` as in the shared library suffix.

Implementations with a very unstable ABI may use the first 6 bytes (as
8 base64-encoded characters) of the SHA-256 hash of their source code
revision and compiler flags, etc, but will probably not have a great need
to distribute binary distributions. Each implementation's community may
decide how to best use the ABI tag.


Platform Tag
============

Basic platform tags
-------------------

In its simplest form, the platform tag is :py:func:`sysconfig.get_platform()` with
all hyphens ``-`` and periods ``.`` replaced with underscore ``_``.
Until the removal of :ref:`distutils` in Python 3.12, this
was ``distutils.util.get_platform()``. For example:

* win32
* linux_i386
* linux_x86_64


.. _manylinux:

``manylinux``
-------------

The simple scheme above is insufficient for public distribution of wheel files
to Linux platforms, due to the large ecosystem of Linux platforms and subtle
differences between them.

Instead, for those platforms, the ``manylinux`` standard represents a common
subset of Linux platforms, and allows building wheels tagged with the
``manylinux`` platform tag which can be used across most common Linux
distributions.

The current standard is the future-proof ``manylinux_x_y`` standard. It defines
tags of the form ``manylinux_x_y_arch``, where ``x`` and ``y`` are glibc major
and minor versions supported (e.g. ``manylinux_2_24_xxx`` should work on any
distro using glibc 2.24+), and ``arch`` is the architecture, matching the value
of :py:func:`sysconfig.get_platform()` on the system as in the "simple" form above.

The following older tags are still supported for backward compatibility:

* ``manylinux1`` supports glibc 2.5 on ``x86_64`` and ``i686`` architectures.
* ``manylinux2010`` supports glibc 2.12 on ``x86_64`` and ``i686``.
* ``manylinux2014`` supports glibc 2.17 on ``x86_64``, ``i686``, ``aarch64``,
  ``armv7l``, ``ppc64``, ``ppc64le``, and ``s390x``.

In general, distributions built for older versions of the specification are
forwards-compatible (meaning that ``manylinux1`` distributions should continue
to work on modern systems) but not backwards-compatible (meaning that
``manylinux2010`` distributions are not expected to work on platforms that
existed before 2010).

Package maintainers should attempt to target the most compatible specification
possible, with the caveat that the provided build environment for
``manylinux1`` and ``manylinux2010`` have reached end-of-life meaning that
these images will no longer receive security updates.

The following table shows the minimum versions of relevant projects to support
the various ``manylinux`` standards:

==========  ==============  =================  =================  =================
Tool        ``manylinux1``  ``manylinux2010``  ``manylinux2014``  ``manylinux_x_y``
==========  ==============  =================  =================  =================
pip         ``>=8.1.0``     ``>=19.0``         ``>=19.3``         ``>=20.3``
auditwheel  ``>=1.0.0``     ``>=2.0.0``        ``>=3.0.0``        ``>=3.3.0`` [#]_
==========  ==============  =================  =================  =================

.. [#] Only support for ``manylinux_2_24`` has been added in auditwheel 3.3.0


``musllinux``
-------------

The ``musllinux`` family of tags is similar to ``manylinux``, but for Linux
platforms that use the musl_ libc rather than glibc (a prime example being Alpine
Linux). The schema is ``musllinux_x_y_arch``, supporting musl ``x.y`` and higher
on the architecture ``arch``.

The musl version values can be obtained by executing the musl libc shared
library the Python interpreter is currently running on, and parsing the output:

.. code-block:: python

   import re
   import subprocess

   def get_musl_major_minor(so: str) -> tuple[int, int] | None:
       """Detect musl runtime version.

       Returns a two-tuple ``(major, minor)`` that indicates musl
       library's version, or ``None`` if the given libc .so does not
       output expected information.

       The libc library should output something like this to stderr::

           musl libc (x86_64)
           Version 1.2.2
           Dynamic Program Loader
       """
       proc = subprocess.run([so], stderr=subprocess.PIPE, text=True)
       lines = (line.strip() for line in proc.stderr.splitlines())
       lines = [line for line in lines if line]
       if len(lines) < 2 or lines[0][:4] != "musl":
           return None
       match = re.match(r"Version (\d+)\.(\d+)", lines[1])
       if match:
           return (int(match.group(1)), int(match.group(2)))
       return None

There are currently two possible ways to find the musl library’s location that a
Python interpreter is running on, either with the system ldd_ command, or by
parsing the ``PT_INTERP`` section’s value from the executable’s ELF_ header.


Use
===

The tags are used by installers to decide which built distribution
(if any) to download from a list of potential built distributions.
The installer maintains a list of (pyver, abi, arch) tuples that it
will support.  If the built distribution's tag is ``in`` the list, then
it can be installed.

It is recommended that installers try to choose the most feature complete
built distribution available (the one most specific to the installation
environment) by default before falling back to pure Python versions
published for older Python releases. Installers are also recommended to
provide a way to configure and re-order the list of allowed compatibility
tags; for example, a user might accept only the ``*-none-any`` tags to only
download built packages that advertise themselves as being pure Python.

Another desirable installer feature might be to include "re-compile from
source if possible" as more preferable than some of the compatible but
legacy pre-built options.

This example list is for an installer running under CPython 3.3 on a
linux_x86_64 system. It is in order from most-preferred (a distribution
with a compiled extension module, built for the current version of
Python) to least-preferred (a pure-Python distribution built with an
older version of Python):

1.  cp33-cp33m-linux_x86_64
2.  cp33-abi3-linux_x86_64
3.  cp3-abi3-linux_x86_64
4.  cp33-none-linux_x86_64*
5.  cp3-none-linux_x86_64*
6.  py33-none-linux_x86_64*
7.  py3-none-linux_x86_64*
8.  cp33-none-any
9.  cp3-none-any
10.  py33-none-any
11.  py3-none-any
12.  py32-none-any
13.  py31-none-any
14.  py30-none-any

* Built distributions may be platform specific for reasons other than C
  extensions, such as by including a native executable invoked as
  a subprocess.

Sometimes there will be more than one supported built distribution for a
particular version of a package.  For example, a packager could release
a package tagged ``cp33-abi3-linux_x86_64`` that contains an optional C
extension and the same distribution tagged ``py3-none-any`` that does not.
The index of the tag in the supported tags list breaks the tie, and the
package with the C extension is installed in preference to the package
without because that tag appears first in the list.

Compressed Tag Sets
===================

To allow for compact filenames of bdists that work with more than
one compatibility tag triple, each tag in a filename can instead be a
'.'-separated, sorted, set of tags.  For example, pip, a pure-Python
package that is written to run under Python 2 and 3 with the same source
code, could distribute a bdist with the tag ``py2.py3-none-any``.
The full list of simple tags is::

    for x in pytag.split('.'):
        for y in abitag.split('.'):
            for z in archtag.split('.'):
                yield '-'.join((x, y, z))

A bdist format that implements this scheme should include the expanded
tags in bdist-specific metadata.  This compression scheme can generate
large numbers of unsupported tags and "impossible" tags that are supported
by no Python implementation e.g. "cp33-cp31u-win64", so use it sparingly.

FAQ
===

What tags are used by default?
    Tools should use the most-preferred architecture dependent tag
    e.g. ``cp33-cp33m-win32`` or the most-preferred pure python tag
    e.g. ``py33-none-any`` by default.  If the packager overrides the
    default it indicates that they intended to provide cross-Python
    compatibility.

What tag do I use if my distribution uses a feature exclusive to the newest version of Python?
    Compatibility tags aid installers in selecting the *most compatible*
    build of a *single version* of a distribution. For example, when
    there is no Python 3.3 compatible build of ``beaglevote-1.2.0``
    (it uses a Python 3.4 exclusive feature) it may still use the
    ``py3-none-any`` tag instead of the ``py34-none-any`` tag. A Python
    3.3 user must combine other qualifiers, such as a requirement for the
    older release ``beaglevote-1.1.0`` that does not use the new feature,
    to get a compatible build.

Why isn't there a ``.`` in the Python version number?
    CPython has lasted 20+ years without a 3-digit major release. This
    should continue for some time.  Other implementations may use _ as
    a delimiter, since both - and . delimit the surrounding filename.

Why normalise hyphens and other non-alphanumeric characters to underscores?
    To avoid conflicting with the ``.`` and ``-`` characters that separate
    components of the filename, and for better compatibility with the
    widest range of filesystem limitations for filenames (including
    being usable in URL paths without quoting).

Why not use special character <X> rather than ``.`` or ``-``?
    Either because that character is inconvenient or potentially confusing
    in some contexts (for example, ``+`` must be quoted in URLs, ``~`` is
    used to denote the user's home directory in POSIX), or because the
    advantages weren't sufficiently compelling to justify changing the
    existing reference implementation for the wheel format defined in :pep:`427`
    (for example, using ``,`` rather than ``.`` to separate components
    in a compressed tag).

Who will maintain the registry of abbreviated implementations?
    New two-letter abbreviations can be requested on the python-dev
    mailing list.  As a rule of thumb, abbreviations are reserved for
    the current 4 most prominent implementations.

Does the compatibility tag go into METADATA or PKG-INFO?
    No.  The compatibility tag is part of the built distribution's
    metadata.  METADATA / PKG-INFO should be valid for an entire
    distribution, not a single build of that distribution.

Why didn't you mention my favorite Python implementation?
    The abbreviated tags facilitate sharing compiled Python code in a
    public index.  Your Python implementation can use this specification
    too, but with longer tags.
    Recall that all "pure Python" built distributions just use ``py``.

Why is the ABI tag (the second tag) sometimes "none" in the reference implementation?
    Since Python 2 does not have an easy way to get to the SOABI
    (the concept comes from newer versions of Python 3) the reference
    implementation at the time of writing guesses "none".  Ideally it
    would detect "py27(d|m|u)" analogous to newer versions of Python,
    but in the meantime "none" is a good enough way to say "don't know".


History
=======

- February 2013: The original version of this specification was approved through
  :pep:`425`.
- January 2016: The ``manylinux1`` tag was approved through :pep:`513`.
- April 2018: The ``manylinux2010`` tag was approved through :pep:`571`.
- July 2019: The ``manylinux2014`` tag was approved through :pep:`599`.
- November 2019: The ``manylinux_x_y`` perennial tag was approved through
  :pep:`600`.
- April 2021: The ``musllinux_x_y`` tag was approved through :pep:`656`.



.. _musl: https://musl.libc.org
.. _ldd: https://www.unix.com/man-page/posix/1/ldd/
.. _elf: https://refspecs.linuxfoundation.org/elf/elf.pdf
