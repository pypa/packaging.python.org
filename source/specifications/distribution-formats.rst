
.. _distribution-formats:

====================
Distribution Formats
====================


Source Distribution Format
==========================

Given :pep:`517`, a new style of source tree format is defined
based in ``pyproject.toml`` which is defined in :pep:`518`.

But the legacy source distribution format still exists and
is defined using ``setup.py``.
It's format is implicitly defined by the behaviour of the
standard library's ``distutils`` module when executing the ``setup.py sdist``.


Binary Distribution Format
==========================

The binary distribution format (``wheel``) is defined in :pep:`427`.
