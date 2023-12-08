
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

   An `OpenAPI <https://spec.openapis.org/oas/v3.1.0>`__ document which
   specifies the full API. It declares both representations, but only details
   the JSON format's schema.

   .. literalinclude:: simple-repository-api.openapi.yml
      :language: yaml

API version scheme
##################

The version of the API is a version number which follows the :ref:`version
specifier specification <version-specifiers>` as only ``Major.Minor``.

Incrementing the major version is used to signal a backwards incompatible
change such that existing clients would no longer be expected to be able to
meaningfully use the API.

Incrementing the minor version is used to signal a backwards compatible change
such that existing clients would still be expected to be able to meaningfully
use the API.

Clients should introspect each response for the repository version, and must
assume version 1.0 if missing. If the major version is greater than expected,
clients must fail with an appropriate error message for the user. If the minor
version is greater than expected, clients should warn the user with an
appropriate message. Clients may continue to use feature detection.

Representations
###############

The index server can respond with one of two different representation formats
for each endpoint: HTML and JSON. The format can be selected by the client
through the use of `content negotiation
<https://www.rfc-editor.org/rfc/rfc2616.html#section-12>`_.

Endpoints
#########

The API consists of two metadata endpoints:

* :ref:`repo_api_projects_list`
* :ref:`repo_api_project_details`

The root URL ``/`` represents the base URL, where it would be prefixed with
the index's URL to construct the full URL which tools make the request for.

If a client makes a request to a URL without a trailing forward-slash ``/``,
then the index server should redirect the client to the same URL with the ``/``
appended.

.. _repo_api_projects_list:

Projects list
-------------

URL: ``/``, the root URL

This endpoint returns a list of all of the :term:`projects <Project>` provided
by the index, with each list item containing the project's name.

HTML representation
^^^^^^^^^^^^^^^^^^^

The response from the index is a valid
`HTML5 <https://html.spec.whatwg.org/>`_ page.

A `metadata element`_ ``<meta>`` may exist anywhere in the HTML document, with
``name`` attribute value equal to the string ``pypi:repository-version``, and
``content`` attribute value equal the API version which the response
implements.

Each project provided by the index has a corresponding `anchor element`_
``<a>``:

* Its body text must exist and is the name of the project (not necessarily
  :ref:`normalized <name-normalization>`).

* Its ``href`` attribute must exist and is a URL to the :ref:`project details
  <repo_api_project_details>` page for the project. This URL must end with a
  forward-slash ``/``, but may be absolute or relative.

An example response page:

.. code-block:: html

   <!DOCTYPE html>
   <html>
     <head>
       <meta name="pypi:repository-version" content="1.0">
       <title>Projects</title>
     </head>
     <body>
       <a href="/frob/">frob</a>
       <a href="/spamspamspam/">spamspamspam</a>
     </body>
   </html>

.. _repo_api_project_details:

Project details
---------------

URL: ``/<project>/``, where ``<project>`` is replaced with the :ref:`normalized
name <name-normalization>` of the project.

This endpoint returns some metadata of the :term:`project <Project>`, along
with a list of all :term:`package files <Distribution Package>` provided by the
index for the project.

If a client uses an unnormalized name for ``<project>``, the index server may
redirect to the URL with the normalized name. Conformant client must always
make requests with normalized names.

API file-related features:

* The file can be hosted anywhere, not necessarily by the index server.

* The file's URL in the list-item is a URL to fetch the file. It may be
  absolute or relative. It's last path segment must be the file's filename.

* Hashes of the file's contents are optional but recommended. The hash name is
  the name of the hash algorithm's function, and the value is the hex-encoded
  digest hash. The function should be one in the standard-library ``hashlib``
  module, and ``sha256`` is preferred.

* A `GPG signature <https://www.rfc-editor.org/rfc/rfc4880.html#section-2.2>`_
  for the file can be accessed at the same URL as the file but with ``.asc``
  appended, if it is provided. For example, the file at
  ``/packages/HolyGrail-1.0.tar.gz`` may have a signature at
  ``/packages/HolyGrail-1.0.tar.gz.asc``.

