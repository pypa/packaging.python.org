
.. _declaring-build-dependencies:

===================================
Declaring build system dependencies
===================================

``pyproject.toml`` is a build system independent file format defined in :pep:`518`
that projects may provide in order to declare any Python level dependencies that
must be installed in order to run the project's build system successfully.


Abstract
========

This PEP specifies how Python software packages should specify what
build dependencies they have in order to execute their chosen build
system. As part of this specification, a new configuration file is
introduced for software packages to use to specify their build
dependencies (with the expectation that the same configuration file
will be used for future configuration details).


Specification
=============

File Format
-----------

The build system dependencies will be stored in a file named
``pyproject.toml`` that is written in the TOML format [#toml]_.

Below we list the tables that tools are expected to recognize/respect.
Tables not specified in this PEP are reserved for future use by other
PEPs.

build-system table
------------------

The ``[build-system]`` table is used to store build-related data.
Initially only one key of the table will be valid and is mandatory
for the table: ``requires``. This key must have a value of a list
of strings representing :pep:`508` dependencies required to execute the
build system (currently that means what dependencies are required to
execute a ``setup.py`` file).

For the vast majority of Python projects that rely upon setuptools,
the ``pyproject.toml`` file will be::

  [build-system]
  # Minimum requirements for the build system to execute.
  requires = ["setuptools", "wheel"]  # PEP 508 specifications.

Because the use of setuptools and wheel are so expansive in the
community at the moment, build tools are expected to use the example
configuration file above as their default semantics when a
``pyproject.toml`` file is not present.

Tools should not require the existence of the ``[build-system]`` table.
A ``pyproject.toml`` file may be used to store configuration details
other than build-related data and thus lack a ``[build-system]`` table
legitimately. If the file exists but is lacking the ``[build-system]``
table then the default values as specified above should be used.
If the table is specified but is missing required fields then the tool
should consider it an error.


tool table
----------

The ``[tool]`` table is where any tool related to your Python
project, not just build tools, can have users specify configuration
data as long as they use a sub-table within ``[tool]``, e.g. the
`flit <https://pypi.python.org/pypi/flit>`_ tool would store its
configuration in ``[tool.flit]``.

We need some mechanism to allocate names within the ``tool.*``
namespace, to make sure that different projects don't attempt to use
the same sub-table and collide. Our rule is that a project can use
the subtable ``tool.$NAME`` if, and only if, they own the entry for
``$NAME`` in the Cheeseshop/PyPI.

JSON Schema
-----------

To provide a type-specific representation of the resulting data from
the TOML file for illustrative purposes only, the following JSON
Schema [#jsonschema]_ would match the data format::

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



References
==========

.. [#toml] TOML
   (https://github.com/toml-lang/toml)

.. [#yaml] YAML
   (http://yaml.org/)

.. [#jsonschema] JSON Schema
   (http://json-schema.org/)
