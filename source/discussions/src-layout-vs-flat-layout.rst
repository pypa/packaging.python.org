=========================
src layout vs flat layout
=========================

The "flat layout" refers to organising a project's files in a folder or
repository, such that the various configuration files and importable
modules/packages are all in the top-level directory.

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
intended to be importable (i.e. ``import awesome_package``) into a subdirectory,
typically ``src/`` (hence the name).

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
  development workflow of a project (typically, an editable installation
  is used for development and a regular installation is used for testing).

* The src layout helps prevent accidental usage of the in-development copy of
  the code.

  This helps avoids issues around improper packaging of a project, like not
  including a file in a release distribution due to misconfiguration of the
  project's packaging tooling.

  The Python interpreter includes the current working directory as the first
  item on the import path. Thus, if an import package/module exists
  in the current working directory with the same name as the import package,
  it will be used instead of an installed copy, which can be a source of
  packaging issues with the flat layout.

* The src layout helps enforce that editable installations are only able to
  import files that were meant to be importable.

  This is especially relevant when the editable installation is implemented
  using a `path configuration file <https://docs.python.org/3/library/site.html#index-2>`_
  that adds the directory to the import path.

  The flat layout would add the other project files (eg: ``README.md``,
  ``tox.ini``) and packaging/tooling configuration files (eg: ``setup.py``,
  ``noxfile.py``) on the import path. This would make certain imports work
  in editable installations but not regular installations.
