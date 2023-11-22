.. _build-system-interface:

======================
Build system interface
======================

This specifications describes a standardized interface for installation
tools like ``pip`` to interact with package source trees and source
distributions.

The project's chosen build system is read from the :ref:`[build-system]
table <pyproject-build-system-table>` of the ``pyproject.toml`` file.
The ``requires`` key defines the build requirements and the
``build-backend`` key specifies a build backend object to use.


Terminology
===========

A *build frontend* is a tool that users might run that takes arbitrary
source trees or source distributions and builds wheels from them. The
actual building is done by each source tree's *build backend*. In a
command like ``pip wheel some-directory/``, pip is acting as a build
frontend.

An *integration frontend* is a tool that users might run that takes a
set of package requirements (e.g. a requirements.txt file) and
attempts to update a working environment to satisfy those
requirements. This may require locating, building, and installing a
combination of wheels and sdists. In a command like ``pip install
lxml==2.4.0``, pip is acting as an integration frontend.


Build requirements
==================

This specification places a number of requirements on the ``requires``
key from the ``[build-system]`` section of ``pyproject.toml``. These are
intended to ensure that projects do not create impossible to satisfy
conditions with their build requirements.

- Project build requirements will define a directed graph of requirements
  (project A needs B to build, B needs C and D, etc.) This graph MUST NOT
  contain cycles.  If (due to lack of co-ordination between projects, for
  example) a cycle is present, front ends MAY refuse to build the project.
- Where build requirements are available as wheels, front ends SHOULD use these
  where practical, to avoid deeply nested builds.  However front ends MAY have
  modes where they do not consider wheels when locating build requirements, and
  so projects MUST NOT assume that publishing wheels is sufficient to break a
  requirement cycle.
- Front ends SHOULD check explicitly for requirement cycles, and terminate
  the build with an informative message if one is found.

Note in particular that the requirement for no requirement cycles means that
backends wishing to self-host (i.e., building a wheel for a backend uses that
backend for the build) need to make special provision to avoid causing cycles.
Typically this will involve specifying themselves as an in-tree backend, and
avoiding external build dependencies (usually by vendoring them).


Build backend interface
========================

The build backend object is looked up according to the ``build-backend``
field of the ``[build-system]`` table. It is expected to have attributes
which provide some or all of the following hooks. The common
``config_settings`` argument is described after the individual hooks.


Mandatory hooks
---------------

build_wheel
'''''''''''

::

    def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
        ...

Must build a .whl file, and place it in the specified ``wheel_directory``. It
must return the basename (not the full path) of the ``.whl`` file it creates,
as a unicode string.

If the build frontend has previously called ``prepare_metadata_for_build_wheel``
and depends on the wheel resulting from this call to have metadata
matching this earlier call, then it should provide the path to the created
``.dist-info`` directory as the ``metadata_directory`` argument. If this
argument is provided, then ``build_wheel`` MUST produce a wheel with identical
metadata. The directory passed in by the build frontend MUST be
identical to the directory created by ``prepare_metadata_for_build_wheel``,
including any unrecognized files it created.

Backends which do not provide the ``prepare_metadata_for_build_wheel`` hook may
either silently ignore the ``metadata_directory`` parameter to ``build_wheel``,
or else raise an exception when it is set to anything other than ``None``.

To ensure that wheels from different sources are built the same way, frontends
may call ``build_sdist`` first, and then call ``build_wheel`` in the unpacked
sdist. But if the backend indicates that it is missing some requirements for
creating an sdist (see below), the frontend will fall back to calling
``build_wheel`` in the source directory.

The source directory may be read-only. Backends should therefore be
prepared to build without creating or modifying any files in the source
directory, but they may opt not to handle this case, in which case
failures will be visible to the user. Frontends are not responsible for
any special handling of read-only source directories.

The backend may store intermediate artifacts in cache locations or
temporary directories. The presence or absence of any caches should not
make a material difference to the final result of the build.

build_sdist
'''''''''''

::

    def build_sdist(sdist_directory, config_settings=None):
        ...

Must build a .tar.gz source distribution and place it in the specified
``sdist_directory``. It must return the basename (not the full path) of the
``.tar.gz`` file it creates, as a unicode string.

Some backends may have extra requirements for creating sdists, such as version
control tools. However, some frontends may prefer to make intermediate sdists
when producing wheels, to ensure consistency.
If the backend cannot produce an sdist because a dependency is missing, or
for another well understood reason, it should raise an exception of a specific
type which it makes available as ``UnsupportedOperation`` on the backend object.
If the frontend gets this exception while building an sdist as an intermediate
for a wheel, it should fall back to building a wheel directly.
The backend does not need to define this exception type if it would never raise
it.



Optional hooks
--------------

get_requires_for_build_wheel
''''''''''''''''''''''''''''

::

  def get_requires_for_build_wheel(config_settings=None):
      ...

This hook MUST return an additional list of strings containing
:ref:`dependency specifiers <dependency-specifiers>`, above and
beyond those specified in the ``pyproject.toml`` file, to be
installed when calling the ``build_wheel`` or
``prepare_metadata_for_build_wheel`` hooks.

Example::

  def get_requires_for_build_wheel(config_settings):
      return ["wheel >= 0.25", "setuptools"]

If not defined, the default implementation is equivalent to ``return []``.

prepare_metadata_for_build_wheel
''''''''''''''''''''''''''''''''

::

  def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
      ...

Must create a ``.dist-info`` directory containing wheel metadata
inside the specified ``metadata_directory`` (i.e., creates a directory
like ``{metadata_directory}/{package}-{version}.dist-info/``). This
directory MUST be a valid ``.dist-info`` directory as defined in the
wheel specification, except that it need not contain ``RECORD`` or
signatures. The hook MAY also create other files inside this
directory, and a build frontend MUST preserve, but otherwise ignore, such files;
the intention
here is that in cases where the metadata depends on build-time
decisions, the build backend may need to record these decisions in
some convenient format for reuse by the actual wheel-building step.

This must return the basename (not the full path) of the ``.dist-info``
directory it creates, as a unicode string.

If a build frontend needs this information and the method is
not defined, it should call ``build_wheel`` and look at the resulting
metadata directly.

get_requires_for_build_sdist
''''''''''''''''''''''''''''

::

  def get_requires_for_build_sdist(config_settings=None):
      ...

This hook MUST return an additional list of strings containing :pep:`508`
dependency specifications, above and beyond those specified in the
``pyproject.toml`` file. These dependencies will be installed when calling the
``build_sdist`` hook.

If not defined, the default implementation is equivalent to ``return []``.


.. todo:: Import :pep:`660` (editable installs) here.


Config settings
---------------

::

  config_settings

This argument, which is passed to all hooks, is an arbitrary
dictionary provided as an "escape hatch" for users to pass ad-hoc
configuration into individual package builds. Build backends MAY
assign any semantics they like to this dictionary. Build frontends
SHOULD provide some mechanism for users to specify arbitrary
string-key/string-value pairs to be placed in this dictionary.
For example, they might support some syntax like ``--package-config CC=gcc``.
In case a user provides duplicate string-keys, build frontends SHOULD
combine the corresponding string-values into a list of strings.
Build frontends MAY also provide arbitrary other mechanisms
for users to place entries in this dictionary. For example, ``pip``
might choose to map a mix of modern and legacy command line arguments
like::

  pip install                                           \
    --package-config CC=gcc                             \
    --global-option="--some-global-option"              \
    --build-option="--build-option1"                    \
    --build-option="--build-option2"

into a ``config_settings`` dictionary like::

  {
   "CC": "gcc",
   "--global-option": ["--some-global-option"],
   "--build-option": ["--build-option1", "--build-option2"],
  }

Of course, it's up to users to make sure that they pass options which
make sense for the particular build backend and package that they are
building.

The hooks may be called with positional or keyword arguments, so backends
implementing them should be careful to make sure that their signatures match
both the order and the names of the arguments above.

All hooks are run with working directory set to the root of the source
tree, and MAY print arbitrary informational text on stdout and
stderr. They MUST NOT read from stdin, and the build frontend MAY
close stdin before invoking the hooks.

The build frontend may capture stdout and/or stderr from the backend. If the
backend detects that an output stream is not a terminal/console (e.g.
``not sys.stdout.isatty()``), it SHOULD ensure that any output it writes to that
stream is UTF-8 encoded. The build frontend MUST NOT fail if captured output is
not valid UTF-8, but it MAY not preserve all the information in that case (e.g.
it may decode using the *replace* error handler in Python). If the output stream
is a terminal, the build backend is responsible for presenting its output
accurately, as for any program running in a terminal.

If a hook raises an exception, or causes the process to terminate,
then this indicates an error.


Build environment
-----------------

One of the responsibilities of a build frontend is to set up the
Python environment in which the build backend will run.

We do not require that any particular "virtual environment" mechanism
be used; a build frontend might use virtualenv, or venv, or no special
mechanism at all. But whatever mechanism is used MUST meet the
following criteria:

- All requirements specified by the project's build-requirements must
  be available for import from Python. In particular:

  - The ``get_requires_for_build_wheel`` and ``get_requires_for_build_sdist`` hooks are
    executed in an environment which contains the bootstrap requirements
    specified in the ``pyproject.toml`` file.

  - The ``prepare_metadata_for_build_wheel`` and ``build_wheel`` hooks are
    executed in an environment which contains the
    bootstrap requirements from ``pyproject.toml`` and those specified by the
    ``get_requires_for_build_wheel`` hook.

  - The ``build_sdist`` hook is executed in an environment which contains the
    bootstrap requirements from ``pyproject.toml`` and those specified by the
    ``get_requires_for_build_sdist`` hook.

- This must remain true even for new Python subprocesses spawned by
  the build environment, e.g. code like::

    import sys, subprocess
    subprocess.check_call([sys.executable, ...])

  must spawn a Python process which has access to all the project's
  build-requirements. This is necessary e.g. for build backends that
  want to run legacy ``setup.py`` scripts in a subprocess.

- All command-line scripts provided by the build-required packages
  must be present in the build environment's PATH. For example, if a
  project declares a build-requirement on `flit
  <https://flit.readthedocs.org/en/latest/>`__, then the following must
  work as a mechanism for running the flit command-line tool::

    import subprocess
    import shutil
    subprocess.check_call([shutil.which("flit"), ...])

