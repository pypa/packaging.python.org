==============================
The Future of Python Packaging
==============================

:Page Status: Incomplete
:Last Reviewed: 2014-04-09


The :ref:`distutils` cross-platform build and distribution system was added to
the Python standard library in late 2000. This means the current Python software
distribution ecosystem (which builds on :ref:`distutils`) has a foundation that
is almost 15 years old, which poses a variety of challenges to successful
evolution.

The current effort to improve the situation started when the ``packaging``
library (also known as ``distutils2``) `failed to be accepted
<https://mail.python.org/pipermail/python-dev/2012-June/120430.html>`_ into the
standard library for Python 3.3.  That effort had spanned from 2009 to 2012.

The current effort is managed by the :term:`Python Packaging Authority (PyPA)`,
in cooperation with members of the Python core development team.


Goals
=====

* To provide a relatively easy to use software distribution infrastructure that
  is also fast, reliable and reasonably secure.  "Reasonably secure", due to
  backwards compatibility constraints preventing turning off some insecure
  legacy features.

* Although it's still being defined, to work towards a "Meta-Packaging" [1]_ system that:

  * Clearly delineates the phases of distribution
  * Allows for multiple interacting tools vs one monolithic tool
  * Specifically allows for alternative build systems, i.e. a `"MetaBuild"
    <http://www.python.org/dev/peps/pep-0426/#metabuild-system>`_ system.

* To improve the docs for users, including the `Python Packaging User Guide`_,
  anything related to packaging on `docs.python.org`_, and the project docs for
  :ref:`pip`, :ref:`setuptools`, :ref:`virtualenv`, and :ref:`wheel`.

* To be progressive, but also be very mindful to not break things that are
  currently working, due to haste.

* To specifically *not* focus at first on adding something to the standard
  library as our solution to our packaging problems.  Adding something to the
  standard library is hard, and once it's added, it's a slow process to change
  it.  Most of the current effort is largely focused on 3rd party projects.

.. _docs.python.org: http://docs.python.org


How to help
===========

* Get involved with one of mainstream :doc:`packaging projects <projects>`.
* Help us catalog and discuss the current problems in packaging and
  installation.  See the `The issue tracker for the problems in packaging
  <https://github.com/pypa/packaging-problems/issues>`_ maintained by
  :term:`PyPA <Python Packaging Authority (PyPA)>`.
* Discuss :doc:`PEPs <peps>` and long terms plans at `distutils-sig
  <http://mail.python.org/mailman/listinfo/distutils-sig>`_.


Presentations & Articles
========================

In addition to this document, there have been some talks and presentations
regarding current and future efforts related to packaging.

* PyCon US, March 2013

  * `Directions in Packaging Q & A Panel (aka "./setup.py install must die")
    <http://pyvideo.org/video/1731/panel-directions-for-packaging>`__

* PyCon AU, July 2013

  * `Nobody Expects the Python Packaging Authority
    <http://pyvideo.org/video/2197/nobody-expects-the-python-packaging-authority>`__

* linux.conf.au 2014

  * Python Packaging 2.0: Playing Well With Others (`video
    <https://www.youtube.com/watch?v=7An2GobbSWU>`_, `article
    <http://lwn.net/Articles/580399>`_)

* PyCon US, April 2014

  * `What is coming in Python packaging
    <https://us.pycon.org/2014/schedule/presentation/204/>`_
  * `Python packaging simplified, for end users, app developers, and open source
    contributors <https://us.pycon.org/2014/schedule/presentation/219>`_

* Personal essays

  * `Nick Coghlan
    <http://python-notes.curiousefficiency.org/en/latest/pep_ideas/core_packaging_api.html>`__


Major Todos
===========

Metadata 2.0
------------

`See the Metadata Open Issues
<https://bitbucket.org/pypa/pypi-metadata-formats/issues?status=new&status=open&priority=blocker>`_

* :ref:`PEP426: Metadata for Python Software Packages 2.0 <PEP426s>`
* :ref:`PEP440: Version Identification and Dependency Specification <PEP440s>`
* `PEP459: Standard Metadata Extensions for Python Software Packages
  <http://legacy.python.org/dev/peps/pep-0459/>`_
* `Wheel 1.1
  <https://bitbucket.org/pypa/pypi-metadata-formats/issue/18/wheel-11>`_
* `sdist 2.0
  <https://bitbucket.org/pypa/pypi-metadata-formats/issue/20/sdist-20>`_
* `PEP for common naming schemes
  <https://bitbucket.org/pypa/pypi-metadata-formats/issue/23/common-filename-scheme>`_
* `Installation Database 2.0 (replace PEP376)
  <https://bitbucket.org/pypa/pypi-metadata-formats/issue/22/installation-database-2>`_


PyPI Infrastructure
-------------------

* Migration from the legacy PyPI server to :ref:`warehouse` (the preview is
  available at https://warehouse.python.org/ running off the live PyPI data)
* :ref:`PEP458 <PEP458s>`: An integration of PyPI with the "The Update Framework (TUF)"
* Improved PyPI upload API


pip
---

* An internal stable api for pip
* Removal of older pip commands and options that aren't popular or well
  maintained (`#906 <https://github.com/pypa/pip/issues/906>`_, `#1046
  <https://github.com/pypa/pip/issues/1046>`_)
* :ref:`pip` needs a `real dependency resolver
  <https://github.com/pypa/pip/issues/988>`_


Docs and Community
------------------

* Refactor the :ref:`virtualenv`, :ref:`setuptools`, and :ref:`wheel` docs to
  be consistent with the `"PyPA Standard Docs Template"
  <https://gist.github.com/qwcode/8431828>`_
* Document pip's (and more generally pypa's) deprecation policy (`Issue 1611
  <https://github.com/pypa/pip/issues/1611>`_)
* A general release email list for all Pypa projects?


More PEPs
---------

* A `"MetaBuild" <http://www.python.org/dev/peps/pep-0426/#metabuild-system>`_
  PEP that would allow projects to specify alternative build systems
  (i.e. something other than setuptools).
* `Wheel 2.0 <https://bitbucket.org/pypa/pypi-metadata-formats/issue/19/wheel-20>`_

----

.. [1] See Nick Coghlan's `The Phases of Distribution
       <http://python-notes.curiousefficiency.org/en/latest/pep_ideas/core_packaging_api.html#the-phases-of-distribution>`_
       and `A Meta-Packaging System
       <http://python-notes.curiousefficiency.org/en/latest/pep_ideas/core_packaging_api.html#a-meta-packaging-system>`_

.. _Python Packaging User Guide: http://packaging.python.org
