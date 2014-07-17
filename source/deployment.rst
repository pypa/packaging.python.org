
========================
Development & Deployment
========================

:Page Status: Incomplete
:Last Reviewed: 2014-04-09


.. _`PyPI mirrors and caches`:

PyPI mirrors and caches
=======================

Mirroring or caching of PyPI can be used to speed up local package
installation, allow offline work, handle corporate firewalls or just plain
Internet flakiness.

Three options are available in this area:

1. pip provides local caching options,
2. devpi provides higher-level caching option, potentially shared amongst
   many users or machines, and
3. bandersnatch provides a local complete mirror of all packages on PyPI.


Caching with pip
----------------

pip provides a number of facilities for speeding up installation by using
local cached copies of packages:

1. `Fast & local installs
   <https://pip.pypa.io/en/latest/user_guide.html#fast-local-installs>`_ by
   downloading all the requirements for a project and then pointing pip at
   those downloaded files instead of going to PyPI.
2. A variation on the above which pre-builds the installation files for
   the requirements using `pip wheel
   <http://pip.readthedocs.org/en/latest/reference/pip_wheel.html>`_::

    $ pip wheel --wheel-dir=/tmp/wheelhouse SomePackage
    $ pip install --no-index --find-links=/tmp/wheelhouse SomePackage


Caching with devpi
------------------

devpi is a caching proxy server which you run on your laptop, or some other
machine you know will always be available to you. See the `devpi
documentation for getting started`__.

__ http://doc.devpi.net/latest/quickstart-pypimirror.html


Complete mirror with bandersnatch
----------------------------------

bandersnatch will set up a complete local mirror of all packages on PyPI (and
only those packages - externally-hosted packages are not mirrored). See the
`bandersnatch documentation for getting that going`__.

__ https://bitbucket.org/pypa/bandersnatch/overview

A benefit of devpi is that it will create a mirror which includes packages
that are external to PyPI, unlike bandersnatch which will only cache packages
hosted on PyPI.



.. _`Supporting multiple Python versions`:

Supporting multiple Python versions
===================================

::

  FIXME

  Useful projects/resources to reference:

  - six
  - tox
  - Travis and Shining Panda CI
  - Ned Batchelder's What's in Which version pages
    - http://nedbatchelder.com/blog/201310/whats_in_which_python_3.html
      - http://nedbatchelder.com/blog/201109/whats_in_which_python.html
  - Lennart Regebro's "Porting to Python 3"
  - the Python 3 porting how to in the main docs
  - cross reference to the stable ABI discussion
    in the binary extensions topic (once that exists)
  - mention version classifiers for distribution metadata



.. _`Patching & Forking`:

Patching & Forking
==================

::

  FIXME

  - locally patch 3rd-part projects to deal with unfixed bugs
     - old style pkg_resources "patch releases":  1.3-fork1
     - PEP440's local identifiers: http://www.python.org/dev/peps/pep-0440/#local-version-identifiers
  - fork and publish when you need to publish a project that depends on the fork
     (DONT use dependency links)



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

  puppet/salt/chef solutions



Fabric/SSH Solutions
====================

::

  FIXME

