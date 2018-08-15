Packaging Python Projects
=========================

This tutorial walks you through how to package a simple Python project. It will
show you how to add the necessary files and structure to create the package, how
to build the package, and how to upload it to the Python Package Index.


A simple project
----------------

This tutorial uses a simple project named ``example_pkg``. If you are unfamiliar
with Python's modules and :term:`import packages <import package>`, take a few
minutes to read over the `Python documentation for packages and modules`_.

To create this project locally, create the following file structure:

.. code-block:: text

    /example_pkg
      /example_pkg
        __init__.py


Once you create this structure, you'll want to run all of the commands in this
tutorial within the top-level folder - so be sure to ``cd example_pkg``.

You should also edit :file:`example_pkg/__init__.py` and put the following
code in there:

.. code-block:: python
    
    name = "example_pkg"

This is just so that you can verify that it installed correctly later in this
tutorial.

.. _Python documentation for packages and modules:
    https://docs.python.org/3/tutorial/modules.html#packages


Creating the package files
--------------------------

You will now create a handful of files to package up this project and prepare it
for distribution. Create the new files listed below - you will add content to
them in the following steps.

.. code-block:: text

    /example_pkg
      /example_pkg
        __init__.py
      setup.py
      LICENSE
      README.md


Creating setup.py
-----------------

:file:`setup.py` is the build script for :ref:`setuptools`. It tells setuptools
about your package (such as the name and version) as well as which code files
to include.

Open :file:`setup.py` and enter the following content, you can personalize
the values if you want:

.. code-block:: python

    import setuptools

    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="example_pkg",
        version="0.0.1",
        author="Example Author",
        author_email="author@example.com",
        description="A small example package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/pypa/sampleproject",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )


:func:`setup` takes several arguments. This example package uses a relatively
minimal set:

- ``name`` is the name of your package. This can be any name as long as only
  contains letters, numbers, ``_`` , and ``-``. It also must not already
  taken on pypi.org.
- ``version`` is the package version see :pep:`440` for more details on
  versions.
- ``author`` and ``author_email`` are used to identify the author of the
  package.
- ``description`` is a short, one-sentence summary of the package.
- ``long_description`` is a detailed description of the package. This is
  shown on the package detail package on the Python Package Index. In
  this case, the long description is loaded from :file:`README.md` which is
  a common pattern.
- ``long_description_content_type`` tells the index what type of markup is
  used for the long description. In this case, it's Markdown.
- ``url`` is the URL for the homepage of the project. For many projects, this
  will just be a link to GitHub, GitLab, Bitbucket, or similar code hosting
  service.
- ``packages`` is a list of all Python :term:`import packages <Import
  Package>` that should be included in the :term:`distribution package`. 
  Instead of listing each package manually, we can use :func:`find_packages`
  to automatically discover all packages and subpackages. In this case, the
  list of packages will be `example_pkg` as that's the only package present.
- ``classifiers`` tell the index and :ref:`pip` some additional metadata
  about your package. In this case, the package is only compatible with Python
  3, is licensed under the MIT license, and is OS-independent. You should
  always include at least which version(s) of Python your package works on,
  which license your package is available under, and which operating systems
  your package will work on. For a complete list of classifiers, see
  https://pypi.org/classifiers/.

There are many more than the ones mentioned here. See
:doc:`/guides/distributing-packages-using-setuptools` for more details.


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


.. _generating archives:

Generating distribution archives
--------------------------------

The next step is to generate :term:`distribution packages <distribution
package>` for the package. These are archives that are uploaded to the Package
Index and can be installed by :ref:`pip`.

Make sure you have the latest versions of ``setuptools`` and ``wheel``
installed:

.. code-block:: bash

    python3 -m pip install --user --upgrade setuptools wheel

.. tip:: IF you have trouble installing these, see the
   :doc:`installing-packages` tutorial.

Now run this command from the same directory where :file:`setup.py` is located:

.. code-block:: bash

    python3 setup.py sdist bdist_wheel

This command should output a lot of text and once completed should generate two
files in the :file:`dist` directory:

.. code-block:: text

    dist/
      example_pkg-0.0.1-py3-none-any.whl
      example_pkg-0.0.1.tar.gz

.. note:: If you run into trouble here, please copy the output and file an issue
  over on `packaging problems`_ and we'll do our best to help you!

