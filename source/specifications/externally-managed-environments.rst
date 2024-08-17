
.. _externally-managed-environments:

===============================
Externally Managed Environments
===============================

While some Python installations are entirely managed by the user that installed
Python, others may be provided and managed by another means (such as the
operating system package manager in a Linux distribution, or as a bundled
Python environment in an application with a dedicated installer).

Attempting to use conventional Python packaging tools to manipulate such
environments can be confusing at best and outright break the entire underlying
operating system at worst. Documentation and interoperability guides only go
so far in resolving such problems.

This specification defines an ``EXTERNALLY-MANAGED`` marker file that allows a
Python installation to indicate to Python-specific tools such as ``pip`` that they
neither install nor remove packages into the interpreter’s default installation
environment, and should instead guide the end user towards using
:ref:`virtual-environments`.

It also standardizes an interpretation of the ``sysconfig`` schemes so
that, if a Python-specific package manager is about to install a
package in an interpreter-wide context, it can do so in a manner that
will avoid conflicting with the external package manager and reduces
the risk of breaking software shipped by the external package manager.


Terminology
===========

A few terms used in this specification have multiple meanings in the
contexts that it spans. For clarity, this specification uses the following
terms in specific ways:

distro
    Short for "distribution," a collection of various sorts of
    software, ideally designed to work properly together, including
    (in contexts relevant to this document) the Python interpreter
    itself, software written in Python, and software written in other
    languages. That is, this is the sense used in phrases such as
    "Linux distro" or "Berkeley Software Distribution."

    A distro can be an operating system (OS) of its own, such as
    Debian, Fedora, or FreeBSD. It can also be an overlay distribution
    that installs on top of an existing OS, such as Homebrew or
    MacPorts.

    This document uses the short term "distro," because the term
    "distribution" has another meaning in Python packaging contexts: a
    source or binary distribution package of a single piece of Python
    language software, that is, in the sense of
    ``setuptools.dist.Distribution`` or "sdist". To avoid confusion,
    this document does not use the plain term "distribution" at all.
    In the Python packaging sense, it uses the full phrase
    "distribution package" or just "package" (see below).

    The provider of a distro - the team or company that collects and
    publishes the software and makes any needed modifications - is its
    **distributor**.
package
    A unit of software that can be installed and used within Python.
    That is, this refers to what Python-specific packaging tools tend
    to call a :term:`distribution package` or simply a "distribution";
    the colloquial abbreviation "package" is used in the sense of the
    Python Package Index.

    This document does not use "package" in the sense of an importable
    name that contains Python modules, though in many cases, a
    distribution package consists of a single importable package of
    the same name.

    This document generally does not use the term "package" to refer
    to units of installation by a distro's package manager (such as
    ``.deb`` or ``.rpm`` files). When needed, it uses phrasing such as
    "a distro's package." (Again, in many cases, a Python package is
    shipped inside a distro's package named something like ``python-``
    plus the Python package name.)
Python-specific package manager
    A tool for installing, upgrading, and/or removing Python packages
    in a manner that conforms to Python packaging standards.
    The most popular Python-specific package
    manager is pip_; other examples include the old `Easy
    Install command <easy-install_>`_ as well as direct usage of a
    ``setup.py`` command.

    .. _pip: https://pip.pypa.io/en/stable/
    .. _easy-install: https://setuptools.readthedocs.io/en/latest/deprecated/easy_install.html

    (Note that the ``easy_install`` command was removed in
    setuptools version 52, released 23 January 2021.)


    (Conda_ is a bit of a special case, as the ``conda``
    command can install much more than just Python packages, making it
    more like a distro package manager in some senses. Since the
    ``conda`` command generally only operates on Conda-created
    environments, most of the concerns in this document do not apply
    to ``conda`` when acting as a Python-specific package manager.)

    .. _conda: https://conda.io
distro package manager
    A tool for installing, upgrading, and/or removing a distro's
    packages in an installed instance of that distro, which is capable
    of installing Python packages as well as non-Python packages, and
    therefore generally has its own database of installed software
    unrelated to the :ref:`database of installed distributions
    <recording-installed-packages>`. Examples include ``apt``, ``dpkg``,
    ``dnf``, ``rpm``, ``pacman``, and ``brew``. The salient feature is
    that if a package was installed by a distro package manager, removing or
    upgrading it in a way that would satisfy a Python-specific package
    manager will generally leave a distro package manager in an
    inconsistent state.

    This document also uses phrases like "external package manager" or
    "system's package manager" to refer to a distro package manager in
    certain contexts.
