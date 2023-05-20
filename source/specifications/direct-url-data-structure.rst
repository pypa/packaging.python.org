
.. _direct-url-data-structure:

=========================
Direct URL Data Structure
=========================

This document specifies a JSON-serializable abstract data structure that can represent
URLs to python projects and distribution artifacts such as VCS source trees, local
source trees, source distributions and wheels.

The representation of the components of this data structure as a :rfc:`1738` URL
is not formally specified at time of writing. A common representation is the pip URL
format. Other examples are provided in :pep:`440`.

.. contents:: Contents
   :local:

Specification
=============

The Direct URL Data Structure MUST be a dictionary, serializable to JSON according to
:rfc:`8259`.

It MUST contain at least two fields. The first one is ``url``, with
type ``string``. Depending on what ``url`` refers to, the second field MUST be
one of ``vcs_info`` (if ``url`` is a VCS reference), ``archive_info`` (if
``url`` is a source archives or a wheel), or ``dir_info`` (if ``url``  is a
local directory). These info fields have a (possibly empty) subdictionary as
value, with the possible keys defined below.

When persisted, ``url`` MUST be stripped of any sensitive authentication information,
for security reasons.

The user:password section of the URL MAY however
be composed of environment variables, matching the following regular
expression::

    \$\{[A-Za-z0-9-_]+\}(:\$\{[A-Za-z0-9-_]+\})?

Additionally, the user:password section of the URL MAY be a
well-known, non security sensitive string. A typical example is ``git``
in the case of an URL such as ``ssh://git@gitlab.com/user/repo``.

VCS URLs
--------

When ``url`` refers to a VCS repository, the ``vcs_info`` key MUST be present
as a dictionary with the following keys:

- A ``vcs`` key (type ``string``) MUST be present, containing the name of the VCS
  (i.e. one of ``git``, ``hg``, ``bzr``, ``svn``). Other VCS's SHOULD be registered by
  writing a PEP to amend this specification.
  The ``url`` value MUST be compatible with the corresponding VCS,
  so an installer can hand it off without transformation to a
  checkout/download command of the VCS.
- A ``requested_revision`` key (type ``string``) MAY be present naming a
  branch/tag/ref/commit/revision/etc (in a format compatible with the VCS).
- A ``commit_id`` key (type ``string``) MUST be present, containing the
  exact commit/revision number that was/is to be installed.
  If the VCS supports commit-hash
  based revision identifiers, such commit-hash MUST be used as
  ``commit_id`` in order to reference an immutable
  version of the source code.

Archive URLs
------------

When ``url`` refers to a source archive or a wheel, the ``archive_info`` key
MUST be present as a dictionary with the following keys:

- A ``hashes`` key SHOULD be present as a dictionary mapping a hash name to a hex
  encoded digest of the file. 
  
  Multiple hashes can be included, and it is up to the consumer to decide what to do
  with multiple hashes (it may validate all of them or a subset of them, or nothing at
  all). 
  
  These hash names SHOULD always be normalized to be lowercase. 
  
  Any hash algorithm available via ``hashlib`` (specifically any that can be passed to
  ``hashlib.new()`` and do not require additional parameters) can be used as a key for
  the hashes dictionary. At least one secure algorithm from
  ``hashlib.algorithms_guaranteed`` SHOULD always be included. At time of writing,
  ``sha256`` specifically is recommended.
  
- A deprecated ``hash`` key (type ``string``) MAY be present for backwards compatibility
  purposes, with value ``<hash-algorithm>=<expected-hash>``.

Producers of the data structure SHOULD emit the ``hashes`` key whether one or multiple
hashes are available. Producers SHOULD continue to emit the ``hash`` key in contexts
where they did so before, so as to keep backwards compatibility for existing clients.

When both the ``hash`` and ``hashes`` keys are present, the hash represented in the
``hash`` key MUST also be present in the ``hashes`` dictionary, so consumers can
consider the ``hashes`` key only if it is present, and fall back to ``hash`` otherwise.

