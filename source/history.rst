.. _`History`:

====================
A Packaging Timeline
====================

:Page Status: Incomplete [#]_
:Last Reviewed: 2014-01-22


**2013-06-09**: The merge of :ref:`setuptools` and `distribute`_ was completed
and released to PyPI. [#]_

**2013-03-23**: :term:`PyPA <Python Packaging Authority (PyPA)>` became the
maintainer for the `Python Packaging User Guide`_, which was forked from the
"Hitchhiker's Guide to Packaging". [#]_

**2013-03-15**: Packaging Dev and User Summits were held at Pycon 2013 to share
ideas on the future of packaging. [#]_ [#]_

**2013-03-14**: The intention to merge :ref:`setuptools` and `distribute`_
was announced by their respective maintainers, PJ Eby and Jason Coombs. [#]_

**2013-03-09**: :ref:`pip` began depending on :ref:`distlib`. [#]_

**2013-03-02**: :ref:`distlib` began releasing to :term:`PyPI <Python Package
Index (PyPI)>`.

**2013-03-17**: :ref:`PEP425 <PEP425s>` and :ref:`PEP427 <PEP427s>` were
accepted.  Together, they specify a built-package format for Python called
:term:`Wheel`.

**2012-06-19**: The effort to include "Distutils2/Packaging" in Python 3.3 was
abandoned due lack of involvement. [#]_

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

**2001**: `PEP241`_ was written to standardize the metadata for packages.

**2000**: `catalog-sig`_ was created to discuss creating a centralized index of
packages.

**2000**: :term:`distutils` was added to the Python standard library in Python 1.6.

**1998**: The `distutils-sig`_ dicussion list was created to discuss the
development of :term:`distutils`.


.. _distutils-sig: http://www.python.org/community/sigs/current/distutils-sig/
.. _catalog-sig: https://mail.python.org/mailman/listinfo/catalog-sig
.. _`Python Packaging User Guide`: https://python-packaging-user-guide.readthedocs.org/en/latest/
.. _PEP241: http://www.python.org/dev/peps/pep-0241
.. _PEP314: http://www.python.org/dev/peps/pep-0314
.. _PEP301: http://www.python.org/dev/peps/pep-0301
.. _distribute: https://pypi.python.org/pypi/distribute

----

.. [#] What's missing: 1) recent PEP438 events 2) D2 evolution and failure, 3)
       PEP453 approval, 4) buildout 2.0 not being isolated
.. [#] http://mail.python.org/pipermail/distutils-sig/2013-June/021160.html
.. [#] http://mail.python.org/pipermail/distutils-sig/2013-March/020224.html
.. [#] https://us.pycon.org/2013/community/openspaces/packaginganddistributionminisummit/
.. [#] http://www.pyvideo.org/video/1731/panel-directions-for-packaging
.. [#] http://mail.python.org/pipermail/distutils-sig/2013-March/020127.html
.. [#] https://github.com/pypa/pip/pull/834
.. [#] http://mail.python.org/pipermail/python-dev/2012-June/120430.html

