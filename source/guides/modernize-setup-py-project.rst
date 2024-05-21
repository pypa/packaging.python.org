.. _modernize-setup-py-project:


==============================================
How to modernize a ``setup.py`` based project?
==============================================


Should ``pyproject.toml`` be added?
===================================

A :term:`pyproject.toml` file is strongly recommended.
The presence of a :file:`pyproject.toml` file itself does not bring much. [#]_
What is actually strongly recommended is the ``[build-system]`` table in :file:`pyproject.toml`.

.. [#] Note that it has influence on the build isolation feature of pip,
    see below.


Should ``setup.py`` be deleted?
===============================

No, :file:`setup.py` can exist in a modern :ref:`setuptools` based project.
The :term:`setup.py` file is a valid configuration file for setuptools
that happens to be written in Python.
However, the following commands are deprecated and **MUST NOT** be run anymore,
and their recommended replacement commands should be used instead:

+---------------------------------+----------------------------------------+
| Deprecated                      | Recommendation                         |
+=================================+========================================+
| ``python setup.py install``     | ``python -m pip install .``            |
+---------------------------------+----------------------------------------+
| ``python setup.py develop``     | ``python -m pip install --editable .`` |
+---------------------------------+----------------------------------------+
| ``python setup.py sdist``       | ``python -m build``                    |
+---------------------------------+                                        |
| ``python setup.py bdist_wheel`` |                                        |
+---------------------------------+----------------------------------------+


For more details:

* :ref:`setup-py-deprecated`


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

For more details:

* :ref:`distributing-packages`
* :ref:`pyproject-build-system-table`
* :doc:`pip:reference/build-system/pyproject-toml`


How to handle additional build-time dependencies?
=================================================

On top of setuptools itself,
if :file:`setup.py` depends on other third-party libraries (outside of Python's standard library),
those must be listed in the ``requires`` list of the ``[build-system]`` table,
so that the build frontend knows to install them
when building the :term:`distributions <Distribution Package>`.

For example, a :file:`setup.py` file such as this:

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


requires a :file:`pyproject.toml` file like this (:file:`setup.py` stays unchanged):

.. code:: toml

    [build-system]
    requires = [
        "setuptools",
        "some-build-toolkit",
    ]
    build-backend = "setuptools.build_meta"


For more details:

* :ref:`pyproject-build-system-table`


What is the build isolation feature?
====================================

Build frontends typically create an ephemeral virtual environment
where they install only the build dependencies (and their dependencies)
that are listed under ``build-system.requires``
and trigger the build in that environment.

For some projects this isolation is unwanted and it can be deactivated as follows:

* ``python -m build --no-isolation``
* ``python -m pip install --no-build-isolation``

For more details:

* :doc:`pip:reference/build-system/pyproject-toml`


How to handle packaging metadata?
=================================

All static metadata can optionally be moved to a ``[project]`` table in :file:`pyproject.toml`.

For example, a :file:`setup.py` file such as this:

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


Read :ref:`pyproject-project-table` for the full specification
of the content allowed in the ``[project]`` table.


How to handle dynamic metadata?
===============================

If some packaging metadata fields are not static
they need to be listed as ``dynamic`` in this ``[project]`` table.

For example, a :file:`setup.py` file such as this:

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


For more details:

* :ref:`declaring-project-metadata-dynamic`


What if something that can not be changed expects a ``setup.py`` file?
======================================================================

For example, a process exists that can not be changed easily
and it needs to execute a command such as ``python setup.py --name``.

It is perfectly fine to leave a :file:`setup.py` file in the project source tree
even after all its content has been moved to :file:`pyproject.toml`.
This file can be as minimalistic as this:

.. code:: python

    import setuptools

    setuptools.setup()


Where to read more about this?
==============================

* :ref:`pyproject-toml-spec`
* :doc:`pip:reference/build-system/pyproject-toml`
* :doc:`setuptools:build_meta`
