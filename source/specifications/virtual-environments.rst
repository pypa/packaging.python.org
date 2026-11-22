
.. _virtual-environments:

====================
Virtual Environments
====================

A virtual environment isolates a Python interpreter and its packages. The
virtual environment has its own Python binary (allowing creation of
environments with various Python versions) and can have its own independent set
of installed Python packages in its site directories, but shares the standard
library with the base installed Python.

A Python interpreter detects whether it is in a virtual environment by looking
for a ``pyvenv.cfg`` file one or two levels above its executable (without
resolving symlinks). The ``pyvenv.cfg`` needs to have at least a ``home`` key
to declare a virtual environment.


Runtime detection of virtual environments
=========================================

At runtime, virtual environments can be identified by virtue of
:py:data:`sys.prefix` (the filesystem location of the running interpreter)
having a different value from :py:data:`sys.base_prefix` (the default
filesystem location of the standard library directories).

:ref:`venv-explanation` in the Python standard library documentation for the
:py:mod:`venv` module covers this along with the concept of "activating" a
virtual environment in an interactive operating system shell (this activation
step is optional and hence the changes it makes can't be reliably used to
detect whether a Python program is running in a virtual environment or not).


``pyvenv.cfg``
==============

The ``pyvenv.cfg`` has lines in the form ``key = value``. The following keys
are defined:

* ``home``: The directory containing the Python executable used to create this
  virtual environment.
* ``include-system-site-packages``: When ``true`` (not case sensitive), the
  ``site`` module will also add the system site directories to ``sys.path``
  after the virtual environment site directories. If ``false``, the system
  site directories are not included. Defaults to ``true``.


Declaring installation environments as Python virtual environments
==================================================================

Even in the absence of a ``pyvenv.cfg`` file, any approach (e.g.
``sitecustomize.py``, patching the installed Python runtime) that results in
:py:data:`sys.prefix` and :py:data:`sys.base_prefix` having different values,
while still providing a matching default package installation scheme in
:py:mod:`sysconfig`, will be detected and behave as a Python virtual
environment.


History
=======

- May 2012: This specification was approved through :pep:`405`.
- Nov 2026: Removed PEP 405 references and clarified that
  ``include-system-site-packages`` defaults to ``true``.
