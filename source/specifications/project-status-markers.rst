.. _project-status-markers:

======================
Project Status Markers
======================

.. note::

    This specification was originally defined in
    :pep:`792`.

.. note::

    :pep:`792` includes changes to the HTML and JSON index APIs.
    These changes are documented in the :ref:`simple-repository-api`
    under :ref:`HTML - Project Detail <simple-repository-html-project-detail>`
    and :ref:`JSON - Project Detail <simple-repository-json-project-detail>`.

Specification
=============

A project always has exactly one status. If no status is explicitly noted,
then the project is considered to be in the ``active`` state.

Indices **MAY** implement any subset of the status markers specified,
as applicable to their needs.

This standard does not prescribe *which* principals (i.e. project maintainers,
index administrators, etc.) are allowed to set and unset which statuses.

``active``
----------

Description: The project is active. This is the default status for a project.

Index semantics:

* The index hosting the project **MUST** allow uploads of new distributions to
  the project.
* The index **MUST** offer existing distributions of the project for download.

Installer semantics: none.

``archived``
------------

Description: The project does not expect to be updated in the future.

Index semantics:

* The index hosting the project **MUST NOT** allow uploads of new distributions to
  the project.
* The index **MUST** offer existing distributions of the project for download.

Installer semantics:

* Installers **MAY** produce warnings about a project's archival.

``quarantined``
---------------

Description: The project is considered generally unsafe for use, e.g. due to
malware.

Index semantics:

* The index hosting the project **MUST NOT** allow uploads of new distributions to
  the project.
* The index **MUST NOT** offer any distributions of the project for download.

Installer semantics:

* Installers **MAY** produce warnings about a project's quarantine, although
  doing so is effectively moot (as the index will not offer any distributions
  for installation).

``deprecated``
--------------

Description: The project is considered obsolete, and may have been superseded
by another project.

Index semantics:

* This status shares the same semantics as ``active``.

Installer semantics:

* Installers **MAY** produce warnings about a project's deprecation.
