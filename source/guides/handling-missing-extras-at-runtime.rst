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
recursively and check whether all are installed in the current environment.

This process is currently quite involved. An implementation can be found in
`packaging-problems #664 <packaging-problems-664_>`_, which is also made
available in the `hbutils <https://pypi.org/project/hbutils/>`_ package as
``hbutils.system.check_reqs``.
The possibility of offering a similar helper function in ``importlib.metadata``
or ``packaging`` themselves is still being discussed
(`packaging-problems #317 <packaging-problems-317_>`_).

With ``check_reqs`` included in your codebase or imported from ``hbutils``,
usage is as simple as:

.. code-block:: python

   extra_installed = check_reqs(["your-package[your-extra]"])

In contrast to the method above, this is typically done in :term:`LBYL` style
prior to importing the modules in question.
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

In each of the previous section's code snippets, we omitted what to actually do
when a missing extra has been identified.

The sensible answers to this questions are intimately linked to *where* in the
code the missing extra detection and import of the optional dependencies should
be performed, so we will look at our options for that as well.

Import at module level, raise exception
---------------------------------------

If your package is a library and the feature that requires the extra is
localized to a specific module or sub-package of your package, one option is to
just raise a custom exception indicating which extra would be required:

.. code-block:: python

   from dataclasses import dataclass

   @dataclass
   class MissingExtra(Exception):
     name: str

   ...

   # if extra not installed (see previous sections):
   raise MissingExtra("your-extra")

Library consumers will then have to either depend on your library with the
extra enabled or handle the possibility that imports of this specific module
fail (putting them in the same situation you were in). Because imports raising
custom exceptions is highly unusual, you should make sure to document this in a
**very** visible manner.

If your package is an application, making *you* the module's consumer, and you
want the application to work without the extra installed (i.e. the extra only
provides optional functionality for the application), you've similarly "pushed"
the problem of dealing with failing imports up one layer. At some point in the
module dependency you'll have to switch to a different strategy, lest your
application just crash with an exception on startup.


Import at module level, replace with exception-raising dummies
--------------------------------------------------------------

An alternative is to delay raising the exception until an actual attempt is
made to *use* the missing dependency. One way to do this is to assign "dummy"
functions that do nothing but raise it to the would-be imported names in the
event that the extra is missing:

.. code-block:: python

   # if extra installed (see previous sections):
   import some_function from optional_dependency

   ...

   # if extra not installed (see previous sections):
   def raise_missing_extra(*args, **kwargs):
     raise MissingExtra("your-extra")

   optional_dependency = raise_missing_extra

Note that, if imports are not mere functions but also objects like classes that
are subclassed from, the exact shape of the dummy objects can get more involved
depending on the expected usage, e.g.

.. code-block:: python

   class RaiseMissingExtra:
     def __init__(self, *args, **kwargs):
       raise MissingExtra("your-extra")

which would in turn not be sufficient for a class with class methods that might
be used without instantiating it, and so on.

By delaying the exception until attempted usage, an application installed
without the extra can start and run normally until the user tries to use
functionality requiring the extra, at which point you can handle it (e.g.
display an appropriate error message).

TODO mention that 3rd party library that does this automatically

Import at function/method level, raise exception
------------------------------------------------

Lastly, another way to delay exception raising until actual usage is to only
perform the check for whether the extra is installed and the corresponding
import when the functionality requiring it is actually used. E.g.:

.. code-block:: python

   def import_extra_module_if_avail():
     # surround this with the appropriate checks / error handling:
     ...
     import your_optional_dependency
     ...

     return your_optional_dependency

   ...

   def some_func_requiring_your_extra():
     try:
       optional_module = import_extra_module_if_avail()
     except MissingExtra:
       ...  # handle missing extra

     # now you can use functionality from the optional dependency, e.g.:
     optional_module.extra_func(...)

While this solution is more robust than the one from the preceding subsection,
it can take more effort to make it work with
:term:`static type checking <static type checker>`:
To correctly statically type a function returning a module, you'd have to
introduce an "artificial" type representing the latter, e.g.

.. code-block:: python

   from typing import cast, Protocol

   class YourOptionalModuleType(Protocol):
     extra_func: Callable[...]
     ...  # other objects you want to use

   def some_func_requiring_your_extra() -> YourOptionalModuleType:
     ...

     return cast(YourOptionalModuleType, optional_module)

An alternative would be to instead have functions that import and return only
the objects you actually need:

.. code-block:: python

   def import_extra_func_if_avail() -> Callable[...]:
     # surround this with the appropriate checks / error handling:
     ...
     from your_optional_dependency import extra_func
     ...

     return extra_func

But this can become verbose when you import a lot of names.


Other considerations
====================

TODO mention that you might want to provide a way for users to check
     availability without performing another action for the last 2 methods


------------------

.. _pkg_resources: https://setuptools.pypa.io/en/latest/pkg_resources.html

.. _packaging-problems-317: https://github.com/pypa/packaging-problems/issues/317

.. _packaging-problems-664: https://github.com/pypa/packaging-problems/issues/664
