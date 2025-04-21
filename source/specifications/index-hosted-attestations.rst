
.. _index-hosted-attestations:

=========================
Index hosted attestations
=========================

.. note:: This specification was originally defined in :pep:`740`.

.. note::

    :pep:`740` includes changes to the HTML and JSON index APIs.
    These changes are documented in the :ref:`simple-repository-api`
    under :ref:`simple-repository-api-base` and :ref:`json-serialization`.

Specification
=============

.. _upload-endpoint:

Upload endpoint changes
-----------------------

.. important::

    The "legacy" upload API is not standardized.
    See `PyPI's Upload API documentation <https://docs.pypi.org/api/upload/>`_
    for how attestations are uploaded.

.. _attestation-object:

Attestation objects
-------------------

An attestation object is a JSON object with several required keys; applications
or signers may include additional keys so long as all explicitly
listed keys are provided. The required layout of an attestation
object is provided as pseudocode below.

.. code-block:: python

  @dataclass
  class Attestation:
      version: Literal[1]
      """
      The attestation object's version, which is always 1.
      """

      verification_material: VerificationMaterial
      """
      Cryptographic materials used to verify `envelope`.
      """

      envelope: Envelope
      """
      The enveloped attestation statement and signature.
      """


  @dataclass
  class Envelope:
      statement: bytes
      """
      The attestation statement.

      This is represented as opaque bytes on the wire (encoded as base64),
      but it MUST be an JSON in-toto v1 Statement.
      """

      signature: bytes
      """
      A signature for the above statement, encoded as base64.
      """

  @dataclass
  class VerificationMaterial:
      certificate: str
      """
      The signing certificate, as `base64(DER(cert))`.
      """

      transparency_entries: list[object]
      """
      One or more transparency log entries for this attestation's signature
      and certificate.
      """

A full data model for each object in ``transparency_entries`` is provided in
:ref:`appendix`. Attestation objects **SHOULD** include one or more
transparency log entries, and **MAY** include additional keys for other
sources of signed time (such as an :rfc:`3161` Time Stamping Authority or a
`Roughtime <https://blog.cloudflare.com/roughtime>`__ server).

Attestation objects are versioned; this PEP specifies version 1. Each version
is tied to a single cryptographic suite to minimize unnecessary cryptographic
agility. In version 1, the suite is as follows:

* Certificates are specified as X.509 certificates, and comply with the
  profile in :rfc:`5280`.
* The message signature algorithm is ECDSA, with the P-256 curve for public keys
  and SHA-256 as the cryptographic digest function.

Future PEPs may change this suite (and the overall shape of the attestation
object) by selecting a new version number.

.. _payload-and-signature-generation:

Attestation statement and signature generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *attestation statement* is the actual claim that is cryptographically signed
over within the attestation object (i.e., the ``envelope.statement``).

The attestation statement is encoded as a
`v1 in-toto Statement object <https://github.com/in-toto/attestation/blob/v1.0/spec/v1.0/statement.md>`__,
in JSON form. When serialized the statement is treated as an opaque binary blob,
avoiding the need for canonicalization.

In addition to being a v1 in-toto Statement, the attestation statement is constrained
in the following ways:

* The in-toto ``subject`` **MUST** contain only a single subject.
* ``subject[0].name`` is the distribution's filename, which **MUST** be
  a valid :ref:`source distribution <source-distribution-format>` or
  :ref:`wheel distribution <binary-distribution-format>` filename.
* ``subject[0].digest`` **MUST** contain a SHA-256 digest. Other digests
  **MAY** be present. The digests **MUST** be represented as hexadecimal strings.
* The following ``predicateType`` values are supported:

  * `SLSA Provenance <https://slsa.dev/provenance/v1>`__: ``https://slsa.dev/provenance/v1``
  * `PyPI Publish Attestation <https://docs.pypi.org/attestations/publish/v1>`__: ``https://docs.pypi.org/attestations/publish/v1``

The signature over this statement is constructed using the
`v1 DSSE signature protocol <https://github.com/secure-systems-lab/dsse/blob/v1.0.0/protocol.md>`__,
with a ``PAYLOAD_TYPE`` of ``application/vnd.in-toto+json`` and a ``PAYLOAD_BODY`` of the JSON-encoded
statement above. No other ``PAYLOAD_TYPE`` is permitted.

.. _provenance-object:

Provenance objects
------------------

The index will serve uploaded attestations along with metadata that can assist
in verifying them in the form of JSON serialized objects.

These *provenance objects* will be available via both the Simple Index
and JSON-based Simple API as described above, and will have the following layout:

.. code-block:: json

    {
        "version": 1,
        "attestation_bundles": [
          {
            "publisher": {
              "kind": "important-ci-service",
              "claims": {},
              "vendor-property": "foo",
              "another-property": 123
            },
            "attestations": [
              { /* attestation 1 ... */ },
              { /* attestation 2 ... */ }
            ]
          }
        ]
    }

or, as pseudocode:

.. code-block:: python

  @dataclass
  class Publisher:
      kind: string
      """
      The kind of Trusted Publisher.
      """

      claims: object | None
      """
      Any context-specific claims retained by the index during Trusted Publisher
      authentication.
      """

      _rest: object
      """
      Each publisher object is open-ended, meaning that it MAY contain additional
      fields beyond the ones specified explicitly above. This field signals that,
      but is not itself present.
      """

  @dataclass
  class AttestationBundle:
      publisher: Publisher
      """
      The publisher associated with this set of attestations.
      """

      attestations: list[Attestation]
      """
      The set of attestations included in this bundle.
      """

  @dataclass
  class Provenance:
      version: Literal[1]
      """
      The provenance object's version, which is always 1.
      """

      attestation_bundles: list[AttestationBundle]
      """
      One or more attestation "bundles".
      """

* ``version`` is ``1``. Like attestation objects, provenance objects are
  versioned, and this PEP only defines version ``1``.
* ``attestation_bundles`` is a **required** JSON array, containing one
  or more "bundles" of attestations. Each bundle corresponds to a
  signing identity (such as a Trusted Publishing identity), and contains
  one or more attestation objects.

  As noted in the ``Publisher`` model,
  each ``AttestationBundle.publisher`` object is specific to its Trusted Publisher
  but must include at minimum:

  * A ``kind`` key, which **MUST** be a JSON string that uniquely identifies the
    kind of Trusted Publisher.
  * A ``claims`` key, which **MUST** be a JSON object containing any context-specific
    claims retained by the index during Trusted Publisher authentication.

  All other keys in the publisher object are publisher-specific.

  Each array of attestation objects is a superset of the ``attestations``
  array supplied by the uploaded through the ``attestations`` field at upload
  time, as described in :ref:`upload-endpoint` and
  :ref:`changes-to-provenance-objects`.

.. _changes-to-provenance-objects:

Changes to provenance objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provenance objects are *not* immutable, and may change over time. Reasons
for changes to the provenance object include but are not limited to:

* Addition of new attestations for a pre-existing signing identity: the index
  **MAY** choose to allow additional attestations by pre-existing signing
  identities, such as newer attestation versions for already uploaded
  files.

* Addition of new signing identities and associated attestations: the index
  **MAY** choose to support attestations from sources other than the file's
  uploader, such as third-party auditors or the index itself. These attestations
  may be performed asynchronously, requiring the index to insert them into
  the provenance object *post facto*.

.. _attestation-verification:

Attestation verification
------------------------

Verifying an attestation object against a distribution file requires verification of each of the
following:

* ``version`` is ``1``. The verifier **MUST** reject any other version.
* ``verification_material.certificate`` is a valid signing certificate, as
  issued by an *a priori* trusted authority (such as a root of trust already
  present within the verifying client).
* ``verification_material.certificate`` identifies an appropriate signing
  subject, such as the machine identity of the Trusted Publisher that published
  the package.
* ``envelope.statement`` is a valid in-toto v1 Statement, with a subject
  and digest that **MUST** match the distribution's filename and contents.
  For the distribution's filename, matching **MUST** be performed by parsing
  using the appropriate source distribution or wheel filename format, as
  the statement's subject may be equivalent but normalized.
* ``envelope.signature`` is a valid signature for ``envelope.statement``
  corresponding to ``verification_material.certificate``,
  as reconstituted via the
  `v1 DSSE signature protocol <https://github.com/secure-systems-lab/dsse/blob/v1.0.0/protocol.md>`__.

In addition to the above required steps, a verifier **MAY** additionally verify
``verification_material.transparency_entries`` on a policy basis, e.g. requiring
at least one transparency log entry or a threshold of entries. When verifying
transparency entries, the verifier **MUST** confirm that the inclusion time for
each entry lies within the signing certificate's validity period.

.. _appendix:

Appendix: Data models for Transparency Log Entries
====================================================

This appendix contains pseudocoded data models for transparency log entries
in attestation objects. Each transparency log entry serves as a source
of signed inclusion time, and can be verified either online or offline.

.. code-block:: python

  @dataclass
  class TransparencyLogEntry:
      log_index: int
      """
      The global index of the log entry, used when querying the log.
      """

      log_id: str
      """
      An opaque, unique identifier for the log.
      """

      entry_kind: str
      """
      The kind (type) of log entry.
      """

      entry_version: str
      """
      The version of the log entry's submitted format.
      """

      integrated_time: int
      """
      The UNIX timestamp from the log from when the entry was persisted.
      """

      inclusion_proof: InclusionProof
      """
      The actual inclusion proof of the log entry.
      """


  @dataclass
  class InclusionProof:
      log_index: int
      """
      The index of the entry in the tree it was written to.
      """

      root_hash: str
      """
      The digest stored at the root of the Merkle tree at the time of proof
      generation.
      """

      tree_size: int
      """
      The size of the Merkle tree at the time of proof generation.
      """

      hashes: list[str]
      """
      A list of hashes required to complete the inclusion proof, sorted
      in order from leaf to root. The leaf and root hashes are not themselves
      included in this list; the root is supplied via `root_hash` and the client
      must calculate the leaf hash.
      """

      checkpoint: str
      """
      The signed tree head's signature, at the time of proof generation.
      """

      cosigned_checkpoints: list[str]
      """
      Cosigned checkpoints from zero or more log witnesses.
      """
