
.. _simple-repository-api:

=====================
Simple repository API
=====================

The interface for querying available package versions and
retrieving packages from an index server comes in two forms:
HTML and JSON.

.. _simple-repository-api-base:

Base HTML API
=============

A repository that implements the simple API is defined by its base URL, this is
the top level URL that all additional URLs are below. The API is named the
"simple" repository due to the fact that PyPI's base URL is
``https://pypi.org/simple/``.

.. note:: All subsequent URLs in this document will be relative to this base
          URL (so given PyPI's URL, a URL of ``/foo/`` would be
          ``https://pypi.org/simple/foo/``.


Within a repository, the root URL (``/`` for this spec which represents the base
URL) **MUST** be a valid HTML5 page with a single anchor element per project in
the repository. The text of the anchor tag **MUST** be the name of
the project and the href attribute **MUST** link to the URL for that particular
project. As an example::

   <!DOCTYPE html>
   <html>
     <body>
       <a href="/frob/">frob</a>
       <a href="/spamspamspam/">spamspamspam</a>
     </body>
   </html>

Below the root URL is another URL for each individual project contained within
a repository. The format of this URL is ``/<project>/`` where the ``<project>``
is replaced by the normalized name for that project, so a project named
"HolyGrail" would have a URL like ``/holygrail/``. This URL must respond with
a valid HTML5 page with a single anchor element per file for the project. The
href attribute **MUST** be a URL that links to the location of the file for
download, and the text of the anchor tag **MUST** match the final path
component (the filename) of the URL. The URL **SHOULD** include a hash in the
form of a URL fragment with the following syntax: ``#<hashname>=<hashvalue>``,
where ``<hashname>`` is the lowercase name of the hash function (such as
``sha256``) and ``<hashvalue>`` is the hex encoded digest.

In addition to the above, the following constraints are placed on the API:

* All URLs which respond with an HTML5 page **MUST** end with a ``/`` and the
  repository **SHOULD** redirect the URLs without a ``/`` to add a ``/`` to the
  end.

* URLs may be either absolute or relative as long as they point to the correct
  location.

* There are no constraints on where the files must be hosted relative to the
  repository.

* There may be any other HTML elements on the API pages as long as the required
  anchor elements exist.

* Repositories **MAY** redirect unnormalized URLs to the canonical normalized
  URL (e.g. ``/Foobar/`` may redirect to ``/foobar/``), however clients
  **MUST NOT** rely on this redirection and **MUST** request the normalized
  URL.

* Repositories **SHOULD** choose a hash function from one of the ones
  guaranteed to be available via the :py:mod:`hashlib` module in the Python standard
  library (currently ``md5``, ``sha1``, ``sha224``, ``sha256``, ``sha384``,
  ``sha512``). The current recommendation is to use ``sha256``.

* If there is a GPG signature for a particular distribution file it **MUST**
  live alongside that file with the same name with a ``.asc`` appended to it.
  So if the file ``/packages/HolyGrail-1.0.tar.gz`` existed and had an
  associated signature, the signature would be located at
  ``/packages/HolyGrail-1.0.tar.gz.asc``.

* A repository **MAY** include a ``data-gpg-sig`` attribute on a file link with
  a value of either ``true`` or ``false`` to indicate whether or not there is a
  GPG signature. Repositories that do this **SHOULD** include it on every link.

* A repository **MAY** include a ``data-requires-python`` attribute on a file
  link. This exposes the :ref:`core-metadata-requires-python` metadata field
  for the corresponding release. Where this is present, installer tools
  **SHOULD** ignore the download when installing to a Python version that
  doesn't satisfy the requirement. For example::

      <a href="..." data-requires-python="&gt;=3">...</a>

  In the attribute value, < and > have to be HTML encoded as ``&lt;`` and
  ``&gt;``, respectively.

Normalized Names
----------------

This spec references the concept of a "normalized" project name. As per
:ref:`the name normalization specification <name-normalization>`
the only valid characters in a name are the ASCII alphabet, ASCII numbers,
``.``, ``-``, and ``_``. The name should be lowercased with all runs of the
characters ``.``, ``-``, or ``_`` replaced with a single ``-`` character. This
can be implemented in Python with the ``re`` module::

   import re

   def normalize(name):
       return re.sub(r"[-_.]+", "-", name).lower()

.. _simple-repository-api-yank:

Adding "Yank" Support to the Simple API
=======================================

Links in the simple repository **MAY** have a ``data-yanked`` attribute
which may have no value, or may have an arbitrary string as a value. The
presence of a ``data-yanked`` attribute **SHOULD** be interpreted as
indicating that the file pointed to by this particular link has been
"Yanked", and should not generally be selected by an installer, except
under specific scenarios.

The value of the ``data-yanked`` attribute, if present, is an arbitrary
string that represents the reason for why the file has been yanked. Tools
that process the simple repository API **MAY** surface this string to
end users.

The yanked attribute is not immutable once set, and may be rescinded in
the future (and once rescinded, may be reset as well). Thus API users
**MUST** be able to cope with a yanked file being "unyanked" (and even
yanked again).


Installers
----------

The desirable experience for users is that once a file is yanked, when
a human being is currently trying to directly install a yanked file, that
it fails as if that file had been deleted. However, when a human did that
awhile ago, and now a computer is just continuing to mechanically follow
the original order to install the now yanked file, then it acts as if it
had not been yanked.

An installer **MUST** ignore yanked releases, if the selection constraints
can be satisfied with a non-yanked version, and **MAY** refuse to use a
yanked release even if it means that the request cannot be satisfied at all.
An implementation **SHOULD** choose a policy that follows the spirit of the
intention above, and that prevents "new" dependencies on yanked
releases/files.

What this means is left up to the specific installer, to decide how to best
fit into the overall usage of their installer. However, there are two
suggested approaches to take:

1. Yanked files are always ignored, unless they are the only file that
   matches a version specifier that "pins" to an exact version using
   either ``==`` (without any modifiers that make it a range, such as
   ``.*``) or ``===``. Matching this version specifier should otherwise
   be done as per :ref:`the version specifiers specification
   <version-specifiers>` for things like local versions, zero padding,
   etc.
2. Yanked files are always ignored, unless they are the only file that
   matches what a lock file (such as ``Pipfile.lock`` or ``poetry.lock``)
   specifies to be installed. In this case, a yanked file **SHOULD** not
   be used when creating or updating a lock file from some input file or
   command.

Regardless of the specific strategy that an installer chooses for deciding
when to install yanked files, an installer **SHOULD** emit a warning when
it does decide to install a yanked file. That warning **MAY** utilize the
value of the ``data-yanked`` attribute (if it has a value) to provide more
specific feedback to the user about why that file had been yanked.


Mirrors
-------

Mirrors can generally treat yanked files one of two ways:

1. They may choose to omit them from their simple repository API completely,
   providing a view over the repository that shows only "active", unyanked
   files.
2. They may choose to include yanked files, and additionally mirror the
   ``data-yanked`` attribute as well.

Mirrors **MUST NOT** mirror a yanked file without also mirroring the
``data-yanked`` attribute for it.

.. _simple-repository-api-versioning:

Versioning PyPI's Simple API
============================

This spec proposes the inclusion of a meta tag on the responses of every
successful request to a simple API page, which contains a name attribute
of "pypi:repository-version", and a content that is a :ref:`version specifiers
specification <version-specifiers>` compatible
version number, which is further constrained to ONLY be Major.Minor, and
none of the additional features supported by :ref:`the version specifiers
specification <version-specifiers>`.

This would end up looking like::

  <meta name="pypi:repository-version" content="1.0">

When interpreting the repository version:

* Incrementing the major version is used to signal a backwards
  incompatible change such that existing clients would no longer be
  expected to be able to meaningfully use the API.
* Incrementing the minor version is used to signal a backwards
  compatible change such that existing clients would still be
  expected to be able to meaningfully use the API.

It is left up to the discretion of any future specs as to what
specifically constitutes a backwards incompatible vs compatible change
beyond the broad suggestion that existing clients will be able to
"meaningfully" continue to use the API, and can include adding,
modifying, or removing existing features.

It is expectation of this spec that the major version will never be
incremented, and any future major API evolutions would utilize a
different mechanism for API evolution. However the major version
is included to disambiguate with future versions (e.g. a hypothetical
simple api v2 that lived at /v2/, but which would be confusing if the
repository-version was set to a version >= 2).

This spec sets the current API version to "1.0", and expects that
future specs that further evolve the simple API will increment the
minor version number.


Clients
-------

Clients interacting with the simple API **SHOULD** introspect each
response for the repository version, and if that data does not exist
**MUST** assume that it is version 1.0.

When encountering a major version greater than expected, clients
**MUST** hard fail with an appropriate error message for the user.

When encountering a minor version greater than expected, clients
**SHOULD** warn users with an appropriate message.

Clients **MAY** still continue to use feature detection in order to
determine what features a repository uses.

.. _simple-repository-api-metadata-file:

Serve Distribution Metadata in the Simple Repository API
========================================================

In a simple repository's project page, each anchor tag pointing to a
distribution **MAY** have a ``data-dist-info-metadata`` attribute. The
presence of the attribute indicates the distribution represented by
the anchor tag **MUST** contain a Core Metadata file that will not be
modified when the distribution is processed and/or installed.

If a ``data-dist-info-metadata`` attribute is present, the repository
**MUST** serve the distribution's Core Metadata file alongside the
distribution with a ``.metadata`` appended to the distribution's file
name. For example, the Core Metadata of a distribution served at
``/files/distribution-1.0-py3.none.any.whl`` would be located at
``/files/distribution-1.0-py3.none.any.whl.metadata``. This is similar
to how :ref:`the base HTML API specification <simple-repository-api-base>`
specifies the GPG signature file's location.

The repository **SHOULD** provide the hash of the Core Metadata file
as the ``data-dist-info-metadata`` attribute's value using the syntax
``<hashname>=<hashvalue>``, where ``<hashname>`` is the lower cased
name of the hash function used, and ``<hashvalue>`` is the hex encoded
digest. The repository **MAY** use ``true`` as the attribute's value
if a hash is unavailable.

Backwards Compatibility
-----------------------

If an anchor tag lacks the ``data-dist-info-metadata`` attribute,
tools are expected to revert to their current behaviour of downloading
the distribution to inspect the metadata.

Older tools not supporting the new ``data-dist-info-metadata``
attribute are expected to ignore the attribute and maintain their
current behaviour of downloading the distribution to inspect the
metadata. This is similar to how prior ``data-`` attribute additions
expect existing tools to operate.

.. _simple-repository-api-json:

JSON-based Simple API for Python Package Indexes
================================================

To enable response parsing with only the standard library, this spec specifies that
all responses (besides the files themselves, and the HTML responses from
:ref:`the base HTML API specification <simple-repository-api-base>`) should be
serialized using `JSON <https://www.json.org/>`_.

To enable zero configuration discovery and to minimize the amount of additional HTTP
requests, this spec extends :ref:`the base HTML API specification
<simple-repository-api-base>` such that all of the API endpoints (other than the
files themselves) will utilize HTTP content negotiation to allow client and server to
select the correct serialization format to serve, i.e. either HTML or JSON.


Versioning
----------

Versioning will adhere to :ref:`the API versioning specification
<simple-repository-api-versioning>` format (``Major.Minor``), which has defined the
existing HTML responses to be ``1.0``. Since this spec does not introduce new features
into the API, rather it describes a different serialization format for the existing
features, this spec does not change the existing ``1.0`` version, and instead just
describes how to serialize that into JSON.

Similar to :ref:`the API versioning specification
<simple-repository-api-versioning>`, the major version number **MUST** be
incremented if any
changes to the new format would result in no longer being able to expect existing
clients to meaningfully understand the format.

Likewise, the minor version **MUST** be incremented if features are
added or removed from the format, but existing clients would be expected to continue
to meaningfully understand the format.

Changes that would not result in existing clients being unable to meaningfully
understand the format and which do not represent features being added or removed
may occur without changing the version number.

This is intentionally vague, as this spec believes it is best left up to future specs
that make any changes to the API to investigate and decide whether or not that
change should increment the major or minor version.

Future versions of the API may add things that can only be represented in a subset
of the available serializations of that version. All serializations version numbers,
within a major version, **SHOULD** be kept in sync, but the specifics of how a
feature serializes into each format may differ, including whether or not that feature
is present at all.

It is the intent of this spec that the API should be thought of as URL endpoints that
return data, whose interpretation is defined by the version of that data, and then
serialized into the target serialization format.


.. _json-serialization:

JSON Serialization
------------------

The URL structure from :ref:`the base HTML API specification
<simple-repository-api-base>` still applies, as this spec only adds an additional
serialization format for the already existing API.

The following constraints apply to all JSON serialized responses described in this
spec:

* All JSON responses will *always* be a JSON object rather than an array or other
  type.

* While JSON doesn't natively support a URL type, any value that represents an
  URL in this API may be either absolute or relative as long as they point to
  the correct location. If relative, they are relative to the current URL as if
  it were HTML.

* Additional keys may be added to any dictionary objects in the API responses
  and clients **MUST** ignore keys that they don't understand.

* All JSON responses will have a ``meta`` key, which contains information related to
  the response itself, rather than the content of the response.

* All JSON responses will have a ``meta.api-version`` key, which will be a string that
  contains the :ref:`API versioning specification
  <simple-repository-api-versioning>` ``Major.Minor`` version number, with the
  same fail/warn semantics as defined in :ref:`the API versioning specification
  <simple-repository-api-versioning>`.

* All requirements of :ref:`the base HTML API specification
  <simple-repository-api-base>` that are not HTML specific still apply.


Project List
~~~~~~~~~~~~

The root URL ``/`` for this spec (which represents the base URL) will be a JSON encoded
dictionary which has a two keys:

- ``projects``: An array where each entry is a dictionary with a single key, ``name``, which represents string of the project name.
- ``meta``: The general response metadata as `described earlier <json-serialization_>`__.

As an example:

.. code-block:: json

    {
      "meta": {
        "api-version": "1.0"
      },
      "projects": [
        {"name": "Frob"},
        {"name": "spamspamspam"}
      ]
    }


.. note::

  The ``name`` field is the same as the one from :ref:`the base HTML API
  specification <simple-repository-api-base>`, which does not specify
  whether it is the non-normalized display name or the normalized name. In practice
  different implementations of these specs are choosing differently here, so relying
  on it being either non-normalized or normalized is relying on an implementation
  detail of the repository in question.


.. note::

  While the ``projects`` key is an array, and thus is required to be in some kind
  of an order, neither :ref:`the base HTML API specification
  <simple-repository-api-base>` nor this spec requires any specific ordering nor
  that the ordering is consistent from one request to the next. Mentally this is
  best thought of as a set, but both JSON and HTML lack the functionality to have
  sets.


Project Detail
~~~~~~~~~~~~~~

The format of this URL is ``/<project>/`` where the ``<project>`` is replaced by the
:ref:`the base HTML API specification <simple-repository-api-base>` normalized
name for that project, so a project named "Silly_Walk" would
have a URL like ``/silly-walk/``.

This URL must respond with a JSON encoded dictionary that has three keys:

- ``name``: The normalized name of the project.
- ``files``: A list of dictionaries, each one representing an individual file.
- ``meta``: The general response metadata as `described earlier <json-serialization_>`__.

Each individual file dictionary has the following keys:

- ``filename``: The filename that is being represented.
- ``url``: The URL that the file can be fetched from.
- ``hashes``: A dictionary mapping a hash name to a hex encoded digest of the file.
  Multiple hashes can be included, and it is up to the client to decide what to do
  with multiple hashes (it may validate all of them or a subset of them, or nothing
  at all). These hash names **SHOULD** always be normalized to be lowercase.

  The ``hashes`` dictionary **MUST** be present, even if no hashes are available
  for the file, however it is **HIGHLY** recommended that at least one secure,
  guaranteed-to-be-available hash is always included.

  By default, any hash algorithm available via :py:mod:`hashlib` (specifically any that can
  be passed to :py:func:`hashlib.new()` and do not require additional parameters) can
  be used as a key for the hashes dictionary. At least one secure algorithm from
  :py:data:`hashlib.algorithms_guaranteed` **SHOULD** always be included. At the time
  of this spec, ``sha256`` specifically is recommended.
- ``requires-python``: An **optional** key that exposes the
  :ref:`core-metadata-requires-python`
  metadata field. Where this is present, installer tools
  **SHOULD** ignore the download when installing to a Python version that
  doesn't satisfy the requirement.

  Unlike ``data-requires-python`` in :ref:`the base HTML API specification
  <simple-repository-api-base>`, the ``requires-python`` key does not
  require any special escaping other than anything JSON does naturally.
- ``dist-info-metadata``: An **optional** key that indicates
  that metadata for this file is available, via the same location as specified in
  :ref:`the API metadata file specification
  <simple-repository-api-metadata-file>` (``{file_url}.metadata``). Where this
  is present, it **MUST** be
  either a boolean to indicate if the file has an associated metadata file, or a
  dictionary mapping hash names to a hex encoded digest of the metadata's hash.

  When this is a dictionary of hashes instead of a boolean, then all the same
  requirements and recommendations as the ``hashes`` key hold true for this key as
  well.

  If this key is missing then the metadata file may or may not exist. If the key
  value is truthy, then the metadata file is present, and if it is falsey then it
  is not.

  It is recommended that servers make the hashes of the metadata file available if
  possible.
- ``gpg-sig``: An **optional** key that acts a boolean to indicate if the file has
  an associated GPG signature or not. The URL for the signature file follows what
  is specified in :ref:`the base HTML API specification
  <simple-repository-api-base>` (``{file_url}.asc``). If this key does not exist, then
  the signature may or may not exist.
- ``yanked``: An **optional** key which may be either a boolean to indicate if the
  file has been yanked, or a non empty, but otherwise arbitrary, string to indicate
  that a file has been yanked with a specific reason. If the ``yanked`` key is present
  and is a truthy value, then it **SHOULD** be interpreted as indicating that the
  file pointed to by the ``url`` field has been "Yanked" as per :ref:`the API
  yank specification <simple-repository-api-yank>`.

As an example:

.. code-block:: json

    {
      "meta": {
        "api-version": "1.0"
      },
      "name": "holygrail",
      "files": [
        {
          "filename": "holygrail-1.0.tar.gz",
          "url": "https://example.com/files/holygrail-1.0.tar.gz",
          "hashes": {"sha256": "...", "blake2b": "..."},
          "requires-python": ">=3.7",
          "yanked": "Had a vulnerability"
        },
        {
          "filename": "holygrail-1.0-py3-none-any.whl",
          "url": "https://example.com/files/holygrail-1.0-py3-none-any.whl",
          "hashes": {"sha256": "...", "blake2b": "..."},
          "requires-python": ">=3.7",
          "dist-info-metadata": true
        }
      ]
    }


.. note::

  While the ``files`` key is an array, and thus is required to be in some kind
  of an order, neither :ref:`the base HTML API specification
  <simple-repository-api-base>` nor this spec requires any specific ordering nor
  that the ordering is consistent from one request to the next. Mentally this is
  best thought of as a set, but both JSON and HTML lack the functionality to have
  sets.


Content-Types
-------------

This spec proposes that all responses from the Simple API will have a standard
content type that describes what the response is (a Simple API response), what
version of the API it represents, and what serialization format has been used.

The structure of this content type will be:

.. code-block:: text

    application/vnd.pypi.simple.$version+format

Since only major versions should be disruptive to clients attempting to
understand one of these API responses, only the major version will be included
in the content type, and will be prefixed with a ``v`` to clarify that it is a
version number.

Which means that for the existing 1.0 API, the content types would be:

- **JSON:** ``application/vnd.pypi.simple.v1+json``
- **HTML:** ``application/vnd.pypi.simple.v1+html``

In addition to the above, a special "meta" version is supported named ``latest``,
whose purpose is to allow clients to request the absolute latest version, without
having to know ahead of time what that version is. It is recommended however,
that clients be explicit about what versions they support.

To support existing clients which expect the existing :ref:`the base HTML API
specification <simple-repository-api-base>` API responses to
use the ``text/html`` content type, this spec further defines ``text/html`` as an alias
for the ``application/vnd.pypi.simple.v1+html`` content type.


Version + Format Selection
--------------------------

Now that there is multiple possible serializations, we need a mechanism to allow
clients to indicate what serialization formats they're able to understand. In
addition, it would be beneficial if any possible new major version to the API can
be added without disrupting existing clients expecting the previous API version.

To enable this, this spec standardizes on the use of HTTP's
`Server-Driven Content Negotiation <https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation>`_.

While this spec won't fully describe the entirety of server-driven content
negotiation, the flow is roughly:

1. The client makes an HTTP request containing an ``Accept`` header listing all
   of the version+format content types that they are able to understand.
2. The server inspects that header, selects one of the listed content types,
   then returns a response using that content type (treating the absence of
   an ``Accept`` header as ``Accept: */*``).
3. If the server does not support any of the content types in the ``Accept``
   header then they are able to choose between 3 different options for how to
   respond:

   a. Select a default content type other than what the client has requested
      and return a response with that.
   b. Return a HTTP ``406 Not Acceptable`` response to indicate that none of
      the requested content types were available, and the server was unable
      or unwilling to select a default content type to respond with.
   c. Return a HTTP ``300 Multiple Choices`` response that contains a list of
      all of the possible responses that could have been chosen.
4. The client interprets the response, handling the different types of responses
   that the server may have responded with.

This spec does not specify which choices the server makes in regards to handling
a content type that it isn't able to return, and clients **SHOULD** be prepared
to handle all of the possible responses in whatever way makes the most sense for
that client.

However, as there is no standard format for how a ``300 Multiple Choices``
response can be interpreted, this spec highly discourages servers from utilizing
that option, as clients will have no way to understand and select a different
content-type to request. In addition, it's unlikely that the client *could*
understand a different content type anyways, so at best this response would
likely just be treated the same as a ``406 Not Acceptable`` error.

This spec **does** require that if the meta version ``latest`` is being used, the
server **MUST** respond with the content type for the actual version that is
contained in the response
(i.e. an ``Accept: application/vnd.pypi.simple.latest+json`` request that returns
a ``v1.x`` response should have a ``Content-Type`` of
``application/vnd.pypi.simple.v1+json``).

The ``Accept`` header is a comma separated list of content types that the client
understands and is able to process. It supports three different formats for each
content type that is being requested:

- ``$type/$subtype``
- ``$type/*``
- ``*/*``

For the use of selecting a version+format, the most useful of these is
``$type/$subtype``, as that is the only way to actually specify the version
and format you want.

The order of the content types listed in the ``Accept`` header does not have any
specific meaning, and the server **SHOULD** consider all of them to be equally
valid to respond with. If a client wishes to specify that they prefer a specific
content type over another, they may use the ``Accept`` header's
`quality value <https://developer.mozilla.org/en-US/docs/Glossary/Quality_values>`_
syntax.

This allows a client to specify a priority for a specific entry in their
``Accept`` header, by appending a ``;q=`` followed by a value between ``0`` and
``1`` inclusive, with up to 3 decimal digits. When interpreting this value,
an entry with a higher quality has priority over an entry with a lower quality,
and any entry without a quality present will default to a quality of ``1``.

However, clients should keep in mind that a server is free to select **any** of
the content types they've asked for, regardless of their requested priority, and
it may even return a content type that they did **not** ask for.

To aid clients in determining the content type of the response that they have
received from an API request, this spec requires that servers always include a
``Content-Type`` header indicating the content type of the response. This is
technically a backwards incompatible change, however in practice
`pip has been enforcing this requirement <https://github.com/pypa/pip/blob/cf3696a81b341925f82f20cb527e656176987565/src/pip/_internal/index/collector.py#L123-L150>`_
so the risks for actual breakages is low.

An example of how a client can operate would look like:

.. code-block:: python

    import email.message
    import requests

    def parse_content_type(header: str) -> str:
        m = email.message.Message()
        m["content-type"] = header
        return m.get_content_type()

    # Construct our list of acceptable content types, we want to prefer
    # that we get a v1 response serialized using JSON, however we also
    # can support a v1 response serialized using HTML. For compatibility
    # we also request text/html, but we prefer it least of all since we
    # don't know if it's actually a Simple API response, or just some
    # random HTML page that we've gotten due to a misconfiguration.
    CONTENT_TYPES = [
        "application/vnd.pypi.simple.v1+json",
        "application/vnd.pypi.simple.v1+html;q=0.2",
        "text/html;q=0.01",  # For legacy compatibility
    ]
    ACCEPT = ", ".join(CONTENT_TYPES)


    # Actually make our request to the API, requesting all of the content
    # types that we find acceptable, and letting the server select one of
    # them out of the list.
    resp = requests.get("https://pypi.org/simple/", headers={"Accept": ACCEPT})

    # If the server does not support any of the content types you requested,
    # AND it has chosen to return a HTTP 406 error instead of a default
    # response then this will raise an exception for the 406 error.
    resp.raise_for_status()


    # Determine what kind of response we've gotten to ensure that it is one
    # that we can support, and if it is, dispatch to a function that will
    # understand how to interpret that particular version+serialization. If
    # we don't understand the content type we've gotten, then we'll raise
    # an exception.
    content_type = parse_content_type(resp.headers.get("content-type", ""))
    match content_type:
        case "application/vnd.pypi.simple.v1+json":
            handle_v1_json(resp)
        case "application/vnd.pypi.simple.v1+html" | "text/html":
            handle_v1_html(resp)
        case _:
            raise Exception(f"Unknown content type: {content_type}")

If a client wishes to only support HTML or only support JSON, then they would
just remove the content types that they do not want from the ``Accept`` header,
and turn receiving them into an error.


Alternative Negotiation Mechanisms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While using HTTP's Content negotiation is considered the standard way for a client
and server to coordinate to ensure that the client is getting an HTTP response that
it is able to understand, there are situations where that mechanism may not be
sufficient. For those cases this spec has alternative negotiation mechanisms that
may *optionally* be used instead.


URL Parameter
^^^^^^^^^^^^^

Servers that implement the Simple API may choose to support a URL parameter named
``format`` to allow the clients to request a specific version of the URL.

The value of the ``format`` parameter should be **one** of the valid content types.
Passing multiple content types, wild cards, quality values, etc... is **not**
supported.

Supporting this parameter is optional, and clients **SHOULD NOT** rely on it for
interacting with the API. This negotiation mechanism is intended to allow for easier
human based exploration of the API within a browser, or to allow documentation or
notes to link to a specific version+format.

Servers that do not support this parameter may choose to return an error when it is
present, or they may simple ignore its presence.

When a server does implement this parameter, it **SHOULD** take precedence over any
values in the client's ``Accept`` header, and if the server does not support the
requested format, it may choose to fall back to the ``Accept`` header, or choose any
of the error conditions that standard server-driven content negotiation typically
has (e.g. ``406 Not Available``, ``303 Multiple Choices``, or selecting a default
type to return).


Endpoint Configuration
^^^^^^^^^^^^^^^^^^^^^^

This option technically is not a special option at all, it is just a natural
consequence of using content negotiation and allowing servers to select which of the
available content types is their default.

If a server is unwilling or unable to implement the server-driven content negotiation,
and would instead rather require users to explicitly configure their client to select
the version they want, then that is a supported configuration.

To enable this, a server should make multiple endpoints (for instance,
``/simple/v1+html/`` and/or ``/simple/v1+json/``) for each version+format that they
wish to support. Under that endpoint, they can host a copy of their repository that
only supports one (or a subset) of the content-types. When a client makes a request
using the ``Accept`` header, the server can ignore it and return the content type
that corresponds to that endpoint.

For clients that wish to require specific configuration, they can keep track of
which version+format a specific repository URL was configured for, and when making
a request to that server, emit an ``Accept`` header that *only* includes the correct
content type.


TUF Support - PEP 458
---------------------

:pep:`458` requires that all API responses are hashable and that they can be uniquely
identified by a path relative to the repository root. For a Simple API repository, the
target path is the Root of our API (e.g. ``/simple/`` on PyPI). This creates
challenges when accessing the API using a TUF client instead of directly using a
standard HTTP client, as the TUF client cannot handle the fact that a target could
have multiple different representations that all hash differently.

:pep:`458` does not specify what the target path should be for the Simple API, but
TUF requires that the target paths be "file-like", in other words, a path like
``simple/PROJECT/`` is not acceptable, because it technically points to a
directory.

The saving grace is that the target path does not *have* to actually match the URL
being fetched from the Simple API, and it can just be a sigil that the fetching code
knows how to transform into the actual URL that needs to be fetched. This same thing
can hold true for other aspects of the actual HTTP request, such as the ``Accept``
header.

Ultimately figuring out how to map a directory to a filename is out of scope for this
spec (but it would be in scope for :pep:`458`), and this spec defers making a decision
about how exactly to represent this inside of :pep:`458` metadata.

However, it appears that the current WIP branch against pip that attempts to implement
:pep:`458` is using a target path like ``simple/PROJECT/index.html``. This could be
modified to include the API version and serialization format using something like
``simple/PROJECT/vnd.pypi.simple.vN.FORMAT``. So the v1 HTML format would be
``simple/PROJECT/vnd.pypi.simple.v1.html`` and the v1 JSON format would be
``simple/PROJECT/vnd.pypi.simple.v1.json``.

In this case, since ``text/html`` is an alias to ``application/vnd.pypi.simple.v1+html``
when interacting through TUF, it likely will make the most sense to normalize to the
more explicit name.

Likewise the ``latest`` metaversion should not be included in the targets, only
explicitly declared versions should be supported.

Recommendations
---------------

This section is non-normative, and represents what the spec authors believe to be
the best default implementation decisions for something implementing this spec, but
it does **not** represent any sort of requirement to match these decisions.

These decisions have been chosen to maximize the number of requests that can be
moved onto the newest version of an API, while maintaining the greatest amount
of compatibility. In addition, they've also tried to make using the API provide
guardrails that attempt to push clients into making the best choices it can.

It is recommended that servers:

- Support all 3 content types described in this spec, using server-driven
  content negotiation, for as long as they reasonably can, or at least as
  long as they're receiving non trivial traffic that uses the HTML responses.

- When encountering an ``Accept`` header that does not contain any content types
  that it knows how to work with, the server should not ever return a
  ``300 Multiple Choice`` response, and instead return a ``406 Not Acceptable``
  response.

  - However, if choosing to use the endpoint configuration, you should prefer to
    return a ``200 OK`` response in the expected content type for that endpoint.

- When selecting an acceptable version, the server should choose the highest version
  that the client supports, with the most expressive/featureful serialization format,
  taking into account the specificity of the client requests as well as any
  quality priority values they have expressed, and it should only use the
  ``text/html`` content type as a last resort.

It is recommended that clients:

- Support all 3 content types described in this spec, using server-driven
  content negotiation, for as long as they reasonably can.

- When constructing an ``Accept`` header, include all of the content types
  that you support.

  You should generally *not* include a quality priority value for your content
  types, unless you have implementation specific reasons that you want the
  server to take into account (for example, if you're using the standard library
  HTML parser and you're worried that there may be some kinds of HTML responses
  that you're unable to parse in some edge cases).

  The one exception to this recommendation is that it is recommended that you
  *should* include a ``;q=0.01`` value on the legacy ``text/html`` content type,
  unless it is the only content type that you are requesting.

- Explicitly select what versions they are looking for, rather than using the
  ``latest`` meta version during normal operation.

- Check the ``Content-Type`` of the response and ensure it matches something
  that you were expecting.

Additional Fields for the Simple API for Package Indexes
========================================================

This specification defines version 1.1 of the simple repository API. For the
HTML version of the API, there is no change from version 1.0. For the JSON
version of the API, the following changes are made:

- The ``api-version`` must specify version 1.1 or later.
- A new ``versions`` key is added at the top level.
- Two new "file information" keys, ``size`` and ``upload-time``, are added to
  the ``files`` data.
- Keys (at any level) with a leading underscore are reserved as private for
  index server use. No future standard will assign a meaning to any such key.

The ``versions`` and ``size`` keys are mandatory. The ``upload-time`` key is
optional.

Versions
--------

An additional key, ``versions`` MUST be present at the top level, in addition to
the keys ``name``, ``files`` and ``meta`` defined in :ref:`the JSON API
specification <simple-repository-api-json>`. This key MUST
contain a list of version strings specifying all of the project versions uploaded
for this project. The value is logically a set, and as such may not contain
duplicates, and the order of the values is not significant.

All of the files listed in the ``files`` key MUST be associated with one of the
versions in the ``versions`` key. The ``versions`` key MAY contain versions with
no associated files (to represent versions with no files uploaded, if the server
has such a concept).

Note that because servers may hold "legacy" data from before the adoption of
:ref:`the version specifiers specification (VSS) <version-specifiers>`, version
strings currently cannot be required to be valid VSS versions, and therefore
cannot be assumed to be orderable using the VSS rules. However, servers SHOULD
use normalised VSS versions where
possible.


Additional file information
---------------------------

Two new keys are added to the ``files`` key.

- ``size``: This field is mandatory. It MUST contain an integer which is the
  file size in bytes.
- ``upload-time``: This field is optional. If present, it MUST contain a valid
  ISO 8601 date/time string, in the format ``yyyy-mm-ddThh:mm:ss.ffffffZ``,
  which represents the time the file was uploaded to the index. As indicated by
  the ``Z`` suffix, the upload time MUST use the UTC timezone. The fractional
  seconds part of the timestamp (the ``.ffffff`` part) is optional, and if
  present may contain up to 6 digits of precision. If a server does not record
  upload time information for a file, it MAY omit the ``upload-time`` key.

Rename dist-info-metadata in the Simple API
===========================================


The keywords "**MUST**", "**MUST NOT**", "**REQUIRED**", "**SHALL**",
"**SHALL NOT**", "**SHOULD**", "**SHOULD NOT**", "**RECOMMENDED**", "**MAY**",
and "**OPTIONAL**"" in this document are to be interpreted as described in
:rfc:`RFC 2119 <2119>`.


Servers
-------

The :ref:`the API metadata file specification
<simple-repository-api-metadata-file>` metadata, when used in the HTML
representation of the Simple API,
**MUST** be emitted using the attribute name ``data-core-metadata``, with the
supported values remaining the same.

The :ref:`the API metadata file specification
<simple-repository-api-metadata-file>` metadata, when used in the :ref:`the
JSON API specification <simple-repository-api-base>` JSON representation of the
Simple API, **MUST** be emitted using the key ``core-metadata``, with the
supported values remaining the same.

To support clients that used the previous key names, the HTML representation
**MAY** also be emitted using the ``data-dist-info-metadata``, and if it does
so it **MUST** match the value of ``data-core-metadata``.



Clients
-------

Clients consuming any of the HTML representations of the Simple API **MUST**
read the :ref:`the API metadata file specification
<simple-repository-api-metadata-file>` metadata from the key
``data-core-metadata`` if it is
present. They **MAY** optionally use the legacy ``data-dist-info-metadata`` if
it is present but ``data-core-metadata`` is not.

Clients consuming the JSON representation of the Simple API **MUST** read the
:ref:`the API metadata file specification
<simple-repository-api-metadata-file>` metadata from the key ``core-metadata``
if it is present. They
**MAY** optionally use the legacy ``dist-info-metadata`` key if it is present
but ``core-metadata`` is not.

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
