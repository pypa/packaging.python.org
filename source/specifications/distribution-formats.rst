
.. _distribution-formats:

====================
Distribution Formats
====================


Source Distribution Format
==========================

With adoption of :pep:`517`, a new style of source tree format is defined
based in ``pyproject.toml`` which is defined on :pep:`518`.

However, the legacy source distribution format still exists and
is defined using ``setup.py``.
Its format is implicitly defined by the behaviour of the
``distutils`` module in the standard library when executing
the ``setup.py sdist``.


Binary Distribution Format
==========================

The binary distribution format (``wheel``) is defined in :pep:`427`.
