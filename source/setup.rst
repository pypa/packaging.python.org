====================
Installing the Tools
====================

:Page Status: Complete
:Last Reviewed: 2014-1-14

Instructions for installing or upgrading :ref:`pip`, :ref:`setuptools`,
:ref:`wheel`, and :ref:`virtualenv`, the :doc:`recommended <current>`
tools for Python packaging and installation.

On Linux and OSX, these tools will usually be available for the system python
from a system package manager (e.g. `yum` or `apt-get` for linux, or `homebrew` for
OSX). Unfortunately, there is often delay in getting the latest version this
way, so in most cases, you'll want to use the instructions below.


pip
---

To install or upgrade pip, securely download `get-pip.py
<https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_. [1]_

Then run the following (which may require administrator access)::

 $ python get-pip.py

.. note::

    Beginning with v1.5.1, pip does not require :ref:`setuptools` prior to running
    `get-pip.py`. Additionally, if :ref:`setuptools` (or `distribute`_) is not
    already installed, `get-pip.py` will install :ref:`setuptools` for you.


setuptools
----------

If ``get-pip.py`` (see above) was not used to install :ref:`pip`, then
you can install or upgrade :ref:`setuptools` like so:

To install setuptools

::

$ pip install setuptools


To upgrade setuptools:

::

$ pip install --upgrade setuptools

   .. note::

      If you have distribute, this will upgrade to you distribute-0.7.X, which
      is just a wrapper, that depends on setuptools. The end result will be that
      you have distribute-0.7.X (which does nothing) *and* the latest setuptools
      installed.  If you'd prefer not to end up with the distribute wrapper,
      then instead, run ``$ pip uninstall distribute``, then ``$ pip install
      setuptools``.



wheel
-----

To install :ref:`wheel`, :ref:`pip` should already be installed (see section above).

To install or upgrade, run the following (which may require administrator access)::

 $ pip install --upgrade wheel


virtualenv
----------

To install :ref:`virtualenv`, :ref:`pip` should already be installed (see section above).

To install or upgrade, run the following (which may require administrator access)::

 $ pip install --upgrade virtualenv

----

.. [1] "Secure" in this context means using a modern browser or a
       tool like `curl` that verifies SSL certificates when downloading from
       https URLs.

.. _distribute: https://pypi.python.org/pypi/distribute
