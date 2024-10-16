.. _declaring-project-metadata:
.. _pyproject-toml-spec:

================================
``pyproject.toml`` specification
================================

.. warning::

   This is a **technical, formal specification**. For a gentle,
   user-friendly guide to ``pyproject.toml``, see
   :ref:`writing-pyproject-toml`.

The ``pyproject.toml`` file acts as a configuration file for packaging-related
tools (as well as other tools).

.. note:: This specification was originally defined in :pep:`518` and :pep:`621`.

The ``pyproject.toml`` file is written in `TOML <https://toml.io>`_. Three
tables are currently specified, namely
:ref:`[build-system] <pyproject-build-system-table>`,
:ref:`[project] <pyproject-project-table>` and
:ref:`[tool] <pyproject-tool-table>`. Other tables are reserved for future
use (tool-specific configuration should use the ``[tool]`` table).

.. _pyproject-build-system-table:

Declaring build system dependencies: the ``[build-system]`` table
=================================================================

The ``[build-system]`` table declares any Python level dependencies that
must be installed in order to run the project's build system
successfully.

.. TODO: merge with PEP 517

The ``[build-system]`` table is used to store build-related data.
Initially, only one key of the table is valid and is mandatory
for the table: ``requires``. This key must have a value of a list
of strings representing dependencies required to execute the
build system. The strings in this list follow the :ref:`version specifier
specification <version-specifiers>`.

An example ``[build-system]`` table for a project built with
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


.. _pyproject-project-table:

Declaring project metadata: the ``[project]`` table
===================================================

The ``[project]`` table specifies the project's :ref:`core metadata <core-metadata>`.

There are two kinds of metadata: *static* and *dynamic*. Static
metadata is specified in the ``pyproject.toml`` file directly and
cannot be specified or changed by a tool (this includes data
*referred* to by the metadata, e.g. the contents of files referenced
by the metadata). Dynamic metadata is listed via the ``dynamic`` key
(defined later in this specification) and represents metadata that a
tool will later provide.

The lack of a ``[project]`` table implicitly means the :term:`build backend <Build Backend>`
will dynamically provide all keys.

The only keys required to be statically defined are:

- ``name``

The keys which are required but may be specified *either* statically
or listed as dynamic are:

- ``version``

All other keys are considered optional and may be specified
statically, listed as dynamic, or left unspecified.

The complete list of keys allowed in the ``[project]`` table are:

- ``authors``
- ``classifiers``
- ``dependencies``
- ``description``
- ``dynamic``
- ``entry-points``
- ``gui-scripts``
- ``keywords``
- ``license``
- ``maintainers``
- ``name``
- ``optional-dependencies``
- ``readme``
- ``requires-python``
- ``scripts``
- ``urls``
- ``version``


``name``
--------

- TOML_ type: string
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Name <core-metadata-name>`

The name of the project.

Tools SHOULD :ref:`normalize <name-normalization>` this name, as soon
as it is read for internal consistency.

``version``
-----------

- TOML_ type: string
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Version <core-metadata-version>`

The version of the project, as defined in the
:ref:`Version specifier specification <version-specifiers>`.

Users SHOULD prefer to specify already-normalized versions.


``description``
---------------

- TOML_ type: string
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Summary <core-metadata-summary>`

The summary description of the project in one line. Tools MAY error
if this includes multiple lines.


``readme``
----------

- TOML_ type: string or table
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Description <core-metadata-description>` and
  :ref:`Description-Content-Type <core-metadata-description-content-type>`

The full description of the project (i.e. the README).

The key accepts either a string or a table. If it is a string then
it is a path relative to ``pyproject.toml`` to a text file containing
the full description. Tools MUST assume the file's encoding is UTF-8.
If the file path ends in a case-insensitive ``.md`` suffix, then tools
MUST assume the content-type is ``text/markdown``. If the file path
ends in a case-insensitive ``.rst``, then tools MUST assume the
content-type is ``text/x-rst``. If a tool recognizes more extensions
than this PEP, they MAY infer the content-type for the user without
specifying this key as ``dynamic``. For all unrecognized suffixes
when a content-type is not provided, tools MUST raise an error.

