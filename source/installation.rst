==================
Installation Guide
==================

:Page Status: Incomplete
:Last Reviewed: 2013-11-03

A guide to installing python :term:`distributions <Distribution>`.


What is "installation"?
=======================

::

   FIXME

   What to cover:

   1. distutils/sysconfig schemes
   2. global vs user installs
   3. virtual environments


Introduction to PyPI
====================

::

   FIXME


What tools to use
=================

:ref:`virtualenv` and :ref:`pip`

::

   FIXME

   What to cover:

   1) Why virtualenv (what about pyenv? buildout?)
   2) Why pip (compare pip vs easy_install in detail); use rationale from PEP453
   3) When to use easy_install ([multi-version] eggs)


Getting started with virtualenv
===============================

::

   FIXME


Getting started with pip
========================

::

   FIXME

   What to cover:

   1. link to:
      - pip's quickstart (which needs improvement)
      - pip's feature overview (which doesn't exist atm)
      - pip's cookbook
      - pip's guide on "wheel caching"
      - pip's usage (which needs better subcommand descriptions and more examples)


Advanced Topics
===============

::

   FIXME

   What to cover:

   1. When to use yum/apt OS packages
   2. debian/unbuntu considerations (dist-packages and it's /usr and /usr/local schemes)
   4. centos/redhat considerations (just one global scheme, unlike debian)
   5. the world of OSX (homebrew, macports etc...)
   6. windows installation considerations
   7. "deploying" python software in the real world
   8. easy_install's pth sys.path modification (that can override --user installs)

