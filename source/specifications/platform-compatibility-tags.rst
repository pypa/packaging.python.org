
.. _platform-compatibility-tags:

===========================
Platform compatibility tags
===========================

Platform compatibility tags allow build tools to mark distributions as being
compatible with specific platforms, and allows installers to understand which
distributions are compatible with the system they are running on.

The platform compatibility tagging model used for the ``wheel`` distribution
format is defined in :pep:`425`.

Platform tags for Windows
-------------------------

The scheme defined in :pep:`425` covers public distribution of wheel files to
systems running Windows.

Platform tags for macOS (Mac OS X)
----------------------------------

The scheme defined in :pep:`425` covers public distribution of wheel files to
systems running macOS (previously known as Mac OS X).

Platform tags for common Linux distributions
--------------------------------------------

.. _manylinux:

The scheme defined in :pep:`425` is insufficient for public distribution of
wheel files (and \*nix wheel files in general) to Linux platforms, due to the
large ecosystem of Linux platforms and subtle differences between them.

Instead, :pep:`600` defines the ``manylinux`` standard, which represents a
common subset of Linux platforms, and allows building wheels tagged with the
``manylinux`` platform tag which can be used across most common Linux
distributions.

There were multiple iterations of the ``manylinux`` specification, each
representing the common subset of Linux platforms at a given point in time:

* ``manylinux1`` (:pep:`513`) supports ``x86_64`` and ``i686``
  architectures, and is based on a compatible Linux platform from 2007.
* ``manylinux2010`` (:pep:`571`) supports ``x86_64`` and ``i686``
  architectures. and updates the previous specification to be based on a
  compatible Linux platform from 2010 instead.
* ``manylinux2014`` (:pep:`599`) adds support for a number of
  additional architectures (``aarch64``, ``armv7l``, ``ppc64``, ``ppc64le``,
  and ``s390x``) and updates the base platform to a compatible Linux platform
  from 2014.

``manylinux_x_y`` (:pep:`600`) supersedes all previous PEPs to define a
future-proof standard. It defines ``x`` and ``y`` as glibc major an minor
versions supported (e.g. ``manylinux_2_24`` should work on any distro using
glibc 2.24+). Previous tags are still supported for backward compatibility.

In general, distributions built for older versions of the specification are
forwards-compatible (meaning that ``manylinux1`` distributions should continue
to work on modern systems) but not backwards-compatible (meaning that
``manylinux2010`` distributions are not expected to work on platforms that
existed before 2010).

Package maintainers should attempt to target the most compatible specification
possible, with the caveat that the provided build environment for
``manylinux1`` and ``manylinux2010`` have reached end-of-life meaning that
these images will no longer receive security updates.

Manylinux compatibility support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Note::
  * The ``manylinux2014`` specification is relatively new and is not yet widely
    recognised by install tools.
  * The ``manylinux_x_y`` specification is relatively new and is not yet widely
    recognised by install tools.

The following table shows the minimum versions of relevant projects to support
the various ``manylinux`` standards:

==========  ==============  =================  =================  =================
Tool        ``manylinux1``  ``manylinux2010``  ``manylinux2014``  ``manylinux_x_y``
==========  ==============  =================  =================  =================
pip         ``>=8.1.0``     ``>=19.0``         ``>=19.3``         ``>=20.3``
auditwheel  ``>=1.0.0``     ``>=2.0.0``        ``>=3.0.0``        ``>=3.3.0`` [#]_
==========  ==============  =================  =================  =================

Platform tags for other \*nix platforms
---------------------------------------

The scheme defined in :pep:`425` is not generally sufficient for public
distribution of wheel files to other \*nix platforms. Efforts are currently
(albeit intermittently) under way to define improved compatibility tagging
schemes for AIX and for Alpine Linux.


.. [#] Only support for ``manylinux_2_24`` has been added in auditwheel 3.3.0