shadow
    To shadow an installed Python package is to cause some other
    package to be preferred for imports without removing any files
    from the shadowed package. This requires multiple entries on
    ``sys.path``: if package A 2.0 installs module ``a.py`` in one
    ``sys.path`` entry, and package A 1.0 installs module ``a.py`` in
    a later ``sys.path`` entry, then ``import a`` returns the module
    from the former, and we say that A 2.0 shadows A 1.0.

Overview
========

This specification is twofold.

First, it describes **a way for distributors of a Python interpreter to
mark that interpreter as having its packages managed by means external
to Python**, such that Python-specific tools like pip should not
change the installed packages in the interpreter's global ``sys.path``
in any way (add, upgrade/downgrade, or remove) unless specifically
overridden. It also provides a means for the distributor to indicate
how to use a virtual environment as an alternative.

This is an opt-in mechanism: by default, the Python interpreter
compiled from upstream sources will not be so marked, and so running
``pip install`` with a self-compiled interpreter, or with a distro
that has not explicitly marked its interpreter, will work as it always
has worked.

Second, it sets the rule that when installing packages to an
interpreter's global context (either to an unmarked interpreter, or if
overriding the marking), **Python-specific package managers should
modify or delete files only within the directories of the sysconfig
scheme in which they would create files**. This permits a distributor
of a Python interpreter to set up two directories, one for its own
managed packages, and one for unmanaged packages installed by the end
user, and ensure that installing unmanaged packages will not delete
(or overwrite) files owned by the external package manager.


Marking an interpreter as using an external package manager
===========================================================

Before a Python-specific package installer (that is, a tool such as
pip - not an external tool such as apt) installs a package into a
certain Python context, it should make the following checks by
default:

1. Is it running outside of a virtual environment? It can determine
   this by whether ``sys.prefix == sys.base_prefix``.

2. Is there an ``EXTERNALLY-MANAGED`` file in the directory identified
   by ``sysconfig.get_path("stdlib", sysconfig.get_default_scheme())``?

If both of these conditions are true, the installer should exit with
an error message indicating that package installation into this Python
interpreter's directory are disabled outside of a virtual environment.

The installer should have a way for the user to override these rules,
such as a command-line flag ``--break-system-packages``. This option
should not be enabled by default and should carry some connotation
that its use is risky.

The ``EXTERNALLY-MANAGED`` file is an INI-style metadata file intended
to be parsable by the standard library configparser_ module. If the
file can be parsed by
``configparser.ConfigParser(interpolation=None)`` using the UTF-8
encoding, and it contains a section ``[externally-managed]``, then the
installer should look for an error message specified in the file and
output it as part of its error. If the first element of the tuple
returned by ``locale.getlocale(locale.LC_MESSAGES)``, i.e., the
language code, is not ``None``, it should look for the error message
as the value of a key named ``Error-`` followed by the language code.
If that key does not exist, and if the language code contains
underscore or hyphen, it should look for a key named ``Error-``
followed by the portion of the language code before the underscore or
hyphen. If it cannot find either of those, or if the language code is
``None``, it should look for a key simply named ``Error``.

.. _configparser: https://docs.python.org/3/library/configparser.html

If the installer cannot find an error message in the file (either
because the file cannot be parsed or because no suitable error key
exists), then the installer should just use a pre-defined error
message of its own, which should suggest that the user create a
virtual environment to install packages.

Software distributors who have a non-Python-specific package manager
that manages libraries in the ``sys.path`` of their Python package
should, in general, ship an ``EXTERNALLY-MANAGED`` file in their
standard library directory. For instance, Debian may ship a file in
``/usr/lib/python3.9/EXTERNALLY-MANAGED`` consisting of something like

.. code-block:: ini

    [externally-managed]
    Error=To install Python packages system-wide, try apt install
     python3-xyz, where xyz is the package you are trying to
     install.

     If you wish to install a non-Debian-packaged Python package,
     create a virtual environment using python3 -m venv path/to/venv.
     Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
     sure you have python3-full installed.

     If you wish to install a non-Debian packaged Python application,
     it may be easiest to use pipx install xyz, which will manage a
     virtual environment for you. Make sure you have pipx installed.

     See /usr/share/doc/python3.9/README.venv for more information.

which provides useful and distro-relevant information
to a user trying to install a package. Optionally,
translations can be provided in the same file:

