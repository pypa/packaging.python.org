.. _downstream-packaging:

===============================
Supporting downstream packaging
===============================

:Page Status: Draft
:Last Reviewed: 2025-?

While PyPI and the Python packaging tools such as :ref:`pip` are the primary
means of distributing Python packages, they are also often made available as part
of other packaging ecosystems. These repackaging efforts are collectively called
*downstream* packaging (your own efforts are called *upstream* packaging),
and include such projects as Linux distributions, Conda, Homebrew and MacPorts.
They generally aim to provide improved support for use cases that cannot be handled
via Python packaging tools alone, such as native integration with a specific operating
system, or assured compatibility with specific versions of non-Python software.

This discussion attempts to explain how downstream packaging is usually done,
and what additional challenges downstream packagers typically face. It aims
to provide some optional guidelines that project maintainers may choose to
follow which help make downstream packaging *significantly* easier
(without imposing any major maintenance hassles on the upstream project).
Note that this is not an all-or-nothing proposal — anything that upstream
maintainers can do is useful, even if it's only a small part. Downstream
maintainers are also willing to prepare patches to resolve these issues.
Having these patches merged can be very helpful, since it removes the need
for different downstreams to carry and keep rebasing the same patches,
and the risk of applying inconsistent solutions to the same problem.

Establishing a good relationship between software maintainers and downstream
packagers can bring mutual benefits. Downstreams are often willing to share
their experience, time and hardware to improve your package. They are
sometimes in a better position to see how your package is used in practice,
and to provide information about its relationships with other packages that
would otherwise require significant effort to obtain.
Packagers can often find bugs before your users hit them in production,
provide bug reports of good quality, and supply patches whenever they can.
For example, they are regularly active in ensuring the packages they redistribute
are updated for any compatibility issues that arise when a new Python version
is released.

Please note that downstream builds include not only binary redistribution,
but also source builds done on user systems (in source-first distributions
such as Gentoo Linux, for example).


.. _provide-complete-source-distributions:

Provide complete source distributions
-------------------------------------

Why?
~~~~

The vast majority of downstream packagers prefer to build packages from source,
rather than use the upstream-provided binary packages. In some cases, using
sources is actually required for the package to be included in the distribution.
This is also true of pure Python packages that provide universal wheels.
The reasons for using source distributions may include:

- Being able to audit the source code of all packages.

- Being able to run the test suite and build documentation.

- Being able to easily apply patches, including backporting commits
  from the project's repository and sending patches back to the project.

- Being able to build on a specific platform that is not covered
  by upstream builds.

- Being able to build against specific versions of system libraries.

- Having a consistent build process across all Python packages.

While it is usually possible to build packages from a Git repository, there are
a few important reasons to provide a static archive file instead:

- Fetching a single file is often more efficient, more reliable and better
  supported than e.g. using a Git clone. This can help users with poor
  Internet connectivity.

- Downstreams often use hashes to verify the authenticity of source files
  on subsequent builds, which require that they remain bitwise identical over
  time. For example, automatically generated Git archives do not guarantee
  this, as the compressed data may change if gzip is upgraded on the server.

- Archive files can be mirrored, reducing both upstream and downstream
  bandwidth use. The actual builds can afterwards be performed in firewalled
  or offline environments, that can only access source files provided
  by the local mirror or redistributed earlier.

- Explicitly publishing archive files can ensure that any dependencies on version control
  system metadata are resolved when creating the source archive. For example, automatically
  generated Git archives omit all of the commit tag information, potentially resulting in
  incorrect version details in the resulting builds.

How?
~~~~

Ideally, **a source distribution archive published on PyPI should include all the files
from the package's Git repository** that are necessary to build the package
itself, run its test suite, build and install its documentation, and any other
files that may be useful to end users, such as shell completions, editor
support files, and so on.

This point applies only to the files belonging to the package itself.
The downstream packaging process, much like Python package managers, will
provision the necessary Python dependencies, system tools and external
libraries that are needed by your package and its build scripts. However,
the files listing these dependencies (for example, ``requirements*.txt`` files)
should also be included, to help downstreams determine the needed dependencies,
and check for changes in them.

Some projects have concerns related to Python package managers using source
distributions from PyPI. They do not wish to increase their size with files
that are not used by these tools, or they do not wish to publish source
distributions at all, as they enable a problematic or outright nonfunctional
fallback to building the particular project from source. In these cases, a good
compromise may be to publish a separate source archive for downstream use
elsewhere, for example by attaching it to a GitHub release. Alternatively,
large files, such as test data, can be split into separate archives.

