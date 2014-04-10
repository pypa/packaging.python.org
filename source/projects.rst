=================
Project Summaries
=================

:Page Status: Complete
:Last Reviewed: 2014-04-09

Summaries and links for the most relevant projects in the space of Python
installation and packaging.


Python Packaging User Guide
===========================

`Docs <http://packaging.python.org>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ |
`Issues <https://github.com/pypa/python-packaging-user-guide/issues>`__ |
`Github <https://github.com/pypa/python-packaging-user-guide>`__ |
User irc:#pypa |
Dev irc:#pypa-dev

This guide!


.. _pip:

pip
===

`Docs <http://www.pip-installer.org/en/latest/>`__ |
`User list <http://groups.google.com/group/python-virtualenv>`__ [1]_ |
`Dev list <http://groups.google.com/group/pypa-dev>`__ |
`Issues <https://github.com/pypa/pip/issues>`__ |
`Github <https://github.com/pypa/pip>`__ |
`PyPI <https://pypi.python.org/pypi/pip/>`__ |
User irc:#pypa |
Dev irc:#pypa-dev

A tool for installing and managing Python packages.

.. _virtualenv:

virtualenv
==========

`Docs <http://www.virtualenv.org>`__ |
`User list <http://groups.google.com/group/python-virtualenv>`__ |
`Dev list <http://groups.google.com/group/pypa-dev>`__ |
`Issues <https://github.com/pypa/virtualenv/issues>`__ |
`Github <https://github.com/pypa/virtualenv>`__ |
`PyPI <https://pypi.python.org/pypi/virtualenv/>`__ |
User irc:#pypa  |
Dev irc:#pypa-dev

A tool for creating isolated Python environments.


.. _setuptools:
.. _easy_install:

setuptools
==========

`Docs <http://pythonhosted.org/setuptools>`__ |
`User list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Dev list <http://groups.google.com/group/pypa-dev>`__ |
`Issues <https://bitbucket.org/pypa/setuptools/issues>`__ |
`Bitbucket <https://bitbucket.org/pypa/setuptools>`__ |
`PyPI <https://pypi.python.org/pypi/setuptools>`__ |
User irc:#pypa  |
Dev irc:#pypa-dev



setuptools (which includes ``easy_install``) is a collection of enhancements to
the Python distutils that allow you to more easily build and distribute Python
packages, especially ones that have dependencies on other packages.

`distribute`_ was a fork of setuptools that was merged back into setuptools (in
v0.7), thereby making setuptools the primary choice for Python packaging.

.. _distutils:

distutils
=========

`Docs <https://docs.python.org/3/library/distutils.html#module-distutils>`__ |
`User list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <http://bugs.python.org>`__ |
User irc:#pypa  |
Dev irc:#pypa-dev

A standard package that comes with the Python Standard Library that has support
for creating and installing :term:`distributions
<Distribution>`. :ref:`Setuptools` provides enhancements to distutils, and is
much more commonly used than distutils by itself.


.. _wheel:

wheel
=====

`Docs <http://wheel.readthedocs.org>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bitbucket.org/pypa/wheel/issues?status=new&status=open>`__ |
`Bitbucket <https://bitbucket.org/pypa/wheel>`__ |
`PyPI <https://pypi.python.org/pypi/wheel>`__ |
User irc:#pypa  |
Dev irc:#pypa-dev


Primarily, the wheel project offers the ``bdist_wheel`` :ref:`setuptools` extension for
creating :term:`wheel distributions <Wheel>`.  Additionally, it offers its own
command line utility for creating and installing wheels.


.. _distlib:

distlib
=======

`Docs <http://pythonhosted.org/distlib>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bitbucket.org/pypa/distlib/issues?status=new&status=open>`__ |
`Bitbucket <https://bitbucket.org/pypa/distlib>`__ |
`PyPI <https://pypi.python.org/pypi/distlib>`__

Distlib is a library which implements low-level functions that relate to
packaging and distribution of Python software.  It consists in part of the
functions from the `distutils2 <https://pypi.python.org/pypi/Distutils2>`_
project, which was intended to be released as ``packaging`` in the Python 3.3
stdlib, but was removed shortly before Python 3.3 entered beta testing.


.. _twine:

twine
=====

`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://github.com/dstufft/twine/issues>`__ |
`Github <https://github.com/dstufft/twine>`__ |
`PyPI <https://pypi.python.org/pypi/twine>`__

Twine is a utility for interacting with PyPI, that offers a secure replacement for
``setup.py upload``.


.. _warehouse:

Warehouse
=========

`Docs <http://warehouse.readthedocs.org/en/latest/>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://github.com/pypa/warehouse/issues>`__ |
`Github <https://github.com/pypa/warehouse>`__ |
Dev irc:#pypa-dev


The new unreleased PyPI application (to replace the current site at https://pypi.python.org/pypi).


.. _buildout:

buildout
========

`Docs <http://www.buildout.org>`__ |
`Mailing list <http://mail.python.org/mailman/listinfo/distutils-sig>`__ [2]_ |
`Issues <https://bugs.launchpad.net/zc.buildout>`__ |
`PyPI <https://pypi.python.org/pypi/zc.buildout>`__ |
irc:#buildout

Buildout is a Python-based build system for creating, assembling and deploying
applications from multiple parts, some of which may be non-Python-based.  It
lets you create a buildout configuration and reproduce the same software later.


.. _bento:

bento
=====

`Docs <http://cournape.github.io/Bento/>`__ |
`Mailing list <http://librelist.com/browser/bento>`__ |
`Issues <https://github.com/cournape/Bento/issues>`__ |
`Github <https://github.com/cournape/Bento>`__ |
`PyPI <https://pypi.python.org/pypi/bento>`__

Bento is a packaging tool solution for python software, targeted as an
alternative to distutils, setuptools, distribute, etc....  Bento's philosophy is
reproducibility, extensibility and simplicity (in that order).


.. _conda:

conda
=====

`Docs <http://docs.continuum.io/conda/index.html>`__

conda is an installation tool for managing `Anaconda
<http://docs.continuum.io/anaconda/index.html>`__ installations. Anaconda is a
collection of powerful packages for Python that enables large-scale data
management, analysis, and visualization for Business Intelligence, Scientific
Analysis, Engineering, Machine Learning, and more.


.. _hashdist:

Hashdist
========

`Docs <http://hashdist.readthedocs.org/en/latest/>`__ |
`Github <https://github.com/hashdist/hashdist/>`__

Hashdist is a library for building non-root software distributions. Hashdist is
trying to be “the Debian of choice for cases where Debian technology doesn’t
work”. The best way for Pythonistas to think about Hashdist may be a more
powerful hybrid of virtualenv and buildout.

----

.. [1] pip was created by the same developer as virtualenv, and early on adopted
       the virtualenv mailing list, and it's stuck ever since.

.. [2] Multiple projects reuse the distutils-sig mailing list as their user list.


.. _distribute: https://pypi.python.org/pypi/distribute
