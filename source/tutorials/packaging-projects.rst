Packaging Python Projects
=========================

This tutorial walks you through how to package a simple Python project. It will
show you how to add the necessary files and structure to create the package, how
to build the package, and how to upload it to the Python Package Index.

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

This tutorial uses a simple project named ``example_package``.  We recommend
following this tutorial as-is using this project, before packaging your own
project.

Create the following file structure locally:

.. code-block:: text

    packaging_tutorial/
    └── src/
        └── example_package/
            ├── __init__.py
            └── example.py

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
    ├── setup.cfg
    ├── src/
    │   └── example_package/
    │       ├── __init__.py
    │       └── example.py
    └── tests/


Creating a test directory
-------------------------

:file:`tests/` is a placeholder for test files. Leave it empty for now.


Creating pyproject.toml
-----------------------

:file:`pyproject.toml` tells build tools (like :ref:`pip` and :ref:`build`)
what is required to build your project. This tutorial uses :ref:`setuptools`,
so open :file:`pyproject.toml` and enter the following content:

.. code-block:: toml

    [build-system]
    requires = ["setuptools>=42"]
    build-backend = "setuptools.build_meta"


``build-system.requires`` gives a list of packages that are needed to build your
package. Listing something here will *only* make it available during the build,
not after it is installed.

``build-system.build-backend`` is the name of Python object that will be used to
perform the build. If you were to use a different build system, such as
:ref:`flit` or :ref:`poetry`, those would go here, and the configuration details
would be completely different than the :ref:`setuptools` configuration described
below.

See :pep:`517` and :pep:`518` for background and details.


Configuring metadata
--------------------

There are two types of metadata: static and dynamic.

* Static metadata (:file:`setup.cfg`): guaranteed to be the same every time. This is
  simpler, easier to read, and avoids many common errors, like encoding errors.
* Dynamic metadata (:file:`setup.py`): possibly non-deterministic. Any items that are
  dynamic or determined at install-time, as well as extension modules or
  extensions to setuptools, need to go into :file:`setup.py`.

Static metadata (:file:`setup.cfg`) should be preferred. Dynamic metadata (:file:`setup.py`)
should be used only as an escape hatch when absolutely necessary. :file:`setup.py` used to
be required, but can be omitted with newer versions of setuptools and pip.


.. tab:: :file:`setup.cfg` (static)

    :file:`setup.cfg` is the configuration file for :ref:`setuptools`. It tells
    setuptools about your package (such as the name and version) as well as which
    code files to include. Eventually much of this configuration may be able to move
    to :file:`pyproject.toml`.

    Open :file:`setup.cfg` and enter the following content. Change the ``name``
    to include your username; this ensures that you have a unique package name
    and that your package doesn't conflict with packages uploaded by other
    people following this tutorial.

    .. code-block:: python

        [metadata]
        name = example-package-YOUR-USERNAME-HERE
        version = 0.0.1
        author = Example Author
        author_email = author@example.com
        description = A small example package
        long_description = file: README.md
        long_description_content_type = text/markdown
        url = https://github.com/pypa/sampleproject
        project_urls =
            Bug Tracker = https://github.com/pypa/sampleproject/issues
        classifiers =
            Programming Language :: Python :: 3
            License :: OSI Approved :: MIT License
            Operating System :: OS Independent

        [options]
        package_dir =
            = src
        packages = find:
        python_requires = >=3.6

        [options.packages.find]
        where = src

    There are a `variety of metadata and options
    <https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html>`_
    supported here. This is in :doc:`configparser <python:library/configparser>`
    format; do not place quotes around values. This example package uses a
    relatively minimal set of ``metadata``:

    - ``name`` is the *distribution name* of your package. This can be any name as
      long as it only contains letters, numbers, ``_`` , and ``-``. It also must not
      already be taken on pypi.org. **Be sure to update this with your username,**
      as this ensures you won't try to upload a package with the same name as one
      which already exists.
    - ``version`` is the package version. See :pep:`440` for more details on
      versions. You can use ``file:`` or ``attr:`` directives to read from a file or
      package attribute.
    - ``author`` and ``author_email`` are used to identify the author of the
      package.
    - ``description`` is a short, one-sentence summary of the package.
    - ``long_description`` is a detailed description of the package. This is
      shown on the package detail page on the Python Package Index. In
      this case, the long description is loaded from :file:`README.md` (which is
      a common pattern) using the ``file:`` directive.
    - ``long_description_content_type`` tells the index what type of markup is
      used for the long description. In this case, it's Markdown.
    - ``url`` is the URL for the homepage of the project. For many projects, this
      will just be a link to GitHub, GitLab, Bitbucket, or similar code hosting
      service.
    - ``project_urls`` lets you list any number of extra links to show on PyPI.
      Generally this could be to documentation, issue trackers, etc.
    - ``classifiers`` gives the index and :ref:`pip` some additional metadata
      about your package. In this case, the package is only compatible with Python
      3, is licensed under the MIT license, and is OS-independent. You should
      always include at least which version(s) of Python your package works on,
      which license your package is available under, and which operating systems
      your package will work on. For a complete list of classifiers, see
      https://pypi.org/classifiers/.

    In the ``options`` category, we have controls for setuptools itself:

    - ``package_dir`` is a mapping of package names and directories.
      An empty package name represents the "root package" --- the directory in
      the project that contains all Python source files for the package --- so
      in this case the ``src`` directory is designated the root package.
    - ``packages`` is a list of all Python :term:`import packages <Import
      Package>` that should be included in the :term:`distribution package
      <Distribution Package>`. Instead of listing each package manually, we can
      use the ``find:`` directive to automatically discover all packages and
      subpackages and ``options.packages.find`` to specify the ``package_dir``
      to use. In this case, the list of packages will be ``example_package`` as
      that's the only package present.
    - ``python_requires`` gives the versions of Python supported by your
      project. Installers like :ref:`pip` will look back through older versions of
      packages until it finds one that has a matching Python version.

    There are many more than the ones mentioned here. See
    :doc:`/guides/distributing-packages-using-setuptools` for more details.


