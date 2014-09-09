.. _`History`:

=================
Packaging History
=================

:Page Status: Complete
:Last Reviewed: 2014-04-09


2014
----

* :ref:`PEP453 <PEP453s>`: Being able to bootstrap ``pip`` into Python
  3.4.
* http://bugs.python.org/issue19407: Modern Installation and Packaging guides on
  python.org.
* :ref:`virtualenv` (v1.11) started installing pip & setuptools using wheels.
* :ref:`pip` (v1.5.1) became available as a cross platform wheel on PyPI.
* :ref:`pip` (v1.5.1) stop requiring :ref:`setuptools` to install wheels.
* ``get-pip.py`` doesn't require setuptools to be installed first
* ``get-pip.py`` installs setuptools for you, if you don't already have it
* `PEP449 <http://www.python.org/dev/peps/pep-0449>`_: Removal of the DNS based
  mirror autodiscovery
* `Refactored the pip docs <https://github.com/pypa/pip/pull/1556>`_ to be
  consistent with the `"PyPA Standard Docs Template"
  <https://gist.github.com/qwcode/8431828>`_

2013
----

* :ref:`distlib` started releasing to PyPI, and :ref:`pip` began depending on it
* Core PyPI infrastructure relocated to OSU/OSL (with significantly
  increased resources)
* The core packaging projects were collected under the :term:`Python Packaging Authority
  (PyPA)` accounts on `GitHub <https://github.com/pypa>`_ and `Bitbucket
  <https://bitbucket.org/pypa/>`_ [2]_
* Distribute merged back into :ref:`setuptools`, and :ref:`setuptools` development
  migrated to the PyPA BitBucket account. [1]_ [5]_
* PyPI supports clients using verified SSL with standard cert bundles
* PyPI forces web users over to SSL
* :ref:`pip` (v1.3) and :ref:`easy_install <setuptools>` (v0.7) use verified SSL by default
* easy_install supports additional hashes beyond md5 (pip already did)
* Fastly CDN enabled for PyPI (donated)
* Restructured the `pip install docs
  <http://pip.pypa.io/en/latest/installing.html>`_ to clarify that
  setuptools and pip are the "base" of the bootstrapping hierarchy
* setuptools available as a cross platform wheel on PyPI
* :ref:`PEP438s` and the associated pip changes.
* :ref:`pip` (v1.4) added support for building and installing :term:`wheels
  <Wheel>`
* :term:`PyPA <Python Packaging Authority (PyPA)>` became the maintainer for the
  `Python Packaging User Guide`_, which was forked from the "Hitchhiker's Guide
  to Packaging".
* Packaging Dev and User Summits were held at Pycon 2013 to share ideas on the
  future of packaging. [3]_ [4]_
* :ref:`PEP425 <PEP425s>` and :ref:`PEP427 <PEP427s>` were accepted.  Together,
  they specify a built-package format for Python called :term:`Wheel`.


Before 2013
-----------

**2012-06-19**: The effort to include "Distutils2/Packaging" in Python 3.3 was
abandoned due lack of involvement. [6]_

**2011-02-28**: The :term:`PyPA <Python Packaging Authority (PyPA)>` is created
to take over the maintenance of :ref:`pip` and :ref:`virtualenv` from Ian Bicking,
led by Carl Meyer, Brian Rosner and Jannis Leidel. Other proposed names were
"ianb-ng", "cabal", "pack" and "Ministry of Installation".

**2008**: `distribute`_ was forked from :ref:`setuptools` by Tarek Ziade, in an
effort to create a more open project.

**2008**: :ref:`pip` was introduced by Ian Bicking as an alternative to
``easy_install`` (the installer included with :ref:`setuptools`)

**2007**: :ref:`virtualenv` was introduced by Ian Bicking, which allowed users
to create isolated Python environments based on a central system installation of
Python.

**2006**: :ref:`buildout` was introduced by Jim Fulton, with the goal to create
a system for repeatable installations of potentially complex projects.

**2004**: :ref:`setuptools` was introduced by Phillip Eby, which included the
:term:`Egg` format, and the ability to declare and automatically install
dependencies.

**2003**: :term:`PyPI <Python Package Index (PyPI)>` was up and running.

**2002**: Richard Jones started work on :term:`PyPI <Python Package Index
(PyPI)>`, and created `PEP301`_ to describe it.

**2001**: `PEP241`_ was written to standardize the metadata for distributions.

**2000**: `catalog-sig`_ was created to discuss creating a centralized index of
distributions.

**2000**: :ref:`distutils` was added to the Python standard library in Python 1.6.

**1998**: The `distutils-sig`_ dicussion list was created to discuss the
development of :ref:`distutils`.


.. _distutils-sig: http://www.python.org/community/sigs/current/distutils-sig/
.. _catalog-sig: https://mail.python.org/mailman/listinfo/catalog-sig
.. _`Python Packaging User Guide`: https://python-packaging-user-guide.readthedocs.org/en/latest/
.. _PEP241: http://www.python.org/dev/peps/pep-0241
.. _PEP314: http://www.python.org/dev/peps/pep-0314
.. _PEP301: http://www.python.org/dev/peps/pep-0301
.. _distribute: https://pypi.python.org/pypi/distribute

----

.. [1] http://mail.python.org/pipermail/distutils-sig/2013-June/021160.html
.. [2] http://mail.python.org/pipermail/distutils-sig/2013-March/020224.html
.. [3] https://us.pycon.org/2013/community/openspaces/packaginganddistributionminisummit/
.. [4] http://www.pyvideo.org/video/1731/panel-directions-for-packaging
.. [5] http://mail.python.org/pipermail/distutils-sig/2013-March/020127.html
.. [6] http://mail.python.org/pipermail/python-dev/2012-June/120430.html

