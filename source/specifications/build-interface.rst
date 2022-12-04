.. _build-frontend-backend-interface:
.. _build-interface:

================================
Build frontend-backend interface
================================

This specification defines a standard interface
between :term:`Build Frontend`\s and :term:`Build Backend`\s
to generate :term:`Distribution Package` artifacts
from :term:`Source Tree`\s of Python :term:`Project`\s.
It was originally introduced in :pep:`PEP 517 <517#build-backend-interface>`
and revised to include editable support in :pep:`660`.

The build backend Python object specified in the
:ref:`build-system-build-backend-key` of the :ref:`build-system-table`
in the :term:`pyproject.toml` config file
MUST have attributes which provide some or all of the following hooks
(as Python callables)
that can be invoked by the build frontend.
The :ref:`build-interface-build-wheel` and :ref:`build-interface-build-sdist`
hooks MUST be provided by any build backend implementing this specification;
all other listed hooks ore optional.
The common ``config_settings`` argument is
:ref:`described after the individual hooks <build-interface-config-settings>`.


.. _build-interface-wheel-hooks:

Wheel hooks
===========

The following backend hooks relate to building a
:ref:`Wheel <binary-distribution-format>` :term:`Built Distribution`.


.. _build-interface-build-wheel:

build_wheel
-----------

.. code-block:: python

    def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
        ...

*Mandatory hook*.
MUST build a :term:`Wheel` ``.whl`` file,
as defined in the :ref:`Wheel specification <binary-distribution-format>`,
and place it in the specified ``wheel_directory``.
MUST return the basename (not the full path) of the ``.whl`` file it creates
as a string.

If the :term:`Build Frontend` has previously called
:ref:`build-interface-prepare-metadata-for-build-wheel`
and depends on the wheel resulting from this call
to have metadata matching this earlier call,
then it SHOULD provide the path to the created :file:`.dist-info` directory
as the ``metadata_directory`` argument.
If this argument is provided,
then ``build_wheel`` MUST produce a wheel with identical metadata.
The directory passed in by the build frontend MUST be identical
to the directory created by
:ref:`build-interface-prepare-metadata-for-build-wheel`,
including any unrecognized files it created.

:term:`Build Backend`\s which do not provide
the :ref:`build-interface-prepare-metadata-for-build-wheel` hook
MAY either silently ignore
the ``metadata_directory`` parameter to ``build_wheel``,
or else raise an exception when it is set to anything other than ``None``.

To ensure that wheels from different sources are built the same way,
frontends MAY call :ref:`build-interface-build-sdist` first,
and then call ``build_wheel`` in the unpacked :term:`Sdist`.
However, if the backend
:ref:`indicates that it is missing some requirements for creating an sdist
<build-interface-build-sdist-requirements>`,
the frontend SHOULD fall back to calling ``build_wheel``
in the :term:`Source Tree`.

The source tree MAY be read-only.
Backends SHOULD therefore be prepared to build without creating or modifying
any files in the source tree, but they MAY opt not to handle this situation,
in which case failures will be visible to the user.
Frontends are not responsible for any special handling
of read-only source directories.

The backend MAY store intermediate artifacts
in cache locations or temporary directories.
The presence or absence of any caches SHOULD not make a material difference
to the final result of the build.


.. _build-interface-get-requires-for-build-wheel:

get_requires_for_build_wheel
----------------------------

.. code-block:: python

    def get_requires_for_build_wheel(config_settings=None):
        ...

*Optional hook*.
This hook MUST return a list of strings containing
:ref:`dependency-specifiers`,
above and beyond those specified in the
:ref:`build-system.requires key <build-system-requires>`
of :ref:`pyproject-toml-config-file`,
to be installed when calling the
:ref:`build-interface-build-wheel`
or :ref:`build-interface-prepare-metadata-for-build-wheel` hooks.

Example:

.. code-block:: python

    def get_requires_for_build_wheel(config_settings):
        return ["wheel >= 0.25", "setuptools"]

If not defined by the :term:`Build Backend`,
the default implementation is equivalent to ``return []``.


.. _build-interface-prepare-metadata-for-build-wheel:

prepare_metadata_for_build_wheel
--------------------------------

.. code-block:: python

    def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
        ...

*Optional hook*.
MUST create a :file:`.dist-info` directory containing :term:`Wheel` metadata
inside the specified ``metadata_directory``;
i.e., a directory like
:file:`{metadata_directory}/{package}-{version}.dist-info/`.
This MUST be a valid :file:`.dist-info` directory
as :ref:`defined in the wheel specification <wheel-dist-info-directory>`,
except that it need not contain ``RECORD``
or :ref:`signatures <wheel-signed-wheel-files>`.
The hook MAY also create other files inside this directory,
and a :term:`Build Frontend` MUST preserve, but otherwise ignore, such files;
the intention here is that in cases where
the metadata depends on build-time decisions,
the :term:`Build Backend` may need to record these decisions
in some convenient format for re-use by the actual wheel-building step.

