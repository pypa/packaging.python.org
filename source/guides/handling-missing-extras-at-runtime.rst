.. _handling-missing-extras-at-runtime:

============================================================
Handling missing optional dependencies ("extras") at runtime
============================================================

If your package has :ref:`optional dependencies ("extras")
<metadata_provides_extra>` which the package consumer hasn't installed, the
default outcome is an ordinary :exc:`ModuleNotFoundError` exception being raised
at the first attempted import of a missing module.

This can make for a bad user experience, because there is no guidance about why
the module is missing - users might think they've found a bug. If you're not
careful, it can even make your package unusable without the extras installed,
e.g. if your package is a library that imports the affected modules from the
top-level module or if it's an application that imports them unconditionally.

As of the time of writing, there is no *great* way to handle this issue in
the Python packaging ecosystem, but there are a few options that might be
better than nothing:

Detecting missing extras
========================

We first consider how to *detect* if an extra is missing, leaving what to do
about it for the next section.

Trying to import and handling failure
-------------------------------------

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


Using ``importlib.metadata`` and ``packaging``
----------------------------------------------

As a safer alternative that does check whether the optional dependencies are
installed at the correct versions, :py:mod:`importlib.metadata` and
:ref:`packaging` can be used to iterate through the extra's requirements
recursively and check whether all are installed in the current environment
(based on `code <hbutils-snippet_>`_ from the `hbutils`_ library):

.. code-block:: python

   # Adapted from (see there for copyright & license):
   # https://github.com/HansBug/hbutils/blob/927b0757449a781ce8e30132f26b06089a24cd71/LICENSE
   # SPDX-License-Identifier: Apache-2.0

   from collections.abc import Iterable
   from importlib.metadata import PackageNotFoundError, distribution, metadata

   from packaging.metadata import Metadata, RawMetadata
   from packaging.requirements import Requirement


   def check_reqs(req_strs: Iterable[str]) -> bool:
     return all(
       _check_req_recursive(req)
       for req_str in req_strs
       if not (req := Requirement(req_str)).marker or req.marker.evaluate()
     )


   def _check_req_recursive(req: Requirement) -> bool:
     try:
       version = distribution(req.name).version
     except PackageNotFoundError:
       return False  # req not installed

     if not req.specifier.contains(version):
       return False  # req version does not match

     req_metadata = Metadata.from_raw(metadata(req.name).json, validate=False)
     for child_req in req_metadata.requires_dist or []:
       # A dependency is only required to be present if ...
       if (
         not child_req.marker  # ... it doesn't have a marker
         or child_req.marker.evaluate()  # ... its marker matches our env
         or any(  # ... its marker matches our env given one of our extras
           child_req.marker.evaluate({"extra": extra}) for extra in req.extras
         )
       ):
         if not _check_req_recursive(child_req):
           return False

     return True


   # Perform check, e.g.:
   extra_installed = check_reqs(["your-package[your-extra]"])

The possibility of offering a helper function similar to ``check_reqs`` in
``importlib.metadata`` or ``packaging`` themselves is still being discussed
(`packaging-problems #317 <packaging-problems-317_>`_).

In contrast to the method above, this check is typically done in :term:`LBYL`
style prior to importing the modules in question.
In principle, it could also be done after the imports succeeded just to check
the version, in which case the imports themselves would have to be wrapped in a
``try``-``except`` block to handle the possibility of not being installed at
all.


Using ``pkg_resources`` (deprecated)
------------------------------------

.. attention::

   ``pkg_resources`` is **deprecated** and the PyPA **strongly discourages**
   its use.
   This method is included in this guide for completeness's sake and only until
   functionality with a similar level of convenience exists in
   ``importlib.metadata`` or ``packaging``.

The now-deprecated `pkg_resources <pkg_resources_>`_ package (part of the
``setuptools`` distribution) provides a ``require`` function, which was the
inspiration for ``check_reqs`` from the previous section. Its usage is quite
similar to ``check_reqs`` but not identical:

.. code-block:: python

   from pkg_resources import require, DistributionNotFound, VersionConflict

   try:
     require(["your-package-name[your-extra]"])
   except DistributionNotFound:
     ...  # handle package(s) not being installed at all
   except VersionConflict:
     ...  # handle version mismatches


Handling missing extras
=======================

Where and how to embed the detection of missing extras in a package and what
actions to take upon learning the outcome depends on the specifics of both the
package and feature requiring the extra.
Some common options are:

- Raise a custom exception that includes the name of the missing extra.
- In applications, show an error message when an attempt is made to use the
  feature that requires the extra.
- In libraries, provide a function that lets library consumers query which
  features are available.

... and probably more.


------------------

.. _hbutils-snippet: https://github.com/HansBug/hbutils/blob/927b0757449a781ce8e30132f26b06089a24cd71/hbutils/system/python/package.py#L171-L242

.. _hbutils: https://pypi.org/project/hbutils/

.. _pkg_resources: https://setuptools.pypa.io/en/latest/pkg_resources.html

.. _packaging-problems-317: https://github.com/pypa/packaging-problems/issues/317
