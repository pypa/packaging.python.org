.. _declaring-project-metadata:

==========================
Declaring project metadata
==========================

:pep:`621` specifies how to write a project's
:ref:`core metadata <core-metadata>` in a ``pyproject.toml`` file for
packaging-related tools to consume. It defines the following
specification as the canonical source for the format used.


Specification
=============

There are two kinds of metadata: *static* and *dynamic*. Static
metadata is specified in the ``pyproject.toml`` file directly and
cannot be specified or changed by a tool (this includes data
*referred* to by the metadata, e.g. the contents of files referenced
by the metadata). Dynamic metadata is listed via the ``dynamic`` key
(defined later in this specification) and represents metadata that a
tool will later provide.

The keys defined in this specification MUST be in a table named
``[project]`` in ``pyproject.toml``. No tools may add keys to this
table which are not defined by this specification. For tools wishing
to store their own settings in ``pyproject.toml``, they may use the
``[tool]`` table as defined in the
:ref:`build dependency declaration specification <declaring-build-dependencies>`.
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

.. code-block:: toml

    [project]
    name = "spam"

``version``
-----------

- TOML_ type: string
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Version <core-metadata-version>`

The version of the project, as defined in the
:ref:`Version specifier specification <version-specifiers>`.

Users SHOULD prefer to specify already-normalized versions.

.. code-block:: toml

    [project]
    version = "2020.0.0"

``description``
---------------

- TOML_ type: string
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Summary <core-metadata-summary>`

The summary description of the project.

.. code-block:: toml

    [project]
    description = "Lovely Spam! Wonderful Spam!"

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

.. code-block:: toml

    [project]
    # A single pyproject.toml file can only have one of the following.
    readme = "README.md"
    readme = "README.rst"
    readme = {file = "README.txt", content-type = "text/markdown"}

``requires-python``
-------------------

- TOML_ type: string
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Requires-Python <core-metadata-requires-python>`

The Python version requirements of the project.

.. code-block:: toml

    [project]
    requires-python = ">=3.8"

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

.. code-block:: toml

    [project]
    # A single pyproject.toml file can only have one of the following.
    license = {file = "LICENSE"}
    license = {text = "MIT License"}

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

.. code-block:: toml

    [project]
    authors = [
      {name = "Pradyun Gedam", email = "pradyun@example.com"},
      {name = "Tzu-Ping Chung", email = "tzu-ping@example.com"},
      {name = "Another person"},
      {email = "different.person@example.com"},
    ]
    maintainers = [
      {name = "Brett Cannon", email = "brett@python.org"}
    ]


``keywords``
------------

- TOML_ type: array of strings
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Keywords <core-metadata-keywords>`

The keywords for the project.

.. code-block:: toml

    [project]
    keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]

``classifiers``
---------------

- TOML_ type: array of strings
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Classifier <core-metadata-classifier>`

Trove classifiers which apply to the project.

.. code-block:: toml

    classifiers = [
      "Development Status :: 4 - Beta",
      "Programming Language :: Python"
    ]

``urls``
--------

- TOML_ type: table with keys and values of strings
- Corresponding :ref:`core metadata <core-metadata>` field:
  :ref:`Project-URL <core-metadata-project-url>`

A table of URLs where the key is the URL label and the value is the
URL itself.

.. code-block:: toml

    [project.urls]
    Homepage = "https://example.com"
    Documentation = "https://readthedocs.org"
    Repository = "https://github.com/me/spam.git"
    Changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"

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

.. code-block:: toml

    [project.scripts]
    spam-cli = "spam:main_cli"

    [project.gui-scripts]
    spam-gui = "spam:main_gui"

    [project.entry-points."spam.magical"]
    tomatoes = "spam:main_tomatoes"


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

.. code-block:: toml

    [project]
    dependencies = [
      "httpx",
      "gidgethub[httpx]>4.0.0",
      "django>2.1; os_name != 'nt'",
      "django>2.0; os_name == 'nt'",
    ]

    [project.optional-dependencies]
    gui = ["PyQt5"]
    cli = [
      "rich",
      "click",
    ]


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

.. code-block:: toml

    dynamic = ["version", "description", "optional-dependencies"]


Example
=======

.. code-block:: toml

    [project]
    name = "spam"
    version = "2020.0.0"
    description = "Lovely Spam! Wonderful Spam!"
    readme = "README.rst"
    requires-python = ">=3.8"
    license = {file = "LICENSE.txt"}
    keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]
    authors = [
      {name = "Pradyun Gedam", email = "pradyun@example.com"},
      {name = "Tzu-Ping Chung", email = "tzu-ping@example.com"},
      {name = "Another person"},
      {email = "different.person@example.com"},
    ]
    maintainers = [
      {name = "Brett Cannon", email = "brett@python.org"}
    ]
    classifiers = [
      "Development Status :: 4 - Beta",
      "Programming Language :: Python"
    ]

    dependencies = [
      "httpx",
      "gidgethub[httpx]>4.0.0",
      "django>2.1; os_name != 'nt'",
      "django>2.0; os_name == 'nt'",
    ]

    # dynamic = ["version", "description"]

    [project.optional-dependencies]
    gui = ["PyQt5"]
    cli = [
      "rich",
      "click",
    ]

    [project.urls]
    Homepage = "https://example.com"
    Documentation = "https://readthedocs.org"
    Repository = "https://github.com/me/spam.git"
    Changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"

    [project.scripts]
    spam-cli = "spam:main_cli"

    [project.gui-scripts]
    spam-gui = "spam:main_gui"

    [project.entry-points."spam.magical"]
    tomatoes = "spam:main_tomatoes"


.. _TOML: https://toml.io
