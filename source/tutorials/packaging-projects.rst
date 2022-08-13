Packaging Python Projects
=========================

This tutorial walks you through how to package a simple Python project. It will
show you how to add the necessary files and structure to create the package, how
to build the package, and how to upload it to the Python Package Index (PyPI).

.. tip::

   If you have trouble running the commands in this tutorial, please copy the command
   and its output, then `open an issue`_ on the `packaging-problems`_ repository on
   GitHub. We'll do our best to help you!

.. _open an issue: https://github.com/pypa/packaging-problems/issues/new?template=packaging_tutorial.yml&title=Trouble+with+the+packaging+tutorial&guide=https://packaging.python.org/tutorials/packaging-projects

.. _packaging-problems: https://github.com/pypa/packaging-problems

Some of the commands require a newer version of :ref:`pip`, so start by making
sure you have the latest version installed:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --upgrade pip

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --upgrade pip


A simple project
----------------

This tutorial uses a simple project named
``example_package_YOUR_USERNAME_HERE``. If your username is ``me``, then the
package would be ``example_package_me``; this ensures that you have a unique
package name that doesn't conflict with packages uploaded by other people
following this tutorial. We recommend following this tutorial as-is using this
project, before packaging your own project.

Create the following file structure locally:

.. code-block:: text

    packaging_tutorial/
    └── src/
        └── example_package_YOUR_USERNAME_HERE/
            ├── __init__.py
            └── example.py

The directory containing the Python files should match the project name. This
simplifies the configuration and is more obvious to users who install the package.

:file:`__init__.py` is required to import the directory as a package, and
should be empty.

:file:`example.py` is an example of a module within the package that could
contain the logic (functions, classes, constants, etc.) of your package.
Open that file and enter the following content:

.. code-block:: python

    def add_one(number):
        return number + 1

If you are unfamiliar with Python's :term:`modules <Module>` and
:term:`import packages <Import Package>`, take a few minutes to read over the
`Python documentation for packages and modules`_.

Once you create this structure, you'll want to run all of the commands in this
tutorial within the ``packaging_tutorial`` directory.

.. _Python documentation for packages and modules:
    https://docs.python.org/3/tutorial/modules.html#packages


Creating the package files
--------------------------

You will now add files that are used to prepare the project for distribution.
When you're done, the project structure will look like this:


.. code-block:: text

    packaging_tutorial/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src/
    │   └── example_package_YOUR_USERNAME_HERE/
    │       ├── __init__.py
    │       └── example.py
    └── tests/


Creating a test directory
-------------------------

:file:`tests/` is a placeholder for test files. Leave it empty for now.


Creating pyproject.toml
-----------------------

.. TODO: Add an intro sentence about pyproject.toml, and a sub-heading for
   "Configuring build tools"

:file:`pyproject.toml` tells "frontend" build tools like :ref:`pip` and
:ref:`build` what "backend" tool to use to create
:term:`distribution packages <Distribution Package>` for your project.
You can choose from a number of backends; this tutorial uses :ref:`Hatchling
<hatch>` by default, but it will work identically with :ref:`setuptools`,
:ref:`Flit <flit>`, :ref:`PDM <pdm>`, and others that support the ``[project]``
table for :ref:`metadata <configuring metadata>`.

.. note::

   Some build backends are part of larger tools that provide a command-line
   interface with additional features like project initialization and version
   management, as well as building, uploading, and installing packages. This
   tutorial uses single-purpose tools that work independently.

Open :file:`pyproject.toml` and enter one of these ``[build-system]`` tables:

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
        requires = ["flit_core>=3.2"]
        build-backend = "flit_core.buildapi"

.. tab:: PDM

    .. code-block:: toml

        [build-system]
        requires = ["pdm-pep517"]
        build-backend = "pdm.pep517.api"


- ``requires`` is a list of packages that are needed to build your package. You
  don't need to install them; build frontends like :ref:`pip` will install them
  automatically in a temporary, isolated virtual environment for use during the
  build process.
- ``build-backend`` is the name of the Python object that frontends will use to
  perform the build.

.. TODO: Add note to check the tools' documentation for the current snippet?

.. _configuring metadata:

Configuring metadata
^^^^^^^^^^^^^^^^^^^^

Open :file:`pyproject.toml` and enter the following content. Change the ``name``
to include your username; this ensures that you have a unique
package name that doesn't conflict with packages uploaded by other people
following this tutorial.

