
.. _simple-repository-api:

=====================
Simple repository API
=====================

The current interface for querying available package versions and
retrieving packages from an index server is defined in :pep:`503`,
with the addition of "yank" support (allowing a kind of file deletion)
as defined in :pep:`592`, specifying the interface version provided
by an index server in :pep:`629` and optionally providing metadata 
separated from the distrobution package as stated in :pep:`658`.
