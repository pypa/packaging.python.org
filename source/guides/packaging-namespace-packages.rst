.. _packaging-namespace-packages:

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
    pyproject.toml

And you use this package in your code like so::

    from mynamespace import subpackage_a
    from mynamespace import subpackage_b

Then you can break these sub-packages into two separate distributions:

.. code-block:: text

    mynamespace-subpackage-a/
        pyproject.toml
        src/
            mynamespace/
                subpackage_a/
                    __init__.py

    mynamespace-subpackage-b/
        pyproject.toml
        src/
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

There are currently two different approaches to creating namespace packages,
from which the latter is discouraged:

#. Use `native namespace packages`_. This type of namespace package is defined
   in :pep:`420` and is available in Python 3.3 and later. This is recommended if
   packages in your namespace only ever need to support Python 3 and
   installation via ``pip``.
#. Use `legacy namespace packages`_. This comprises `pkgutil-style namespace packages`_
   and `pkg_resources-style namespace packages`_.

Native namespace packages
-------------------------

Python 3.3 added **implicit** namespace packages from :pep:`420`. All that is
required to create a native namespace package is that you just omit
:file:`__init__.py` from the namespace package directory. An example file
structure (following :ref:`src-layout <setuptools:src-layout>`):

.. code-block:: text

    mynamespace-subpackage-a/
        pyproject.toml # AND/OR setup.py, setup.cfg
        src/
            mynamespace/ # namespace package
                # No __init__.py here.
                subpackage_a/
                    # Regular import packages have an __init__.py.
                    __init__.py
                    module.py

It is extremely important that every distribution that uses the namespace
package omits the :file:`__init__.py` or uses a pkgutil-style
:file:`__init__.py`. If any distribution does not, it will cause the namespace
logic to fail and the other sub-packages will not be importable.

The ``src-layout`` directory structure allows automatic discovery of packages
by most :term:`build backends <Build Backend>`. See :ref:`src-layout-vs-flat-layout`
for more information. If however you want to manage exclusions or inclusions of packages
yourself, this is possible to be configured in the top-level :file:`pyproject.toml`:

.. code-block:: toml

    [build-system]
    ...

    [tool.setuptools.packages.find]
    where = ["src/"]
    include = ["mynamespace.subpackage_a"]

    [project]
    name = "mynamespace-subpackage-a"
    ...

The same can be accomplished with a :file:`setup.cfg`:

.. code-block:: ini

    [options]
    package_dir =
        =src
    packages = find_namespace:

    [options.packages.find]
    where = src

Or :file:`setup.py`:

.. code-block:: python

    from setuptools import setup, find_namespace_packages

    setup(
        name='mynamespace-subpackage-a',
        ...
        packages=find_namespace_packages(where='src/', include=['mynamespace.subpackage_a']),
        package_dir={'': 'src'},
    )

:ref:`setuptools` will search the directory structure for implicit namespace
packages by default.

A complete working example of two native namespace packages can be found in
the `native namespace package example project`_.

.. _native namespace package example project:
    https://github.com/pypa/sample-namespace-packages/tree/master/native

.. note:: Because native and pkgutil-style namespace packages are largely
    compatible, you can use native namespace packages in the distributions that
    only support Python 3 and pkgutil-style namespace packages in the
    distributions that need to support Python 2 and 3.


Legacy namespace packages
-------------------------

These two methods, that were used to create namespace packages prior to :pep:`420`,
are now considered to be obsolete and should not be used unless you need compatibility
with packages already using this method. Also, :doc:`pkg_resources <setuptools:pkg_resources>`
has been deprecated.

To migrate an existing package, all packages sharing the namespace must be migrated simultaneously.

.. warning:: While native namespace packages and pkgutil-style namespace
    packages are largely compatible, pkg_resources-style namespace packages
    are not compatible with the other methods. It's inadvisable to use
    different methods in different distributions that provide packages to the
    same namespace.

pkgutil-style namespace packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python 2.3 introduced the :doc:`pkgutil <python:library/pkgutil>` module and the
:py:func:`python:pkgutil.extend_path` function. This can be used to declare namespace
packages that need to be compatible with both Python 2.3+ and Python 3. This
is the recommended approach for the highest level of compatibility.

To create a pkgutil-style namespace package, you need to provide an
:file:`__init__.py` file for the namespace package:

.. code-block:: text

    mynamespace-subpackage-a/
        src/
            pyproject.toml # AND/OR setup.cfg, setup.py
            mynamespace/
                __init__.py  # Namespace package __init__.py
                subpackage_a/
                    __init__.py  # Regular package __init__.py
                    module.py

The :file:`__init__.py` file for the namespace package needs to contain
the following:

.. code-block:: python

    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

**Every** distribution that uses the namespace package must include such
an :file:`__init__.py`. If any distribution does not, it will cause the
namespace logic to fail and the other sub-packages will not be importable.  Any
additional code in :file:`__init__.py` will be inaccessible.

A complete working example of two pkgutil-style namespace packages can be found
in the `pkgutil namespace example project`_.

.. _extend_path:
    https://docs.python.org/3/library/pkgutil.html#pkgutil.extend_path
.. _pkgutil namespace example project:
    https://github.com/pypa/sample-namespace-packages/tree/master/pkgutil


pkg_resources-style namespace packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:doc:`Setuptools <setuptools:index>` provides the `pkg_resources.declare_namespace`_ function and
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

    mynamespace-subpackage-a/
        src/
            pyproject.toml # AND/OR setup.cfg, setup.py
            mynamespace/
                __init__.py  # Namespace package __init__.py
                subpackage_a/
                    __init__.py  # Regular package __init__.py
                    module.py

The :file:`__init__.py` file for the namespace package needs to contain
the following:

.. code-block:: python

    __import__('pkg_resources').declare_namespace(__name__)

**Every** distribution that uses the namespace package must include such an
:file:`__init__.py`. If any distribution does not, it will cause the
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

.. _pkg_resources.declare_namespace:
    https://setuptools.readthedocs.io/en/latest/pkg_resources.html#namespace-package-support
.. _pkg_resources namespace example project:
    https://github.com/pypa/sample-namespace-packages/tree/master/pkg_resources
