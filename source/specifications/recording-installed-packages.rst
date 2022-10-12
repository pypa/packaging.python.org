.. _recording-installed-packages:

============================
Recording installed projects
============================

This document specifies a common format of recording information
about Python :term:`projects <Project>` installed in an environment.
A common metadata format allows tools to query, manage or uninstall projects,
regardless of how they were installed.

Almost all information is optional.
This allows tools outside the Python ecosystem, such as Linux package managers,
to integrate with Python tooling as much as possible.
For example, even if an installer cannot easily provide a list of installed
files in a format specific to Python tooling, it should still record the name
and version of the installed project.


History and change workflow
===========================

The metadata described here was first specified in :pep:`376`, and later
amended in :pep:`627`.
It was formerly known as *Database of Installed Python Distributions*.
Further amendments (except trivial language or typography fixes) must be made
through the PEP process (see :pep:`1`).

While this document is the normative specification, these PEPs that introduce
changes to it may include additional information such as rationales and
backwards compatibility considerations.


The .dist-info directory
========================

Each project installed from a distribution must, in addition to files,
install a "``.dist-info``" directory located alongside importable modules and
packages (commonly, the ``site-packages`` directory).

This directory is named as ``{name}-{version}.dist-info``, with ``name`` and
``version`` fields corresponding to :ref:`core-metadata`. Both fields must be
normalized (see :pep:`PEP 503 <503#normalized-names>` and
:pep:`PEP 440 <440#normalization>` for the definition of normalization for
each field respectively), and replace dash (``-``) characters with
underscore (``_``) characters, so the ``.dist-info`` directory always has
exactly one dash (``-``) character in its stem, separating the ``name`` and
``version`` fields.

Historically, tools have failed to replace dot characters or normalize case in
the ``name`` field, or not perform normalization in the ``version`` field.
Tools consuming ``.dist-info`` directories should expect those fields to be
unnormalized, and treat them as equivalent to their normalized counterparts.
New tools that write ``.dist-info`` directories MUST normalize both ``name``
and ``version`` fields using the rules described above, and existing tools are
encouraged to start normalizing those fields.

.. note::

    The ``.dist-info`` directory's name is formatted to unambigiously represent
    a distribution as a filesystem path. Tools presenting a distribution name
    to a user should avoid using the normalized name, and instead present the
    specified name (when needed prior to resolution to an installed package),
    or read the respective fields in Core Metadata, since values listed there
    are unescaped and accurately reflect the distribution. Libraries should
    provide API for such tools to consume, so tools can have access to the
    unnormalized name when displaying distrubution information.

This ``.dist-info`` directory can contain these files, described in detail
below:

* ``METADATA``: contains project metadata
* ``RECORD``: records the list of installed files.
* ``INSTALLER``: records the name of the tool used to install the project.

The ``METADATA`` file is mandatory.
All other files may be omitted at the installing tool's discretion.
Additional installer-specific files may be present.

.. note::

   The :ref:`binary-distribution-format` specification describes additional
   files that may appear in the ``.dist-info`` directory of a :term:`Wheel`.
   Such files may be copied to the ``.dist-info`` directory of an
   installed project.

The previous versions of this specification also specified a ``REQUESTED``
file. This file is now considered a tool-specific extension, but may be
standardized again in the future. See `PEP 376 <https://www.python.org/dev/peps/pep-0376/#requested>`_
for its original meaning.


The METADATA file
=================

The ``METADATA`` file contains metadata as described in the :ref:`core-metadata`
specification, version 1.1 or greater.

The ``METADATA`` file is mandatory.
If it cannot be created, or if required core metadata is not available,
installers must report an error and fail to install the project.


The RECORD file
===============

The ``RECORD`` file holds the list of installed files.
It is a CSV file containing one record (line) per installed file.

The CSV dialect must be readable with the default ``reader`` of Python's
``csv`` module:

* field delimiter: ``,`` (comma),
* quoting char: ``"`` (straight double quote),
* line terminator: either ``\r\n`` or ``\n``.

Each record is composed of three elements: the file's **path**, the **hash**
of the contents, and its **size**.

The *path* may be either absolute, or relative to the directory containing
the ``.dist-info`` directory (commonly, the ``site-packages`` directory).
On Windows, directories may be separated either by forward- or backslashes
(``/`` or ``\``).

