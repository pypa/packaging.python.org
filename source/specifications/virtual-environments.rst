
.. _virtual-environments:

===========================
Python Virtual Environments
===========================

In Python 3.3 and later versions, :pep:`405` provides interpreter level support
for the concept of "Python Virtual Environments". Each virtual environment has
its own Python binary (allowing creation of environments with various Python
versions) and can have its own independent set of installed Python packages in
its site directories, but shares the standard library with the base installed
Python. While the concept of virtual environments existed prior to this update,
there was no previously standardised mechanism for declaring or discovering them.

Runtime detection of virtual environments
=========================================

At runtime, virtual environments can be identified by virtue of ``sys.prefix``
(the filesystem location of the running interpreter) having a different value
from ``sys.base_prefix`` (the default filesytem location of the standard library
directories).

Declaring installation environments as Python virtual environments
==================================================================

As described in :pep:`405`, a Python virtual environment in its simplest form
consists of nothing more than a copy or symlink of the Python binary accompanied
by a ``site-packages`` directory and a ``pyvenv.cfg`` file with a ``home`` key
that indicates where to find the Python standard library modules.

This split installation and ``pyvenv.cfg`` file approach can be used by *any*
Python installation provider that desires Python-specific tools to be aware that
they are already operating in a virtual environment and no further environment
nesting is required or desired.

However, any approach that results in ``sys.prefix`` and ``sys.base_prefix``
having different values, while still providing a valid package installation
scheme in ``sysconfig``, will be detected and behave as a Python virtual
environment.