This MUST return the basename (not the full path)
of the :file:`.dist-info` directory it creates as a string.

If a build frontend needs this information and the method is not defined,
it SHOULD call :ref:`build-interface-build-wheel`
and look at the resulting metadata directly.


.. _build-interface-sdist-hooks:

Sdist hooks
===========

The following backend hooks relate to building a
:ref:`Sdist <source-distribution-format>` :term:`Source Distribution`.


.. _build-interface-build-sdist:

build_sdist
-----------

.. code-block:: python

    def build_sdist(sdist_directory, config_settings=None):
        ...

*Mandatory hook*.
MUST build a :term:`Sdist` :term:`Source Distribution`,
as defined in the :ref:`Sdist specification <source-distribution-format>`,
and place it in the specified ``sdist_directory``.
MUST return the basename (not the full path) of the sdist file it creates
as a string.

.. _build-interface-build-sdist-requirements:

:term:`Build Frontend`\s MAY prefer produce wheels
from intermediate sdists, to ensure consistency.
However, some :term:`Build Backend`\s
MAY have extra requirements for creating sdists,
such as version control tools.
If the backend cannot produce an sdist because a dependency is missing,
or for another well understood reason,
it SHOULD raise an exception of a specific type
which it makes available as ``UnsupportedOperation`` on the backend object.
If the frontend gets this exception while building an sdist
as an intermediate for a wheel,
it SHOULD fall back to building a wheel directly.
The backend does not need to define this exception type
if it would never raise it.


.. _build-interface-get-requires-for-build-sdist:

get_requires_for_build_sdist
----------------------------

.. code-block:: python

    def get_requires_for_build_sdist(config_settings=None):
        ...

*Optional hook*.
This hook MUST return a list of strings containing
:ref:`dependency-specifiers`,
above and beyond those specified in the
:ref:`build-system.requires key <build-system-requires>`
of :ref:`pyproject-toml-config-file`,
to be installed when calling the :ref:`build-interface-build-sdist` hook.

If not defined, the default implementation is equivalent to ``return []``.


.. _build-interface-editable-hooks:

Editable hooks
==============

The following backend hooks relate to building
an :term:`Editable Installation`.
These hooks are used to build a :term:`Wheel` that, when installed,
allows that :term:`Distribution` to be imported
from its :term:`Source Tree` directory.


.. _build-interface-build-editable:

build_editable
--------------

.. code-block:: python

    def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
        ...

*Optional hook*.
MUST build a :term:`Wheel` ``.whl`` file,
as defined in the :ref:`Wheel specification <binary-distribution-format>`,
and place it in the specified ``wheel_directory``.
MUST return the basename (not the full path) of the ``.whl`` file it creates
as a string.

:term:`Build backend`\s MUST populate the generated wheel with files that,
when installed, will result in a working :term:`Editable Installation`.
Backends MAY use various techniques to achieve this goal,
such as :pep:`those suggested in PEP 660 <660#what-to-put-in-the-wheel>`.

Backends MAY do an in-place build of the distribution as a side effect
so that any extension modules or other built artifacts are ready to be used.

Runtime dependencies (:ref:`Requires-Dist <core-metadata-requires-dist>`)
and other :ref:`core metadata <core-metadata>` of the built wheel
MUST be identical to that produced by :ref:`build-interface-build-wheel`
or :ref:`build-interface-prepare-metadata-for-build-wheel`;
with the exception that for ``build_editable``,
Build Backends MAY add dependencies (such as `editables`_)
that are necessary for their editable mechanism to function at runtime.

The filename for the "editable" wheel MUST follow the wheel
:ref:`wheel-file-name-convention`;
it MAY use different :ref:`platform-compatibility-tags`
than for :ref:`build-interface-build-wheel`,
but its tags MUST be compatible with the platform this hook is executed on.

If the :term:`Build Frontend` has previously called
:ref:`build-interface-prepare-metadata-for-build-editable`
and depends on the wheel resulting from this call
to have metadata matching this earlier call,
then it SHOULD provide the path to the created ``.dist-info`` directory
as the ``metadata_directory`` argument.
If this argument is provided,
then ``build_editable`` MUST produce a wheel with identical metadata.
The directory passed in by the build frontend MUST be identical
to the directory created by
:ref:`build-interface-prepare-metadata-for-build-editable`,
including any unrecognized files it created.

