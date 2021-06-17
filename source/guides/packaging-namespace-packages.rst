============================
Packaging namespace packages
============================

Namespace packages allow you to split the sub-packages and modules within a
single :term:`package <Import Package>` across multiple, separate
:term:`distribution packages <Distribution Package>` (referred to as
**distributions** in this document to avoid ambiguity). For example, if you
have the following package structure:

.. code-block:: text
    
    mynamespace/
        __init__.py
        subpackage_a/
            __init__.py
            ...
        subpackage_b/
            __init__.py
            ...
        module_b.py
    setup.py

And you use this package in your code like so::

    from mynamespace import subpackage_a
    from mynamespace import subpackage_b

Then you can break these sub-packages into two separate distributions:

.. code-block:: text
    
    mynamespace-subpackage-a/
        setup.py
        mynamespace/
            subpackage_a/
                __init__.py

    mynamespace-subpackage-b/
        setup.py
        mynamespace/
            subpackage_b/
                __init__.py
            module_b.py

Each sub-package can now be separately installed, used, and versioned.

Namespace packages can be useful for a large collection of loosely-related
packages (such as a large corpus of client libraries for multiple products from
a single company). However, namespace packages come with several caveats and
are not appropriate in all cases. A simple alternative is to use a prefix on
all of your distributions such as ``import mynamespace_subpackage_a`` (you
could even use ``import mynamespace_subpackage_a as subpackage_a`` to keep the
import object short).


Creating a namespace package
============================

There are currently three different approaches to creating namespace packages:

#. Use `native namespace packages`_. This type of namespace package is defined
   in :pep:`420` and is available in Python 3.3 and later. This is recommended if
   packages in your namespace only ever need to support Python 3 and
   installation via ``pip``.
#. Use `pkgutil-style namespace packages`_. This is recommended for new
   packages that need to support Python 2 and 3 and installation via both
   ``pip`` and ``python setup.py install``.
#. Use `pkg_resources-style namespace packages`_. This method is recommended if
   you need compatibility with packages already using this method or if your
   package needs to be zip-safe.

.. warning:: While native namespace packages and pkgutil-style namespace
    packages are largely compatible, pkg_resources-style namespace packages
    are not compatible with the other methods. It's inadvisable to use
    different methods in different distributions that provide packages to the
    same namespace.

Native namespace packages
-------------------------

Python 3.3 added **implicit** namespace packages from :pep:`420`. All that is
required to create a native namespace package is that you just omit
:file:`__init__.py` from the namespace package directory. An example file
structure:

.. code-block:: text

    setup.py
    mynamespace/
        # No __init__.py here.
        subpackage_a/
            # Sub-packages have __init__.py.
            __init__.py
            module.py

It is extremely important that every distribution that uses the namespace
package omits the :file:`__init__.py` or uses a pkgutil-style
:file:`__init__.py`. If any distribution does not, it will cause the namespace
logic to fail and the other sub-packages will not be importable.

Because ``mynamespace`` doesn't contain an :file:`__init__.py`,
:func:`setuptools.find_packages` won't find the sub-package. You must
use :func:`setuptools.find_namespace_packages` instead or explicitly
list all packages in your :file:`setup.py`. For example:

.. code-block:: python

    from setuptools import setup, find_namespace_packages

    setup(
        name='mynamespace-subpackage-a',
        ...
        packages=find_namespace_packages(include=['mynamespace.*'])
    )

A complete working example of two native namespace packages can be found in
the `native namespace package example project`_.

.. _native namespace package example project:
    https://github.com/pypa/sample-namespace-packages/tree/master/native

.. note:: Because native and pkgutil-style namespace packages are largely
    compatible, you can use native namespace packages in the distributions that
    only support Python 3 and pkgutil-style namespace packages in the
    distributions that need to support Python 2 and 3.

pkgutil-style namespace packages
--------------------------------

Python 2.3 introduced the `pkgutil`_ module and the
`extend_path`_ function. This can be used to declare namespace
packages that need to be compatible with both Python 2.3+ and Python 3. This
is the recommended approach for the highest level of compatibility.

To create a pkgutil-style namespace package, you need to provide an
:file:`__init__.py` file for the namespace package:

.. code-block:: text

    setup.py
    mynamespace/
        __init__.py  # Namespace package __init__.py
        subpackage_a/
            __init__.py  # Sub-package __init__.py
            module.py

The :file:`__init__.py` file for the namespace package needs to contain
**only** the following:

.. code-block:: python

    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

**Every** distribution that uses the namespace package must include an
identical :file:`__init__.py`. If any distribution does not, it will cause the
namespace logic to fail and the other sub-packages will not be importable.  Any
additional code in :file:`__init__.py` will be inaccessible.

A complete working example of two pkgutil-style namespace packages can be found
in the `pkgutil namespace example project`_.

.. _pkgutil: https://docs.python.org/3/library/pkgutil.html
.. _extend_path:
    https://docs.python.org/3/library/pkgutil.html#pkgutil.extend_path
.. _pkgutil namespace example project:
    https://github.com/pypa/sample-namespace-packages/tree/master/pkgutil


pkg_resources-style namespace packages
--------------------------------------

`Setuptools`_ provides the `pkg_resources.declare_namespace`_ function and
the ``namespace_packages`` argument to :func:`~setuptools.setup`. Together
these can be used to declare namespace packages. While this approach is no
longer recommended, it is widely present in most existing namespace packages.
If you are creating a new distribution within an existing namespace package that
uses this method then it's recommended to continue using this as the different
methods are not cross-compatible and it's not advisable to try to migrate an
existing package.

To create a pkg_resources-style namespace package, you need to provide an
:file:`__init__.py` file for the namespace package:

.. code-block:: text

    setup.py
    mynamespace/
        __init__.py  # Namespace package __init__.py
        subpackage_a/
            __init__.py  # Sub-package __init__.py
            module.py

The :file:`__init__.py` file for the namespace package needs to contain
**only** the following:

.. code-block:: python

    __import__('pkg_resources').declare_namespace(__name__)

**Every** distribution that uses the namespace package must include an
identical :file:`__init__.py`. If any distribution does not, it will cause the
namespace logic to fail and the other sub-packages will not be importable.  Any
additional code in :file:`__init__.py` will be inaccessible.

.. note:: Some older recommendations advise the following in the namespace
    package :file:`__init__.py`:

    .. code-block:: python

        try:
            __import__('pkg_resources').declare_namespace(__name__)
        except ImportError:
            __path__ = __import__('pkgutil').extend_path(__path__, __name__)

    The idea behind this was that in the rare case that setuptools isn't
    available packages would fall-back to the pkgutil-style packages. This
    isn't advisable because pkgutil and pkg_resources-style namespace packages
    are not cross-compatible. If the presence of setuptools is a concern
    then the package should just explicitly depend on setuptools via
    ``install_requires``.

Finally, every distribution must provide the ``namespace_packages`` argument
to :func:`~setuptools.setup` in :file:`setup.py`. For example:

.. code-block:: python

    from setuptools import find_packages, setup

    setup(
        name='mynamespace-subpackage-a',
        ...
        packages=find_packages()
        namespace_packages=['mynamespace']
    )

A complete working example of two pkg_resources-style namespace packages can be found
in the `pkg_resources namespace example project`_.

.. _setuptools: https://setuptools.readthedocs.io
.. _pkg_resources.declare_namespace:
    https://setuptools.readthedocs.io/en/latest/setuptools.html#namespace-packages
.. _pkg_resources namespace example project:
    https://github.com/pypa/sample-namespace-packages/tree/master/pkg_resources
