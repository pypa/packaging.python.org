.. _distribution-package-vs-import-package:

=======================================
Distribution package vs. import package
=======================================

A number of different concepts are commonly referred to by the word
"package". This page clarifies the differences between two distinct but
related meanings in Python packaging, "distribution package" and "import
package".

What's a distribution package?
==============================

A distribution package is a piece of software that you can install.
Most of the time, this is synonymous with "project". When you type ``pip
install pkg``, or when you write ``dependencies = ["pkg"]`` in your
``pyproject.toml``, ``pkg`` is the name of a distribution package. When
you search or browse the PyPI_, the most widely known centralized source for
installing Python libraries and tools, what you see is a list of distribution
packages. Alternatively, the term "distribution package" can be used to
refer to a specific file that contains a certain version of a project.

Note that in the Linux world, a "distribution package",
most commonly abbreviated as "distro package" or just "package",
is something provided by the system package manager of the `Linux distribution <distro_>`_,
which is a different meaning.


What's an import package?
=========================

An import package is a Python module. Thus, when you write ``import
pkg`` or ``from pkg import func`` in your Python code, ``pkg`` is the
name of an import package. More precisely, import packages are special
Python modules that can contain submodules. For example, the ``numpy``
package contains modules like ``numpy.linalg`` and
``numpy.fft``. Usually, an import package is a directory on the file
system, containing modules as ``.py`` files and subpackages as
subdirectories.

You can use an import package as soon as you have installed a distribution
package that provides it.


What are the links between distribution packages and import packages?
=====================================================================

Most of the time, a distribution package provides one single import
package (or non-package module), with a matching name. For example,
``pip install numpy`` lets you ``import numpy``.

However, this is only a convention. PyPI and other package indices *do not
enforce any relationship* between the name of a distribution package and the
import packages it provides. (A consequence of this is that you cannot blindly
install the PyPI package ``foo`` if you see ``import foo``; this may install an
unintended, and potentially even malicious package.)

A distribution package could provide an import package with a different
name. An example of this is the popular Pillow_ library for image
processing. Its distribution package name is ``Pillow``, but it provides
the import package ``PIL``. This is for historical reasons: Pillow
started as a fork of the PIL library, thus it kept the import name
``PIL`` so that existing PIL users could switch to Pillow with little
effort. More generally, a fork of an existing library is a common reason
for differing names between the distribution package and the import
package.

On a given package index (like PyPI), distribution package names must be
unique. On the other hand, import packages have no such requirement.
Import packages with the same name can be provided by several
distribution packages. Again, forks are a common reason for this.

Conversely, a distribution package can provide several import packages,
although this is less common. An example is the attrs_ distribution
package, which provides both an ``attrs`` import package with a newer
API, and an ``attr`` import package with an older but supported API.


How do distribution package names and import package names compare?
===================================================================

Import packages should have valid Python identifiers as their name (the
:ref:`exact rules <python:identifiers>` are found in the Python
documentation) [#non-identifier-mod-name]_. In particular, they use underscores ``_`` as word
separator and they are case-sensitive.

On the other hand, distribution packages can use hyphens ``-`` or
underscores ``_``. They can also contain dots ``.``, which is sometimes
used for packaging a subpackage of a :ref:`namespace package
<packaging-namespace-packages>`. For most purposes, they are insensitive
to case and to ``-`` vs.  ``_`` differences, e.g., ``pip install
Awesome_Package`` is the same as ``pip install awesome-package`` (the
precise rules are given in the :ref:`name normalization specification
<name-normalization>`).



---------------------------

.. [#non-identifier-mod-name] Although it is technically possible
   to import packages/modules that do not have a valid Python identifier as
   their name, using :doc:`importlib <python:library/importlib>`,
   this is vanishingly rare and strongly discouraged.


.. _distro: https://en.wikipedia.org/wiki/Linux_distribution
.. _PyPI: https://pypi.org
.. _Pillow: https://pypi.org/project/Pillow
.. _attrs: https://pypi.org/project/attrs
