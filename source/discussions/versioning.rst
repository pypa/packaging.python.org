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
examples of version numbers [#version-examples]_:

- A simple version (final release): ``1.2.0``
- A development release: ``1.2.0.dev1``
- An alpha release: ``1.2.0a1``
- A beta release: ``1.2.0b1``
- A release candidate: ``1.2.0rc1``
- A post-release: ``1.2.0.post1``
- A post-release of an alpha release (possible, but discouraged): ``1.2.0a1.post1``
- A simple version with only two components: ``23.12``
- A simple version with just one component: ``42``
- A version with an epoch: ``1!1.0``

Projects can use a cycle of pre-releases to support testing by their users
before a final release. In order, the steps are: alpha releases, beta releases,
release candidates, final release. Pip and other modern Python package
installers ignore pre-releases by default when deciding which versions of
dependencies to install, unless explicitly requested (e.g., with
``pip install pkg==1.1a3`` or ``pip install --pre pkg``).

The purpose of development releases is to support releases made early during a
development cycle, for example, a nightly build, or a build from the latest
source in a Linux distribution.

Post-releases are used to address minor errors in a final release that do not
affect the distributed software, such as correcting an error in the release
notes. They should not be used for bug fixes; these should be done with a new
final release (e.g., incrementing the third component when using semantic
versioning).

Finally, epochs, a rarely used feature, serve to fix the sorting order when
changing the versioning scheme. For example, if a project is using calendar
versioning, with versions like 23.12, and switches to semantic versioning, with
versions like 1.0, the comparison between 1.0 and 23.12 will go the wrong way.
To correct this, the new version numbers should have an explicit epoch, as in
"1!1.0", in order to be treated as more recent than the old version numbers.



Semantic versioning vs. calendar versioning
===========================================

A versioning scheme is a formalized way to interpret the segments of a version
number, and to decide which should be the next version number for a new release
of a package. Two versioning schemes are commonly used for Python packages,
semantic versioning and calendar versioning.

.. caution::

   The decision which version number to choose is up to a
   project's maintainer. This effectively means that version
   bumps reflect the maintainer's view. That view may differ
   from the end-users' perception of what said formalized
   versioning scheme promises them.

   There are known exceptions for selecting the next version
   number. The maintainers may consciously choose to break the
   assumption that the last version segment only contains
   backwards-compatible changes.
   One such case is when security vulnerability needs to be
   addressed. Security releases often come in patch versions
   but contain breaking changes inevitably.


Semantic versioning
-------------------

The idea of *semantic versioning* (or SemVer) is to use 3-part version numbers,
*major.minor.patch*, where the project author increments:

- *major* when they make incompatible API changes,
- *minor* when they add functionality in a backwards-compatible manner, and
- *patch*, when they make backwards-compatible bug fixes.

A majority of Python projects use a scheme that resembles semantic
versioning. However, most projects, especially larger ones, do not strictly
adhere to semantic versioning, since many changes are technically breaking
changes but affect only a small fraction of users. Such projects tend to
increment the major number when the incompatibility is high, or to signal a
shift in the project, rather than for any tiny incompatibility
[#semver-strictness]_. Conversely, a bump of the major version number
is sometimes used to signal significant but backwards-compatible new
features.

For those projects that do use strict semantic versioning, this approach allows
users to make use of :ref:`compatible release version specifiers
<version-specifiers-compatible-release>`, with the ``~=`` operator.  For
example, ``name ~= X.Y`` is roughly equivalent to ``name >= X.Y, == X.*``, i.e.,
it requires at least release X.Y, and allows any later release with greater Y as
long as X is the same. Likewise, ``name ~= X.Y.Z`` is roughly equivalent to
``name >= X.Y.Z, == X.Y.*``, i.e., it requires at least X.Y.Z and allows a later
release with same X and Y but higher Z.

Python projects adopting semantic versioning should abide by clauses 1-8 of the
`Semantic Versioning 2.0.0 specification <semver_>`_.

The popular :doc:`Sphinx <sphinx:index>` documentation generator is an example
project that uses strict semantic versioning (:doc:`Sphinx versioning policy
<sphinx:internals/release-process>`). The famous :doc:`NumPy <numpy:index>`
scientific computing package explicitly uses "loose" semantic versioning, where
releases incrementing the minor version can contain backwards-incompatible API
changes (:doc:`NumPy versioning policy <numpy:dev/depending_on_numpy>`).


Calendar versioning
-------------------

Semantic versioning is not a suitable choice for all projects, such as those
with a regular time based release cadence and a deprecation process that
provides warnings for a number of releases prior to removal of a feature.

A key advantage of date-based versioning, or `calendar versioning <calver_>`_
(CalVer), is that it is straightforward to tell how old the base feature set of
a particular release is given just the version number.

Calendar version numbers typically take the form *year.month* (for example,
23.12 for December 2023).

:doc:`Pip <pip:index>`, the standard Python package installer, uses calendar
versioning.


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


Local version identifiers
=========================

Public version identifiers are designed to support distribution via :term:`PyPI
<Python Package Index (PyPI)>`. Python packaging tools also support the notion
of a :ref:`local version identifier <local-version-identifiers>`, which can be
used to identify local development builds not intended for publication, or
modified variants of a release maintained by a redistributor.

A local version identifier takes the form of a public version identifier,
followed by "+" and a local version label. For example, a package with
Fedora-specific patches applied could have the version "1.2.1+fedora.4".
Another example is versions computed by setuptools-scm_, a setuptools plugin
that reads the version from Git data. In a Git repository with some commits
since the latest release, setuptools-scm generates a version like
"0.5.dev1+gd00980f", or if the repository has untracked changes, like
"0.5.dev1+gd00980f.d20231217".

.. _runtime-version-access:

Accessing version information at runtime
========================================

Version information for all :term:`distribution packages <Distribution Package>`
that are locally available in the current environment can be obtained at runtime
using the standard library's :func:`importlib.metadata.version` function::

   >>> importlib.metadata.version("cryptography")
   '41.0.7'

Many projects also choose to version their top level
:term:`import packages <Import Package>` by providing a package level
``__version__`` attribute::

   >>> import cryptography
   >>> cryptography.__version__
   '41.0.7'

This technique can be particularly valuable for CLI applications which want
to ensure that version query invocations (such as ``pip -V``) run as quickly
as possible.

Package publishers wishing to ensure their reported distribution package and
import package versions are consistent with each other can review the
:ref:`single-source-version` discussion for potential approaches to doing so.

As import packages and modules are not *required* to publish runtime
version information in this way (see the withdrawn proposal in
:pep:`PEP 396 <396>`), the ``__version__`` attribute should either only be
queried with interfaces that are known to provide it (such as a project
querying its own version or the version of one of its direct dependencies),
or else the querying code should be designed to handle the case where the
attribute is missing [#fallback-to-dist-version]_.

Some projects may need to publish version information for external APIs
that aren't the version of the module itself. Such projects should
define their own project-specific ways of obtaining the relevant information
at runtime. For example, the standard library's :mod:`ssl` module offers
multiple ways to access the underlying OpenSSL library version::

   >>> ssl.OPENSSL_VERSION
   'OpenSSL 3.2.2 4 Jun 2024'
   >>> ssl.OPENSSL_VERSION_INFO
   (3, 2, 0, 2, 0)
   >>> hex(ssl.OPENSSL_VERSION_NUMBER)
   '0x30200020'

--------------------------------------------------------------------------------

.. [#version-examples] Some more examples of unusual version numbers are
   given in a `blog post <versions-seth-larson_>`_ by Seth Larson.

.. [#semver-strictness] For some personal viewpoints on this issue, see these
   blog posts: `by Hynek Schlawak <semver-hynek-schlawack_>`_, `by Donald Stufft
   <semver-donald-stufft_>`_, `by Bernát Gábor <semver-bernat-gabor_>`_, `by
   Brett Cannon <semver-brett-cannon_>`_. For a humoristic take, read about
   ZeroVer_.

.. [#fallback-to-dist-version] A full list mapping the top level names available
   for import to the distribution packages that provide those import packages and
   modules may be obtained through the standard library's
   :func:`importlib.metadata.packages_distributions` function. This means that
   even code that is attempting to infer a version to report for all importable
   top-level names has a means to fall back to reporting the distribution
   version information if no ``__version__`` attribute is defined. Only standard
   library modules, and modules added via means other than Python package
   installation would fail to have version information reported in that case.


.. _zerover: https://0ver.org
.. _calver: https://calver.org
.. _semver: https://semver.org
.. _semver-bernat-gabor: https://bernat.tech/posts/version-numbers/
.. _semver-brett-cannon: https://snarky.ca/why-i-dont-like-semver/
.. _semver-donald-stufft: https://caremad.io/posts/2016/02/versioning-software/
.. _semver-hynek-schlawack: https://hynek.me/articles/semver-will-not-save-you/
.. _setuptools-scm: https://setuptools-scm.readthedocs.io
.. _versions-seth-larson: https://sethmlarson.dev/pep-440
