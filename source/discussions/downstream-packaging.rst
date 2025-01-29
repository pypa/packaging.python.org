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
release. Alternatively, large files, such as test data, can be split into
separate archives.

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


.. _Support building against system dependencies:

Support building against system dependencies
--------------------------------------------
Some Python projects have non-Python dependencies, such as libraries written
in C or C++. Trying to use the system versions of these dependencies
in upstream packaging may cause a number of problems for end users:

- The published wheels require a binary-compatible version of the used library
  to be present on the user's system. If the library is missing or installed
  in incompatible version, the Python package may fail with errors that
  are not clear to inexperienced users, or even misbehave at runtime.

- Building from source distribution requires a source-compatible version
  of the dependency to be present, along with its development headers and other
  auxiliary files that some systems package separately from the library itself.

- Even for an experienced user, installing a compatible dependency version
  may be very hard. For example, the used Linux distribution may not provide
  the required version, or some other package may require an incompatible
  version.

- The linkage between the Python package and its system dependency is not
  recorded by the packaging system. The next system update may upgrade
  the library to a newer version that breaks binary compatibility with
  the Python package, and requires user intervention to fix.

For these reasons, you may reasonable to decide to either link statically
to your dependencies, or to provide a local copies in the installed package.
You may also vendor the dependency in your source distribution.  Sometimes
these dependencies are also repackaged on PyPI, and can be installed
like a regular Python packages.

However, none of these issues apply to downstream packaging, and downstreams
have good reasons to prefer dynamically linking to system dependencies.
In particular:

- Static linking and vendoring obscures the use of external dependencies,
  making source auditing harder.

- Dynamic linking makes it possible to easily and quickly replace the used
  libraries, which can be particularly important when they turn out to
  be vulnerable or buggy.

- Using system dependencies makes the package benefit from downstream
  customization that can improve the user experience on a particular platform,
  without the downstream maintainers having to consistently patch
  the dependencies vendored in different packages. This can include
  compatibility improvements and security hardening.

- Static linking and vendoring could result in multiple different versions
  of the same library being loaded in the same process (e.g. when you use two
  Python packages that link to different versions of the same library).
  This can cause no problems, but it could also lead to anything from subtle
  bugs to catastrophic failures.

- Last but not least, static linking and vendoring results in duplication,
  and may increase the use of both the disk space and memory.

A good compromise between the needs of both parties is to provide a switch
between using vendored and system dependencies. Ideally, if the package has
multiple vendored dependencies, it should provide both individual switches
for each dependency, and a general switch, for example using
a  ``USE_SYSTEM_DEPS`` environment variable to control the default. If switched
on, and a particular dependency is either missing or incompatible, the build
should fail with an explanatory message, giving the packager an explicit
indication of the problem and a chance to consciously decide on the preferred
course of action.


.. _Support downstream testing:

Support downstream testing
--------------------------
A variety of downstream projects run some degree of testing on the packaged
Python projects. Depending on the particular case, this can range from minimal
smoke testing to comprehensive runs of the complete test suite. There can
be various reasons for doing this, for example:

- Verifying that the downstream packaging did not introduce any bugs.

- Testing on a platform that is not covered by upstream testing.

- Finding subtle bugs that can only be reproduced on a particular hardware,
  system package versions, and so on.

- Testing the released package against newer dependency version than the ones
  present during upstream release testing.

- Testing the package in an environment closely resembling the production
  setup. This can detect issues caused by nontrivial interactions between
  different installed packages, including packages that are not dependencies
  of your package, but nevertheless can cause issues.

- Testing the released package against newer Python versions (including newer
  point releases), or less tested Python implementations such as PyPy.

Admittedly, sometimes downstream testing may yield false positives or
inconvenience you about scenarios that you are not interested in supporting.
However, perhaps even more often it does provide early notice of problems,
or find nontrivial bugs that would otherwise cause issues for your users
in production. And believe me, the majority of downstream packagers are doing
their best to double-check their results, and help you triage and fix the bugs
that they report.

There is a number of things that you can do to help us test your package
better. Some of them were already mentioned in this discussion. Some examples
are:

- **Include the test files and fixtures in the source distribution**, or make it
  possible to easily download them separately.

- **Do not write to the package directories during testing.** Downstream test
  setups sometimes run tests on top of the installed package, and modifications
  performed during testing and temporary test files may end up being part
  of the installed package!

- **Make the test suite work offline.** Mock network interactions, using
  packages such as responses_ or vcrpy_. If that is not possible, make it
  possible to easily disable the tests using Internet access, e.g. via a pytest
  marker.  Use pytest-socket_ to verify that your tests work offline. This
  often makes your own test workflows faster and more reliable as well.

- **Make your tests work without a specialized setup**, or perform the necessary
  setup as part of test fixtures. Do not ever assume that you can connect
  to system services such as databases — in an extreme case, you could crash
  a production service!

- **If your package has optional dependencies, make their tests optional as
  well.** Either skip them if the needed packages are not installed, or add
  markers to make deselecting easy.

- More generally, **add markers to tests with special requirements**. These can
  include e.g. significant space usage, significant memory usage, long runtime,
  incompatibility with parallel testing.

- **Do not assume that the test suite will be run with -Werror.** Downstreams
  often need to disable that, as it causes false positives, e.g. due to newer
  dependency versions. Assert for warnings using ``pytest.warns()`` rather
  than ``pytest.raises()``!

- **Aim to make your test suite reliable and reproducible.** Avoid flaky tests.
  Avoid depending on specific platform details, don't rely on exact results
  of floating-point computation, or timing of operations, and so on. Fuzzing
  has its advantages, but you want to have static test cases for completeness
  as well.

- **Split tests by their purpose, and make it easy to skip categories that are
  irrelevant or problematic.** Since the primary purpose of downstream testing
  is to ensure that the package itself works, we generally are not interested
  in e.g. checking code coverage, code formatting, typing or running
  benchmarks. These tests can fail as dependencies are upgraded or the system
  is under load, without actually affecting the package itself.

- If your test suite takes significant time to run, **support testing
  in parallel.** Downstreams often maintain a large number of packages,
  and testing them all takes a lot of time. Using pytest-xdist_ can help them
  avoid bottlenecks.

- Ideally, **support running your test suite via PyTest**. PyTest_ has many
  command-line arguments that are truly helpful to downstreams, such as
  the ability to conveniently deselect tests, rerun flaky tests
  (via pytest-rerunfailures_), add a timeout to prevent tests from hanging
  (via pytest-timeout_) or run tests in parallel (via pytest-xdist_).


.. _responses: https://pypi.org/project/responses/
.. _vcrpy: https://pypi.org/project/vcrpy/
.. _pytest-socket: https://pypi.org/project/pytest-socket/
.. _pytest-xdist: https://pypi.org/project/pytest-xdist/
.. _pytest: https://pytest.org/
.. _pytest-rerunfailures: https://pypi.org/project/pytest-rerunfailures/
.. _pytest-timeout: https://pypi.org/project/pytest-timeout/
