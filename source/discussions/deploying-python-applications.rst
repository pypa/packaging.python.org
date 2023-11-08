
=============================
Deploying Python applications
=============================

:Page Status: Incomplete
:Last Reviewed: 2021-8-24


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
  integration platforms.  The issues are similar to the "multiple Python
  versions" section above, not sure whether this should be a separate section.
  Even on Windows x64, both the 32 bit and 64 bit versions of Python enjoy
  significant usage.



OS packaging & installers
=========================

::

  FIXME

  - Building rpm/debs for projects
  - Building rpms/debs for whole virtualenvs
  - Building macOS installers for Python projects
  - Building Android APKs with Kivy+P4A or P4A & Buildozer

Windows
-------

::

  FIXME

  - Building Windows installers for Python projects

Pynsist
^^^^^^^

`Pynsist <https://pypi.org/project/pynsist>`__ is a tool that bundles Python
programs together with the Python-interpreter into a single installer based on
NSIS. In most cases, packaging only requires the user to choose a version of
the Python-interpreter and declare the dependencies of the program. The tool
downloads the specified Python-interpreter for Windows and packages it with all
the dependencies in a single Windows-executable installer.

The installed program can be started from a shortcut that the installer adds to
the start-menu. It uses a Python interpreter installed within its application
directory, independent of any other Python installation on the computer.

A big advantage of Pynsist is that the Windows packages can be built on Linux.
There are several examples for different kinds of programs (console, GUI) in
the :any:`documentation <pynsist:index>`. The tool is released
under the MIT-licence.

Application bundles
===================

::

  FIXME

  - wheels kinda/sorta

Windows
-------

py2exe
^^^^^^

`py2exe <https://pypi.org/project/py2exe/>`__ is a distutils extension which
allows to build standalone Windows executable programs (32-bit and 64-bit)
from Python scripts. Python versions included in the official development
cycle are supported (refers to `Status of Python branches`__). py2exe can
build console executables and windows (GUI) executables. Building windows
services, and DLL/EXE COM servers might work but it is not actively supported.
The distutils extension is released under the MIT-licence and Mozilla
Public License 2.0.

.. __: https://devguide.python.org/#status-of-python-branches

macOS
-----

py2app
^^^^^^

`py2app <https://pypi.org/project/py2app/>`__ is a Python setuptools
command which will allow you to make standalone macOS application
bundles and plugins from Python scripts. Note that py2app MUST be used
on macOS to build applications, it cannot create Mac applications on other
platforms. py2app is released under the MIT-license.

Unix (including Linux and macOS)
-----------------------------------

pex
^^^

`pex <https://pypi.org/project/pex/>`__ is  a library for generating .pex
(Python EXecutable) files which are executable Python environments in the
spirit of virtualenvs. pex is an expansion upon the ideas outlined in :pep:`441`
and makes the deployment of Python applications as simple as cp. pex files may
even include multiple platform-specific Python distributions, meaning that a
single pex file can be portable across Linux and macOS. pex is released under the
Apache License 2.0.

Configuration management
========================

::

  FIXME

  puppet
  salt
  chef
  ansible
  fabric
