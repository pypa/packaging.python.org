
.. _externally-managed-environments:

===============================
Externally Managed Environments
===============================

While some Python installations are entirely managed by the user that installed
Python, others may be provided and managed by another means (such as the
operating system package manager in a Linux distribution, or as a bundled
Python environment in an application with a dedicated installer).

Attempting to use conventional Python packaging tools to manipulate such
environments can be confusing at best and outright break the entire underlying
operating system at worst. Documentation and interoperability guides only go
so far in resolving such problems.

:pep:`668` defined an ``EXTERNALLY-MANAGED`` marker file that allows a Python
installation to indicate to Python-specific tools such as ``pip`` that they
neither install nor remove packages into the interpreter’s default installation
environment, and should instead guide the end user towards using
:ref:`virtual-environments`.
