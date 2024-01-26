=======================
Names and normalization
=======================

This specification defines the format that names for packages and extras are
required to follow. It also describes how to normalize them, which should be
done before lookups and comparisons.


.. _name-format:

Name format
===========

A valid name consists only of ASCII letters and numbers, period,
underscore and hyphen. It must start and end with a letter or number.
This means that valid project names are limited to those which match the
following regex (run with :py:data:`re.IGNORECASE`)::

    ^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$


.. _name-normalization:

Name normalization
==================

The name should be lowercased with all runs of the characters ``.``, ``-``, or
``_`` replaced with a single ``-`` character. This can be implemented in Python
with the re module:

.. code-block:: python

    import re

    def normalize(name):
        return re.sub(r"[-_.]+", "-", name).lower()

This means that the following names are all equivalent:

* ``friendly-bard`` (normalized form)
* ``Friendly-Bard``
* ``FRIENDLY-BARD``
* ``friendly.bard``
* ``friendly_bard``
* ``friendly--bard``
* ``FrIeNdLy-._.-bArD`` (a *terrible* way to write a name, but it is valid)

History
=======

- September 2015: The specification of name normalized was approved through
  :pep:`503 <503#normalized-names>`.
- November 2015: The specification of valid names was approved through
  :pep:`508 <508#names>`.