An "editable" wheel uses the wheel format not for distribution
but as ephemeral communication between the build system and the front end.
This wheel MUST NOT be exposed to end users, nor cached, nor distributed.


.. _build-interface-get-requires-for-build-editable:

get_requires_for_build_editable
-------------------------------

.. code-block:: python

    def get_requires_for_build_editable(config_settings=None):
        ...

*Optional hook*.
This hook MUST return a list of strings containing
:ref:`dependency-specifiers`,
above and beyond those specified in the
:ref:`build-system.requires key <build-system-requires>`
of :ref:`pyproject-toml-config-file`,
to be installed when calling the
:ref:`build-interface-build-editable`
or :ref:`build-interface-prepare-metadata-for-build-editable` hooks.

If not defined by the :term:`Build Backend`,
the default implementation is equivalent to ``return []``.


.. _build-interface-prepare-metadata-for-build-editable:

prepare_metadata_for_build_editable
-----------------------------------

.. code-block:: python

    def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
        ...

*Optional hook*.
MUST create a :file:`.dist-info` directory containing :term:`Wheel` metadata
inside the specified ``metadata_directory``;
i.e., a directory like
:file:`{metadata_directory}/{package}-{version}.dist-info/`.
This MUST be a valid :file:`.dist-info` directory
as :ref:`defined in the wheel specification <wheel-dist-info-directory>`,
except that it need not contain ``RECORD``
or :ref:`signatures <wheel-signed-wheel-files>`.
The hook MAY also create other files inside this directory,
and a :term:`Build Frontend` MUST preserve, but otherwise ignore, such files;
the intention here is that in cases where
the metadata depends on build-time decisions,
the :term:`Build Backend` may need to record these decisions
in some convenient format for re-use by the actual wheel-building step.

This MUST return the basename (not the full path)
of the :file:`.dist-info` directory it creates as a string.

If a build frontend needs this information and the method is not defined,
it SHOULD call :ref:`build-interface-build-editable`
and look at the resulting metadata directly.


.. _build-interface-hook-invocation:

Hook invocation
===============

The hooks MAY be called with positional or keyword arguments,
so backends implementing them SHOULD be careful to make sure that
their signatures match both the order and the names of the arguments above.

All hooks MUST be run with the working directory set to the
root of the :term:`Source Tree`
(or :ref:`unpacked sdist <build-interface-build-sdist-requirements>`),
and MAY print arbitrary informational text to ``stdout`` and ``stderr``.
They MUST NOT read from ``stdin``,
and the build frontend MAY close ``stdin`` before invoking the hooks.

The build frontend MAY capture ``stdout`` and/or ``stderr`` from the backend.
If the backend detects that an output stream is not a terminal/console
(e.g. ``not sys.stdout.isatty()``),
it SHOULD ensure that any output it writes to that stream is UTF-8 encoded.
The build frontend MUST NOT fail if captured output is not valid UTF-8,
but it MAY not preserve all the information in that case
(e.g. it may decode output using the ``'replace'`` error handler in Python).
If the output stream is a terminal,
the build backend is responsible for presenting its output accurately,
as for any program running in a terminal.

If a hook raises an exception, or causes the process to terminate,
then this indicates an error.


.. _build-interface-config-settings:

Config settings
===============

The ``config_settings`` argument, which is passed to all hooks,
is an arbitrary dictionary provided as an "escape hatch"
for users to pass ad-hoc configuration into individual package builds.
:term:`Build Backend`\s MAY assign any semantics they like to this dictionary.

:term:`Build Frontend`\s SHOULD provide some mechanism for users to specify
arbitrary string-key/string-value pairs to be placed in this dictionary.
For example, they might support some syntax like ``--package-config CC=gcc``.
Build frontends MAY also provide arbitrary other mechanisms
for users to place entries in this dictionary.
For example, ``pip`` might choose to map the following mix
of modern and legacy command line arguments:

.. code-block:: shell

    pip install                                             \
        --package-config CC=gcc                             \
        --global-option="--some-global-option"              \
        --build-option="--build-option1"                    \
        --build-option="--build-option2"

into a ``config_settings`` dictionary as:

.. code-block:: python

    {
        "CC": "gcc",
        "--global-option": ["--some-global-option"],
        "--build-option": ["--build-option1", "--build-option2"],
    }

Of course, it is up to users to ensure that they pass options
which make sense for the particular build backend
and package that they are building.


.. _build-interface-build-environment:

Build environment
=================

One of the responsibilities of a :term:`Build Frontend` is
to set up the Python environment in which the :term:`Build Backend` will run.