The ``readme`` key may also take a table. The ``file`` key has a
string value representing a path relative to ``pyproject.toml`` to a
file containing the full description. The ``text`` key has a string
value which is the full description. These keys are
mutually-exclusive, thus tools MUST raise an error if the metadata
specifies both keys.

A table specified in the ``readme`` key also has a ``content-type``
key which takes a string specifying the content-type of the full
description. A tool MUST raise an error if the metadata does not
specify this key in the table. If the metadata does not specify the
``charset`` parameter, then it is assumed to be UTF-8. Tools MAY
support other encodings if they choose to. Tools MAY support
alternative content-types which they can transform to a content-type
as supported by the :ref:`core metadata <core-metadata>`. Otherwise
tools MUST raise an error for unsupported content-types.


``requires-python``
-------------------

- TOML_ type: string
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Requires-Python <core-metadata-requires-python>`

The Python version requirements of the project.


``license``
-----------

- TOML_ type: table
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`License <core-metadata-license>`

The table may have one of two keys. The ``file`` key has a string
value that is a file path relative to ``pyproject.toml`` to the file
which contains the license for the project. Tools MUST assume the
file's encoding is UTF-8. The ``text`` key has a string value which is
the license of the project.  These keys are mutually exclusive, so a
tool MUST raise an error if the metadata specifies both keys.


``authors``/``maintainers``
---------------------------

- TOML_ type: Array of inline tables with string keys and values
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Author <core-metadata-author>`,
  :ref:`Author-email <core-metadata-author-email>`,
  :ref:`Maintainer <core-metadata-maintainer>`, and
  :ref:`Maintainer-email <core-metadata-maintainer-email>`

The people or organizations considered to be the "authors" of the
project. The exact meaning is open to interpretation — it may list the
original or primary authors, current maintainers, or owners of the
package.

The "maintainers" key is similar to "authors" in that its exact
meaning is open to interpretation.

These keys accept an array of tables with 2 keys: ``name`` and
``email``. Both values must be strings. The ``name`` value MUST be a
valid email name (i.e. whatever can be put as a name, before an email,
in :rfc:`822`) and not contain commas. The ``email`` value MUST be a
valid email address. Both keys are optional, but at least one of the
keys must be specified in the table.

Using the data to fill in :ref:`core metadata <core-metadata>` is as
follows:

1. If only ``name`` is provided, the value goes in
   :ref:`Author <core-metadata-author>` or
   :ref:`Maintainer <core-metadata-maintainer>` as appropriate.
2. If only ``email`` is provided, the value goes in
   :ref:`Author-email <core-metadata-author-email>` or
   :ref:`Maintainer-email <core-metadata-maintainer-email>`
   as appropriate.
3. If both ``email`` and ``name`` are provided, the value goes in
   :ref:`Author-email <core-metadata-author-email>` or
   :ref:`Maintainer-email <core-metadata-maintainer-email>`
   as appropriate, with the format ``{name} <{email}>``.
4. Multiple values should be separated by commas.


``keywords``
------------

- TOML_ type: array of strings
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Keywords <core-metadata-keywords>`

The keywords for the project.


``classifiers``
---------------

- TOML_ type: array of strings
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Classifier <core-metadata-classifier>`

Trove classifiers which apply to the project.


``urls``
--------