Local directories
-----------------

When ``url`` refers to a local directory, the ``dir_info`` key MUST be
present as a dictionary with the following key:

- ``editable`` (type: ``boolean``): ``true`` if the distribution was/is to be installed
  in editable mode, ``false`` otherwise. If absent, default to ``false``.

When ``url`` refers to a local directory, it MUST have the ``file`` scheme and
be compliant with :rfc:`8089`. In
particular, the path component must be absolute. Symbolic links SHOULD be
preserved when making relative paths absolute.

Projects in subdirectories
--------------------------

A top-level ``subdirectory`` field MAY be present containing a directory path,
relative to the root of the VCS repository, source archive or local directory,
to specify where ``pyproject.toml`` or ``setup.py`` is located.

Registered VCS
==============

This section lists the registered VCS's; expanded, VCS-specific information
on how to use the ``vcs``, ``requested_revision``, and other fields of
``vcs_info``; and in
some cases additional VCS-specific fields.
Tools MAY support other VCS's although it is RECOMMENDED to register
them by writing a PEP to amend this specification. The ``vcs`` field SHOULD be the command name
(lowercased). Additional fields that would be necessary to
support such VCS SHOULD be prefixed with the VCS command name.

Git
---

Home page

   https://git-scm.com/

vcs command

   git

``vcs`` field

   git

``requested_revision`` field

   A tag name, branch name, Git ref, commit hash, shortened commit hash,
   or other commit-ish.

``commit_id`` field

   A commit hash (40 hexadecimal characters sha1).

.. note::

   Tools can use the ``git show-ref`` and ``git symbolic-ref`` commands
   to determine if the ``requested_revision`` corresponds to a Git ref.
   In turn, a ref beginning with ``refs/tags/`` corresponds to a tag, and
   a ref beginning with ``refs/remotes/origin/`` after cloning corresponds
   to a branch.

Mercurial
---------

Home page

   https://www.mercurial-scm.org/

vcs command

   hg

``vcs`` field

   hg

``requested_revision`` field

   A tag name, branch name, changeset ID, shortened changeset ID.

``commit_id`` field

   A changeset ID (40 hexadecimal characters).

Bazaar
------

Home page

   _`https://bazaar.canonical.com` *(Not responding as of 5/2023)*

vcs command

   bzr

``vcs`` field

   bzr

``requested_revision`` field

   A tag name, branch name, revision id.

``commit_id`` field

   A revision id.

Subversion
----------

Home page

   https://subversion.apache.org/

vcs command

   svn

``vcs`` field

   svn

``requested_revision`` field

   ``requested_revision`` must be compatible with ``svn checkout`` ``--revision`` option.
   In Subversion, branch or tag is part of ``url``.

``commit_id`` field

   Since Subversion does not support globally unique identifiers,
   this field is the Subversion revision number in the corresponding
   repository.

Examples
========

Source archive:

.. code::

    {
        "url": "https://github.com/pypa/pip/archive/1.3.1.zip",
        "archive_info": {
            "hashes": {
                "sha256": "2dc6b5a470a1bde68946f263f1af1515a2574a150a30d6ce02c6ff742fcc0db8"
            }
        }
    }

Git URL with tag and commit-hash:

.. code::

    {
        "url": "https://github.com/pypa/pip.git",
        "vcs_info": {
            "vcs": "git",
            "requested_revision": "1.3.1",
            "commit_id": "7921be1537eac1e97bc40179a57f0349c2aee67d"
        }
    }

Local directory:

.. code::

   {
       "url": "file:///home/user/project",
       "dir_info": {}
   }

Local directory in editable mode:

.. code::

   {
       "url": "file:///home/user/project",
       "dir_info": {
           "editable": true
       }
   }

History
=======

- March 2020: this data structure was originally specified as part of the
  ``direct_url.json`` metadata file in :pep:`610` and is formally documented here.
- January 2023: Added the ``archive_info.hashes`` key
  ([discussion](https://discuss.python.org/t/22299)).
