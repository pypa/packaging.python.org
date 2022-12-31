.. _name-normalization:

==========================
Package name normalization
==========================

Project names are "normalized" for use in various contexts. This document describes how project names should be normalized.

Valid non-normalized names
--------------------------

A valid name consists only of ASCII letters and numbers, period,
underscore and hyphen. It must start and end with a letter or number.
This means that valid project names are limited to those which match the
following regex (run with ``re.IGNORECASE``)::

    ^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$

Normalization
-------------

The name should be lowercased with all runs of the characters ``.``, ``-``, or ``_`` replaced with a single ``-`` character. This can be implemented in Python with the re module:

.. code-block:: python

    import re

    def normalize(name):
        return re.sub(r"[-_.]+", "-", name).lower()

This means that the following names are all equivalent:

* ``friendly-bard``  (normalized form)
* ``Friendly-Bard``
* ``FRIENDLY-BARD``
* ``friendly.bard``
* ``friendly_bard``
* ``friendly--bard``
* ``FrIeNdLy-._.-bArD`` (a _terrible_ way to write a name, but it is valid)
