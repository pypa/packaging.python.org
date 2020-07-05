.. _`PyPI mirrors and caches`:

================================
Package index mirrors and caches
================================

:Page Status: Incomplete
:Last Reviewed: 2014-12-24

.. contents:: Contents
   :local:


Mirroring or caching of PyPI can be used to speed up local package installation,
allow offline work, handle corporate firewalls or just plain Internet flakiness.

Three options are available in this area:

1. pip provides local caching options,
2. devpi provides higher-level caching option, potentially shared amongst
   many users or machines, and
3. bandersnatch provides a local complete mirror of all PyPI :term:`packages
   <Distribution Package>`.


Caching with pip
----------------

pip provides a number of facilities for speeding up installation by using local
cached copies of :term:`packages <Distribution Package>`:

1. `Fast & local installs
   <https://pip.pypa.io/en/latest/user_guide/#installing-from-local-packages>`_
   by downloading all the requirements for a project and then pointing pip at
   those downloaded files instead of going to PyPI.
2. A variation on the above which pre-builds the installation files for
   the requirements using `pip wheel
   <https://pip.readthedocs.io/en/latest/reference/pip_wheel.html>`_::

    $ pip wheel --wheel-dir=/tmp/wheelhouse SomeProject
    $ pip install --no-index --find-links=/tmp/wheelhouse SomeProject


Caching with devpi
------------------

devpi is a caching proxy server which you run on your laptop, or some other
machine you know will always be available to you. See the `devpi
documentation for getting started`__.

__ http://doc.devpi.net/latest/quickstart-pypimirror.html


Complete mirror with bandersnatch
----------------------------------

bandersnatch will set up a complete local mirror of all PyPI :term:`packages
<Distribution Package>` (externally-hosted packages are not mirrored). See
the `bandersnatch documentation for getting that going`__.

__ https://github.com/pypa/bandersnatch/

A benefit of devpi is that it will create a mirror which includes
:term:`packages <Distribution Package>` that are external to PyPI, unlike
bandersnatch which will only cache :term:`packages <Distribution Package>`
hosted on PyPI.
