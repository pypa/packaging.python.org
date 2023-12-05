
.. _simple-repository-api:

=====================
Simple repository API
=====================

The simple repository API is an HTTP-based protocol for tools to list and
download Python :term:`packages <Distribution Package>`. It is the API which
:term:`package indexes <Package Index>` implement to provide package managers
(eg :ref:`pip`) enough information to determine what to install for a given set
of :term:`requirements <Requirement>`, then go on to install those packages.

There is one version series for the API: version 1. Minor versions add optional
features, and are described below.

The API consists of two endpoints: listing :term:`projects <Project>` available
in the index, and listing package files for (and some other details of) a given
project. These endpoints are provided as responses from an HTTP server.

There are two representations of responses from the API: HTML and JSON. Apart
from optional features, these representations provide the same information.

Specification
=============

.. collapse:: OpenAPI

   An `OpenAPI <https://swagger.io/specification>`__ document which specifies
   the full API for both representations.

   .. literalinclude:: simple-repository-api.openapi.yml
      :language: yaml

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
