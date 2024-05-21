.. _distributing-packages:

===================================
Packaging and distributing projects
===================================

:Page Status: Outdated
:Last Reviewed: 2023-12-14

This section covers some additional details on configuring, packaging and
distributing Python projects with ``setuptools`` that aren't covered by the
introductory tutorial in :doc:`/tutorials/packaging-projects`.  It still assumes
that you are already familiar with the contents of the
:doc:`/tutorials/installing-packages` page.

The section does *not* aim to cover best practices for Python project
development as a whole.  For example, it does not provide guidance or tool
recommendations for version control, documentation, or testing.

For more reference material, see :std:doc:`Building and Distributing
Packages <setuptools:userguide/index>` in the :ref:`setuptools` docs, but note
that some advisory content there may be outdated. In the event of
conflicts, prefer the advice in the Python Packaging User Guide.



Requirements for packaging and distributing
===========================================
1. First, make sure you have already fulfilled the :ref:`requirements for
   installing packages <installing_requirements>`.

2.  Install "twine" [1]_:

    .. tab:: Unix/macOS

        .. code-block:: bash

            python3 -m pip install twine

    .. tab:: Windows

        .. code-block:: bat

            py -m pip install twine

   You'll need this to upload your project :term:`distributions <Distribution
   Package>` to :term:`PyPI <Python Package Index (PyPI)>` (see :ref:`below
   <Uploading your Project to PyPI>`).


Configuring your project
========================


Initial files
-------------

setup.py
~~~~~~~~

The most important file is :file:`setup.py` which exists at the root of your
project directory. For an example, see the `setup.py
<https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py>`_ in the `PyPA
sample project <https://github.com/pypa/sampleproject>`_.

:file:`setup.py` serves two primary functions:

1. It's the file where various aspects of your project are configured. The
   primary feature of :file:`setup.py` is that it contains a global ``setup()``
   function.  The keyword arguments to this function are how specific details
   of your project are defined.  The most relevant arguments are explained in
   :ref:`the section below <setup() args>`.

2. It's the command line interface for running various commands that
   relate to packaging tasks. To get a listing of available commands, run
   ``python3 setup.py --help-commands``.


setup.cfg
~~~~~~~~~

:file:`setup.cfg` is an ini file that contains option defaults for
:file:`setup.py` commands.  For an example, see the `setup.cfg
<https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.cfg>`_ in the `PyPA
sample project <https://github.com/pypa/sampleproject>`_.


README.rst / README.md
~~~~~~~~~~~~~~~~~~~~~~

