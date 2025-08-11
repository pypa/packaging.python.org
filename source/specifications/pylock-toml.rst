.. _pylock-toml-spec:
.. _lock-file-spec:

=============================
``pylock.toml`` Specification
=============================

The ``pylock.toml`` file format is for specifying dependencies to enable
reproducible installation in a Python environment.

.. note:: This specification was originally defined in :pep:`751`.


---------
File Name
---------

A lock file MUST be named :file:`pylock.toml` or match the regular expression
``r"^pylock\.([^.]+)\.toml$"`` if a name for the lock file is desired or if
multiple lock files exist (i.e. the regular expression
``r"^pylock\.([^.]+\.)?toml$"`` for any file name). The prefix and suffix of a
named file MUST be lowercase when possible, for easy detection and removal,
e.g.:

.. code-block:: Python

  if len(filename) > 11 and filename.startswith("pylock.") and filename.endswith(".toml"):
      name = filename.removeprefix("pylock.").removesuffix(".toml")

The expectation is that services that automatically install from lock files will
search for:

1. The lock file with the service's name and doing the default install
2. A multi-use :file:`pylock.toml` with a dependency group with the name of the service
3. The default install of :file:`pylock.toml`

E.g. a cloud host service named "spam" would first look for
:file:`pylock.spam.toml` to install from, and if that file didn't exist then install
from :file:`pylock.toml` and look for a dependency group named "spam" to use if
present.

The lock file(s) SHOULD be located in the directory as appropriate for the scope
of the lock file. Locking against a single :file:`pyproject.toml`, for instance,
would place the :file:`pylock.toml` in the same directory. If the lock file covered
multiple projects in a monorepo, then the expectation is the :file:`pylock.toml`
file would be in the directory that held all the projects being locked.


-----------
File Format
-----------

The format of the file is TOML_.

Tools SHOULD write their lock files in a consistent way to minimize noise in
diff output. Keys in tables -- including the top-level table -- SHOULD be
recorded in a consistent order (if inspiration is desired, this specification has tried to
write down keys in a logical order). As well, tools SHOULD sort arrays in
consistent order. Usage of inline tables SHOULD also be kept consistent.


.. _pylock-lock-version:

``lock-version``
================

- **Type**: string; value of ``"1.0"``
- **Required?**: yes
- **Inspiration**: :ref:`core-metadata-metadata-version`
- Record the file format version that the file adheres to.
- This PEP specifies the initial version -- and only valid value until future
  updates to the standard change it -- as ``"1.0"``.
- If a tool supports the major version but not the minor version, a tool
  SHOULD warn when an unknown key is seen.
- If a tool doesn't support a major version, it MUST raise an error.


.. _pylock-environments:

``environments``
================

- **Type**: Array of strings
- **Required?**: no
- **Inspiration**: uv_
- A list of :ref:`dependency-specifiers-environment-markers` for
  which the lock file is considered compatible with.
- Tools SHOULD write exclusive/non-overlapping environment markers to ease in
  understanding.


.. _pylock-requires-python:

``requires-python``
===================

- **Type**: string
- **Required?**: no
- **Inspiration**: PDM_, Poetry_, uv_
- Specifies the :ref:`core-metadata-requires-python` for the minimum
  Python version compatible for any environment supported by the lock file
  (i.e. the minimum viable Python version for the lock file).


.. _pylock-extras:

``extras``
==========

- **Type**: Array of strings
- **Required?**: no; defaults to ``[]``
- **Inspiration**: :ref:`core-metadata-provides-extra`
- The list of :ref:`extras <core-metadata-provides-extra>` supported
  by this lock file.
- Lockers MAY choose to not support writing lock files that support extras and
  dependency groups (i.e. tools may only support exporting a single-use lock
  file).
- Tools supporting extras MUST also support dependency groups.
- Tools should explicitly set this key to an empty array to signal that the
  inputs used to generate the lock file had no extras (e.g. a
  :ref:`pyproject.toml <pyproject-toml-spec>` file had no
  :ref:`[project.optional-dependencies] <pyproject-toml-optional-dependencies>`
  table), signalling that the lock file is, in effect, multi-use even if it only
  looks to be single-use.


.. _pylock-dependency-groups:

``dependency-groups``
=====================

