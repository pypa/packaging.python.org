
.. _declaring-build-dependencies:

===================================
Declaring build system dependencies
===================================

The ``pyproject.toml`` file is written in `TOML <https://toml.io>`_.
Among other metadata (such as :ref:`project metadata <declaring-project-metadata>`),
it declares any Python level dependencies that must be installed in order to
run the project's build system successfully.

.. TODO: move this sentence elsewhere

Tables not defined by PyPA specifications are reserved for future use.


build-system table
------------------

.. TODO: merge with PEP 517

The ``[build-system]`` table is used to store build-related data.
Initially,  only one key of the table is valid and is mandatory
for the table: ``requires``. This key must have a value of a list
of strings representing dependencies required to execute the
build system. The strings in this list follow the :ref:`version specifier
specification <version-specifiers>`.

An example ``build-system`` table for a project built with
``setuptools`` is:

.. code-block:: toml

   [build-system]
   # Minimum requirements for the build system to execute.
   requires = ["setuptools"]

Build tools are expected to use the example configuration file above as
their default semantics when a ``pyproject.toml`` file is not present.

Tools should not require the existence of the ``[build-system]`` table.
A ``pyproject.toml`` file may be used to store configuration details
other than build-related data and thus lack a ``[build-system]`` table
legitimately. If the file exists but is lacking the ``[build-system]``
table then the default values as specified above should be used.
If the table is specified but is missing required fields then the tool
should consider it an error.


.. TODO: move elsewhere

tool table
----------

The ``[tool]`` table is where any tool related to your Python
project, not just build tools, can have users specify configuration
data as long as they use a sub-table within ``[tool]``, e.g. the
`flit <https://pypi.python.org/pypi/flit>`_ tool would store its
configuration in ``[tool.flit]``.

A mechanism is needed to allocate names within the ``tool.*``
namespace, to make sure that different projects do not attempt to use
the same sub-table and collide. Our rule is that a project can use
the subtable ``tool.$NAME`` if, and only if, they own the entry for
``$NAME`` in the Cheeseshop/PyPI.

JSON Schema
-----------

To provide a type-specific representation of the resulting data from
the TOML file for illustrative purposes only, the following
`JSON Schema <https://json-schema.org>`_ would match the data format:

.. code-block:: json

   {
       "$schema": "http://json-schema.org/schema#",

       "type": "object",
       "additionalProperties": false,

       "properties": {
           "build-system": {
               "type": "object",
               "additionalProperties": false,

               "properties": {
                   "requires": {
                       "type": "array",
                       "items": {
                           "type": "string"
                       }
                   }
               },
               "required": ["requires"]
           },

           "tool": {
               "type": "object"
           }
       }
   }
