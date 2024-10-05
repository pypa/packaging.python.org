.. _handling-missing-extras-at-runtime:

============================================================
Handling missing optional dependencies ("extras") at runtime
============================================================

If your package has :ref:`optional dependencies ("extras")
<metadata_provides_extra>` which the package consumer hasn't installed, the
default outcome is an ordinary `ModuleNotFoundError` exception being raised at
the first attempted import of a missing module.

This can make for a bad user experience, because there is no guidance about why
the module is missing - users might think they've found a bug. If you're not
careful, it can even make your package unusable without the extras installed,
e.g. if your package is a library that imports the affected modules from the
top-level module or from the application entry point if it's an application.

As of the time of writing, there is no *great* way to handle this issue in
the Python packaging ecosystem, but there are a few options that might be
better than nothing:


Overall approach
================

TODO General guidance about how to isolate imports in question

TODO Optimistic vs pessimistic handling?


Handling failing imports
========================

The perhaps simplest option, which is also in line with the :term:`EAFP`
principle, is to just import your optional dependency modules as normal and
handle the relevant exceptions if the import fails:

.. code-block:: python

   try:
     import your_optional_dependency
   except ModuleNotFoundError:
     ...  # handle missing dependency

However, this can lead to difficult-to-debug errors when
``your_optional_dependency`` *is* installed, but at the wrong version (e.g.
because another installed package depends on it with a wider version
requirement than specified by your extra).


Using ``pkg_resources`` (deprecated)
====================================

The now-deprecated :ref:`pkg_resources <ResourceManager API>` package (part of
the ``setuptools`` distribution) provides a ``require`` function that you can
use to check if a given optional dependency of your package is installed or
not:

.. :: TODO ask setuptools to add labels for pkg_resources & require, then link
      properly


.. code-block:: python

   from pkg_resources import require, DistributionNotFound, VersionConflict

   try:
     require(["your-package-name[your-extra]"])
   except DistributionNotFound:
     ...  # handle package(s) not being installed at all
   except VersionConflict:
     ...  # handle version mismatches

Unfortunately, no drop-in replacement for this functionality exists in
``pkg_resources``'s "official" successor packages yet
(`packaging-problems #317 <packaging-problems-317_>`_).


Using 3rd-party libraries
=========================

In response to the aforementioned lack of a replacement for
``pkg_resources.require``, at least one 3rd party implementation of this
functionality using only the ``packaging`` and ``importlib.metadata`` modules
has been created (`packaging-problems #664 <packaging-problems-664_>`_) and
made available in the 3rd-party `hbutils <https://pypi.org/project/hbutils/>`_
package as ``hbutils.system.check_reqs``.


------------------

.. _packaging-problems-317: https://github.com/pypa/packaging-problems/issues/317

.. _packaging-problems-664: https://github.com/pypa/packaging-problems/issues/664

