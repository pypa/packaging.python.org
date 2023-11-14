.. _writing-pyproject-toml:

===============================
Writing your ``pyproject.toml``
===============================

``pyproject.toml`` is a configuration file used by packaging tools, as
well as other tools such as linters, type checkers, etc. There are
three possible TOML tables in this file.

- The ``[build-system]`` table is **strongly recommended**. It allows
  you to declare which :term:`build backend` you use and which other
  dependencies are needed to build your project.

- The ``[project]`` table is the format that most build backends use to specify
  your project's basic metadata, such as the dependencies, your name, etc.

- The ``[tool]`` table has arbitrary subtables corresponding to tools, whether
  packaging-related or not, e.g., ``[tool.hatch]``, ``[tool.black]``,
  ``[tool.mypy]``. We only touch upon this table here because its contents are
  entirely tool-specific. Consult each tool's documentation to know what it can
  contain.

.. note::

   There is a significant difference between the ``[build-system]`` and
   ``[project]`` tables. The former should always be present, regardless of
   which build backend you use (since it *defines* the tool you use). The latter
   is understood by *most* build backends, but some build backends use a
   different format.

   At the time of this writing (November 2023), Poetry_ is a notable build
   backend that does not use the ``[project]`` table (it uses the
   ``[tool.poetry]`` table instead).

   Also, the setuptools_ build backend supports both the ``[project]`` table,
   and the older format in ``setup.cfg`` or ``setup.py``. For new projects, it
   is recommended to use the ``[project]`` table, and keep ``setup.py`` only if
   some programmatic configuration is needed (especially building C extensions),
   but the ``setup.cfg`` and ``setup.py`` formats are still valid. See
   :ref:`setup-py-deprecated`.



Declaring the build backend
===========================

The ``[build-system]`` table contains a ``build-backend`` key, which specifies
the build backend to be used. It also contains a ``requires`` key, which is a
list of dependencies needed to build the project -- this is typically just the
build backend package, but it may also contain additional dependencies. You can
also constrain the versions, e.g., ``requires = ["setuptools >= 61.0"]``.

Usually, you'll just copy what your build backend's documentation suggests. Here
are the values for some common build backends:

.. tab:: Hatchling

    .. code-block:: toml

        [build-system]
        requires = ["hatchling"]
        build-backend = "hatchling.build"

.. tab:: setuptools

    .. code-block:: toml

        [build-system]
        requires = ["setuptools>=61.0"]
        build-backend = "setuptools.build_meta"

.. tab:: Flit

    .. code-block:: toml

        [build-system]
        requires = ["flit_core>=3.4"]
        build-backend = "flit_core.buildapi"

.. tab:: PDM

    .. code-block:: toml

        [build-system]
        requires = ["pdm-backend"]
        build-backend = "pdm.backend"


The rest of this guide is devoted to the ``[project]`` table.


Static vs. dynamic metadata
===========================

Most of the time, you will directly write the value of a ``[project]``
field. For example: ``requires-python = ">= 3.8"``, or ``version =
"1.0"``.

However, in some cases, it is useful to let your build backend compute
the metadata for you. For example: many build backends can read the
version from a ``__version__`` attribute in your code, or similar.
In such cases, you should mark the field as dynamic using, e.g.,

.. code-block:: toml

   [project]
   dynamic = ["version"]


When a field is dynamic, it is the build backend's responsibility to
fill it.  Consult your build backend's documentation to learn how it
does it.


Basic information
=================

``name``
--------

Put the name of your project on PyPI. This field is required and is the
only field that cannot be marked as dynamic.

.. code-block:: toml

   [project]
   name = "spam-eggs"


``version``
-----------

Put the version of your project.

.. code-block:: toml

    [project]
    version = "2020.0.0"

Some more complicated version specifiers like ``2020.0.0a1`` (for an alpha
release) are possible; see the :ref:`specification <version-specifiers>`
for full details.

This field is required, although it is often marked as dynamic using

.. code-block:: toml

   [project]
   dynamic = ["version"]



Dependencies and requirements
=============================

``dependencies``/``optional-dependencies``
------------------------------------------

If your project has dependencies, list them like this:

.. code-block:: toml

   [project]
   dependencies = [
     "httpx",
     "gidgethub[httpx]>4.0.0",
     "django>2.1; os_name != 'nt'",
     "django>2.0; os_name == 'nt'",
   ]

See :ref:`Dependency specifiers <dependency-specifiers>` for the full
syntax you can use to constrain versions.

You may want to make some of your dependencies optional, if they are
only needed for a specific feature of your package. In that case, put
them in ``optional-dependencies``.

.. code-block:: toml

    [project.optional-dependencies]
    gui = ["PyQt5"]
    cli = [
      "rich",
      "click",
    ]

Each of the keys defines a "packaging extra". In the example above, one
could use, e.g., ``pip install your-project-name[gui]`` to install your
project with GUI support, adding the PyQt5 dependency.


``requires-python``
-------------------

