
.. _platform-compatibility-tags:

===========================
Platform compatibility tags
===========================

The platform compatibility tagging model used for ``wheel`` distribution is
defined in :pep:`425`.

.. _manylinux:

Manylinux tags
==============

The scheme defined in :pep:`425` is insufficient for public distribution
of Linux wheel files (and \*nix wheel files in general), so the *manylinux*
platform tags were defined, to allow providing wheels for many common Linux
distributions. See :pep:`513` for more about how this works.

* ``manylinux1`` is defined in :pep:`513`, for x86_64 and i686 architectures.
* ``manylinux2010`` is defined in :pep:`571`, for x86_64 and i686 architectures.
  It is based on a platform from 2010, whereas ``manylinux1`` is based on a
  platform from 2007. This means that ``manylinux2010`` packages are easier to
  create, but not compatible with some older systems where ``manylinux1``
  packages would work.

  ``manylinux2010`` is not yet widely recognised by install tools.
