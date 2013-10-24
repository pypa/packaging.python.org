====================
Installing the Tools
====================

Instructions for installing or upgrading :ref:`setuptools`, :ref:`pip`, and
:ref:`virtualenv`, the de facto tools for Python packaging and installation.

On Linux and OSX, these tools will usually be available for the system python
from a system package manager (e.g. `yum` or `apt-get` for linux, or `homebrew` for
OSX). Unfortunately, there is often delay in getting the latest version this
way, so in most cases, you'll want to use the instructions below.


setuptools
----------

:ref:`setuptools` supports building, packaging, and uploading projects to
:term:`PyPI <Python Package Index (PyPI)>`, and is also a requirement of
:ref:`pip`.

To install setuptools from scratch:

1. Securely download `ez_setup.py
   <https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py>`_. [2]_

2. Then run the following (which may require administrator access)::

   $ python ez_setup.py


   .. warning::

      Prior to Setuptools-1.0, `ez_setup.py` was not secure, and is currently
      only secure when your environment contains secure versions of either
      `curl`, `wget`, or `powershell`. [2]_ If you're not sure if you're
      environment fulfills this requirement, then the safest approach is to
      securely download the setuptools archive directly from :term:`PyPI <Python
      Package Index (PyPI)>`, unpack it, and run "python setup.py install" from
      inside the unpacked directory.


To upgrade a previous install of :ref:`setuptools` or :ref:`distribute`, there are two
scenarios.


1. You currently have *some* version of pip.

   ::

   $ pip install --upgrade setuptools

   .. note::

      If you have distribute, this will upgrade to you distribute-0.7.X, which
      is just a wrapper, that depends on setuptools. The end result will be that
      you have distribute-0.7.X (which does nothing) *and* the latest setuptools
      installed.  If you'd prefer not to end up with the distribute wrapper,
      then instead, run ``$ pip uninstall distribute``, then go back to step #1
      above which installs setuptools from scratch.

2. You currently don't have pip.

   Follow the pip install procedure below, then come back and run::

   $ pip install --upgrade setuptools


pip
---

pip requires :ref:`setuptools`, which has to be installed first (see section above), before pip can run. [1]_

Securely download `get-pip.py <https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_. [2]_

Then run the following (which may require administrator access), to install (or upgrade to) the
latest version of pip::

 $ python get-pip.py


virtualenv
----------

Although it's not strictly required for the tutorials in this guide, using
:ref:`virtualenv` to create isolated Python environments (that already contain copies of
:ref:`setuptools` and :ref:`pip`) is a common practice when installing packages.

For more details, see http://www.virtualenv.org.

To install :ref:`virtualenv`, :ref:`pip` should already be installed (see section above).

To install or upgrade, run the following (which may require administrator access)::

 $ pip install --upgrade virtualenv


.. [1] As of pip 1.4, pip started requiring :ref:`setuptools`, not :ref:`distribute`
       (a fork of setuptools). :ref:`setuptools` and :ref:`distribute` are now merged
       back together as "setuptools".
.. [2] "Secure" in this context means using a modern browser or a
       tool like `curl` that verifies SSL certificates when downloading from
       https URLs.