.. code-block:: ini

    Error-de_DE=Wenn ist das Nunstück git und Slotermeyer?

     Ja! Beiherhund das Oder die Virtualenvironment gersput!

In certain contexts, such as single-application container images that
aren't updated after creation, a distributor may choose not to ship an
``EXTERNALLY-MANAGED`` file, so that users can install whatever they
like (as they can today) without having to manually override this
rule.

Writing to only the target ``sysconfig`` scheme
===============================================

Usually, a Python package installer installs to directories in a
scheme returned by the ``sysconfig`` standard library package.
Ordinarily, this is the scheme returned by
``sysconfig.get_default_scheme()``, but based on configuration (e.g.
``pip install --user``), it may use a different scheme.

Whenever the installer is installing to a ``sysconfig`` scheme, this
specification declares that the installer should never modify or delete files
outside of that scheme. For instance, if it's upgrading a package, and
the package is already installed in a directory outside that scheme
(perhaps in a directory from another scheme), it should leave the
existing files alone.

If the installer does end up shadowing an existing installation during
an upgrade, we recommend that it produces a warning at the end of its
run.

If the installer is installing to a location outside of a
``sysconfig`` scheme (e.g., ``pip install --target``), then this
subsection does not apply.

Recommendations for distros
===========================

This section is non-normative. It provides best practices we believe
distros should follow unless they have a specific reason otherwise.

Mark the installation as externally managed
-------------------------------------------

Distros should create an ``EXTERNALLY-MANAGED`` file in their
``stdlib`` directory.

Guide users towards virtual environments
----------------------------------------

The file should contain a useful and distro-relevant error message
indicating both how to install system-wide packages via the distro's
package manager and how to set up a virtual environment. If your
distro is often used by users in a state where the ``python3`` command
is available (and especially where ``pip`` or ``get-pip`` is
available) but ``python3 -m venv`` does not work, the message should
indicate clearly how to make ``python3 -m venv`` work properly.

Consider packaging pipx_, a tool for installing Python-language
applications, and suggesting it in the error. pipx automatically
creates a virtual environment for that application alone, which is a
much better default for end users who want to install some
Python-language software (which isn't available in the distro) but are
not themselves Python users. Packaging pipx in the distro avoids the
irony of instructing users to ``pip install --user
--break-system-packages pipx`` to *avoid* breaking system packages.
Consider arranging things so your distro's package / environment for
Python for end users (e.g., ``python3`` on Fedora or ``python3-full``
on Debian) depends on pipx.

.. _pipx: https://github.com/pypa/pipx

Keep the marker file in container images
----------------------------------------

Distros that produce official images for single-application containers
(e.g., Docker container images) should keep the
``EXTERNALLY-MANAGED`` file, preferably in a way that makes it not
go away if a user of that image installs package updates inside
their image (think ``RUN apt-get dist-upgrade``).

Create separate distro and local directories
--------------------------------------------

Distros should place two separate paths on the system interpreter's
``sys.path``, one for distro-installed packages and one for packages
installed by the local system administrator, and configure
``sysconfig.get_default_scheme()`` to point at the latter path. This
ensures that tools like pip will not modify distro-installed packages.
The path for the local system administrator should come before the
distro path on ``sys.path`` so that local installs take preference
over distro packages.

For example, Fedora and Debian (and their derivatives) both implement
this split by using ``/usr/local`` for locally-installed packages and
``/usr`` for distro-installed packages. Fedora uses
``/usr/local/lib/python3.x/site-packages`` vs.
``/usr/lib/python3.x/site-packages``. (Debian uses
``/usr/local/lib/python3/dist-packages`` vs.
``/usr/lib/python3/dist-packages`` as an additional layer of
separation from a locally-compiled Python interpreter: if you build
and install upstream CPython in ``/usr/local/bin``, it will look at
``/usr/local/lib/python3/site-packages``, and Debian wishes to make
sure that packages installed via the locally-built interpreter don't
show up on ``sys.path`` for the distro interpreter.)

Note that the ``/usr/local`` vs. ``/usr`` split is analogous to how
the ``PATH`` environment variable typically includes
``/usr/local/bin:/usr/bin`` and non-distro software installs to
``/usr/local`` by default. This split is `recommended by the
Filesystem Hierarchy Standard`__.

.. __: https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04s09.html

There are two ways you could do this. One is, if you are building and
packaging Python libraries directly (e.g., your packaging helpers
unpack a wheel or call ``setup.py install``), arrange
for those tools to use a directory that is not in a ``sysconfig``
scheme but is still on ``sys.path``.

The other is to arrange for the default ``sysconfig`` scheme to change
when running inside a package build versus when running on an
installed system. The ``sysconfig`` customization hooks from
bpo-43976_ should make this easy (once accepted and implemented):
make your packaging tool set an
environment variable or some other detectable configuration, and
define a ``get_preferred_schemes`` function to return a different
scheme when called from inside a package build. Then you can use ``pip
install`` as part of your distro packaging.

.. _bpo-43976: https://bugs.python.org/issue43976

We propose adding a ``--scheme=...`` option to instruct pip to run
against a specific scheme. (See `Implementation Notes`_ below for how
pip currently determines schemes.) Once that's available, for local
testing and possibly for actual packaging, you would be able to run
something like ``pip install --scheme=posix_distro`` to explicitly
install a package into your distro's location (bypassing
``get_preferred_schemes``). One could also, if absolutely needed, use
``pip uninstall --scheme=posix_distro`` to use pip to remove packages
from the system-managed directory.

