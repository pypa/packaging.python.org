
.. _simple-repository-api:

=====================
Simple repository API
=====================

The interface for querying available package versions and
retrieving packages from an index server comes in two forms:
HTML and JSON.

The HTML format is defined in :pep:`503`, with the addition of "yank"
support (allowing a kind of file deletion) in :pep:`592`, specifying
the interface version provided by an index server in :pep:`629`, and
providing package metadata independently from a package in
:pep:`658` and revised in :pep:`714`.

The JSON format is defined in :pep:`691`, with additional fields
added in :pep:`700`, and revisions around providing package metadata
independently from a package in :pep:`714`.