A build backend MUST be prepared to function in any environment which
meets the above criteria. In particular, it MUST NOT assume that it
has access to any packages except those that are present in the
stdlib, or that are explicitly declared as build-requirements.

Frontends should call each hook in a fresh subprocess, so that backends are
free to change process global state (such as environment variables or the
working directory). A Python library will be provided which frontends can use
to easily call hooks this way.

Recommendations for build frontends (non-normative)
'''''''''''''''''''''''''''''''''''''''''''''''''''

A build frontend MAY use any mechanism for setting up a build
environment that meets the above criteria. For example, simply
installing all build-requirements into the global environment would be
sufficient to build any compliant package -- but this would be
sub-optimal for a number of reasons. This section contains
non-normative advice to frontend implementers.

A build frontend SHOULD, by default, create an isolated environment
for each build, containing only the standard library and any
explicitly requested build-dependencies. This has two benefits:

- It allows for a single installation run to build multiple packages
  that have contradictory build-requirements. E.g. if package1
  build-requires pbr==1.8.1, and package2 build-requires pbr==1.7.2,
  then these cannot both be installed simultaneously into the global
  environment -- which is a problem when the user requests ``pip
  install package1 package2``. Or if the user already has pbr==1.8.1
  installed in their global environment, and a package build-requires
  pbr==1.7.2, then downgrading the user's version would be rather
  rude.

- It acts as a kind of public health measure to maximize the number of
  packages that actually do declare accurate build-dependencies. We
  can write all the strongly worded admonitions to package authors we
  want, but if build frontends don't enforce isolation by default,
  then we'll inevitably end up with lots of packages on PyPI that
  build fine on the original author's machine and nowhere else, which
  is a headache that no-one needs.

However, there will also be situations where build-requirements are
problematic in various ways. For example, a package author might
accidentally leave off some crucial requirement despite our best
efforts; or, a package might declare a build-requirement on ``foo >=
1.0`` which worked great when 1.0 was the latest version, but now 1.1
is out and it has a showstopper bug; or, the user might decide to
build a package against numpy==1.7 -- overriding the package's
preferred numpy==1.8 -- to guarantee that the resulting build will be
compatible at the C ABI level with an older version of numpy (even if
this means the resulting build is unsupported upstream). Therefore,
build frontends SHOULD provide some mechanism for users to override
the above defaults. For example, a build frontend could have a
``--build-with-system-site-packages`` option that causes the
``--system-site-packages`` option to be passed to
virtualenv-or-equivalent when creating build environments, or a
``--build-requirements-override=my-requirements.txt`` option that
overrides the project's normal build-requirements.

The general principle here is that we want to enforce hygiene on
package *authors*, while still allowing *end-users* to open up the
hood and apply duct tape when necessary.


.. _in-tree-build-backends:

In-tree build backends
----------------------

In certain circumstances, projects may wish to include the source code for the
build backend directly in the source tree, rather than referencing the backend
via the ``requires`` key. Two specific situations where this would be expected
are:

- Backends themselves, which want to use their own features for building
  themselves ("self-hosting backends")
- Project-specific backends, typically consisting of a custom wrapper around a
  standard backend, where the wrapper is too project-specific to be worth
  distributing independently ("in-tree backends")

Projects can specify that their backend code is hosted in-tree by including the
``backend-path`` key in ``pyproject.toml``. This key contains a list of
directories, which the frontend will add to the start of ``sys.path`` when
loading the backend, and running the backend hooks.

There are two restrictions on the content of the ``backend-path`` key:

- Directories in ``backend-path`` are interpreted as relative to the project
  root, and MUST refer to a location within the source tree (after relative
  paths and symbolic links have been resolved).
- The backend code MUST be loaded from one of the directories specified in
  ``backend-path`` (i.e., it is not permitted to specify ``backend-path`` and
  *not* have in-tree backend code).

The first restriction is to ensure that source trees remain self-contained,
and cannot refer to locations outside of the source tree. Frontends SHOULD
check this condition (typically by resolving the location to an absolute path
and resolving symbolic links, and then checking it against the project root),
and fail with an error message if it is violated.

The ``backend-path`` feature is intended to support the implementation of
in-tree backends, and not to allow configuration of existing backends. The
second restriction above is specifically to ensure that this is how the feature
is used. Front ends MAY enforce this check, but are not required to. Doing so
would typically involve checking the backend's ``__file__`` attribute against
the locations in ``backend-path``.


History
=======

This specification was originally proposed and approved as :pep:`517`.

The following changes were made to this specification after the initial reference
implementation was released in pip 19.0.

* Cycles in build requirements were explicitly prohibited.
* Support for in-tree backends and self-hosting of backends was added by
  the introduction of the ``backend-path`` key in the ``[build-system]``
  table.
* Clarified that the ``setuptools.build_meta:__legacy__`` backend is
  an acceptable alternative to directly invoking ``setup.py`` for source trees
  that don't specify ``build-backend`` explicitly. (This clarification
  is now in the :ref:`pyproject.toml specification <pyproject-toml-spec>`.)
