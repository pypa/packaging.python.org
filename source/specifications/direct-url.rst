
.. _direct-url:

==========================================================
Recording the Direct URL Origin of installed distributions
==========================================================

This document specifies a :file:`direct_url.json` file in the
:file:`*.dist-info` directory of an installed distribution, to record the
Direct URL Origin of the distribution.

.. contents:: Contents
   :local:

Specification
=============

The :file:`direct_url.json` file MUST be created in the :file:`*.dist-info`
directory by installers when installing a distribution from a requirement
specifying a direct URL reference (including a VCS URL).

This file MUST NOT be created when installing a distribution from an other
type of requirement (i.e. name plus version specifier).

This JSON file MUST be a UTF-8 encoded, :rfc:`8259` compliant, serialization of the
:doc:`direct-url-data-structure`.

.. note::

  When the requested URL has the file:// scheme and points to a local directory that happens to contain a
  VCS checkout, installers MUST NOT attempt to infer any VCS information and
  therefore MUST NOT output any VCS related information (such as ``vcs_info``)
  in :file:`direct_url.json`.

.. note::

   As a general rule, installers should as much as possible preserve the
   information that was provided in the requested URL when generating
   :file:`direct_url.json`. For example user:password environment variables
   should be preserved and ``requested_revision`` should reflect the revision that was
   provided in the requested URL as faithfully as possible. This information is
   however *enriched* with more precise data, such as ``commit_id``.


Example pip commands and their effect on direct_url.json
========================================================

Commands that generate a ``direct_url.json``:

* ``pip install https://example.com/app-1.0.tgz``
* ``pip install https://example.com/app-1.0.whl``
* ``pip install "git+https://example.com/repo/app.git#egg=app&subdirectory=setup"``
* ``pip install ./app``
* ``pip install file:///home/user/app``
* ``pip install --editable "git+https://example.com/repo/app.git#egg=app&subdirectory=setup"``
  (in which case, ``url`` will be the local directory where the git repository has been
  cloned to, and ``dir_info`` will be present with ``"editable": true`` and no
  ``vcs_info`` will be set)
* ``pip install -e ./app``

Commands that *do not* generate a ``direct_url.json``

* ``pip install app``
* ``pip install app --no-index --find-links https://example.com/``

History
=======

``direct_url.json`` was originally specified in :pep:`610` and is formally documented
here.