* The file's release's :ref:`core-metadata-requires-python` metadata field may
  be provided. Clients should ignore the file when installing to an environment
  for a version of Python which doesn't satisfy the requirement.

* Files may be marked as `yanked <simple_repo_api_yanked>`_.

HTML representation
^^^^^^^^^^^^^^^^^^^

The response from the index is a valid
`HTML5 <https://html.spec.whatwg.org/>`_ page.

A `metadata element`_ ``<meta>`` may exist anywhere in the HTML document, with
``name`` attribute value equal to the string ``pypi:repository-version``, and
``content`` attribute value equal the API version which the response
implements.

Each distribution package file provided by the index for the project has a
corresponding `anchor element`_ ``<a>``:

* Its body text must exist and is the file's filename.

* Its ``href`` attribute must exist and is the file's URL.

  * This URL should also include a URL fragment of the form
    ``#<hash>=<value>``, where ``<hash>`` is the hash name  and ``<value>`` is
    hash value.

* A ``data-gpg-sig`` `data attribute`_ may exist, and have value ``true`` to
  indicate a file has a GPG signature (at the location described above), or
  ``false`` to indicate no signature. Indexes should do this for none or all
  files (not some).

* A ``data-requires-python`` `data attribute`_ may exist, and have value equal
  to the :ref:`core-metadata-requires-python` metadata field for the file's
  release, with HTML-encoding (less-than ``<`` becomes the string ``&lt;``, and
  greater-than ``>`` becomes the string ``&gt;``).

* A ``data-yanked`` `data attribute`_ may exist to indicate the file was
  `yanked <simple_repo_api_yanked>`_. The attribute may have a value which
  specifies the reason the file is yanked.

.. _simple_repo_api_yanked:

Yanked files
############

A yanked :term:`package file <Distribution Package>` is one intended to be
now-unavailable for installation from the index. The file's yank-status can be
changed at anypoint (to be unyanked, or even yanked again).

Indexes may provide a textual reason for why the file has been yanked, and
clients may display that reason to end-users.

From :pep:`592`, the intention for the behaviour with yanked files is:

   The desirable experience for users is that once a file is yanked, when a
   human being is currently trying to directly install a yanked file, that it
   fails as if that file had been deleted. However, when a human did that
   awhile ago, and now a computer is just continuing to mechanically follow the
   original order to install the now yanked file, then it acts as if it had not
   been yanked.

Installers must ignore yanked :term:`releases <Release>` if a non-yanked
release satisfies the :term:`requirement <Requirement>`. Installers may refuse
to install a yanked release and not install anything. Installers should follow
the spirit of the intention quoted above and prevent new dependencies on yanked
releases and files.

Installers should emit a warning when it does decide to install a yanked file.
That warning may utilize the reason for the yanking.

What this means is left up to the specific installer, to decide how to best fit
into the overall usage of their installer. However, there are two suggested
approaches to take:

* Yanked files are always ignored, unless they are the only file that matches a
  version specifier that “pins” to an exact version using either ``==``
  (without any modifiers that make it a range, such as ``.*``) or ``===``.
  Matching this version specifier should otherwise be done as per :pep:`440`
  for things like local versions, zero padding, etc.

* Yanked files are always ignored, unless they are the only file that matches
  what a lock file (such as Pipfile.lock or poetry.lock) specifies to be
  installed. In this case, a yanked file SHOULD not be used when creating or
  updating a lock file from some input file or command.

Mirror indexes may omit list-items for yanked files in their responses to
clients, or may include list-items for yanked files along with their
yank-status (this status must be present for yanked files).

History
=======

* September 2015: initial form of the HTML format, in :pep:`503`
* July 2016: Requires-Python metadata, in an update to :pep:`503`
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

.. _anchor element: https://html.spec.whatwg.org/#the-a-element

.. _data attribute: https://html.spec.whatwg.org/#attr-data-*

.. _metadata element: https://html.spec.whatwg.org/#the-meta-element
