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

TODO example

TODO mention it doesn't check versions, so a bit dangerous


Using ``pkg_resources``
=======================

The now-deprecated ``pkg_resources`` package (part of the ``setuptools``
distribution) provides a ``require`` function that you can use to check if a
given optional dependency of your package is installed or not:


.. code-block:: python

   from pkg_resources import require, DistributionNotFound, VersionConflict

   try:
     require(["your-package-name[your-extra]"])
   except DistributionNotFound:
     ...  # handle package(s) not being installed at all
   except VersionConflict:
     ...  # handle version mismatches

Unfortunately, no replacement for this functionality exists in
``pkg_resources``'s successor packages yet
(`packaging-problems #664 <packaging-problems #664>`_).


------------------

.. _packaging-problems-664: https://github.com/pypa/packaging-problems/issues/664