.. code-block:: toml

    [project]
    name = "example_package_YOUR_USERNAME_HERE"
    version = "0.0.1"
    authors = [
      { name="Example Author", email="author@example.com" },
    ]
    description = "A small example package"
    readme = "README.md"
    license = { file="LICENSE" }
    requires-python = ">=3.7"
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

    [project.urls]
    "Homepage" = "https://github.com/pypa/sampleproject"
    "Bug Tracker" = "https://github.com/pypa/sampleproject/issues"

- ``name`` is the *distribution name* of your package. This can be any name as
  long as it only contains letters, numbers, ``.``, ``_`` , and ``-``. It also
  must not already be taken on PyPI. **Be sure to update this with your
  username** for this tutorial, as this ensures you won't try to upload a
  package with the same name as one which already exists.
- ``version`` is the package version. See the :ref:`version specifier specification <version-specifiers>`
  for more details on versions. Some build backends allow it to be specified
  another way, such as from a file or a git tag.
- ``authors`` is used to identify the author of the package; you specify a name
  and an email for each author. You can also list ``maintainers`` in the same
  format.
- ``description`` is a short, one-sentence summary of the package.
- ``readme`` is a path to a file containing a detailed description of the
  package. This is shown on the package detail page on PyPI.
  In this case, the description is loaded from :file:`README.md` (which is a
  common pattern). There also is a more advanced table form described in the
  :ref:`project metadata specification <declaring-project-metadata>`.
- ``license`` is the path to the :file:`LICENSE` file, described below.
- ``requires-python`` gives the versions of Python supported by your
  project. Installers like :ref:`pip` will look back through older versions of
  packages until it finds one that has a matching Python version.
- ``classifiers`` gives the index and :ref:`pip` some additional metadata
  about your package. In this case, the package is only compatible with Python
  3, is licensed under the MIT license, and is OS-independent. You should
  always include at least which version(s) of Python your package works on,
  which license your package is available under, and which operating systems
  your package will work on. For a complete list of classifiers, see
  https://pypi.org/classifiers/.
- ``urls`` lets you list any number of extra links to show on PyPI.
  Generally this could be to the source, documentation, issue trackers, etc.

See the :ref:`project metadata specification <declaring-project-metadata>` for
details on these and other fields that can be defined in the ``[project]``
table. Other common fields are ``keywords`` to improve discoverability and the
``dependencies`` that are required to install your package.

Creating README.md
------------------

Open :file:`README.md` and enter the following content. You can customize this
if you'd like.

