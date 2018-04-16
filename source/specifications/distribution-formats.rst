
.. _distribution-formats:

====================
Distribution Formats
====================


Source Distribution Format
==========================

With adoption of :pep:`517`, a new style of source distribution format is
defined based on ``pyproject.toml`` which is defined in :pep:`518`.

There is also the legacy source distribution format, implicitly defined by
the behaviour of ``distutils`` module in the the standard library,
when executing ``setup.py sdist``.

Binary Distribution Format
==========================

The binary distribution format (``wheel``) is defined in :pep:`427`.