This lets you declare the minimum version of Python that you support
[#requires-python-upper-bounds]_.

.. code-block:: toml

   [project]
   requires-python = ">= 3.8"



Creating executable scripts
===========================

To install a command as part of your package, declare it in the
``[project.scripts]`` table.

.. code-block:: toml

   [project.scripts]
   spam-cli = "spam:main_cli"

In this example, after installing your project, a ``spam-cli`` command
will be available. Executing this command will do the equivalent of
``from spam import main_cli; main_cli()``.

On Windows, scripts packaged this way need a terminal, so if you launch
them from within a graphical application, they will make a terminal pop
up. To prevent this from happening, use the ``[project.gui-scripts]``
table instead of ``[project.scripts]``.

.. code-block:: toml

   [project.gui-scripts]
   spam-gui = "spam:main_gui"

In that case, launching your script from the command line will give back
control immediately, leaving the script to run in the background.

The difference between ``[project.scripts]`` and
``[project.gui-scripts]`` is only relevant on Windows.



About your project
==================

``authors``/``maintainers``
---------------------------

Both of these fields contain lists of people identified by a name and/or
an email address.

.. code-block:: toml

    [project]
    authors = [
      {name = "Pradyun Gedam", email = "pradyun@example.com"},
      {name = "Tzu-Ping Chung", email = "tzu-ping@example.com"},
      {name = "Another person"},
      {email = "different.person@example.com"},
    ]
    maintainers = [
      {name = "Brett Cannon", email = "brett@example.com"}
    ]


``description``
---------------

This should be a one-line description of your project, to show as the
"headline" of your project page on PyPI (`example <pypi-pip_>`_).

.. code-block:: toml

    [project]
    description = "Lovely Spam! Wonderful Spam!"


``readme``
----------

This is a longer description of your project, to display on your project
page on PyPI. Typically, your project will have a ``README.md`` or
``README.rst`` file and you just put its file name here.

.. code-block:: toml

    [project]
    readme = "README.md"

The README's format is auto-detected from the extension:

- ``README.md`` → Markdown,
- ``README.rst`` → reStructuredText (without Sphinx extensions).

You can also specify the format explicitly, like this:

.. code-block:: toml

   [project]
   readme = {file = "README.txt", content-type = "text/markdown"}
   # or
   readme = {file = "README.txt", content-type = "text/x-rst"}


``license``
-----------

This can take two forms. You can put your license in a file, typically
``LICENSE`` or ``LICENSE.txt``, and link that file here:

.. code-block:: toml

    [project]
    license = {file = "LICENSE"}

or you can write the name of the license:


.. code-block:: toml

    [project]
    license = {text = "MIT License"}



``keywords``
------------

This will help PyPI's search box to suggest your project when people
search for these keywords.

.. code-block:: toml

    [project]
    keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]


``classifiers``
---------------

A list of PyPI classifiers that apply to your project. Check the
`full list of possibilities <classifier-list_>`_.

.. code-block:: toml

    classifiers = [
      "Development Status :: 4 - Beta",
      "Programming Language :: Python"
    ]


``urls``
--------

A list of URLs associated with your project, displayed on the left
sidebar of your PyPI project page.

.. code-block:: toml

    [project.urls]
    Homepage = "https://example.com"
    Documentation = "https://readthedocs.org"
    Repository = "https://github.com/me/spam.git"
    Issues = "https://github.com/me/spam/issues"
    Changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"

Note that if the key contains spaces, it needs to be quoted, e.g.,
``Website = "https://example.com"`` but
``"Official Website" = "https://example.com"``.



Advanced plugins
================

Some packages can be extended through plugins. Examples include Pytest_
and Pygments_. To create such a plugin, you need to declare it in a subtable
of ``[project.entry-points]`` like this:

.. code-block:: toml

   [project.entry-points."spam.magical"]
   tomatoes = "spam:main_tomatoes"

See the :ref:`Plugin guide <plugin-entry-points>` for more information.



A full example
==============

.. code-block:: toml

   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"

   [project]
   name = "spam-eggs"
   version = "2020.0.0"
   dependencies = [
     "httpx",
     "gidgethub[httpx]>4.0.0",
     "django>2.1; os_name != 'nt'",
     "django>2.0; os_name == 'nt'",
   ]
   requires-python = ">=3.8"
   authors = [
     {name = "Pradyun Gedam", email = "pradyun@example.com"},
     {name = "Tzu-Ping Chung", email = "tzu-ping@example.com"},
     {name = "Another person"},
     {email = "different.person@example.com"},
   ]
   maintainers = [
     {name = "Brett Cannon", email = "brett@example.com"}
   ]
   description = "Lovely Spam! Wonderful Spam!"
   readme = "README.rst"
   license = {file = "LICENSE.txt"}
   keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]
   classifiers = [
     "Development Status :: 4 - Beta",
     "Programming Language :: Python"
   ]

   [project.optional-dependencies]
   gui = ["PyQt5"]
   cli = [
     "rich",
     "click",
   ]

   [project.urls]
   Homepage = "https://example.com"
   Documentation = "https://readthedocs.org"
   Repository = "https://github.com/me/spam.git"
   "Bug Tracker" = "https://github.com/me/spam/issues"
   Changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"

   [project.scripts]
   spam-cli = "spam:main_cli"

   [project.gui-scripts]
   spam-gui = "spam:main_gui"

   [project.entry-points."spam.magical"]
   tomatoes = "spam:main_tomatoes"


------------------

.. [#requires-python-upper-bounds] Think twice before applying an upper bound
   like ``requires-python = "<= 3.10"`` here. `This blog post <requires-python-blog-post_>`_
   contains some information regarding possible problems.

.. _setuptools: https://setuptools.pypa.io
.. _poetry: https://python-poetry.org
.. _pypi-pip: https://pypi.org/project/pip
.. _classifier-list: https://pypi.org/classifiers
.. _requires-python-blog-post: https://iscinumpy.dev/post/bound-version-constraints/#pinning-the-python-version-is-special
.. _pytest: https://pytest.org
.. _pygments: https://pygments.org
