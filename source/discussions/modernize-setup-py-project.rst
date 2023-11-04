.. _modernize-setup-py-project:


==============================================
How to modernize a ``setup.py`` based project?
==============================================


Must there be a ``pyproject.toml`` file?
========================================

Yes. This is strongly recommended.
The presence of a :file:`pyproject.toml` file itself does not bring much.
What is necessary is the ``[build-system]`` table first,
and then the ``[project]`` table.


Must ``setup.py`` be deleted?
=============================

No. There is no such requirement for a modern :ref:`setuptools` based project.
The :term:`setup.py` is a valid configuration file for setuptools
that happens to be written in Python.
However the following deprecated commands **MUST NOT** be run anymore,
and their recommended replacement commands can be used instead:

+---------------------------------+----------------------------------------+
| Deprecated                      | Current recommendation                 |
+=================================+========================================+
| ``python setup.py install``     | ``python -m pip install .``            |
+---------------------------------+----------------------------------------+
| ``python setup.py develop``     | ``python -m pip install --editable .`` |
+---------------------------------+----------------------------------------+
| ``python setup.py sdist``       | ``python -m build``                    |
+---------------------------------+                                        |
| ``python setup.py bdist_wheel`` |                                        |
+---------------------------------+----------------------------------------+

.. todo::

    Add link to the "Is setup.py deprecated?" page for details.


Where to start?
===============

The :term:`project` must contain a :file:`pyproject.toml` file at the root of its source tree
that contains a ``[build-system]`` table like so:

.. code:: toml

    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"


This is the standardized method of letting :term:`build frontends <Build Frontend>` know
that :ref:`setuptools` is the :term:`build backend <Build Backend>` for this project.

Note that the presence of a :file:`pyproject.toml` file (even if empty)
triggers :ref:`pip` to change its default behavior to use *build isolation*.


How to handle additional build-time dependencies?
=================================================

On top of setuptools itself,
if :file:`setup.py` depends on other third-party libraries (outside of Python's standard library),
those must be listed in the ``requires`` list of the ``[build-system]`` table,
so that the build frontend knows to install them
when building the :term:`distributions <Distribution Package>`.

For example a :file:`setup.py` file such as this:

.. code:: python

    import setuptools
    import some_build_toolkit  # comes from the `some-build-toolkit` library

    def get_version():
        version = some_build_toolkit.compute_version()
        return version

    setuptools.setup(
        name="my-project",
        version=get_version(),
    )


requires a :file:`pyproject.toml` file like this:

.. code:: toml

    [build-system]
    requires = [
        "setuptools",
        "some-build-toolkit",
    ]
    build-backend = "setuptools.build_meta"


What is the build isolation feature?
====================================

Build frontends typically create an ephemeral virtual environment
where they install only the build dependencies (and their dependencies)
that are listed under ``build-sytem.requires``
and trigger the build in that environment.

For some projects this isolation is unwanted and it can be deactivated as follows:

* ``python -m build --no-isolation``
* ``python -m install --no-build-isolation``


How to handle packaging metadata?
=================================

All static metadata can be moved to a ``[project]`` table in the :file:`pyproject.toml` file.

For example a :file:`setup.py` file such as this:

.. code:: python

    import setuptools

    setuptools.setup(
        name="my-project",
        version="1.2.3",
    )


can be entirely replaced by a :file:`pyproject.toml` file like this:

.. code:: toml

    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "my-project"
    version = "1.2.3"


Read :ref:`declaring-project-metadata` for the full specification
of the content allowed in the ``[project]`` table.


How to handle dynamic metadata?
===============================

If some packaging metadata fields are not static
they need to be listed as ``dynamic`` in this ``[project]`` table.

For example a :file:`setup.py` file such as this:

.. code:: python

    import setuptools
    import some_build_toolkit

    def get_version():
        version = some_build_toolkit.compute_version()
        return version

    setuptools.setup(
        name="my-project",
        version=get_version(),
    )


can be modernized as follows:

.. code:: toml

    [build-system]
    requires = [
        "setuptools",
        "some-build-toolkit",
    ]
    build-backend = "setuptools.build_meta"

    [project]
    name = "my-project"
    dynamic = ["version"]


.. code:: python

    import setuptools
    import some_build_toolkit

    def get_version():
        version = some_build_toolkit.compute_version()
        return version

    setuptools.setup(
        version=get_version(),
    )


What if something that can not be changed expects a ``setup.py`` file?
======================================================================

Maybe there is a process somewhere that can not be changed and
that wants to run a command such as ``python setup.py --name``.

It is perfectly fine to leave a :file:`setup.py` file in the project source tree
even after all its content has been moved to :file:`pyproject.toml`.
This file can be as minimalistic as this:

.. code:: python

    import setuptools

    setuptools.setup()


Where to read more about this?
==============================

* :doc:`setuptools:build_meta`
