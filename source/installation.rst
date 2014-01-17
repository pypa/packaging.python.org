==========================
Installing Python Packages
==========================

:Page Status: Incomplete
:Last Reviewed: 2013-12-01


A guide to installing python :term:`packages <Package (Meaning #2)>` from
:term:`PyPI <Python Package Index (PyPI)>` and other sources.


Goals and Workflow
==================

Managing packages
-----------------

Most often we use 3rd party python packages and modules to help build our
own software, or need them to install them as part of working with others' code.

Simplistically, you could simply copy relevant python source files within
your own code's folder (sometimes known as *vendoring*), however most often
this practice is not manageable in the long term, or when faced with
dealing with many projects.

**pip** is used to install python packages from PyPI automatically
for us, allowing us to manage our dependencies on other python packages easily.


Managing projects
-----------------

:ref:`pip` installs a package into its surrounding python environment. Normally,
this might be your system's Python, available at all times. When dealing
with only a few projects, or very few packages, this can be just fine - those
installed packages will then be available everywhere.

You may find when working on more projects, with larger sets of package
dependencies, this can become unmanageable. It can be hard to track which
package "belongs" to which project, or if a package is used by more than one;
different projects may want different versions of a package, creating a conflict.

**virtualenv** is a tool used to create isolated python environments. You would
most often create one :ref:`virtualenv` environment per project; ``pip``
will then install packages into only that environment, ensuring each
project maintains its own isolated set of packages to use. Different
environments may be "activated" and "deactivated" to switch between projects.


Introduction to PyPI
====================

The Python Package Index (PyPI) is the canonical online resource used to
search for and download python packages provided by the community. Anyone
may register, upload and download packages. You can view it on the web at
http://pypi.python.org/

A page for each python project lists information and downloads for that
project. `Django`_'s, for example, has information on where to learn more
about the project, and lists two downloads at the time of writing; one for a
wheel and one for its source distribution. A listing of Categories below,
also known as `classifiers`_ can hint at python versions the package supports
and what sort of software it is.

To register and upload your own packages to PyPI, you can `register`_ a user
account in order to do so. More information is provided on later in this guide.


.. _Django: https://pypi.python.org/pypi/Django
.. _classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
.. _register: https://pypi.python.org/pypi?%3Aaction=register_form

What tools to use
=================

The :term:`PyPA <Python Packaging Authority (PyPA)>` currently :doc:`recommends
<current>` :ref:`pip` for package installation and :ref:`virtualenv` for 
managing virtual environments.

Although some other installation tools exist, ``pip`` is currently regarded
as modern, widely compatible with most distributed python packages, and is
also :ref:`included <PEP453s>` with Python 3.4. An older tool, ``easy_install``,
comes with setuptools but is generally inferior to ``pip``. One exception is
that it is capable of installing Egg files, should you come across them, while
pip is not.

Virtualenv is easily the most widely used tool for creating virtual
environments. One may have noticed that Python 3.3 includes the `venv`_
module, which looks similar. Although it implements the same underlying concept,
``pyvenv`` has less features and niceties that make ``virtualenv`` a great
user-facing tool, and could be said to be slightly lower-level.

::

   FIXME

   What to cover:

   1) Why virtualenv (what about pyenv? buildout?)
   2) Why pick *one* installer to recommend?
       the rationale from PEP453
   3) why pip?
      - feature breakdown in the "pip vs easy_install" chart in the additional section weighs in pip's favor
      - Decoupled from packaging tools.
      - what easy_install bugs mentioned in PEP453 does pip address?
   4) mention easy_install for the Yes cases in the "pip vs easy_install" chart.

.. pyvenv: http://docs.python.org/dev/library/venv.html


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


What is "installation"?
=======================

::

   FIXME

   What to cover:

   1. distutils/sysconfig schemes
   2. global vs user installs
   3. virtual environments


Related Additional Topics
=========================

* :ref:`pip vs easy_install`
* :ref:`easy_install and sys.path`
* :ref:`Installing on Debian/Ubuntu`
* :ref:`Installing on CentOS/RedHat`
* :ref:`Installing on Windows`
* :ref:`Installing on OSX`
* :ref:`NumPy and the Science Stack`
