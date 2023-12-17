.. _versioning:
.. _`Choosing a versioning scheme`:

==========
Versioning
==========

This discussion covers all aspects of versioning Python packages.


Valid version numbers
=====================

Different Python projects may use different versioning schemes based on the
needs of that particular project, but in order to be compatible with tools like
:ref:`pip`, all of them are required to comply with a flexible format for
version identifiers, for which the authoritative reference is the
:ref:`specification of version specifiers <version-specifiers>`. Here are some
examples of version numbers:

.. code-block:: text

  1.2.0.dev1  # Development release
  1.2.0a1     # Alpha Release
  1.2.0b1     # Beta Release
  1.2.0rc1    # Release Candidate
  1.2.0       # Final Release
  1.2.0.post1 # Post Release
  15.10       # Date based release
  23          # Serial release


Semantic versioning vs. calendar versioning
===========================================

A versioning scheme is a way to interpret version numbers of a package, and to
decide which should be the next version number for a new release of a package.
Two versioning schemes are commonly used for Python packages, semantic
versioning and calendar versioning.

Semantic versioning is recommended for most new projects.

Semantic versioning
-------------------

The idea of *semantic versioning* is to use 3-part version numbers,
*major.minor.maintenance*, where the project author increments:

- *major* when they make incompatible API changes,
- *minor* when they add functionality in a backwards-compatible manner, and
- *maintenance*, when they make backwards-compatible bug fixes.

Note that many projects, especially larger ones, do not use strict semantic
versioning since many changes are technically breaking changes but affect only a
small fraction of users. Such projects tend to increment the major number when
the incompatibility is high, rather than for any tiny incompatibility, or to
signal a shift in the project.

For those projects that do adhere to semantic versioning strictly, this approach
allows users to make use of :ref:`compatible release version specifiers
<version-specifiers-compatible-release>`, with the ``~=`` operator.  For
example, ``name ~= X.Y`` is roughly equivalent to ``name >= X.Y, == X.*``, i.e.,
it requires at least release X.Y, and allows any later release with greater Y as
long as X is the same. Likewise, ``name ~= X.Y.Z`` is roughly equivalent to
``name >= X.Y.Z, == X.Y.*``, i.e., it requires at least X.Y.Z and allows a later
release with same X and Y but higher Z.

Python projects adopting semantic versioning should abide by clauses 1-8 of the
`Semantic Versioning 2.0.0 specification <semver_>`_.


Calendar versioning
-------------------

Semantic versioning is not a suitable choice for all projects, such as those
with a regular time based release cadence and a deprecation process that
provides warnings for a number of releases prior to removal of a feature.

A key advantage of date-based versioning, or `calendar versioning <calver_>`_,
is that it is straightforward to tell how old the base feature set of a
particular release is given just the version number.

Calendar version numbers typically take the form *year.month* (for example,
23.10 for December 2023).


Other schemes
-------------

Serial versioning refers to the simplest possible versioning scheme, which
consists of a single number incremented every release. While serial versioning
is very easy to manage as a developer, it is the hardest to track as an end
user, as serial version numbers convey little or no information regarding API
backwards compatibility.

Combinations of the above schemes are possible. For example, a project may
combine date based versioning with serial versioning to create a *year.serial*
numbering scheme that readily conveys the approximate age of a release, but
doesn't otherwise commit to a particular release cadence within the year.



Pre-release versioning
======================

Regardless of the base versioning scheme, pre-releases for a given final release
may be published as:

* Zero or more dev releases, denoted with a ".devN" suffix,
* Zero or more alpha releases, denoted with a ".aN" suffix,
* Zero or more beta releases, denoted with a ".bN" suffix,
* Zero or more release candidates, denoted with a ".rcN" suffix.

Pip and other modern Python package installers ignore pre-releases by default
when deciding which versions of dependencies to install.


Local version identifiers
=========================

Public version identifiers are designed to support distribution via :term:`PyPI
<Python Package Index (PyPI)>`. Python packaging tools also support the notion
of a :ref:`local version identifier <local-version-identifiers>`, which can be
used to identify local development builds not intended for publication, or
modified variants of a release maintained by a redistributor.

A local version identifier takes the form of a public version identifier,
followed by "+" and a local version label. For example:

.. code-block:: text

   1.2.0.dev1+hg.5.b11e5e6f0b0b  # 5th VCS commit since 1.2.0.dev1 release
   1.2.1+fedora.4                # Package with downstream Fedora patches applied




.. _calver: https://calver.org
.. _semver: https://semver.org
