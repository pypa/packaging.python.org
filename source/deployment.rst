
======================
Application Deployment
======================

:Page Status: Incomplete
:Last Reviewed: 2014-07-24

.. contents::


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
  - Building Windows installers for Python projects
  - Building Mac OS X installers for Python projects



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
