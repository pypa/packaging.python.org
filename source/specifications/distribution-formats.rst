
.. _distribution-formats:

====================
Distribution Formats
====================


Source Distribution Format
==========================

The accepted style of source distribution format based
on ``pyproject.toml``, defined in :pep:`518` and adopted by :pep:`517`
has not been implemented yet.

There is also the legacy source distribution format, implicitly defined by
the behaviour of ``distutils`` module in the the standard library,
when executing ``setup.py sdist``.

Binary Distribution Format
==========================

The binary distribution format (``wheel``) is defined in :pep:`427`.
