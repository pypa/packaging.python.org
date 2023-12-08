
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

History
=======

* September 2015: initial form of the HTML format, in :pep:`503`
* May 2019: "yank" support, in :pep:`592`
* July 2020: API versioning convention and metadata, and declaring the HTML
  format as API v1, in :pep:`629`
* May 2021: providing package metadata independently from a package, in
  :pep:`658`
* May 2022: initial form of the JSON format, with a mechanism for clients to
  choose between them, and declaring both formats as API v1, in :pep:`691`
* October 2022: project versions and file size and upload-time in the JSON
  format, in :pep:`700`
* June 2023: renaming the field which provides package metadata independently
  from a package, in :pep:`714`