The *hash* is either an empty string or the name of a hash algorithm from
``hashlib.algorithms_guaranteed``, followed by the equals character ``=`` and
the digest of the file's contents, encoded with the urlsafe-base64-nopad
encoding (``base64.urlsafe_b64encode(digest)`` with trailing ``=`` removed).

The *size* is either the empty string, or file's size in bytes,
as a base 10 integer.

For any file, either or both of the *hash* and *size* fields may be left empty.
Commonly, entries for ``.pyc`` files and the ``RECORD`` file itself have empty
*hash* and *size*.
For other files, leaving the information out is discouraged, as it
prevents verifying the integrity of the installed project.

If the ``RECORD`` file is present, it must list all installed files of the
project, except ``.pyc`` files corresponding to ``.py`` files listed in
``RECORD``, which are optional.
Notably, the contents of the ``.dist-info`` directory (including the ``RECORD``
file itself) must be listed.
Directories should not be listed.

To completely uninstall a package, a tool needs to remove all
files listed in ``RECORD``, all ``.pyc`` files (of all optimization levels)
corresponding to removed ``.py`` files, and any directories emptied by
the uninstallation.

Here is an example snippet of a possible ``RECORD`` file::

    /usr/bin/black,sha256=iFlOnL32lIa-RKk-MDihcbJ37wxmRbE4xk6eVYVTTeU,220
    ../../../bin/blackd,sha256=lCadt4mcU-B67O1gkQVh7-vsKgLpx6ny1le34Jz6UVo,221
    __pycache__/black.cpython-38.pyc,,
    __pycache__/blackd.cpython-38.pyc,,
    black-19.10b0.dist-info/INSTALLER,sha256=zuuue4knoyJ-UwPPXg8fezS7VCrXJQrAP7zeNuwvFQg,4
    black-19.10b0.dist-info/LICENSE,sha256=nAQo8MO0d5hQz1vZbhGqqK_HLUqG1KNiI9erouWNbgA,1080
    black-19.10b0.dist-info/METADATA,sha256=UN40nGoVVTSpvLrTBwNsXgZdZIwoKFSrrDDHP6B7-A0,58841
    black-19.10b0.dist-info/RECORD,,
    black.py,sha256=45IF72OgNfF8WpeNHnxV2QGfbCLubV5Xjl55cI65kYs,140161
    blackd.py,sha256=JCxaK4hLkMRwVfZMj8FRpRRYC0172-juKqbN22bISLE,6672
    blib2to3/__init__.py,sha256=9_8wL9Scv8_Cs8HJyJHGvx1vwXErsuvlsAqNZLcJQR0,8
    blib2to3/__pycache__/__init__.cpython-38.pyc,,
    blib2to3/__pycache__/pygram.cpython-38.pyc,sha256=zpXgX4FHDuoeIQKO_v0sRsB-RzQFsuoKoBYvraAdoJw,1512
    blib2to3/__pycache__/pytree.cpython-38.pyc,sha256=LYLplXtG578ZjaFeoVuoX8rmxHn-BMAamCOsJMU1b9I,24910
    blib2to3/pygram.py,sha256=mXpQPqHcamFwch0RkyJsb92Wd0kUP3TW7d-u9dWhCGY,2085
    blib2to3/pytree.py,sha256=RWj3IL4U-Ljhkn4laN0C3p7IRdfvT3aIRjTV-x9hK1c,28530

If the ``RECORD`` file is missing, tools that rely on ``.dist-info`` must not
attempt to uninstall or upgrade the package.
(This does not apply to tools that rely on other sources of information,
such as system package managers in Linux distros.)


The INSTALLER file
==================

If present, ``INSTALLER`` is a single-line text file naming the tool used to
install the project.
If the installer is executable from the command line, ``INSTALLER``
should contain the command name.
Otherwise, it should contain a printable ASCII string.

The file can be terminated by zero or more ASCII whitespace characters.

Here are examples of two possible ``INSTALLER`` files::

    pip

::

    MegaCorp Cloud Install-O-Matic

This value should be used for informational purposes only.
For example, if a tool is asked to uninstall a project but finds no ``RECORD``
file, it may suggest that the tool named in ``INSTALLER`` may be able to do the
uninstallation.

The direct_url.json file
========================

This file MUST be created by installers when installing a distribution from a
requirement specifying a direct URL reference (including a VCS URL).

This file MUST NOT be created when installing a distribution from an other type
of requirement (i.e. name plus version specifier).

Its detailed specification is at :ref:`direct-url`.
