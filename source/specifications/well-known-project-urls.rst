.. _`well-known-project-urls`:

===================================
Well-known Project URLs in Metadata
===================================

.. important::

    This document is primarily of interest to metadata *consumers*,
    who should use the normalization rules and well-known list below
    to make their presentation of project URLs consistent across the
    Python ecosystem.

    Metadata *producers* (such as build tools and individual package
    maintainers) may continue to use any labels they please, within the
    overall ``Project-URL`` length restrictions. However, when possible, users are
    *encouraged* to pick meaningful labels that normalize to well-known
    labels.

.. note::

    See :ref:`Writing your pyproject.toml - urls <writing-pyproject-toml-urls>`
    for user-oriented guidance on choosing project URL labels in your package's
    metadata.

.. note:: This specification was originally defined in :pep:`753`.

:pep:`753` deprecates the :ref:`core-metadata-home-page` and
:ref:`core-metadata-download-url` metadata fields in favor of
:ref:`core-metadata-project-url`, and defines a normalization and
lookup procedure for determining whether a ``Project-URL`` is
"well-known," i.e. has the semantics assigned to ``Home-page``,
``Download-URL``, or other common project URLs.

This allows indices (such as the Python Package Index) and other downstream
metadata consumers to present project URLs in a
consistent manner.

.. _project-url-label-normalization:

Label normalization
===================

.. note::

    Label normalization is performed by metadata *consumers*, not metadata
    producers.

To determine whether a ``Project-URL`` label is "well-known," metadata
consumers should normalize the label before comparing it to the
:ref:`list of well-known labels <well-known-labels>`.

The normalization procedure for ``Project-URL`` labels is defined
by the following Python function:

.. code-block:: python

    import string

    def normalize_label(label: str) -> str:
        chars_to_remove = string.punctuation + string.whitespace
        removal_map = str.maketrans("", "", chars_to_remove)
        return label.translate(removal_map).lower()

In plain language: a label is *normalized* by deleting all ASCII punctuation
and whitespace, and then converting the result to lowercase.

The following table shows examples of labels before (raw) and after
normalization:

.. list-table::
    :header-rows: 1

    * - Raw
      - Normalized
    * - ``Homepage``
      - ``homepage``
    * - ``Home-page``
      - ``homepage``
    * - ``Home page``
      - ``homepage``
    * - ``Change_Log``
      - ``changelog``
    * - ``What's New?``
      - ``whatsnew``
    * - ``github``
      - ``github``

.. _well-known-labels:

Well-known labels
=================

.. note::

    The list of well-known labels is a living standard, maintained as part of
    this document.

The following table lists labels that are well-known for the purpose of
specializing the presentation of ``Project-URL`` metadata:

.. list-table::
   :header-rows: 1

   * - Label (Human-readable equivalent)
     - Description
     - Aliases
   * - ``homepage`` (Homepage)
     - The project's home page
     - *(none)*
   * - ``source`` (Source Code)
     - The project's hosted source code or repository
     - ``repository``, ``sourcecode``, ``github``
   * - ``download`` (Download)
     - A download URL for the current distribution, equivalent to ``Download-URL``
     - *(none)*
   * - ``changelog`` (Changelog)
     - The project's comprehensive changelog
     - ``changes``, ``whatsnew``, ``history``
   * - ``releasenotes`` (Release Notes)
     - The project's curated release notes
     - *(none)*
   * - ``documentation`` (Documentation)
     - The project's online documentation
     - ``docs``
   * - ``issues`` (Issue Tracker)
     - The project's bug tracker
     - ``bugs``, ``issue``, ``tracker``, ``issuetracker``, ``bugtracker``
   * - ``funding`` (Funding)
     - Funding Information
     - ``sponsor``, ``donate``, ``donation``

Package metadata consumers may choose to render aliased labels the same as
their "parent" well known label, or further specialize them.

Example behavior
================

The following shows the flow of project URL metadata from
``pyproject.toml`` to core metadata to a potential index presentation:

.. code-block:: toml
    :caption: Example project URLs in standard configuration

    [project.urls]
    "Home Page" = "https://example.com"
    DOCUMENTATION = "https://readthedocs.org"
    Repository = "https://upstream.example.com/me/spam.git"
    GitHub = "https://github.com/example/spam"

.. code-block:: email
    :caption: Core metadata representation

    Project-URL: Home page, https://example.com
    Project-URL: DOCUMENTATION, https://readthedocs.org
    Project-URL: Repository, https://upstream.example.com/me/spam.git
    Project-URL: GitHub, https://github.com/example/spam

.. code-block:: text
    :caption: Potential rendering

    Homepage: https://example.com
    Documentation: https://readthedocs.org
    Source Code: https://upstream.example.com/me/spam.git
    Source Code (GitHub): https://github.com/example/spam

Observe that the core metadata appears in the form provided by the user
(since metadata *producers* do not perform normalization), but the
metadata *consumer* normalizes and identifies appropriate
human-readable equivalents based on the normalized form:

* ``Home page`` becomes ``homepage``, which is rendered as ``Homepage``
* ``DOCUMENTATION`` becomes ``documentation``, which is rendered as ``Documentation``
* ``Repository`` becomes ``repository``, which is rendered as ``Source Code``
* ``GitHub`` becomes ``github``, which is rendered as ``Source Code (GitHub)``
  (as a specialization of ``Source Code``)