.. code-block:: md

    # Example Package

    This is a simple example package. You can use
    [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
    to write your content.


Creating a LICENSE
------------------

It's important for every package uploaded to the Python Package Index to include
a license. This tells users who install your package the terms under which they
can use your package. For help picking a license, see
https://choosealicense.com/. Once you have chosen a license, open
:file:`LICENSE` and enter the license text. For example, if you had chosen the
MIT license:

.. code-block:: text

    Copyright (c) 2018 The Python Packaging Authority

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


Including other files
---------------------

The files listed above will be included automatically in your
:term:`source distribution <Source Distribution (or "sdist")>`. If you want to
include additional files, see the documentation for your build backend.

.. _generating archives:

Generating distribution archives
--------------------------------

The next step is to generate :term:`distribution packages <Distribution Package>`
for the package. These are archives that are uploaded to the Python
Package Index and can be installed by :ref:`pip`.

Make sure you have the latest version of PyPA's :ref:`build` installed:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --upgrade build

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --upgrade build

.. tip:: If you have trouble installing these, see the
   :doc:`installing-packages` tutorial.

Now run this command from the same directory where :file:`pyproject.toml` is located:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m build

.. tab:: Windows

    .. code-block:: bat

        py -m build

This command should output a lot of text and once completed should generate two
files in the :file:`dist` directory:

.. code-block:: text

    dist/
    ├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
    └── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz


The ``tar.gz`` file is a :term:`source distribution <Source Distribution (or "sdist")>`
whereas the ``.whl`` file is a :term:`built distribution <Built Distribution>`.
Newer :ref:`pip` versions preferentially install built distributions, but will
fall back to source distributions if needed. You should always upload a source
distribution and provide built distributions for the platforms your project is
compatible with. In this case, our example package is compatible with Python on
any platform so only one built distribution is needed.

Uploading the distribution archives
-----------------------------------

Finally, it's time to upload your package to the Python Package Index!

The first thing you'll need to do is register an account on TestPyPI, which
is a separate instance of the package index intended for testing and
experimentation. It's great for things like this tutorial where we don't
necessarily want to upload to the real index. To register an account, go to
https://test.pypi.org/account/register/ and complete the steps on that page.
You will also need to verify your email address before you're able to upload
any packages.  For more details, see :doc:`/guides/using-testpypi`.

To securely upload your project, you'll need a PyPI `API token`_. Create one at
https://test.pypi.org/manage/account/#api-tokens, setting the "Scope" to "Entire
account". **Don't close the page until you have copied and saved the token — you
won't see that token again.**

.. _API token: https://test.pypi.org/help/#apitoken

Now that you are registered, you can use :ref:`twine` to upload the
distribution packages. You'll need to install Twine:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --upgrade twine

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --upgrade twine

Once installed, run Twine to upload all of the archives under :file:`dist`:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m twine upload --repository testpypi dist/*

.. tab:: Windows

    .. code-block:: bat

        py -m twine upload --repository testpypi dist/*

You will be prompted for a username and password. For the username,
use ``__token__``. For the password, use the token value, including
the ``pypi-`` prefix.

After the command completes, you should see output similar to this:

.. code-block::

    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: __token__
    Uploading example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 kB • 00:01 • ?
    Uploading example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?

Once uploaded, your package should be viewable on TestPyPI; for example:
``https://test.pypi.org/project/example_package_YOUR_USERNAME_HERE``.


Installing your newly uploaded package
--------------------------------------

You can use :ref:`pip` to install your package and verify that it works.
Create a :ref:`virtual environment <Creating and using Virtual Environments>`
and install your package from TestPyPI:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE

Make sure to specify your username in the package name!

pip should install the package from TestPyPI and the output should look
something like this:

.. code-block:: text

    Collecting example-package-YOUR-USERNAME-HERE
      Downloading https://test-files.pythonhosted.org/packages/.../example_package_YOUR_USERNAME_HERE_0.0.1-py3-none-any.whl
    Installing collected packages: example_package_YOUR_USERNAME_HERE
    Successfully installed example_package_YOUR_USERNAME_HERE-0.0.1

.. note:: This example uses ``--index-url`` flag to specify TestPyPI instead of
   live PyPI. Additionally, it specifies ``--no-deps``. Since TestPyPI doesn't
   have the same packages as the live PyPI, it's possible that attempting to
   install dependencies may fail or install something unexpected. While our
   example package doesn't have any dependencies, it's a good practice to avoid
   installing dependencies when using TestPyPI.

You can test that it was installed correctly by importing the package.
Make sure you're still in your virtual environment, then run Python:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3

.. tab:: Windows

    .. code-block:: bat

        py

and import the package:

.. code-block:: python

    >>> from example_package_YOUR_USERNAME_HERE import example
    >>> example.add_one(2)
    3


Next steps
----------

**Congratulations, you've packaged and distributed a Python project!**
✨ 🍰 ✨

Keep in mind that this tutorial showed you how to upload your package to Test
PyPI, which isn't a permanent storage. The Test system occasionally deletes
packages and accounts. It is best to use TestPyPI for testing and experiments
like this tutorial.

When you are ready to upload a real package to the Python Package Index you can
do much the same as you did in this tutorial, but with these important
differences:

* Choose a memorable and unique name for your package. You don't have to append
  your username as you did in the tutorial, but you can't use an existing name.
* Register an account on https://pypi.org - note that these are two separate
  servers and the login details from the test server are not shared with the
  main server.
* Use ``twine upload dist/*`` to upload your package and enter your credentials
  for the account you registered on the real PyPI.  Now that you're uploading
  the package in production, you don't need to specify ``--repository``; the
  package will upload to https://pypi.org/ by default.
* Install your package from the real PyPI using ``python3 -m pip install [your-package]``.

At this point if you want to read more on packaging Python libraries here are
some things you can do:

.. TODO: Add links to other guides
.. TODO: Add links to backend configuration docs

* Consider packaging tools that provide a single command-line interface for
  project management and packaging, such as :ref:`hatch`, :ref:`flit`,
  :ref:`pdm`, and :ref:`poetry`.
* Read :pep:`517` and :pep:`518` for background and details on build tool configuration.
* Read about :doc:`/guides/packaging-binary-extensions`.

