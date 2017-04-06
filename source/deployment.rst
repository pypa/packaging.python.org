
======================
Application Deployment
======================

:Page Status: Incomplete
:Last Reviewed: 2014-11-11

.. contents:: Contents
   :local:


Overview
========


Supporting multiple hardware platforms
--------------------------------------

::

  FIXME

  Meaning: x86, x64, ARM, others?

  For Python-only distributions, it *should* be straightforward to deploy on all
  platforms where Python can run.

  For distributions with binary extensions, deployment is major headache.  Not only
  must the extensions be built on all the combinations of operating system and
  hardware platform, but they must also be tested, preferably on continuous
  integration platforms.  The issues are similar to the "multiple python
  versions" section above, not sure whether this should be a separate section.
  Even on Windows x64, both the 32 bit and 64 bit versions of Python enjoy
  significant usage.



OS Packaging & Installers
=========================

::

  FIXME

  - Building rpm/debs for projects
  - Building rpms/debs for whole virtualenvs
  - Building Mac OS X installers for Python projects
  - Building Android APKs with Kivy+P4A or P4A & Buildozer

Windows
-------

::

  FIXME

  - Building Windows installers for Python projects

Pynsist
^^^^^^^

`Pynsist <https://pypi.python.org/pypi/pynsist>`__ is a tool that bundles Python
programs together with the Python-interpreter into a single installer based on
NSIS. In most cases, packaging only requires the user to choose a version of
the Python-interpreter and declare the dependencies of the program. The tool
downloads the specified Python-interpreter for Windows and packages it with all
the dependencies in a single Windows-executable installer.

The installer installs or updates the Python-interpreter on the users system,
which can be used independently of the packaged program. The program itself,
can be started from a shortcut, that the installer places in the start-menu.
Uninstalling the program leaves the Python installation of the user intact.

A big advantage of pynsist is that the Windows packages can be built on Linux.
There are several examples for different kinds of programs (console, GUI) in
the `documentation <https://pynsist.readthedocs.io>`__. The tool is released
under the MIT-licence.

Application Bundles
===================

::

  FIXME

  - py2exe/py2app/PEX
  - wheels kinda/sorta


Configuration Management
========================

::

  FIXME

  puppet
  salt
  chef
  ansible
  fabric
