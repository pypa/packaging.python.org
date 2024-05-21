.. _setup-py-deprecated:


===========================
Is ``setup.py`` deprecated?
===========================

No, :term:`setup.py` and :ref:`setuptools` are not deprecated.

Setuptools is perfectly usable as a :term:`build backend`
for packaging Python projects.
And :file:`setup.py` is a valid configuration file for :ref:`setuptools`
that happens to be written in Python, instead of in *TOML* for example
(a similar practice is used by other tools
like *nox* and its :file:`noxfile.py` configuration file,
or *pytest* and :file:`conftest.py`).

However, ``python setup.py`` and the use of :file:`setup.py`
as a command line tool are deprecated.

This means that commands such as the following **MUST NOT** be run anymore:

* ``python setup.py install``
* ``python setup.py develop``
* ``python setup.py sdist``
* ``python setup.py bdist_wheel``


What commands should be used instead?
=====================================

+---------------------------------+----------------------------------------+
| Deprecated                      | Recommendation                         |
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


What about other commands?
==========================

What are some replacements for the other ``python setup.py`` commands?


``python setup.py test``
------------------------

The recommendation is to use a test runner such as pytest_.

.. _pytest: https://docs.pytest.org/


``python setup.py check``, ``python setup.py register``, and ``python setup.py upload``
---------------------------------------------------------------------------------------

A trusted replacement is :ref:`twine`:

* ``python -m twine check --strict dist/*``
* ``python -m twine register dist/*.whl`` [#not-pypi]_
* ``python -m twine upload dist/*``

.. [#not-pypi] Not necessary, nor supported on :term:`PyPI <Python Package Index (PyPI)>`.
    But might be necessary on other :term:`package indexes <package index>` (for example :ref:`devpi`).


``python setup.py --version``
-----------------------------

A possible replacement solution (among others) is to rely on setuptools-scm_:

* ``python -m setuptools_scm``

.. _setuptools-scm: https://setuptools-scm.readthedocs.io/en/latest/usage/#as-cli-tool


Remaining commands
------------------

This guide does not make suggestions of replacement solutions for those commands:

.. hlist::
    :columns: 4

    * ``alias``
    * ``bdist``
    * ``bdist_dumb``
    * ``bdist_egg``
    * ``bdist_rpm``
    * ``build``
    * ``build_clib``
    * ``build_ext``
    * ``build_py``
    * ``build_scripts``
    * ``clean``
    * ``dist_info``
    * ``easy_install``
    * ``editable_wheel``
    * ``egg_info``
    * ``install``
    * ``install_data``
    * ``install_egg_info``
    * ``install_headers``
    * ``install_lib``
    * ``install_scripts``
    * ``rotate``
    * ``saveopts``
    * ``setopt``
    * ``upload_docs``


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
