.. _pyproject-toml-config-file:

=====================================
The pyproject.toml configuration file
=====================================

:term:`pyproject.toml` is a build-system-independent, tool-agnostic
file in `TOML format <toml_>`__.
for storing Python build, packaging and tool configuration,
originally defined in :pep:`518`
and extended to include the :ref:`pyproject-toml-project-table` in :pep:`621`.

It is typically located at the root of the :term:`Source Tree`
for Python :term:`Project`\s,
and included in the top-level directory of all :term:`Source Distribution`\s.

The valid top-level tables are listed below.
Tables and their respective keys not specified here are reserved for future use,
to be proposed in future PEPs,
and MUST NOT be defined or used for any purpose.
Rather, the :ref:`pyproject-toml-tool-table` SHOULD be used instead.


.. _pyproject-toml-build-system:
.. _pyproject-toml-build-system-table:

``[build-system]`` table
========================

The ``[build-system]`` table is used to store build-related configuration.
If the table is present but has no non-empty values,
tools SHOULD consider it an error.

The contents and interpretation of the ``[build-system]`` table
are defined in the :ref:`declaring-build-system` specification.
Keys not defined in that specification MUST NOT be added to this table.


.. _pyproject-toml-project-table:
.. _pyproject-toml-metadata:

``[project]`` table
===================

The ``[project]`` table is the standardized place to declare a project's
:ref:`core metadata <core-metadata>` for tools to consume.
The lack of a ``[project]`` table implicitly means that
the :term:`Build Backend` will dynamically provide all core metadata fields.
If the table is present but has no non-empty values,
tools MUST consider it an error.

The contents and interpretation of the ``[project]`` table
are defined in the :ref:`declaring-project-metadata` specification.
Keys not defined in that specification MUST NOT be added to this table.


.. _pyproject-toml-tool:
.. _pyproject-toml-tool-table:

``[tool]`` table
================

The ``[tool]`` table is where tools related to Python projects,
not just build systems, may allow users to specify configuration data.
Tools MUST use a named sub-table within ``[tool]`` to do this,
which to avoid collisions, MUST have as its key a name the project owns on
the :term:`Python Package Index (PyPI)`.
For example, the :ref:`flit` tool would store its configuration under
``[tool.flit]``.

The contents and interpretation of each tool sub-table
are defined by each respective tool and its documentation.


.. _toml: https://toml.io/