- **Type**: Array of strings
- **Required?**: no; defaults to ``[]``
- **Inspiration**: :ref:`pyproject-tool-table`
- The list of :ref:`dependency-groups` publicly supported by this lock
  file (i.e. dependency groups users are expected to be able to specify via a
  tool's UI).
- Lockers MAY choose to not support writing lock files that support extras and
  dependency groups (i.e. tools may only support exporting a single-use lock
  file).
- Tools supporting dependency groups MUST also support extras.
- Tools SHOULD explicitly set this key to an empty array to signal that the
  inputs used to generate the lock file had no dependency groups (e.g. a
  :ref:`pyproject.toml <pyproject-toml-spec>` file had no
  :ref:`[dependency-groups] <dependency-groups>` table), signalling that the
  lock file is, in effect, multi-use even if it only looks to be single-use.


.. _pylock-default-groups:

``default-groups``
==================

- **Type**: Array of strings
- **Required?**: no; defaults to ``[]``
- **Inspiration**: Poetry_, PDM_
- The name of synthetic dependency groups to represent what should be installed
  by default (e.g. what
  :ref:`[project.dependencies] <pyproject-toml-dependencies>` implicitly
  represents).
- Meant to be used in situations where :ref:`pylock-packages-marker`
  necessitates such a group to exist.
- The groups listed by this key SHOULD NOT be listed in
  :ref:`pylock-dependency-groups` as the groups are not meant to be directly
  exposed to users by name but instead via an installer's UI.


.. _pylock-created-by:

``created-by``
==============

- **Type**: string
- **Required?**: yes
- **Inspiration**: Tools with their name in their lock file name
- Records the name of the tool used to create the lock file.
- Tools MAY use the :ref:`pylock-tool` table to record enough details that it
  can be inferred what inputs were used to create the lock file.
- Tools SHOULD record the normalized name of the tool if it is available as a
  Python package to facilitate finding the tool.


.. _pylock-packages:

``[[packages]]``
================

- **Type**: array of tables
- **Required?**: yes
- **Inspiration**: PDM_, Poetry_, uv_
- An array containing all packages that *may* be installed.
- Packages MAY be listed multiple times with varying data, but all packages to
  be installed MUST narrow down to a single entry at install time.


.. _pylock-packages-name:

``packages.name``
-----------------

- **Type**: string
- **Required?**: yes
- **Inspiration**: :ref:`core-metadata-name`
- The name of the package :ref:`normalized <name-normalization>`.


.. _pylock-packages-version:

``packages.version``
--------------------

- **Type**: string
- **Required?**: no
- **Inspiration**: :ref:`core-metadata-version`
- The version of the package.
- The version SHOULD be specified when the version is known to be stable
  (i.e. when an :ref:`sdist <source-distribution-format>` or
  :ref:`wheels <binary-distribution-format>` are specified).
- The version MUST NOT be included when it cannot be guaranteed to be consistent
  with the code used (i.e. when a
  :ref:`source tree <source-distribution-format-source-tree>` is used).


.. _pylock-packages-marker:

``packages.marker``
-------------------

- **Type**: string
- **Required?**: no
- **Inspiration**: PDM_
- The
  :ref:`environment marker <dependency-specifiers-environment-markers>`
  which specify when the package should be installed.


.. _pylock-packages-requires-python:

``packages.requires-python``
----------------------------

- **Type**: string
- **Required?**: no
- **Inspiration**: :ref:`core-metadata-requires-python`
- Holds the :ref:`version-specifiers` for Python version compatibility
  for the package.


.. _pylock-packages-dependencies:

``[[packages.dependencies]]``
-----------------------------

- **Type**: array of tables
- **Required?**: no
- **Inspiration**: PDM_, Poetry_, uv_
- Records the other entries in :ref:`pylock-packages` which are direct
  dependencies of this package.
- Each entry is a table which contains the minimum information required to tell
  which other package entry it corresponds to where doing a key-by-key
  comparison would find the appropriate package with no ambiguity (e.g. if there
  are two entries for the ``spam`` package, then you can include the version
  number like ``{name = "spam", version = "1.0.0"}``, or by source like
  ``{name = "spam", vcs = { url = "..."}``).
- Tools MUST NOT use this information when doing installation; it is purely
  informational for auditing purposes.


.. _pylock-packages-vcs:

``[packages.vcs]``
------------------

- **Type**: table
- **Required?**: no; mutually-exclusive with :ref:`pylock-packages-directory`,
  :ref:`pylock-packages-archive`, :ref:`pylock-packages-sdist`, and
  :ref:`pylock-packages-wheels`
- **Inspiration**: :ref:`direct-url-data-structure`
- Record the version control system details for the
  :ref:`source tree <source-distribution-format-source-tree>` it
  contains.
- Tools MAY choose to not support version control systems, both from a locking
  and/or installation perspective.
- Tools MAY choose to only support a subset of the available VCS types.
- Tools SHOULD provide a way for users to opt in/out of using version control
  systems.
- Installation from a version control system is considered originating from a
  :ref:`direct URL reference <direct-url>`.


.. _pylock-packages-vcs-type:

``packages.vcs.type``
'''''''''''''''''''''

- **Type**: string; supported values specified in
  :ref:`direct-url-data-structure-registered-vcs`
- **Required?**: yes
- **Inspiration**: :ref:`direct-url-data-structure-vcs`
- The type of version control system used.


.. _pylock-packages-vcs-url:

``packages.vcs.url``
''''''''''''''''''''

- **Type**: string
- **Required?**: if :ref:`pylock-packages-vcs-path` is not specified
- **Inspiration**: :ref:`direct-url-data-structure-vcs`
- The URL_ to the source tree.


.. _pylock-packages-vcs-path:

``packages.vcs.path``
'''''''''''''''''''''

- **Type**: string
- **Required?**: if :ref:`pylock-packages-vcs-url` is not specified
- **Inspiration**: :ref:`direct-url-data-structure-vcs`
- The path to the local directory of the source tree.
- If a relative path is used it MUST be relative to the location of this file.
- If the path is relative it MAY use POSIX-style path separators explicitly
  for portability.


.. _pylock-packages-vcs-requested-revision:

``packages.vcs.requested-revision``
'''''''''''''''''''''''''''''''''''

- **Type**: string
- **Required?**: no
- **Inspiration**: :ref:`direct-url-data-structure-vcs`
- The branch/tag/ref/commit/revision/etc. that the user requested.
- This is purely informational and to facilitate writing the
  :ref:`direct-url-data-structure`; it MUST NOT be used to checkout
  the repository.


.. _pylock-packages-vcs-commit-id:

``packages.vcs.commit-id``
''''''''''''''''''''''''''

- **Type**: string
- **Required?**: yes
- **Inspiration**: :ref:`direct-url-data-structure-vcs`
- The exact commit/revision number that is to be installed.
- If the VCS supports commit-hash based revision identifiers, such a
  commit-hash, it MUST be used as the commit ID in order to reference an
  immutable version of the source code.


.. _pylock-packages-vcs-subdirectory:

``packages.vcs.subdirectory``
'''''''''''''''''''''''''''''

- **Type**: string
- **Required?**: no
- **Inspiration**: :ref:`direct-url-data-structure-subdirectories`
- The subdirectory within the
  :ref:`source tree <source-distribution-format-source-tree>` where
  the project root of the project is (e.g. the location of the
  :ref:`pyproject.toml <pyproject-toml-spec>` file).
- The path MUST be relative to the root of the source tree structure.


.. _pylock-packages-directory:

``[packages.directory]``
------------------------

- **Type**: table
- **Required?**: no; mutually-exclusive with :ref:`pylock-packages-vcs`,
  :ref:`pylock-packages-archive`, :ref:`pylock-packages-sdist`, and
  :ref:`pylock-packages-wheels`
- **Inspiration**: :ref:`direct-url-data-structure-local-directory`
- Record the local directory details for the
  :ref:`source tree <source-distribution-format-source-tree>` it
  contains.
- Tools MAY choose to not support local directories, both from a locking
  and/or installation perspective.
- Tools SHOULD provide a way for users to opt in/out of using local directories.
- Installation from a directory is considered originating from a
  :ref:`direct URL reference <direct-url>`.


.. _pylock-packages-directory-path:

``packages.directory.path``
'''''''''''''''''''''''''''

- **Type**: string
- **Required?**: yes
- **Inspiration**: :ref:`direct-url-data-structure-local-directory`
- The local directory where the source tree is.
- If the path is relative it MUST be relative to the location of the lock file.
- If the path is relative it MAY use POSIX-style path separators for
  portability.


.. _pylock-packages-directory-editable:

``packages.directory.editable``
'''''''''''''''''''''''''''''''

- **Type**: boolean
- **Required?**: no; defaults to ``false``
- **Inspiration**: :ref:`direct-url-data-structure-local-directory`
- A flag representing whether the source tree was an editable install at lock
  time.
- An installer MAY choose to ignore this flag if user actions or context would
  make an editable install unnecessary or undesirable (e.g. a container image
  that will not be mounted for development purposes but instead deployed to
  production where it would be treated at read-only).


.. _pylock-packages-directory-subdirectory:

``packages.directory.subdirectory``
'''''''''''''''''''''''''''''''''''

See :ref:`pylock-packages-vcs-subdirectory`.


.. _pylock-packages-archive:

``[packages.archive]``
----------------------

- **Type**: table
- **Required?**: no
- **Inspiration**: :ref:`direct-url-data-structure-archive`
- A direct reference to an archive file to install from
  (this can include wheels and sdists, as well as other archive formats
  containing a source tree).
- Tools MAY choose to not support archive files, both from a locking
  and/or installation perspective.
- Tools SHOULD provide a way for users to opt in/out of using archive files.
- Installation from an archive file is considered originating from a
  :ref:`direct URL reference <direct-url>`.


.. _pylock-packages-archive-url:

``packages.archive.url``
''''''''''''''''''''''''

See :ref:`pylock-packages-vcs-url`.


.. _pylock-packages-archive-path:

``packages.archive.path``
'''''''''''''''''''''''''

See :ref:`pylock-packages-vcs-path`.


.. _pylock-packages-archive-size:

``packages.archive.size``
'''''''''''''''''''''''''

- **Type**: integer
- **Required?**: no
- **Inspiration**: uv_, :ref:`simple-repository-api`
- The size of the archive file.
- Tools SHOULD provide the file size when reasonably possible (e.g. the file
  size is available via the Content-Length_ header from a HEAD_ HTTP request).


.. _pylock-packages-archive-upload-time:

``packages.archive.upload-time``
''''''''''''''''''''''''''''''''

- **Type**: datetime
- **Required?**: no
- **Inspiration**: :ref:`simple-repository-api`
- The time the file was uploaded.
- The date and time MUST be recorded in UTC.


.. _pylock-packages-archive-hashes:

``[packages.archive.hashes]``
'''''''''''''''''''''''''''''

- **Type**: Table of strings
- **Required?**: yes
- **Inspiration**: PDM_, Poetry_, uv_, :ref:`simple-repository-api`
- A table listing known hash values of the file where the key is the hash
  algorithm and the value is the hash value.
- The table MUST contain at least one entry.
- Hash algorithm keys SHOULD be lowercase.
- At least one secure algorithm from :py:data:`hashlib.algorithms_guaranteed`
  SHOULD always be included (at time of writing, sha256 specifically is
  recommended.


.. _pylock-packages-archive-subdirectory:

``packages.archive.subdirectory``
''''''''''''''''''''''''''''''''''

See :ref:`pylock-packages-vcs-subdirectory`.


.. _pylock-packages-index:

``packages.index``
------------------

- **Type**: string
- **Required?**: no
- **Inspiration**: uv_
- The base URL for the package index from :ref:`simple-repository-api`
  where the sdist and/or wheels were found (e.g. ``https://pypi.org/simple/``).
- When possible, this SHOULD be specified to assist with generating
  `software bill of materials`_ -- aka SBOMs -- and to assist in finding a file
  if a URL ceases to be valid.
- Tools MAY support installing from an index if the URL recorded for a specific
  file is no longer valid (e.g. returns a 404 HTTP error code).


.. _pylock-packages-sdist:

``[packages.sdist]``
--------------------

- **Type**: table
- **Required?**: no; mutually-exclusive with :ref:`pylock-packages-vcs`,
  :ref:`pylock-packages-directory`, and :ref:`pylock-packages-archive`
- **Inspiration**: uv_
- Details of a :ref:`source-distribution-format-sdist` for the
  package.
- Tools MAY choose to not support sdist files, both from a locking
  and/or installation perspective.
- Tools SHOULD provide a way for users to opt in/out of using sdist files.


.. _pylock-packages-sdist-name:

``packages.sdist.name``
'''''''''''''''''''''''

- **Type**: string
- **Required?**: no, not when the last component of
  :ref:`pylock-packages-sdist-path`/ :ref:`pylock-packages-sdist-url` would be
  the same value
- **Inspiration**: PDM_, Poetry_, uv_
- The file name of the :ref:`source-distribution-format-sdist` file.


.. _pylock-packages-sdist-upload-time:

``packages.sdist.upload-time``
''''''''''''''''''''''''''''''

See :ref:`pylock-packages-archive-upload-time`.


.. _pylock-packages-sdist-url:

``packages.sdist.url``
''''''''''''''''''''''

See :ref:`pylock-packages-archive-url`.


.. _pylock-packages-sdist-path:

``packages.sdist.path``
'''''''''''''''''''''''

See :ref:`pylock-packages-archive-path`.


.. _pylock-packages-sdist-size:

``packages.sdist.size``
'''''''''''''''''''''''

See :ref:`pylock-packages-archive-size`.


.. _pylock-packages-sdist-hashes:

``packages.sdist.hashes``
'''''''''''''''''''''''''

See :ref:`pylock-packages-archive-hashes`.



.. _pylock-packages-wheels:

``[[packages.wheels]]``
-----------------------

- **Type**: array of tables
- **Required?**: no; mutually-exclusive with :ref:`pylock-packages-vcs`,
  :ref:`pylock-packages-directory`, and :ref:`pylock-packages-archive`
- **Inspiration**: PDM_, Poetry_, uv_
- For recording the wheel files as specified by
  :ref:`binary-distribution-format` for the package.
- Tools MUST support wheel files, both from a locking and installation
  perspective.


.. _pylock-packages-wheels-name:

``packages.wheels.name``
''''''''''''''''''''''''

- **Type**: string
- **Required?**: no, not when the last component of
  :ref:`pylock-packages-wheels-path`/ :ref:`pylock-packages-wheels-url` would be
  the same value
- **Inspiration**: PDM_, Poetry_, uv_
- The file name of the :ref:`binary-distribution-format` file.


.. _pylock-packages-wheels-upload-time:

``packages.wheels.upload-time``
'''''''''''''''''''''''''''''''

See :ref:`pylock-packages-archive-upload-time`.


.. _pylock-packages-wheels-url:

``packages.wheels.url``
'''''''''''''''''''''''

See :ref:`pylock-packages-archive-url`.


.. _pylock-packages-wheels-path:

``packages.wheels.path``
''''''''''''''''''''''''

See :ref:`pylock-packages-archive-path`.


.. _pylock-packages-wheels-size:

``packages.wheels.size``
''''''''''''''''''''''''

See :ref:`pylock-packages-archive-size`.


.. _pylock-packages-wheels-hashes:

``packages.wheels.hashes``
''''''''''''''''''''''''''

See :ref:`pylock-packages-archive-hashes`.


.. _pylock-packages-attestation-identities:

``[[packages.attestation-identities]]``
---------------------------------------

- **Type**: array of tables
- **Required?**: no
- **Inspiration**: :ref:`provenance-object`
- A recording of the attestations for **any** file recorded for this package.
- If available, tools SHOULD include the attestation identities found.
- Publisher-specific keys are to be included in the table as-is
  (i.e. top-level), following the spec at
  :ref:`index-hosted-attestations`.


.. _pylock-packages-attestation-identities-kind:

``packages.attestation-identities.kind``
''''''''''''''''''''''''''''''''''''''''

- **Type**: string
- **Required?**: yes
- **Inspiration**: :ref:`provenance-object`
- The unique identity of the Trusted Publisher.


.. _pylock-packages-tool:

``[packages.tool]``
-------------------

- **Type**: table
- **Required?**: no
- **Inspiration**: :ref:`pyproject-tool-table`
- Similar usage as that of the :ref:`pylock-tool` table from the
  :ref:`pyproject-toml-spec`, but at the package version level instead
  of at the lock file level (which is also available via :ref:`pylock-tool`).
- Data recorded in the table MUST be disposable (i.e. it MUST NOT affect
  installation).


.. _pylock-tool:

``[tool]``
==========

- **Type**: table
- **Required?**: no
- **Inspiration**: :ref:`pyproject-tool-table`
- See :ref:`pylock-packages-tool`.


-------
Example
-------

.. literalinclude:: pylock-toml/pylock.example.toml


------------
Installation
------------

The following outlines the steps to be taken to install from a lock file
(while the requirements are prescriptive, the general steps and order are
a suggestion):

#. Gather the extras and dependency groups to install and set ``extras`` and
   ``dependency_groups`` for marker evaluation, respectively.

   #. ``extras`` SHOULD be set to the empty set by default.
   #. ``dependency_groups`` SHOULD be the set created from
      :ref:`pylock-default-groups` by default.

#. Check if the metadata version specified by :ref:`pylock-lock-version` is
   supported; an error or warning MUST be raised as appropriate.
#. If :ref:`pylock-requires-python` is specified, check that the environment
   being installed for meets the requirement; an error MUST be raised if it is
   not met.
#. If :ref:`pylock-environments` is specified, check that at least one of the
   environment marker expressions is satisfied; an error MUST be raised if no
   expression is satisfied.
#. For each package listed in :ref:`pylock-packages`:

   #. If :ref:`pylock-packages-marker` is specified, check if it is satisfied;
      if it isn't, skip to the next package.
   #. If :ref:`pylock-packages-requires-python` is specified, check if it is
      satisfied; an error MUST be raised if it isn't.
   #. Check that no other conflicting instance of the package has been slated to
      be installed; an error about the ambiguity MUST be raised otherwise.
   #. Check that the source of the package is specified appropriately (i.e.
      there are no conflicting sources in the package entry);
      an error MUST be raised if any issues are found.
   #. Add the package to the set of packages to install.

#. For each package to be installed:

   - If :ref:`pylock-packages-vcs` is set:

     #. Clone the repository to the commit ID specified in
        :ref:`pylock-packages-vcs-commit-id`.
     #. :ref:`Build <source-distribution-format-source-tree>` the package,
        respecting :ref:`pylock-packages-vcs-subdirectory`.
     #. :ref:`Install <binary-distribution-format>`.

   - Else if :ref:`pylock-packages-directory` is set:

     #. :ref:`Build <source-distribution-format-source-tree>` the package,
        respecting :ref:`pylock-packages-directory-subdirectory`.
     #. :ref:`Install <binary-distribution-format>`.

   - Else if :ref:`pylock-packages-archive` is set:

     #. Get the file.
     #. Validate using :ref:`pylock-packages-archive-size` and
        :ref:`pylock-packages-archive-hashes`.
     #. :ref:`Build <source-distribution-format-source-tree>` the package,
        respecting :ref:`pylock-packages-archive-subdirectory`.
     #. :ref:`Install <binary-distribution-format>`.

   - Else if there are entries for :ref:`pylock-packages-wheels`:

     #. Look for the appropriate wheel file based on
        :ref:`pylock-packages-wheels-name`; if one is not found then move on to
        :ref:`pylock-packages-sdist` or an error MUST be raised about a
        lack of source for the project.
     #. Get the file:

        - If :ref:`pylock-packages-wheels-path` is set, use it.
        - Else if :ref:`pylock-packages-wheels-url` is set, try to use it;
          optionally tools MAY use :ref:`pylock-packages-index` or some
          tool-specific mechanism to download the selected wheel file (tools
          MUST NOT try to change what wheel file to download based on what's
          available; what file to install should be determined in an offline
          fashion for reproducibility).

     #. Validate using :ref:`pylock-packages-wheels-size` and
        :ref:`pylock-packages-wheels-hashes`.
     #. :ref:`Install <binary-distribution-format>`.

   - Else if no :ref:`pylock-packages-wheels` file is found or
     :ref:`pylock-packages-sdist` is solely set:

     #. Get the file.

        - If :ref:`pylock-packages-sdist-path` is set, use it.
        - Else if :ref:`pylock-packages-sdist-url` is set, try to use it; tools
          MAY use :ref:`pylock-packages-index` or some tool-specific mechanism
          to download the file.

     #. Validate using :ref:`pylock-packages-sdist-size` and
        :ref:`pylock-packages-sdist-hashes`.
     #. :ref:`Build <source-distribution-format-sdist>` the package.
     #. :ref:`Install <binary-distribution-format>`.


-------
History
-------

- April 2025: Initial version, approved via :pep:`751`.


.. _Content-Length: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length
.. _Dependabot: https://docs.github.com/en/code-security/dependabot
.. _HEAD: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD
.. _PDM: https://pypi.org/project/pdm/
.. _pip-tools: https://pypi.org/project/pip-tools/
.. _Poetry: https://pypi.org/project/poetry/
.. _requirements file:
.. _requirements files: https://pip.pypa.io/en/stable/reference/requirements-file-format/
.. _software bill of materials: https://www.cisa.gov/sbom
.. _TOML: https://toml.io/
.. _uv: https://pypi.org/project/uv/
.. _URL: https://url.spec.whatwg.org/
