.. _downstream-packaging:

========================================
How to make downstream packaging easier?
========================================

:Page Status: Draft
:Last Reviewed: 2025-?

While PyPI and the Python packaging tools such as :ref:`pip` are the primary
means of distributing your packages, they are often also made available as part
of other packaging ecosystems. These repackaging efforts are collectively called
*downstream* packaging (your own efforts are called *upstream* packaging),
and include such projects as Linux distributions, Conda, Homebrew and MacPorts.
They often aim to provide good support for use cases that cannot be handled
via Python packaging tools alone, such as good integration with non-Python
software.

This discussion attempts to explain how downstream packaging is usually done,
and what challenges are downstream packagers facing. It ultimately aims to give
you some hints on how you can make downstream packaging easier.

Please note that downstream builds include not only binary redistribution,
but also source builds done on user systems, in source-first distributions
such as Gentoo Linux.


.. _Provide complete source distributions:

Provide complete source distributions
-------------------------------------
The vast majority of downstream packagers prefer to build packages from source,
rather than use the upstream-provided binary packages. This is also true
of pure Python packages that provide universal wheels. The reasons for using
source distributions may include:

- being able to audit the source code of all packages

- being able to run the test suite and build documentation

- being able to easily apply patches, including backporting commits from your
  repository and sending patches back to you

- being able to build against a specific platform that is not covered
  by upstream builds

- being able to build against specific versions of system libraries

- having a consistent build process across all Python packages

Ideally, a source distribution archive should include all the files necessary
to build the package itself, run its test suite, build and install its
documentation, and any other files that may be useful to end users, such
as shell completions, editor support files, and so on.

Some projects are concerned about increasing the size of source distribution,
or do not wish Python packaging tools to fall back to source distributions
automatically.  In these cases, a good compromise may be to publish a separate
source archive for downstream use, for example by attaching it to a GitHub
release.

While it is usually possible to build packages from a git repository, there are
a few important reasons to provide a static archive file instead:

- Fetching a single file is often more efficient, more reliable and better
  supported than e.g. using a git clone. This can help users with a shoddy
  Internet connection.

- Downstreams often use checksums to verify the authenticity of source files
  on subsequent builds, which require that they remain bitwise identical over
  time. For example, automatically generated git archives do not guarantee
  that.

- Archive files can be mirrored, reducing both upstream and downstream
  bandwidth use. The actual builds can afterwards be performed in firewalled
  or offline environments, that can only access source files provided
  by the local mirror or redistributed earlier.

A good idea is to use a release workflow that starts by building a source
distribution, and then performs all the remaining release steps (such as
running tests and building wheels) from the unpacked source distribution. This
ensures that the source distribution is actually tested, and reduces the risk
that users installing from it will hit build failures or install an incomplete
package.


.. _Do not use the Internet during the build process:

Do not use the Internet during the build process
------------------------------------------------
Downstream builds are frequently done in sandboxed environments that cannot
access the Internet. Therefore, it is important that your source distribution
includes all the files needed for the package to build or allows provisioning
them externally, and can build successfully without Internet access.

Ideally, it should not even attempt to access the Internet at all, unless
explicitly requested to. If that is not possible to achieve, the next best
thing is to provide an opt-out switch to disable all Internet access, and fail
if some of the required files are missing instead of trying to fetch them. This
could be done e.g. by checking whether a ``NO_NETWORK`` environment variable is
to a non-empty value. Please also remember that if you are fetching remote
resources, you should verify their authenticity, e.g.  against a checksum, to
protect against the file being substituted by a malicious party.

Even if downloads are properly authenticated, using the Internet is discouraged
for a number of reasons:

- The Internet connection may be unstable (e.g. poor reception) or suffer from
  temporary problems that could cause the downloads to fail or hang.

- The remote resources may become temporarily or even permanently unavailable,
  making the build no longer possible. This is especially problematic when
  someone needs to build an old package version.

- Accessing remote servers poses a privacy issue and a potential security issue,
  as it exposes information about the system building the package.

- The user may be using a service with a limited data plan, in which
  uncontrolled Internet access may result in additional charges or other
  inconveniences.

Since downstreams frequently also run tests and build documentation, the above
should ideally extend to these processes as well.
