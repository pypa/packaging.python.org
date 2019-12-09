================================
Creating and discovering plugins
================================

Often when creating a Python application or library you'll want the ability to
provide customizations or extra features via **plugins**. Because Python
packages can be separately distributed, your application or library may want to
automatically **discover** all of the plugins available.

There are three major approaches to doing automatic plugin discovery:

#. `Using naming convention`_.
#. `Using namespace packages`_.
#. `Using package metadata`_.


Using naming convention
=======================

If all of the plugins for your application follow the same naming convention,
you can use :func:`pkgutil.iter_modules` to discover all of the top-level
modules that match the naming convention. For example, `Flask`_ uses the
naming convention ``flask_{plugin_name}``. If you wanted to automatically
discover all of the Flask plugins installed:

.. code-block:: python

    import importlib
    import pkgutil

    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('flask_')
    }

If you had both the `Flask-SQLAlchemy`_ and `Flask-Talisman`_ plugins installed
then ``discovered_plugins`` would be:

.. code-block:: python

    {
        'flask_sqlachemy': <module: 'flask_sqlalchemy'>,
        'flask_talisman': <module: 'flask_talisman'>,
    }

Using naming convention for plugins also allows you to query the
Python Package Index's `simple API`_ for all packages that conform to your
naming convention.

.. _Flask: https://pypi.org/project/Flask/
.. _Flask-SQLAlchemy: https://pypi.org/project/Flask-SQLAlchemy/
.. _Flask-Talisman: https://pypi.org/project/flask-talisman
.. _simple API: https://www.python.org/dev/peps/pep-0503/#specification


Using namespace packages
========================

:doc:`Namespace packages <packaging-namespace-packages>` can be used to provide
a convention for where to place plugins and also provides a way to perform
discovery. For example, if you make the sub-package ``myapp.plugins`` a
namespace package then other :term:`distributions <Distribution Package>` can
provide modules and packages to that namespace. Once installed, you can use
:func:`pkgutil.iter_modules` to discover all modules and packages installed
under that namespace:

.. code-block:: python

    import importlib
    import pkgutil

    import myapp.plugins

    def iter_namespace(ns_pkg):
        # Specifying the second argument (prefix) to iter_modules makes the
        # returned name an absolute name instead of a relative one. This allows
        # import_module to work without having to do additional modification to
        # the name.
        return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(myapp.plugins)
    }

Specifying ``myapp.plugins.__path__`` to :func:`~pkgutil.iter_modules` causes
it to only look for the modules directly under that namespace. For example,
if you have installed distributions that provide the modules ``myapp.plugins.a``
and ``myapp.plugins.b`` then ``discovered_plugins`` in this case would be:

.. code-block:: python

    {
        'a': <module: 'myapp.plugins.a'>,
        'b': <module: 'myapp.plugins.b'>,
    }

This sample uses a sub-package as the namespace package (``myapp.plugins``), but
it's also possible to use a top-level package for this purpose (such as
``myapp_plugins``). How to pick the namespace to use is a matter of preference,
but it's not recommended to make your project's main top-level package
(``myapp`` in this case) a namespace package for the purpose of plugins, as one
bad plugin could cause the entire namespace to break which would in turn make
your project unimportable. For the "namespace sub-package" approach to work,
the plugin packages must omit the :file:`__init__.py` for your top-level
package directory (``myapp`` in this case) and include the namespace-package
style :file:`__init__.py` in the namespace sub-package directory
(``myapp/plugins``).  This also means that plugins will need to explicitly pass
a list of packages to :func:`setup`'s ``packages`` argument instead of using
:func:`setuptools.find_packages`.

.. warning:: Namespace packages are a complex feature and there are several
    different ways to create them. It's highly recommended to read the
    :doc:`packaging-namespace-packages` documentation and clearly document
    which approach is preferred for plugins to your project.

Using package metadata
======================

`Setuptools`_ provides `special support`_ for plugins. By
providing the ``entry_points`` argument to :func:`setup` in :file:`setup.py`
plugins can register themselves for discovery.

For example if you have a package named ``myapp-plugin-a`` and it includes
in its :file:`setup.py`:

.. code-block:: python

    setup(
        ...
        entry_points={'myapp.plugins': 'a = myapp_plugin_a'},
        ...
    )

Then you can discover and load all of the registered entry points by using
:func:`pkg_resources.iter_entry_points`:

.. code-block:: python

    import pkg_resources

    discovered_plugins = {
        entry_point.name: entry_point.load()
        for entry_point
        in pkg_resources.iter_entry_points('myapp.plugins')
    }

In this example, ``discovered_plugins`` would be:

.. code-block:: python

    {
        'a': <module: 'myapp_plugin_a'>,
    }

.. note:: The ``entry_point`` specification in :file:`setup.py` is fairly
    flexible and has a lot of options. It's recommended to read over the entire
    section on `entry points`_.

.. _Setuptools: http://setuptools.readthedocs.io
.. _special support:
.. _entry points:
    http://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins
