
.. _distribution-formats:

====================
Distribution formats
====================


Source distribution format
==========================

The accepted style of source distribution format based
on ``pyproject.toml``, defined in :pep:`518` and adopted by :pep:`517`
has not been implemented yet.

There is also the legacy source distribution format, implicitly defined by
the behaviour of ``distutils`` module in the standard library,
when executing ``setup.py sdist``.

Binary distribution format
==========================

The binary distribution format (``wheel``) is defined in :pep:`427`.