.. tab:: :file:`setup.py` (dynamic)

    :file:`setup.py` is the build script for :ref:`setuptools`. It tells setuptools
    about your package (such as the name and version) as well as which code files
    to include.

    Open :file:`setup.py` and enter the following content.  Change the ``name``
    to include your username; this ensures that you have a unique package name
    and that your package doesn't conflict with packages uploaded by other
    people following this tutorial.

    .. code-block:: python

        import setuptools

        with open("README.md", "r", encoding="utf-8") as fh:
            long_description = fh.read()

        setuptools.setup(
            name="example-package-YOUR-USERNAME-HERE",
            version="0.0.1",
            author="Example Author",
            author_email="author@example.com",
            description="A small example package",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/pypa/sampleproject",
            project_urls={
                "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
            },
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            package_dir={"": "src"},
            packages=setuptools.find_packages(where="src"),
            python_requires=">=3.6",
        )


    :func:`setup` takes several arguments. This example package uses a relatively
    minimal set:

    - ``name`` is the *distribution name* of your package. This can be any name as
      long as it only contains letters, numbers, ``_`` , and ``-``. It also must not
      already be taken on pypi.org. **Be sure to update this with your username,**
      as this ensures you won't try to upload a package with the same name as one
      which already exists.
    - ``version`` is the package version. See :pep:`440` for more details on
      versions.
    - ``author`` and ``author_email`` are used to identify the author of the
      package.
    - ``description`` is a short, one-sentence summary of the package.
    - ``long_description`` is a detailed description of the package. This is
      shown on the package detail page on the Python Package Index. In
      this case, the long description is loaded from :file:`README.md`, which is
      a common pattern.
    - ``long_description_content_type`` tells the index what type of markup is
      used for the long description. In this case, it's Markdown.
    - ``url`` is the URL for the homepage of the project. For many projects, this
      will just be a link to GitHub, GitLab, Bitbucket, or similar code hosting
      service.
    - ``project_urls`` lets you list any number of extra links to show on PyPI.
      Generally this could be to documentation, issue trackers, etc.
    - ``classifiers`` gives the index and :ref:`pip` some additional metadata
      about your package. In this case, the package is only compatible with Python
      3, is licensed under the MIT license, and is OS-independent. You should
      always include at least which version(s) of Python your package works on,
      which license your package is available under, and which operating systems
      your package will work on. For a complete list of classifiers, see
      https://pypi.org/classifiers/.
    - ``package_dir`` is a dictionary with package names for keys and directories
      for values. An empty package name represents the "root package" --- the
      directory in the project that contains all Python source files for the
      package --- so in this case the ``src`` directory is designated the root
      package.
    - ``packages`` is a list of all Python :term:`import packages <Import
      Package>` that should be included in the :term:`distribution package
      <Distribution Package>`. Instead of listing each package manually, we can
      use :func:`find_packages` to automatically discover all packages and
      subpackages under ``package_dir``. In this case, the list of packages will
      be ``example_package`` as that's the only package present.
    - ``python_requires`` gives the versions of Python supported by your
      project. Installers like :ref:`pip` will look back though older versions of
      packages until it finds one that has a matching Python version.

    There are many more than the ones mentioned here. See
    :doc:`/guides/distributing-packages-using-setuptools` for more details.

    .. warning::

      You may see some existing projects or other Python packaging tutorials that
      import their ``setup`` function from ``distutils.core`` rather than
      ``setuptools``. This is a legacy approach that installers support
      for backwards compatibility purposes [1]_, but using the legacy ``distutils`` API
      directly in new projects is strongly discouraged, since ``distutils`` is
      deprecated as per :pep:`632` and will be removed from the standard library
      in Python 3.12.