A build frontend MAY use any "virtual environment" mechanism it chooses;
such as virtualenv, venv, or no special mechanism at all.
However, whatever mechanism is used MUST meet the following criteria:

- All dependencies required by the build backend
  MUST be available for import from Python.
  In particular:

  - The :ref:`build-interface-get-requires-for-build-wheel`,
    :ref:`build-interface-get-requires-for-build-sdist`
    and :ref:`build-interface-get-requires-for-build-editable` hooks
    MUST be executed in an environment which contains the requires specified in
    :ref:`build-system.requires in pyproject.toml <build-system-requires>`.

  - The :ref:`build-interface-prepare-metadata-for-build-wheel`
    and :ref:`build-interface-build-wheel` hooks
    MUST be executed in an environment which contains the
    ``build-system.requires`` requirements
    and those specified by the
    :ref:`build-interface-get-requires-for-build-wheel` hook.

  - The :ref:`build-interface-build-sdist` hook
    MUST be executed in an environment which contains the
    ``build-system.requires`` requirements
    and those specified by the
    :ref:`build-interface-get-requires-for-build-sdist` hook.

  - The :ref:`build-interface-prepare-metadata-for-build-editable`
    and :ref:`build-interface-build-editable` hooks
    MUST be executed in an environment which contains the
    ``build-system.requires`` requirements
    and those specified by the
    :ref:`build-interface-get-requires-for-build-editable` hook.

- This MUST remain true even for new Python subprocesses
  spawned by the build environment.
  For example, code like:

  .. code-block:: python

      import subprocess, sys
      subprocess.run([sys.executable, ...])

  MUST spawn a Python process which has access to all the project's
  build requirements.
  This is necessary for build backends that want to
  e.g. run legacy :file:`setup.py` scripts in a subprocess.

- All command-line scripts provided by the build requirements
  MUST be present in the build environment's ``PATH``.
  For example, if a project declares a build-requirement on :ref:`flit`,
  then the following MUST work
  as a mechanism for running the Flit command-line tool:

  .. code-block:: python

      import shutil, subprocess
      subprocess.run([shutil.which("flit"), ...])

A build backend MUST be prepared to function in any environment
which meets the above criteria.
In particular, it MUST NOT assume that it has access to any packages
except those that are present in the Python standard library,
or that are explicitly declared as build requirements.

Frontends SHOULD call each hook in a fresh subprocess,
so that backends are free to change process global state
(such as environment variables or the working directory).
A Python library will be provided which frontends can use
to easily call hooks this way.

Frontends MAY use any mechanism
for setting up a build environment that meets the above criteria,
including simply installing all build requirements into the global environment.
However, a build frontend SHOULD, by default,
create an isolated environment for each build,
containing only the Python standard library
and any explicitly requested build dependencies.

Build frontends SHOULD provide some mechanism for users to override
the above defaults.
For example, a build frontend could have a
``--build-with-system-site-packages`` option that causes the
``--system-site-packages`` option to be passed to
virtualenv-or-equivalent when creating build environments,
or a ``--build-requirements-override=my-requirements.txt`` option that
overrides the project's normal build-time requirements.


.. _build-interface-frontend-requirements-for-editable-installs:

Frontend requirements for editable installs
===========================================

:term:`Build Frontend`\s MUST install "editable" wheels
built with the :ref:`build-interface-build-editable` hook
in the same way as normal :term:`Wheel`\s
built with the :ref:`build-interface-build-wheel` hook.
This also means uninstallation of :term:`Editable Installation`\s
MUST NOT require any special treatment.

Frontends MUST create a :file:`direct_url.json` file
in the :file:`.dist-info` directory of the installed distribution,
as specified in the :ref:`direct-url` specification.
The ``url`` value MUST be a ``file://`` URI to the :term:`Project` directory
(i.e. the directory containing the project's :term:`pyproject.toml`),
and the ``dir_info`` value MUST be ``{'editable': true}``.

Frontends MUST execute :ref:`build-interface-get-requires-for-build-editable`
hooks in an environment which contains the
:ref:`build system requirements <build-system-requires>`
specified in :ref:`pyproject-toml-config-file`.

Frontends MUST execute the
:ref:`build-interface-prepare-metadata-for-build-editable`
and :ref:`build-interface-build-editable` hooks
in an environment which contains
the build system requirements from :file:`pyproject.toml`
and those specified by the
:ref:`build-interface-get-requires-for-build-editable` hook.

Frontends MUST NOT expose the wheel obtained from
:ref:`build-interface-build-editable` to end users.
The wheel MUST be discarded after installation
and MUST NOT be cached nor distributed.


.. _`editables`: https://pypi.org/project/editables/
