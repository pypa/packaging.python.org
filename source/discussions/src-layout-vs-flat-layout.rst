.. _src-layout-vs-flat-layout:

=========================
src layout vs flat layout
=========================

The "flat layout" refers to organising a project's files in a folder or
repository, such that the various configuration files and
:term:`import packages <Import Package>` are all in the top-level directory.

::

    .
    ├── README.md
    ├── noxfile.py
    ├── pyproject.toml
    ├── setup.py
    ├── awesome_package/
    │   ├── __init__.py
    │   └── module.py
    └── tools/
        ├── generate_awesomeness.py
        └── decrease_world_suck.py

The "src layout" deviates from the flat layout by moving the code that is
intended to be importable (i.e. ``import awesome_package``, also known as
:term:`import packages <Import Package>`) into a subdirectory. This
subdirectory is typically named ``src/``, hence "src layout".

::

    .
    ├── README.md
    ├── noxfile.py
    ├── pyproject.toml
    ├── setup.py
    ├── src/
    │    └── awesome_package/
    │       ├── __init__.py
    │       └── module.py
    └── tools/
        ├── generate_awesomeness.py
        └── decrease_world_suck.py

Here's a breakdown of the important behaviour differences between the src
layout and the flat layout:

* The src layout requires installation of the project to be able to run its
  code, and the flat layout does not.

  This means that the src layout involves an additional step in the
  development workflow of a project (typically, an
  :doc:`editable installation <setuptools:userguide/development_mode>`
  is used for development and a regular installation is used for testing).

* The src layout helps prevent accidental usage of the in-development copy of
  the code.

  This is relevant since the Python interpreter includes the current working
  directory as the first item on the import path. This means that if an import
  package exists in the current working directory with the same name as an
  installed import package, the variant from the current working directory will
  be used. This can lead to subtle  misconfiguration of the project's packaging
  tooling, which could result in files not being included in a distribution.

  The src layout helps avoid this by keeping import packages in a directory
  separate from the root directory of the project, ensuring that the installed
  copy is used.

* The src layout helps enforce that an
  :doc:`editable installation <setuptools:userguide/development_mode>` is only
  able to import files that were meant to be importable.

  This is especially relevant when the editable installation is implemented
  using a `path configuration file <https://docs.python.org/3/library/site.html#index-2>`_
  that adds the directory to the import path.

  The flat layout would add the other project files (eg: ``README.md``,
  ``tox.ini``) and packaging/tooling configuration files (eg: ``setup.py``,
  ``noxfile.py``) on the import path. This would make certain imports work
  in editable installations but not regular installations.

.. _running-cli-from-source-src-layout:

Running a command-line interface from source with src-layout
============================================================

Due to the firstly mentioned specialty of the src layout, a command-line
interface can not be run directly from the :term:`source tree <Project Source Tree>`,
but requires installation of the package in
:doc:`Development Mode <setuptools:userguide/development_mode>`
for testing purposes. Since this can be unpractical in some situations,
a workaround could be to prepend the package folder to  Python's
:py:data:`sys.path` when called via its :file:`__main__.py` file:

.. code-block:: python

    import os
    import sys

    if not __package__:
        # Make CLI runnable from source tree with
        #    python src/package
        package_source_path = os.path.dirname(os.path.dirname(__file__))
        sys.path.insert(0, package_source_path)