.. _packaging problems:
  https://github.com/pypa/packaging-problems/issues/new?title=Trouble+following+packaging+libraries+tutorial


The ``tar.gz`` file is a :term:`source archive` whereas the ``.whl`` file is a
:term:`built distribution`. Newer :ref:`pip` versions preferentially install
built distributions, but will fall back to source archives if needed. You
should always upload a source archive and provide built archives for the
platforms your project is compatible with. In this case, our example package is
compatible with Python on any platform so only one built distribution is needed.

Uploading the distribution archives
-----------------------------------

Finally, it's time to upload your package to the Python Package Index!

The first thing you'll need to do is register an account on `Test PyPI`. Test
PyPI is a separate instance of the package index intended for testing and
experimentation. It's great for things like this tutorial where we don't
necessarily want to upload to the real index. To register an account, go to
https://test.pypi.org/account/register/ and complete the steps on that page.
You will also need to verify your email address before you're able to upload
any packages.  For more details on Test PyPI, see
:doc:`/guides/using-testpypi`.

Now that you are registered, you can use :ref:`twine` to upload the
distribution packages. You'll need to install Twine:

.. code-block:: bash

    python3 -m pip install --user --upgrade twine

Once installed, run Twine to upload all of the archives under :file:`dist`:

.. code-block:: bash

    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

You will be prompted for the username and password you registered with Test
PyPI. After the command completes, you should see output similar to this:

.. code-block:: bash

    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: [your username]
    Enter your password:
    Uploading example_pkg-0.0.1-py3-none-any.whl
    100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
    Uploading example_pkg-0.0.1.tar.gz
    100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]

.. note:: If you get an error that says ``The user '[your username]' isn't
  allowed to upload to project 'example-pkg'``, you'll need to go and pick
  a unique name for your package. A good choice is
  ``example_pkg_your_username``. Update the ``name`` argument in
  :file:`setup.py`, remove the :file:`dist` folder, and
  :ref:`regenerate the archives <generating archives>`.


Once uploaded your package should be viewable on TestPyPI, for example,
https://test.pypi.org/project/example-pkg


Installing your newly uploaded package
--------------------------------------

You can use :ref:`pip` to install your package and verify that it works.
Create a new :ref:`virtualenv` (see :doc:`/tutorials/installing-packages` for
detailed instructions) and install your package from TestPyPI:

.. code-block:: bash

    python3 -m pip install --index-url https://test.pypi.org/simple/ example_pkg

.. note:: If you used a different package name in the preview step, replace
  ``example_pkg`` in the command above with your package name.

pip should install the package from Test PyPI and the output should look
something like this:

.. code-block:: text

    Collecting example_pkg
      Downloading https://test-files.pythonhosted.org/packages/.../example_pkg-0.0.1-py3-none-any.whl
    Installing collected packages: example-pkg
    Successfully installed example-pkg-0.0.1

You can test that it was installed correctly by importing the module and
referencing the ``name`` property you put in :file:`__init__.py` earlier.

Run the Python interpreter (make sure you're still in your virtualenv):

.. code-block:: bash

    python

And then import the module and print out the ``name`` property. This should be
the same regardless of what you name you gave your :term:`distribution package`
in :file:`setup.py` because your :term:`import package` is ``example_pkg``.

.. code-block:: python

    >>> import example_pkg
    >>> example_pkg.name
    'example_pkg'


Next steps
----------

**Congratulations, you've packaged and distributed a Python project!**
✨ 🍰 ✨

Keep in mind that this tutorial showed you how to upload your package to Test
PyPI and Test PyPI is ephemeral. It's not unusual for packages and accounts to
be deleted occasionally. If you want to upload your package to the real Python
Package Index you can do it by registering an account on https://pypi.org and
following the same instructions, however, use ``twine upload dist/*`` to upload
your package and enter your credentials for the account you registered on the
real PyPI. You can install your package from the real PyPI using
``pip install your-package``.

At this point if you want to read more on packaging Python libraries here are
some things you can do:

* Read more about using :ref:`setuptools` to package libraries in
  :doc:`/guides/distributing-packages-using-setuptools`.
* Read about :doc:`/guides/packaging-binary-extensions`.
* Consider alternatives to :ref:`setuptools` such as :ref:`flit`, `hatch`_,
  and `poetry`_.

.. _hatch: https://github.com/ofek/hatch
.. _poetry: https://github.com/sdispater/poetry
