===============
Packaging Guide
===============

:Page Status: Incomplete
:Last Reviewed: 2013-11-26


A guide to packaging python :term:`projects <Project>` into :term:`distributions
<Distribution>` and uploading them to :term:`PyPI <Python Package Index (PyPI)>`.


What is "packaging"?
====================

::

   FIXME

   What to cover:

   1. the uses of the term "packaging"
     a. creating/maintaining a setup.py
     b. the act of creating distributions (or packages)
   2. source vs built vs binary distributions
   3. Why package at all? what's the point? Is it just about PyPI?


Current packaging formats
=========================

::

   FIXME

   What to cover:

   1) sdist and wheel are the most relevant currently
   2) what defines an sdist? (sdist 2.0 is coming)
   3) wheel? why not egg? what was wrong with egg?


What tools to use
=================

:ref:`setuptools` and :ref:`wheel` (for ``bdist_wheel``)

::

   FIXME

   What to cover:

   1. Why setuptools (and not distutils)?
   2. What happened to distutils2? Can we be trusted again to give recommendations?  : )
   3. Is setuptools stable and supported by PyPA?
   4. Why the wheel project implementation of wheel? It's not a PyPA project?
   5. twine for uploading?


Getting started with setuptools
===============================

::

   FIXME

   What to cover:

   1. link to the setuptools "Getting Started" guide
      (which doesn't really exist atm, but needs to)
   2. Highlight which features are relevant *today*
      (ideally a link into setuptools)
   3. Explain how setuptools builds on top of distutils (maybe cover some hisory of why it's like this)
      (ideally a link into setuptools docs)
   4. link to the "Complete Guide to setup.py", which covers all subcommands and keywords (including distutils)
      (this does *not* exist atm, but ideally it exists in the setuptools docs, not in these docs)


Getting started with wheel
==========================

::

   FIXME

   What to cover:

   1. installing the wheel project
   2. using bdist_wheel (and why "pip wheel" is for a different use case and covered in the install guide)
   3. the pep425 tagging system
   4. "universal" wheels
   5. the current PyPI upload block on linux platform wheels (and why they're blocked)


Advanced Topics
===============

* :ref:`Wheel vs Egg`
* :ref:`Building RPMs for Python projects`
* :ref:`Building debs for Python projects`

