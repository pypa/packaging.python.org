==============================
The Future of Python Packaging
==============================

:Page Status: Complete
:Last Reviewed: 2014-01-19


The :term:`distutils` cross-platform build and distribution system was added to
the Python standard library in late 1998. This means the current Python software
distribution ecosystem (which builds on :term:`distutils`) has a foundation that
is almost 15 years old, which poses a variety of challenges to successful
evolution.

The current effort to improve the situation started when the ``packaging``
library (also known as ``distutils2``) `failed to be accepted
<https://mail.python.org/pipermail/python-dev/2012-June/120430.html>`_ into the
standard library for Python 3.3.  That effort had spanned from 2009 to 2012.
While ``packaging`` itself is no longer under development, it did help lay the
foundations for the current effort.

The current effort is managed by the :term:`Python Packaging Authority (PyPA)`,
in cooperation with members of the Python core development team.

Goals
=====

* To provide a relatively easy to use software distribution infrastructure that
  is also fast, reliable and reasonably secure.  "Reasonably secure", due to
  backwards compatibility constraints preventing turning off some insecure
  legacy features.
* To improve the docs for users, including the `Python Packaging User Guide
  <https://python-packaging-user-guide.readthedocs.org>`_, anything related to
  packaging on `docs.python.org`_, and the project docs for :ref:`pip`,
  :ref:`setuptools`, :ref:`virtualenv`, and :ref:`wheel`.
* To be progressive, but also be very mindful to not break things that are
  currently working, due to haste.
* To specifically *not* focus at first on adding something to the standard
  library as our solution to our packaging problems.  Adding something to the
  standard library is hard, and once it's added, it's a slow process to change
  it.  Most of the current effort is largely focused on 3rd party projects.

.. _docs.python.org: http://docs.python.org

Presentations & Articles
========================

In addition to this document, there have been some talks and presentations
regarding current and future efforts related to packaging.

* PyCon US, March 2013

  * `Directions in Packaging Q & A Panel (aka "./setup.py install must die")
    <http://pyvideo.org/video/1731/panel-directions-for-packaging>`__

* PyCon AU, July 2013

  * `Nobody Expects the Python Packaging Authority
    <http://pyvideo.org/video/2197/nobody-expects-the-python-packaging-authority>`__ [1]_

* Personal essays

  * `Nick Coghlan <http://python-notes.curiousefficiency.org/en/latest/pep_ideas/core_packaging_api.html>`__


Completed work
==============

2013
----

* :ref:`distlib` started releasing to PyPI, and pip began depending on it
* Core PyPI infrastructure relocated to OSU/OSL (with significantly
  increased resources)
* The core packaging projects were collected under the :term:`Python Packaging Authority
  (PyPA)` accounts on `GitHub <https://github.com/pypa>`_ and `Bitbucket
  <https://bitbucket.org/pypa/>`_
* distribute merged back into :ref:`setuptools`, and :ref:`setuptools` development
  migrated to the PyPA BitBucket account
* PyPI supports clients using verified SSL with standard cert bundles
* PyPI forces web users over to SSL
* :ref:`pip` (>=1.3) and :ref:`easy_install <setuptools>` (>=0.7) use verified SSL by default
* easy_install supports additional hashes beyond md5 (pip already did)
* Fastly CDN enabled for PyPI (donated)
* Restructured the `pip install docs
  <http://www.pip-installer.org/en/latest/installing.html>`_ to clarify that
  setuptools and pip are the "base" of the bootstrapping hierarchy
* setuptools available as a cross platform wheel on PyPI
* :ref:`PEP438s` and the associated pip changes.

2014
----

* virtualenv installs pip & setuptools using wheels.

Work in Progress
================

* :ref:`PEP453 <PEP453s>`: Having ``pip`` be available by default in Python 3.4 distributions
* `PEP449 <http://www.python.org/dev/peps/pep-0449>`_: Removal of the DNS based mirror autodiscovery

Future Work
===========

2014
----

* :ref:`pip` (>=1.5.1) available as a cross platform wheel on PyPI
* :ref:`pip` (>=1.5.1) doesn't require :ref:`setuptools` to install wheels
* ``get-pip.py`` installs setuptools for you, if you don't already have it
* Improved handling of in-place pip upgrades on Windows
* Migration from the legacy PyPI server to :ref:`warehouse` (the preview is
  available at https://preview-pypi.python.org/ running off the live PyPI data)
* "Metadata 2.0" (:ref:`PEP426 <PEP426s>` / :ref:`PEP440 <PEP440s>`)
* :ref:`pip` should `get a real dependency resolver <https://github.com/pypa/pip/issues/988>`_
* Removal of older pip commands and options that aren't popular or well
  maintained (`#906 <https://github.com/pypa/pip/issues/906>`_, `#1046
  <https://github.com/pypa/pip/issues/1046>`_)
* Public release of the `Python Packaging User Guide
  <https://python-packaging-user-guide.readthedocs.org>`_

TBD
---

* PEPs for "sdist 2.0" and wheel 1.1
* A `"MetaBuild" <http://www.python.org/dev/peps/pep-0426/#metabuild-system>`_
  PEP that would allow projects to specify alternative build systems
  (i.e. something other than setuptools).
* :ref:`PEP458 <PEP458s>`: An integration of PyPI with the "The Update Framework (TUF)"
* An update of :ref:`PEP376 <PEP376s>` (the installation format) to be json based
* An internal stable api for pip
* Improved PyPI upload API
* Improved local PyPI hosting solutions (e.g. like `devpi <http://doc.devpi.net/latest/devpi>`_)

----

.. [1] Repeated that at PyTexas, but can't find a video link for it.  Anyone?