On the other hand, some projects (NumPy_, for instance) decide to include tests
in their installed packages. This has the added advantage of permitting users to
run tests after installing them, for example to check for regressions
after upgrading a dependency. Yet another approach is to split tests or test
data into a separate Python package. Such an approach was taken by
the cryptography_ project, with the large test vectors being split
to cryptography-vectors_ package.

A good idea is to use your source distribution in the release workflow.
For example, the :ref:`build` tool does exactly that — it first builds a source
distribution, and then uses it to build a wheel. This ensures that the source
distribution actually works, and that it won't accidentally install fewer files
than the official wheels.

Ideally, also use the source distribution to run tests, build documentation,
and so on, or add specific tests to make sure that all necessary files were
actually included. Understandably, this requires more effort, so it's fine
not do that — downstream packagers will report any missing files promptly.


.. _no-internet-access-in-builds:

Do not use the Internet during the build process
------------------------------------------------

Why?
~~~~

Downstream builds are frequently done in sandboxed environments that cannot
access the Internet. The package sources are unpacked into this environment,
and all the necessary dependencies are installed.

Even if this is not the case, and assuming that you took sufficient care to
properly authenticate downloads, using the Internet is discouraged for a number
of reasons:

- The Internet connection may be unstable (e.g. due to poor reception)
  or suffer from temporary problems that could cause the process to fail
  or hang.

- The remote resources may become temporarily or even permanently
  unavailable, making the build no longer possible. This is especially
  problematic when someone needs to build an old package version.

- The remote resources may change, making the build not reproducible.

- Accessing remote servers poses a privacy issue and a potential
  security issue, as it exposes information about the system building
  the package.

- The user may be using a service with a limited data plan, in which
  uncontrolled Internet access may result in additional charges or other
  inconveniences.

How?
~~~~

If the package is implementing any custom build *backend* actions that use
the Internet, for example by automatically downloading vendored dependencies
or fetching Git submodules, its source distribution should either include all
of these files or allow provisioning them externally, and the Internet must not
be used if the files are already present.

Note that this point does not apply to Python dependencies that are specified
in the package metadata, and are fetched during the build and installation
process by *frontends* (such as :ref:`build` or :ref:`pip`). Downstreams use
frontends that use local provisioning for Python dependencies.

Ideally, custom build scripts should not even attempt to access the Internet
at all, unless explicitly requested to. If any resources are missing and need
to be fetched, they should ask the user for permission first. If that is not
feasible, the next best thing is to provide an opt-out switch to disable
all Internet access. This could be done e.g. by checking whether
a ``NO_NETWORK`` environment variable is set to a non-empty value.

Since downstreams frequently also run tests and build documentation, the above
should ideally extend to these processes as well.

Please also remember that if you are fetching remote resources, you absolutely
must *verify their authenticity* (usually against a hash), to protect against
the file being substituted by a malicious party.


.. _support-system-dependencies-in-builds:

Support building against system dependencies
--------------------------------------------

Why?
~~~~

Some Python projects have non-Python dependencies, such as libraries written
in C or C++. Trying to use the system versions of these dependencies
in upstream packaging may cause a number of problems for end users:

- The published wheels require a binary-compatible version of the used
  library to be present on the user's system. If the library is missing
  or an incompatible version is installed, the Python package may fail with errors
  that are not clear to inexperienced users, or even misbehave at runtime.

- Building from a source distribution requires a source-compatible version
  of the dependency to be present, along with its development headers
  and other auxiliary files that some systems package separately
  from the library itself.

- Even for an experienced user, installing a compatible dependency version
  may be very hard. For example, the used Linux distribution may not provide
  the required version, or some other package may require an incompatible
  version.

- The linkage between the Python package and its system dependency is not
  recorded by the packaging system. The next system update may upgrade
  the library to a newer version that breaks binary compatibility with
  the Python package, and requires user intervention to fix.

For these reasons, you may reasonably decide to either statically link
your dependencies, or to provide local copies in the installed package.
You may also vendor the dependency in your source distribution. Sometimes
these dependencies are also repackaged on PyPI, and can be declared as
project dependencies like any other Python package.

However, none of these issues apply to downstream packaging, and downstreams
have good reasons to prefer dynamically linking to system dependencies.
In particular:

