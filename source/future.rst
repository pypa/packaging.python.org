==============================
The Future of Python Packaging
==============================

:Page Status: Incomplete [1]_
:Last Reviewed: 10-29-2013


The `distutils` cross-platform build and distribution system was added to
the Python standard library in late 1998. This means the current Python
software distribution ecosystem is almost 15 years old, which poses a
variety of challenges to successful evolution.

The current attempt really started when the decision was made to remove
the incomplete ``packaging`` project (also known as ``distutils2``) from
the standard library prior to the release of Python 3.3.

While ``distutils2`` itself is no longer under development, that project
laid the foundations for many of the current efforts (and also highlighted
the fact that, while the ``setup.py install`` is highly problematic,
``setup.py`` is significantly more reasonable as an interface to a build
system.


Overall Goal
============

The primary aim of Python Packaging Authority is to provide a relatively
easy to use software distribution infrastructure that is also fast,
reliable and reasonably secure.

"Reasonably secure" is the aim, since backwards compatibility constraints
prevent turning of some insecure legacy features (like API access over HTTP)
and the PyPI index operators only promise to deliver the bits to end users
that were uploaded by the original author. Whether or not those bits
themselves are malicious is ultimately up to end users to determine for
themselves.


Panels, Presentations & Other Articles
======================================

In addition to this document, there have been some talks and presentations
regarding current and future efforts related to packaging.

* PyCon US, March 2013

  * `Directions in Packaging Q & A Panel (aka "./setup.py install must die")
    <http://pyvideo.org/video/1731/panel-directions-for-packaging>`__

* PyCon AU, July 2013

  * `Nobody Expects the Python Packaging Authority
    <http://pyvideo.org/video/2197/nobody-expects-the-python-packaging-authority>`__

.. Repeated that at PyTexas, but can't find a video link for it

* Personal essays

  * `Nick Coghlan <http://python-notes.curiousefficiency.org/en/latest/pep_ideas/core_packaging_api.html>`__


Completed work
==============

* Core PyPI infrastructure relocated to OSU/OSL (with significantly
  increased resources)
* Core packaging projects collected under the Python Packaging Authority
  accounts on GitHub and BitBucket
* distribute merged back into setuptools, and setuptools development
  migrated to BitBucket
* PyPI supports clients using verified SSL with standard cert bundles
* PyPI forces web users over to SSL
* easy_install and pip use verified SSL by default
* setuptools/easy_install support additional hashes beyond md5
* PEP 8 cleanup (including clarification of what constitutes an internal API)
* Fastly CDN enabled for PyPI (donated)
* Restructured the installation documentation on pip-installer.org to ensure
  setuptools and pip are clearly the "base" of the bootstrapping hierarchy

Approved work (in progress)
===========================

* PEP 438 (Transitioning to PyPI file hosting)
* PEP 449 (Removal of the DNS based mirror autodiscovery)


Upcoming work (Python 3.4/pip 1.5 timeframe)
============================================

* PEP 453 (explicit pip bootstrapping in the standar library)
* improved handling of in-place pip upgrades on Windows
* improved handling of pip/setuptools/pkg_resources division of
  responsibility
* both pip and setuptools available as cross platform wheel files on PyPI
* Key requirement: "pip uninstall setuptools" must be supported &
  must not fundamentally break pip (but may disable installation from
  anything other than wheel files)


Upcoming work (post Python 3.4/pip 1.6 timeframe)
=================================================

Experimental versions of items mentioned in this section may already be
available.

* further proposals target pip 1.6 - decoupled from CPython release cycle
* metadata 2.0 (PEP 426/440)
* sdist 2.0 and wheel 1.1
* installation database format update
* revisit TUF-for-PyPI (that's more likely to be pip 1.7
  timeframe, though...)


Independent activities & miscellaneous suggestions
==================================================

* improved PyPI upload API (Donald's working on this)
* getting Warehouse to a point where it can be brought online as
  "pypi-next.python.org"
* TUF-for-PyPI exploration (the TUF folks seems to have this well in hand)
* improved local PyPI hosting (especially devpi)
* getting this guide up to scratch, so the python.org docs can refer to it
  as the primary resource for developers wanting to distribute or install
  Python packagers

.. [1] Many items need be linked and expanded so this can made more accessible to regular python users.