To install packages with pip, you would also need to either suppress
the ``EXTERNALLY-MANAGED`` marker file to allow pip to run or to
override it on the command line. You may want to use the same means
for suppressing the marker file in build chroots as you do in
container images.

The advantage of setting these up to be automatic (suppressing the
marker file in your build environment and having
``get_preferred_schemes`` automatically return your distro's scheme)
is that an unadorned ``pip install`` will work inside a package build,
which generally means that an unmodified upstream build script that
happens to internally call ``pip install`` will do the right thing.
You can, of course, just ensure that your packaging process always
calls ``pip install --scheme=posix_distro --break-system-packages``,
which would work too.

The best approach here depends a lot on your distro's conventions and
mechanisms for packaging.

Similarly, the ``sysconfig`` paths that are not for importable Python
code - that is, ``include``, ``platinclude``, ``scripts``, and
``data`` - should also have two variants, one for use by
distro-packaged software and one for use for locally-installed
software, and the distro should be set up such that both are usable.
For instance, a typical FHS-compliant distro will use
``/usr/local/include`` for the default scheme's ``include`` and
``/usr/include`` for distro-packaged headers and place both on the
compiler's search path, and it will use ``/usr/local/bin`` for the
default scheme's ``scripts`` and ``/usr/bin`` for distro-packaged
entry points and place both on ``$PATH``.


Implementation Notes
====================

This section is non-normative and contains notes relevant to both the
specification and potential implementations.

Currently (as of May 2021), pip does not directly expose a way to choose
a target ``sysconfig`` scheme, but it has three ways of looking up schemes
when installing:

``pip install``
    Calls ``sysconfig.get_default_scheme()``, which is usually (in
    upstream CPython and most current distros) the same as
    ``get_preferred_scheme('prefix')``.

``pip install --prefix=/some/path``
    Calls ``sysconfig.get_preferred_scheme('prefix')``.

``pip install --user``
    Calls ``sysconfig.get_preferred_scheme('user')``.

Finally, ``pip install --target=/some/path`` writes directly to
``/some/path`` without looking up any schemes.

Debian currently carries a `patch to change the default install
location inside a virtual environment`__, using a few heuristics
(including checking for the ``VIRTUAL_ENV`` environment variable),
largely so that the directory used in a virtual environment remains
``site-packages`` and not ``dist-packages``. This does not
particularly affect this proposal, because the implementation of that
patch does not actually change the default ``sysconfig`` scheme, and
notably does not change the result of
``sysconfig.get_path("stdlib")``.

.. __: https://sources.debian.org/src/python3.7/3.7.3-2+deb10u3/debian/patches/distutils-install-layout.diff/

Fedora currently carries a `patch to change the default install
location when not running inside rpmbuild`__, which they use to
implement the two-system-wide-directories approach. This is
conceptually the sort of hook envisioned by bpo-43976_, except
implemented as a code patch to ``distutils`` instead of as a changed
``sysconfig`` scheme.

.. __: https://src.fedoraproject.org/rpms/python3.9/blob/f34/f/00251-change-user-install-location.patch

The implementation of ``is_virtual_environment`` above, as well as the
logic to load the ``EXTERNALLY-MANAGED`` file and find the error
message from it, may as well get added to the standard library
(``sys`` and ``sysconfig``, respectively), to centralize their
implementations, but they don't need to be added yet.




Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.



History
=======

- June 2022: This specification was approved through :pep:`668`.
