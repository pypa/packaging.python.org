.. _setup-py-deprecated:


===========================
Is ``setup.py`` deprecated?
===========================

No, :term:`setup.py` is not deprecated,
it is a valid configuration file for :ref:`setuptools`
that happens to be written in Python, instead of in *TOML* for example
(a similar practice is used by other tools
like *nox* and its :file:`nox.py` configuration file,
or *pytest* and :file:`conftest.py`).

And of course *setuptools* itself is not deprecated either.

It is however deprecated to run ``python setup.py`` as a command line tool.

This means for example that the following commands **MUST NOT** be run anymore:

* ``python setup.py install``
* ``python setup.py develop``
* ``python setup.py sdist``
* ``python setup.py bdist_wheel``


What commands should be used instead?
=====================================

+---------------------------------+----------------------------------------+
| Deprecated                      | Current recommendation                 |
+=================================+========================================+
| ``python setup.py install``     | ``python -m pip install .``            |
+---------------------------------+----------------------------------------+
| ``python setup.py develop``     | ``python -m pip install --editable .`` |
+---------------------------------+----------------------------------------+
| ``python setup.py sdist``       | ``python -m build`` [#needs-build]_    |
+---------------------------------+                                        |
| ``python setup.py bdist_wheel`` |                                        |
+---------------------------------+----------------------------------------+


.. [#needs-build] This requires the :ref:`build` dependency.
    It is recommended to always build and publish both the source distribution
    and wheel of a project, which is what ``python -m build`` does.
    If necessary the ``--sdist`` and ``--wheel`` options can be used
    to generate only one or the other.


In order to install a setuptools based project,
it was common to run :file:`setup.py`'s ``install`` command such as:
``python setup.py install``.
Nowadays, the recommended method is to use :ref:`pip` directly
with a command like this one: ``python -m pip install .``.
Where the dot ``.`` is actually a file system path,
it is the path notation for the current directory.
Indeed, *pip* accepts a path to
a project's source tree directory on the local filesystem
as argument to its ``install`` sub-command.
So this would also be a valid command:
``python -m pip install path/to/project``.

As for the installation in *develop* mode aka *editable* mode,
instead of ``python setup.py develop``
one can use the ``--editable`` option of pip's *install* sub-command:
``python -m pip install --editable .``.

One recommended, simple, and straightforward method of building
:term:`source distributions <Source Distribution (or "sdist")>`
and :term:`wheels <Wheel>`
is to use the :ref:`build` tool with a command like
``python -m build``
which triggers the generation of both distribution formats.
If necessary the ``--sdist`` and ``--wheel`` options can be used
to generate only one or the other.
Note that the build tool needs to be installed separately.

The command ``python setup.py install`` was deprecated
in setuptools version *58.3.0*.


What about custom commands?
===========================

Likewise, custom :file:`setup.py` commands are deprecated.
The recommendation is to migrate those custom commands
to a task runner tool or any other similar tool.
Some examples of such tools are:
chuy, make, nox or tox, pydoit, pyinvoke, taskipy, and thx.


What about custom build steps?
==============================

Custom build steps that for example
either overwrite existing steps such as ``build_py``, ``build_ext``, and ``bdist_wheel``
or add new build steps are not deprecated.
Those will be automatically called as expected.


Should ``setup.py`` be deleted?
===============================

Although the usage of :file:`setup.py` as an executable script is deprecated,
its usage as a configuration file for setuptools is absolutely fine.
There is likely no modification needed in :file:`setup.py`.


Is ``pyproject.toml`` mandatory?
================================

While it is not technically necessary yet,
it is **STRONGLY RECOMMENDED** for a project to have a :file:`pyproject.toml` file
at the root of its source tree with a content like this:

.. code:: toml

    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"


The guide :ref:`modernize-setup-py-project` has more details about this.

The standard fallback behavior for a :term:`build frontend <Build Frontend>`
in the absence of a :file:`pyproject.toml` file and its ``[build-system]`` table
is to assume that the :term:`build backend <Build Backend>` is setuptools.


Why? What does it all mean?
===========================

One way to look at it is that the scope of setuptools
has now been reduced to the role of a build backend.


Where to read more about this?
==============================

* https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html

* :doc:`setuptools:deprecated/commands`