- In many cases, reliably sharing dynamic dependencies between components is a large part
  of the *purpose* of a downstream packaging ecosystem. Helping to support that makes it
  easier for users of those systems to access upstream projects in their preferred format.

- Static linking and vendoring obscures the use of external dependencies,
  making source auditing harder.

- Dynamic linking makes it possible to quickly and systematically replace the used
  libraries across an entire downstream packaging ecosystem, which can be particularly
  important when they turn out to contain a security vulnerability or critical bug.

- Using system dependencies makes the package benefit from downstream
  customization that can improve the user experience on a particular platform,
  without the downstream maintainers having to consistently patch
  the dependencies vendored in different packages. This can include
  compatibility improvements and security hardening.

- Static linking and vendoring can result in multiple different versions of the
  same library being loaded in the same process (for example, attempting to
  import two Python packages that link to different versions of the same library).
  This sometimes works without incident, but it can also lead to anything from library
  loading errors, to subtle runtime bugs, to catastrophic failures (like suddenly
  crashing and losing data).

- Last but not least, static linking and vendoring results in duplication,
  and may increase the use of both disk space and memory.

How?
~~~~

A good compromise between the needs of both parties is to provide a switch
between using vendored and system dependencies. Ideally, if the package has
multiple vendored dependencies, it should provide both individual switches
for each dependency, and a general switch to control the default for them,
e.g. via a ``USE_SYSTEM_DEPS`` environment variable.

If the user requests using system dependencies, and a particular dependency
is either missing or incompatible, the build should fail with an explanatory
message rather than fall back to a vendored version. This gives the packager
the opportunity to notice their mistake and a chance to consciously decide
how to solve it.

It is reasonable for upstream projects to leave *testing* of building with
system dependencies to their downstream repackagers. The goal of these guidelines
is to facilitate more effective collaboration between upstream projects and downstream
repackagers, not to suggest upstream projects take on tasks that downstream repackagers
are better equipped to handle.

.. _support-downstream-testing:

Support downstream testing
--------------------------

Why?
~~~~

A variety of downstream projects run some degree of testing on the packaged
Python projects. Depending on the particular case, this can range from minimal
smoke testing to comprehensive runs of the complete test suite. There can
be various reasons for doing this, for example:

- Verifying that the downstream packaging did not introduce any bugs.

- Testing on additional platforms that are not covered by upstream testing.

- Finding subtle bugs that can only be reproduced with particular hardware,
  system package versions, and so on.

- Testing the released package against newer (or older) dependency versions than
  the ones present during upstream release testing.

- Testing the package in an environment closely resembling the production
  setup. This can detect issues caused by non-trivial interactions between
  different installed packages, including packages that are not dependencies
  of your package, but nevertheless can cause issues.

- Testing the released package against newer Python versions (including
  newer point releases), or less tested Python implementations such as PyPy.

Admittedly, sometimes downstream testing may yield false positives or bug
reports about scenarios the upstream project is not interested in supporting.
However, perhaps even more often it does provide early notice of problems,
or find non-trivial bugs that would otherwise cause issues for the upstream
project's users. While mistakes do happen, the majority of downstream packagers
are doing their best to double-check their results, and help upstream
maintainers triage and fix the bugs that they reported.

How?
~~~~

There are a number of things that upstream projects can do to help downstream
repackagers test their packages efficiently and effectively, including some of the suggestions
already mentioned above. These are typically improvements that make the test suite more
reliable and easier to use for everyone, not just downstream packagers.
Some specific suggestions are:

- Include the test files and fixtures in the source distribution, or make it
  possible to easily download them separately.

- Do not write to the package directories during testing. Downstream test
  setups sometimes run tests on top of the installed package, and modifications
  performed during testing and temporary test files may end up being part
  of the installed package!

- Make the test suite work offline. Mock network interactions, using
  packages such as responses_ or vcrpy_. If that is not possible, make it
  possible to easily disable the tests using Internet access, e.g. via a pytest_
  marker. Use pytest-socket_ to verify that your tests work offline. This
  often makes your own test workflows faster and more reliable as well.

- Make your tests work without a specialized setup, or perform the necessary
  setup as part of test fixtures. Do not ever assume that you can connect
  to system services such as databases — in an extreme case, you could crash
  a production service!

- If your package has optional dependencies, make their tests optional as
  well. Either skip them if the needed packages are not installed, or add
  markers to make deselecting easy.

- More generally, add markers to tests with special requirements. These can
  include e.g. significant space usage, significant memory usage, long runtime,
  incompatibility with parallel testing.

- Do not assume that the test suite will be run with ``-Werror``. Downstreams
  often need to disable that, as it causes false positives, e.g. due to newer
  dependency versions. Assert for warnings using ``pytest.warns()`` rather
  than ``pytest.raises()``!

- Aim to make your test suite reliable and reproducible. Avoid flaky tests.
  Avoid depending on specific platform details, don't rely on exact results
  of floating-point computation, or timing of operations, and so on. Fuzzing
  has its advantages, but you want to have static test cases for completeness
  as well.

- Split tests by their purpose, and make it easy to skip categories that are
  irrelevant or problematic. Since the primary purpose of downstream testing
  is to ensure that the package itself works, downstreams are not generally interested
  in tasks such as checking code coverage, code formatting, typechecking or running
  benchmarks. These tests can fail as dependencies are upgraded or the system
  is under load, without actually affecting the package itself.

- If your test suite takes significant time to run, support testing
  in parallel. Downstreams often maintain a large number of packages,
  and testing them all takes a lot of time. Using pytest-xdist_ can help them
  avoid bottlenecks.

- Ideally, support running your test suite via ``pytest``. pytest_ has many
  command-line arguments that are truly helpful to downstreams, such as
  the ability to conveniently deselect tests, rerun flaky tests
  (via pytest-rerunfailures_), add a timeout to prevent tests from hanging
  (via pytest-timeout_) or run tests in parallel (via pytest-xdist_).
  Note that test suites don't need to be *written* with ``pytest`` to be
  *executed* with ``pytest``: ``pytest`` is able to find and execute almost
  all test cases that are compatible with the standard library's ``unittest``
  test discovery.


.. _aim-for-stable-releases:

Aim for stable releases
-----------------------

Why?
~~~~

Many downstreams provide stable release channels in addition to the main
package streams. The goal of these channels is to provide more conservative
upgrades to users with higher stability needs. These users often prefer
to trade having the newest features available for lower risk of issues.

While the exact policies differ, an important criterion for including a new
package version in a stable release channel is for it to be available in testing
for some time already, and have no known major regressions. For example,
in Gentoo Linux a package is usually marked stable after being available
in testing for a month, and being tested against the versions of its
dependencies that are marked stable at the time.

However, there are circumstances which demand more prompt action. For example,
if a security vulnerability or a major bug is found in the version that is
currently available in the stable channel, the downstream is facing a need
to resolve it. In this case, they need to consider various options, such as:

- putting a new version in the stable channel early,

- adding patches to the version currently published,

- or even downgrading the stable channel to an earlier release.

Each of these options involves certain risks and a certain amount of work,
and packagers needs to weigh them to determine the course of action.

How?
~~~~

There are some things that upstreams can do to tailor their workflow to stable
release channels. These actions often are beneficial to the package's users
as well. Some specific suggestions are:

- Adjust the release frequency to the rate of code changes. Packages that
  are released rarely often bring significant changes with every release,
  and a higher risk of accidental regressions.

- Avoid mixing bug fixes and new features, if possible. In particular, if there
  are known bug fixes merged already, consider making a new release before
  merging feature branches.

- Consider making prereleases after major changes, to provide more testing
  opportunities for users and downstreams willing to opt-in.

- If your project is subject to very intense development, consider splitting
  one or more branches that include a more conservative subset of commits,
  and are released separately. For example, Django_ currently maintains three
  release branches in addition to main.

- Even if you don't wish to maintain additional branches permanently, consider
  making additional patch releases with minimal changes to the previous
  version, especially when a security vulnerability is discovered.

- Split your changes into focused commits that address one problem at a time,
  to make it easier to cherry-pick changes to earlier releases when necessary.


.. _responses: https://pypi.org/project/responses/
.. _vcrpy: https://pypi.org/project/vcrpy/
.. _pytest-socket: https://pypi.org/project/pytest-socket/
.. _pytest-xdist: https://pypi.org/project/pytest-xdist/
.. _pytest: https://pytest.org/
.. _pytest-rerunfailures: https://pypi.org/project/pytest-rerunfailures/
.. _pytest-timeout: https://pypi.org/project/pytest-timeout/
.. _Django: https://www.djangoproject.com/
.. _NumPy: https://numpy.org/
.. _cryptography: https://pypi.org/project/cryptography/
.. _cryptography-vectors: https://pypi.org/project/cryptography-vectors/
