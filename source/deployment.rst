
========================
Development & Deployment
========================


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



.. _`PyPI mirrors an caches`:

PyPI mirrors and caches
=======================

::

  FIXME

  - local --find-links
  - tools like https://pypi.python.org/pypi/devpi-server


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