Creating README.md
------------------

Open :file:`README.md` and enter the following content. You can customize this
if you'd like.

.. code-block:: md

    # Example Package

    This is a simple example package. You can use
    [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
    to write your content.


Because our configuration loads :file:`README.md` to provide a
``long_description``, :file:`README.md` must be included along with your
code when you :ref:`generate a source distribution <generating archives>`.
Newer versions of :ref:`setuptools` will do this automatically.


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
control what goes in this explicitly, see :ref:`Using MANIFEST.in`.

The final :term:`built distribution <Built Distribution>` will have the Python
files in the discovered or listed Python packages. If you want to control what
goes here, such as to add data files, see
:doc:`Including Data Files <setuptools:userguide/datafiles>`
from the :doc:`setuptools docs <setuptools:index>`.

.. _generating archives:

Generating distribution archives
--------------------------------

The next step is to generate :term:`distribution packages <Distribution
Package>` for the package. These are archives that are uploaded to the Python
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
      example-package-YOUR-USERNAME-HERE-0.0.1-py3-none-any.whl
      example-package-YOUR-USERNAME-HERE-0.0.1.tar.gz


The ``tar.gz`` file is a :term:`source archive <Source Archive>` whereas the
``.whl`` file is a :term:`built distribution <Built Distribution>`. Newer
:ref:`pip` versions preferentially install built distributions, but will fall
back to source archives if needed. You should always upload a source archive and
provide built archives for the platforms your project is compatible with. In
this case, our example package is compatible with Python on any platform so only
one built distribution is needed.

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

.. code-block:: bash

    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: [your username]
    Enter your password:
    Uploading example-package-YOUR-USERNAME-HERE-0.0.1-py3-none-any.whl
    100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
    Uploading example-package-YOUR-USERNAME-HERE-0.0.1.tar.gz
    100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]


Once uploaded your package should be viewable on TestPyPI, for example,
https://test.pypi.org/project/example-package-YOUR-USERNAME-HERE


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
      Downloading https://test-files.pythonhosted.org/packages/.../example-package-YOUR-USERNAME-HERE-0.0.1-py3-none-any.whl
    Installing collected packages: example-package-YOUR-USERNAME-HERE
    Successfully installed example-package-YOUR-USERNAME-HERE-0.0.1

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

    >>> from example_package import example
    >>> example.add_one(2)
    3

Note that the :term:`import package <Import Package>` is ``example_package``
regardless of what ``name`` you gave your :term:`distribution package <Distribution
Package>` in :file:`setup.cfg` or :file:`setup.py` (in this case,
``example-package-YOUR-USERNAME-HERE``).

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
  your username as you did in the tutorial.
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

* Read more about using :ref:`setuptools` to package libraries in
  :doc:`/guides/distributing-packages-using-setuptools`.
* Read about :doc:`/guides/packaging-binary-extensions`.
* Consider alternatives to :ref:`setuptools` such as :ref:`flit`, :ref:`hatch`,
  and :ref:`poetry`.

----

.. [1] Some legacy Python environments may not have ``setuptools``
       pre-installed, and the operators of those environments may still be
       requiring users to install packages by running ``setup.py install``
       commands, rather than providing an installer like ``pip`` that
       automatically installs required build dependendencies. These
       environments will not be able to use many published packages until the
       environment is updated to provide an up to date Python package
       installation client (e.g. by running ``python -m ensurepip``).