- TOML_ type: table with keys and values of strings
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Project-URL <core-metadata-project-url>`

A table of URLs where the key is the URL label and the value is the
URL itself. See :ref:`well-known-project-urls` for normalization rules
and well-known rules when processing metadata for presentation.


Entry points
------------

- TOML_ type: table (``[project.scripts]``, ``[project.gui-scripts]``,
  and ``[project.entry-points]``)
- :ref:`Entry points specification <entry-points>`

There are three tables related to entry points. The
``[project.scripts]`` table corresponds to the ``console_scripts``
group in the :ref:`entry points specification <entry-points>`. The key
of the table is the name of the entry point and the value is the
object reference.

The ``[project.gui-scripts]`` table corresponds to the ``gui_scripts``
group in the :ref:`entry points specification <entry-points>`. Its
format is the same as ``[project.scripts]``.

The ``[project.entry-points]`` table is a collection of tables. Each
sub-table's name is an entry point group. The key and value semantics
are the same as ``[project.scripts]``. Users MUST NOT create
nested sub-tables but instead keep the entry point groups to only one
level deep.

Build back-ends MUST raise an error if the metadata defines a
``[project.entry-points.console_scripts]`` or
``[project.entry-points.gui_scripts]`` table, as they would
be ambiguous in the face of ``[project.scripts]`` and
``[project.gui-scripts]``, respectively.


``dependencies``/``optional-dependencies``
------------------------------------------

- TOML_ type: Array of :pep:`508` strings (``dependencies``), and a
  table with values of arrays of :pep:`508` strings
  (``optional-dependencies``)
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Requires-Dist <core-metadata-requires-dist>` and
  :ref:`Provides-Extra <core-metadata-provides-extra>`

The (optional) dependencies of the project.

For ``dependencies``, it is a key whose value is an array of strings.
Each string represents a dependency of the project and MUST be
formatted as a valid :pep:`508` string. Each string maps directly to
a :ref:`Requires-Dist <core-metadata-requires-dist>` entry.

For ``optional-dependencies``, it is a table where each key specifies
an extra and whose value is an array of strings. The strings of the
arrays must be valid :pep:`508` strings. The keys MUST be valid values
for :ref:`Provides-Extra <core-metadata-provides-extra>`. Each value
in the array thus becomes a corresponding
:ref:`Requires-Dist <core-metadata-requires-dist>` entry for the
matching :ref:`Provides-Extra <core-metadata-provides-extra>`
metadata.



.. _declaring-project-metadata-dynamic:

``dynamic``
-----------

- TOML_ type: array of string
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Dynamic <core-metadata-dynamic>`

Specifies which keys listed by this PEP were intentionally
unspecified so another tool can/will provide such metadata
dynamically. This clearly delineates which metadata is purposefully
unspecified and expected to stay unspecified compared to being
provided via tooling later on.

- A build back-end MUST honour statically-specified metadata (which
  means the metadata did not list the key in ``dynamic``).
- A build back-end MUST raise an error if the metadata specifies
  ``name`` in ``dynamic``.
- If the :ref:`core metadata <core-metadata>` specification lists a
  field as "Required", then the metadata MUST specify the key
  statically or list it in ``dynamic`` (build back-ends MUST raise an
  error otherwise, i.e. it should not be possible for a required key
  to not be listed somehow in the ``[project]`` table).
- If the :ref:`core metadata <core-metadata>` specification lists a
  field as "Optional", the metadata MAY list it in ``dynamic`` if the
  expectation is a build back-end will provide the data for the key
  later.
- Build back-ends MUST raise an error if the metadata specifies a
  key statically as well as being listed in ``dynamic``.
- If the metadata does not list a key in ``dynamic``, then a build
  back-end CANNOT fill in the requisite metadata on behalf of the user
  (i.e. ``dynamic`` is the only way to allow a tool to fill in
  metadata and the user must opt into the filling in).
- Build back-ends MUST raise an error if the metadata specifies a
  key in ``dynamic`` but the build back-end was unable to determine
  the data for it (omitting the data, if determined to be the accurate
  value, is acceptable).



.. _pyproject-tool-table:

Arbitrary tool configuration: the ``[tool]`` table
==================================================

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



History
=======

- May 2016: The initial specification of the ``pyproject.toml`` file, with just
  a ``[build-system]`` containing a ``requires`` key and a ``[tool]`` table, was
  approved through :pep:`518`.

- November 2020: The specification of the ``[project]`` table was approved
  through :pep:`621`.



.. _TOML: https://toml.io