All projects should contain a readme file that covers the goal of the project.
The most common format is `reStructuredText
<https://docutils.sourceforge.io/rst.html>`_ with an "rst" extension, although
this is not a requirement; multiple variants of `Markdown
<https://daringfireball.net/projects/markdown/>`_ are supported as well (look
at ``setup()``'s :ref:`long_description_content_type <description>` argument).

For an example, see `README.md
<https://github.com/pypa/sampleproject/blob/main/README.md>`_ from the `PyPA
sample project <https://github.com/pypa/sampleproject>`_.

.. note:: Projects using :ref:`setuptools` 0.6.27+ have standard readme files
   (:file:`README.rst`, :file:`README.txt`, or :file:`README`) included in
   source distributions by default. The built-in :ref:`distutils` library adopts
   this behavior beginning in Python 3.7. Additionally, :ref:`setuptools`
   36.4.0+ will include a :file:`README.md` if found. If you are using
   setuptools, you don't need to list your readme file in :file:`MANIFEST.in`.
   Otherwise, include it to be explicit.

MANIFEST.in
~~~~~~~~~~~

A :file:`MANIFEST.in` is needed when you need to package additional files that
are not automatically included in a source distribution.  For details on
writing a :file:`MANIFEST.in` file, including a list of what's included by
default, see ":ref:`Using MANIFEST.in`".

However, you may not have to use a :file:`MANIFEST.in`. For an example, the `PyPA
sample project <https://github.com/pypa/sampleproject>`_ has removed its manifest
file, since all the necessary files have been included by :ref:`setuptools` 43.0.0
and newer.

.. note:: :file:`MANIFEST.in` does not affect binary distributions such as wheels.

LICENSE.txt
~~~~~~~~~~~

Every package should include a license file detailing the terms of
distribution. In many jurisdictions, packages without an explicit license can
not be legally used or distributed by anyone other than the copyright holder.
If you're unsure which license to choose, you can use resources such as
`GitHub's Choose a License <https://choosealicense.com/>`_ or consult a lawyer.

For an example, see the `LICENSE.txt
<https://github.com/pypa/sampleproject/blob/main/LICENSE.txt>`_ from the `PyPA
sample project <https://github.com/pypa/sampleproject>`_.

<your package>
~~~~~~~~~~~~~~

Although it's not required, the most common practice is to include your
Python modules and packages under a single top-level package that has the same
:ref:`name <setup() name>` as your project, or something very close.

For an example, see the `sample
<https://github.com/pypa/sampleproject/tree/main/src/sample>`_ package that's
included in the `PyPA sample project <https://github.com/pypa/sampleproject>`_.


.. _`setup() args`:

setup() args
------------

As mentioned above, the primary feature of :file:`setup.py` is that it contains
a global ``setup()`` function.  The keyword arguments to this function are how
specific details of your project are defined.

Some are temporarily explained below until their information is moved elsewhere.
The full list can be found :doc:`in the setuptools documentation
<setuptools:references/keywords>`.

Most of the snippets given are
taken from the `setup.py
<https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py>`_ contained in the
`PyPA sample project <https://github.com/pypa/sampleproject>`_.



See :ref:`Choosing a versioning scheme` for more information on ways to use versions to convey
compatibility information to your users.




``packages``
~~~~~~~~~~~~

::

  packages=find_packages(include=['sample', 'sample.*']),

Set ``packages`` to a list of all :term:`packages <Import Package>` in your
project, including their subpackages, sub-subpackages, etc.  Although the
packages can be listed manually, ``setuptools.find_packages()`` finds them
automatically.  Use the ``include`` keyword argument to find only the given
packages.  Use the ``exclude`` keyword argument to omit packages that are not
intended to be released and installed.


``py_modules``
~~~~~~~~~~~~~~

::

    py_modules=["six"],

If your project contains any single-file Python modules that aren't part of a
package, set ``py_modules`` to a list of the names of the modules (minus the
``.py`` extension) in order to make :ref:`setuptools` aware of them.


``install_requires``
~~~~~~~~~~~~~~~~~~~~

::

 install_requires=['peppercorn'],

"install_requires" should be used to specify what dependencies a project
minimally needs to run. When the project is installed by :ref:`pip`, this is the
specification that is used to install its dependencies.

For more on using "install_requires" see :ref:`install_requires vs Requirements files`.



.. _`Package Data`:

``package_data``
~~~~~~~~~~~~~~~~

::

 package_data={
     'sample': ['package_data.dat'],
 },


Often, additional files need to be installed into a :term:`package <Import
Package>`. These files are often data that’s closely related to the package’s
implementation, or text files containing documentation that might be of interest
to programmers using the package. These files are called "package data".

The value must be a mapping from package name to a list of relative path names
that should be copied into the package. The paths are interpreted as relative to
the directory containing the package.

For more information, see :std:doc:`Including Data Files
<setuptools:userguide/datafiles>` from the
:std:doc:`setuptools docs <setuptools:index>`.


.. _`Data Files`:

``data_files``
~~~~~~~~~~~~~~

::

    data_files=[('my_data', ['data/data_file'])],

Although configuring :ref:`Package Data` is sufficient for most needs, in some
cases you may need to place data files *outside* of your :term:`packages
<Import Package>`.  The ``data_files`` directive allows you to do that.
It is mostly useful if you need to install files which are used by other
programs, which may be unaware of Python packages.

Each ``(directory, files)`` pair in the sequence specifies the installation
directory and the files to install there. The ``directory`` must be a relative
path (although this may change in the future, see
`wheel Issue #92 <https://github.com/pypa/wheel/issues/92>`_),
and it is interpreted relative to the installation prefix
(Python’s ``sys.prefix`` for a default installation;
``site.USER_BASE`` for a user installation).
Each file name in ``files`` is interpreted relative to the :file:`setup.py`
script at the top of the project source distribution.

For more information see the distutils section on :ref:`Installing Additional Files
<setuptools:distutils-additional-files>`.

.. note::

  When installing packages as egg, ``data_files`` is not supported.
  So, if your project uses :ref:`setuptools`, you must use ``pip``
  to install it. Alternatively, if you must use ``python setup.py``,
  then you need to pass the ``--old-and-unmanageable`` option.


``scripts``
~~~~~~~~~~~

Although ``setup()`` supports a :ref:`scripts
<setuptools:distutils-installing-scripts>`
keyword for pointing to pre-made scripts to install, the recommended approach to
achieve cross-platform compatibility is to use :ref:`console_scripts` entry
points (see below).


Choosing a versioning scheme
----------------------------

See :ref:`versioning` for information on common version schemes and how to
choose between them.


Working in "development mode"
=============================

You can install a project in "editable"
or "develop" mode while you're working on it.
When installed as editable, a project can be
edited in-place without reinstallation:
changes to Python source files in projects installed as editable will be reflected the next time an interpreter process is started.

To install a Python package in "editable"/"development" mode
Change directory to the root of the project directory and run:

.. code-block:: bash

   python3 -m pip install -e .


The pip command-line flag ``-e`` is short for ``--editable``, and ``.`` refers
to the current working directory, so together, it means to install the current
directory (i.e. your project) in editable mode.  This will also install any
dependencies declared with ``install_requires`` and any scripts declared with
``console_scripts``.  Dependencies will be installed in the usual, non-editable
mode.

You may want to install some of your dependencies in editable
mode as well. For example, supposing your project requires "foo" and "bar", but
you want "bar" installed from VCS in editable mode, then you could construct a
requirements file like so::

  -e .
  -e bar @ git+https://somerepo/bar.git

The first line says to install your project and any dependencies. The second
line overrides the "bar" dependency, such that it's fulfilled from VCS, not
PyPI.

If, however, you want "bar" installed from a local directory in editable mode, the requirements file should look like this, with the local paths at the top of the file::

  -e /path/to/project/bar
  -e .

Otherwise, the dependency will be fulfilled from PyPI, due to the installation order of the requirements file.  For more on requirements files, see the :ref:`Requirements File
<pip:Requirements Files>` section in the pip docs.  For more on VCS installs,
see the :ref:`VCS Support <pip:VCS Support>` section of the pip docs.

Lastly, if you don't want to install any dependencies at all, you can run:

.. code-block:: bash

   python3 -m pip install -e . --no-deps


For more information, see the
:doc:`Development Mode <setuptools:userguide/development_mode>` section
of the :ref:`setuptools` docs.

.. _`Packaging your project`:

Packaging your project
======================

To have your project installable from a :term:`Package Index` like :term:`PyPI
<Python Package Index (PyPI)>`, you'll need to create a :term:`Distribution
<Distribution Package>` (aka ":term:`Package <Distribution Package>`") for your
project.

Before you can build wheels and sdists for your project, you'll need to install the
``build`` package:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install build

.. tab:: Windows

    .. code-block:: bat

        py -m pip install build


Source distributions
--------------------

Minimally, you should create a :term:`Source Distribution <Source Distribution (or
"sdist")>`:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m build --sdist

.. tab:: Windows

    .. code-block:: bat

        py -m build --sdist


A "source distribution" is unbuilt (i.e. it's not a :term:`Built
Distribution`), and requires a build step when installed by pip.  Even if the
distribution is pure Python (i.e. contains no extensions), it still involves a
build step to build out the installation metadata from :file:`setup.py` and/or
:file:`setup.cfg`.


Wheels
------

You should also create a wheel for your project. A wheel is a :term:`built
package <Built Distribution>` that can be installed without needing to go
through the "build" process. Installing wheels is substantially faster for the
end user than installing from a source distribution.

If your project is pure Python then you'll be creating a
:ref:`"Pure Python Wheel" (see section below) <Pure Python Wheels>`.

If your project contains compiled extensions, then you'll be creating what's
called a :ref:`*Platform Wheel* (see section below) <Platform Wheels>`.

.. note:: If your project also supports Python 2 *and* contains no C extensions,
  then you should create what's called a *Universal Wheel* by adding the
  following to your :file:`setup.cfg` file:

  .. code-block:: text

     [bdist_wheel]
     universal=1

  Only use this setting if your project does not have any C extensions *and*
  supports Python 2 and 3.


.. _`Pure Python Wheels`:

Pure Python Wheels
~~~~~~~~~~~~~~~~~~

*Pure Python Wheels* contain no compiled extensions, and therefore only require a
single Python wheel.

To build the wheel:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m build --wheel

.. tab:: Windows

    .. code-block:: bat

        py -m build --wheel

The ``wheel`` package will detect that the code is pure Python, and build a
wheel that's named such that it's usable on any Python 3 installation.  For
details on the naming of wheel files, see :pep:`425`.

If you run ``build`` without ``--wheel`` or ``--sdist``, it will build both
files for you; this is useful when you don't need multiple wheels.

.. _`Platform Wheels`:

Platform Wheels
~~~~~~~~~~~~~~~

*Platform Wheels* are wheels that are specific to a certain platform like Linux,
macOS, or Windows, usually due to containing compiled extensions.

To build the wheel:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m build --wheel

.. tab:: Windows

    .. code-block:: bat

        py -m build --wheel


The ``wheel`` package will detect that the code is not pure Python, and build
a wheel that's named such that it's only usable on the platform that it was
built on. For details on the naming of wheel files, see :pep:`425`.

.. note::

  :term:`PyPI <Python Package Index (PyPI)>` currently supports uploads of
  platform wheels for Windows, macOS, and the multi-distro ``manylinux*`` ABI.
  Details of the latter are defined in :pep:`513`.


.. _`Uploading your Project to PyPI`:

Uploading your Project to PyPI
==============================

When you ran the command to create your distribution, a new directory ``dist/``
was created under your project's root directory. That's where you'll find your
distribution file(s) to upload.

.. note:: These files are only created when you run the command to create your
  distribution. This means that any time you change the source of your project
  or the configuration in your :file:`setup.py` file, you will need to rebuild
  these files again before you can distribute the changes to PyPI.

.. note:: Before releasing on main PyPI repo, you might prefer
  training with the `PyPI test site <https://test.pypi.org/>`_ which
  is cleaned on a semi regular basis. See :ref:`using-test-pypi` on
  how to setup your configuration in order to use it.

.. warning:: In other resources you may encounter references to using
  ``python setup.py register`` and ``python setup.py upload``. These methods
  of registering and uploading a package are **strongly discouraged** as it may
  use a plaintext HTTP or unverified HTTPS connection on some Python versions,
  allowing your username and password to be intercepted during transmission.

.. tip:: The reStructuredText parser used on PyPI is **not** Sphinx!
  Furthermore, to ensure safety of all users, certain kinds of URLs and
  directives are forbidden or stripped out (e.g., the ``.. raw::``
  directive). **Before** trying to upload your distribution, you should check
  to see if your brief / long descriptions provided in :file:`setup.py` are
  valid.  You can do this by running :std:doc:`twine check <index>` on
  your package files:

  .. code-block:: bash

     twine check dist/*

Create an account
-----------------

First, you need a :term:`PyPI <Python Package Index (PyPI)>` user account. You
can create an account
`using the form on the PyPI website <https://pypi.org/account/register/>`_.

Now you'll create a PyPI `API token`_ so you will be able to securely upload
your project.

Go to https://pypi.org/manage/account/#api-tokens and create a new
`API token`_; don't limit its scope to a particular project, since you
are creating a new project.

**Don't close the page until you have copied and saved the token — you
won't see that token again.**

.. Note:: To avoid having to copy and paste the token every time you
  upload, you can create a :file:`$HOME/.pypirc` file:

  .. code-block:: text

    [pypi]
    username = __token__
    password = <the token value, including the `pypi-` prefix>

  **Be aware that this stores your token in plaintext.**

  For more details, see the :ref:`specification <pypirc>` for :file:`.pypirc`.

.. _register-your-project:
.. _API token: https://pypi.org/help/#apitoken

Upload your distributions
-------------------------

Once you have an account you can upload your distributions to
:term:`PyPI <Python Package Index (PyPI)>` using :ref:`twine`.

The process for uploading a release is the same regardless of whether
or not the project already exists on PyPI - if it doesn't exist yet,
it will be automatically created when the first release is uploaded.

For the second and subsequent releases, PyPI only requires that the
version number of the new release differ from any previous releases.

.. code-block:: bash

    twine upload dist/*

You can see if your package has successfully uploaded by navigating to the URL
``https://pypi.org/project/<sampleproject>`` where ``sampleproject`` is
the name of your project that you uploaded. It may take a minute or two for
your project to appear on the site.

----

.. [1] Depending on your platform, this may require root or Administrator
       access. :ref:`pip` is currently considering changing this by `making user
       installs the default behavior
       <https://github.com/pypa/pip/issues/1668>`_.
