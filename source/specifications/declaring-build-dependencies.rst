.. _declaring-build-system:

==================================
Declaring a project's build system
==================================

As originally specified in
:pep:`PEP 517 <517#source-trees>` and :pep:`PEP 518 <518#build-system-table>`,
projects may define a :ref:`build-system-table`
in their :ref:`pyproject.toml config file <pyproject-toml-config-file>`
to declare their :term:`Build Backend`
(as specified in the :ref:`build-interface` specification)
and its dependencies.


.. _build-system:
.. _build-system-table:

``[build-system]`` table
========================

The ``[build-system]`` table is used to store build-related configuration.

.. _build-system-table-default:

Tools SHOULD NOT require the existence of the ``[build-system]`` table.
If it or a :term:`pyproject.toml` file is not present,
tools SHOULD assume the following default value:

.. code-block:: toml

    [build-system]
    # Minimum requirements for the build system to execute.
    requires = ["setuptools"]
    # The build backend Python object to invoke.
    build-system = "setuptools.build_meta:__legacy__"

If the table is present but is missing a value
for the mandatory :ref:`build-system-requires-key`,
tools SHOULD consider it an error.

The valid top-level keys are listed below.
Keys not defined in this specification MUST NOT be added to this table.


.. _build-system-requires:
.. _build-system-requires-key:
.. _declaring-build-dependencies:

``requires`` key
----------------

The ``requires`` key is used to declare the Python-level dependencies
that must be installed in order to run
the project's :term:`Build Backend` successfully.

The key's value MUST be a list of valid string :ref:`dependency-specifiers`
required to execute the
:ref:`specified build backend <build-system-build-backend>`.

For a build tool such as :ref:`flit` with a backend package ``flit_core``,
an example ``requires`` value specifying a particular version range might be:

.. code-block:: toml

    [build-system]
    requires = ["flit_core >=3.2,<4"]

Projects still relying on a legacy implicit :term:`setup.py` invocation
can specify the following value for the ``requires`` key:

.. code-block:: toml

    [build-system]
    requires = ["setuptools"]

This is the :ref:`default value <build-system-table-default>` for this key
if the :ref:`build-system-table` is not present in a :term:`pyproject.toml`.
If the table is defined but is missing a value for the ``requires`` key,
tools SHOULD consider it an error.

The following requirements also apply:

- Project build requirements will define a directed graph of requirements
  (project ``A`` needs ``B`` to build, ``B`` needs ``C`` and ``D``, etc.).
  This graph MUST NOT contain cycles.
  If (due to lack of co-ordination between projects, for example)
  a cycle is present, :term:`Build Frontend`\s MAY refuse to build the project.
- Where build requirements are available as :term:`Wheel`\s,
  frontends SHOULD use these where practical, to avoid deeply nested builds.
  However, frontends MAY have modes
  where they do not consider wheels when locating build requirements,
  and so projects MUST NOT assume that publishing wheels
  is sufficient to break a requirement cycle.
- Frontends SHOULD check explicitly for requirement cycles,
  and SHOULD terminate the build with an informative message if one is found.

.. note::

    The requirement for no requirement cycles means that
    backends wishing to self-host
    (i.e., building a wheel for a backend uses that backend for the build)
    need to make special provision to avoid causing cycles.
    Typically, this will involve specifying themselves as an
    :ref:`in-tree backend <build-system-in-tree-backend>`,
    and avoiding external build dependencies (usually by vendoring them).


.. _build-system-build-backend:
.. _build-system-build-backend-key:

``build-backend`` key
---------------------

The ``build-backend`` key specifies the project's :term:`Build Backend`.
Its value MUST be a string naming the Python object
that exposes attributes with callables for each of
the :ref:`build-interface` hooks supported by the backend.
This is formatted following the same :file:`{module}:{object}` syntax as
an :ref:`entry point <entry-points>`.

For example, with the value:

.. code-block:: toml

    [build-system]
    build-backend = "flit_core.buildapi:main"

then the ``module`` would be ``flit_core.buildapi``
and the ``object`` would be ``main``,
so the ``backend`` would be looked up by executing the equivalent of:

.. code-block:: python

    import flit_core.buildapi
    backend = flit_core.buildapi.main

The ``object`` part MAY be omitted,
for cases where the importable ``module`` is the top-level ``backend`` object.
For example, with the value:

.. code-block:: toml

    [build-system]
    build-backend = "flit_core.buildapi"

then the ``module`` would still be ``flit_core.buildapi``
and the ``object`` part not specified,
so the ``backend`` would be looked up by executing the equivalent of:

.. code-block:: python

    import flit_core.buildapi
    backend = flit_core.buildapi

Formally, the string SHOULD satisfy the grammar:

.. code-block:: text

    identifier = (letter | '_') (letter | '_' | digit)*
    module_path = identifier ('.' identifier)*
    object_path = identifier ('.' identifier)*
    entry_point = module_path (':' object_path)?

which would import ``module_path``
and then look up ``module_path.object_path``
(or just ``module_path``, if no ``object_path`` is specified).

When importing the module,
the directory containing the :term:`Source Tree`
MUST NOT be added to :data:`python:sys.path` and searched for the module,
including by Python's automatic behavior of adding
the working directory or script directory to the path,
unless present anyway due to :mod:`python:site` or :envvar:`python:PYTHONPATH`.

If a ``build-backend`` key is not present within
a :ref:`build-system-table` of a :term:`pyproject.toml` file,
:term:`Build Frontend`\s SHOULD assume a default value for it of:

.. code-block:: toml

    [build-system]
    build-backend = "setuptools.build_meta:__legacy__"

or else MAY revert to the legacy behaviour of directly executing
a :term:`setup.py` script at the root of the project's source tree.
Projects MAY still include a :file:`setup.py`
for compatibility with legacy tools that do not conform to this specification.


.. _build-system-backend-path:
.. _build-system-backend-path-key:
.. _build-system-in-tree-backend:

``backend-path`` key
--------------------

The optional ``backend-path`` key specifies where
a local :term:`Build Backend` can be loaded from,
for projects that may wish to include the source code for their build backend
directly in their :term:`Source Tree`,
rather than referencing the backend via the :ref:`build-system-requires-key`.
Its value is a list of string paths to the directories which should be
inserted at the beginning of :data:`python:sys.path` to import the ``module``
specified in the :ref:`build-system-build-backend-key`.

For example, suppose a project has a backend ``object`` named ``backend_object``
located inside a Python module located at
:file:`project_subdirectory/backend_directory/backend_package/backend_module.py`
relative to the project source tree root directory
(i.e. the directory in which the :file:`pyproject.toml` is located),
and with ``backend_package`` being a Python :term:`Import Package`
(i.e. with a :file:`__init__.py` file inside it).
Therefore, the ``build-backend`` and ``backend-path`` configuration would be:

.. code-block:: toml

    [build-system]
    build-backend = "backend_package.backend_module:backend_object"
    backend-path = ["project_subdirectory/backend_directory"]

Accordingly, ``project_subdirectory/backend_directory`` would be
inserted at the beginning of ``sys.path``
and ``backend_package.backend_module`` would be imported from there,
with its ``backend_object`` attribute looked up as the ``backend`` object.
This is roughly equivalent to:

.. code-block:: python

    import sys
    sys.path.insert(0, "project_subdirectory/backend_directory")
    import backend_package.backend_module
    backend = backend_package.backend_module.backend_object

There are restrictions on the content of the ``backend-path`` key:

- Directories in ``backend-path`` are interpreted as
  relative to the project root (i.e. the :file:`pyproject.toml` directory),
  and MUST refer to a location within the :term:`Source Tree`
  (after relative paths and symbolic links have been resolved).
  :term:`Build Frontend`\s SHOULD check this condition
  (typically by resolving the location to an absolute path
  and resolving symbolic links,
  and then checking that it is within the project root)
  and fail with an error message if it is violated.
- The backend code MUST be loaded from one of
  the directories specified in ``backend-path``
  (i.e., ``backend-path`` MUST NOT be specified without in-tree backend code).
  Frontends MAY enforce this check, but are not required to.
  Doing so would typically involve
  checking the backend's :attr:`python:__file__` attribute
  against the locations in ``backend-path``.
