===============================================
Tutorial on Packaging and Distributing Projects
===============================================

:Page Status: Complete
:Last Reviewed: 2014-09-30

.. contents:: Contents
   :local:

This tutorial covers the basics of how to create and distribute your
own Python projects.  This tutorial assumes that you are already familiar
with the contents of the :doc:`installing`.


Setup for Project Distributors
==============================

This section describes steps to follow before distributing your own
Python packages.

First, make sure you have already followed the :ref:`setup steps for
installing packages <installing_setup>`.

In addition, you'll need :ref:`wheel` (if you will be building wheels), and
:ref:`twine`, for uploading to :term:`PyPI <Python Package Index (PyPI)>`.

We recommend the following installation sequence:

1. For building :term:`wheels <Wheel>`: ``pip install wheel`` [1]_

2. For uploading :term:`distributions <Distribution>`: ``pip install twine``
   [1]_


Creating your own Project
=========================

In the sections below, we'll reference the `PyPA sample project
<https://github.com/pypa/sampleproject>`_. which exists as a companion to this
tutorial.


Layout
------

The critical requirement for creating projects using :ref:`setuptools` is to
have a ``setup.py``. For an example, see `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_.  We'll cover the
components of ``setup.py`` in the sections below.

Although it's not required, most projects will organize the code using a `single
top-level package <https://github.com/pypa/sampleproject/tree/master/sample>`_,
that's named the same as the project.

Additionally, most projects will contain the following files:

* A `README <https://github.com/pypa/sampleproject/blob/master/README.rst>`_ for
  explaining the project.
* A `setup.cfg <https://github.com/pypa/sampleproject/blob/master/setup.cfg>`_
  that contains option defaults for ``setup.py`` commands.
* A `MANIFEST.in
  <https://github.com/pypa/sampleproject/blob/master/MANIFEST.in>`_ that defines
  additional files to be included in the project distribution when it's
  packaged.


Name
----

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

  name = 'sample'

This will determine how your project is listed on :term:`PyPI <Python Package
Index (PyPI)>`. For details on permitted characters, see the `name
<http://legacy.python.org/dev/peps/pep-0426/#name>`_ section from :ref:`PEP426
<PEP426s>`.


Version
-------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

  version = '1.2.0'


Projects should aim to comply with the `version scheme
<http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
specified in :ref:`PEP440 <PEP440s>`.  Here are some examples:

::

  1.2.0.dev1  # Development release
  1.2.0a1     # Alpha Release
  1.2.0b1     # Beta Release
  1.2.0rc1    # RC Release
  1.2.0       # Final Release
  1.2.0.post1 # Post Release

If the project code itself needs run-time access to the version, the simplest
way is to keep the version in both ``setup.py`` and your code. If you'd rather
not duplicate the value, there are a few ways to manage this. See the
":ref:`Single sourcing the version`" Advanced Topics section.


Packages
--------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

  packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

It's required to list the :term:`packages <Package (Meaning #1)>` to be included
in your project.  Although they can be listed manually,
``setuptools.find_packages`` finds them automatically.  Use the ``exclude``
keyword argument to omit packages that are not intended to be released and
installed.


Metadata
--------

It's important to include various metadata about your project.

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

    # A description of your project
    description='A sample Python project',
    long_description=long_description,

    # The project's main homepage
    url='https://github.com/pypa/sampleproject',

    # Author details
    author='The Python Packaging Authority',
    author_email='pypa-dev@googlegroups.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='sample setuptools development',



Dependencies
------------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

 install_requires = ['peppercorn']

"install_requires" should be used to specify what dependences a project
minimally needs to run. When the project is installed by :ref:`pip`, this is the
specification that is used to install its dependencies.

For more on using "install_requires" see :ref:`install_requires vs Requirements files`.


.. _`Package Data`:

Package Data
------------

Often, additional files need to be installed into a :term:`package <Package
(Meaning #1)>`. These files are often data that’s closely related to the
package’s implementation, or text files containing documentation that might be
of interest to programmers using the package. These files are called "package
data".

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

 package_data={
     'sample': ['package_data.dat'],
 }


The value must be a mapping from package name to a list of relative path names
that should be copied into the package. The paths are interpreted as relative to
the directory containing the package.

For more information, see `Including Data Files
<http://pythonhosted.org/setuptools/setuptools.html#including-data-files>`_ from
the `setuptools docs <http://pythonhosted.org/setuptools/setuptools.html>`_.


.. _`Data Files`:

Data Files
----------

Although configuring :ref:`Package Data` is sufficient for most needs, in some
cases you may need to place data files *outside* of your :term:`packages
<Package (Meaning #1)>`.  The ``data_files`` directive allows you to do that.

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

    data_files=[('my_data', ['data/data_file'])],

Each (directory, files) pair in the sequence specifies the installation
directory and the files to install there. If directory is a relative path, it is
interpreted relative to the installation prefix (Python’s sys.prefix for
pure-Python distributions, sys.exec_prefix for distributions that contain
extension modules). Each file name in files is interpreted relative to the
``setup.py`` script at the top of the project source distribution.

For more information see the distutils section on `Installing Additional Files
<http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files>`_.

.. note::

  :ref:`setuptools` allows absolute "data_files" paths, and pip honors them as
  absolute, when installing from :term:`sdist <Source Distribution (or
  "sdist")>`.  This is not true, when installing from :term:`wheel`
  distributions. Wheels don't support absolute paths, and they end up being
  installed relative to "site-packages".  For discussion see `wheel Issue #92
  <https://bitbucket.org/pypa/wheel/issue/92>`_.


Scripts
-------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

  entry_points={
      'console_scripts': [
          'sample=sample:main',
      ],
  },

Although ``setup.py`` supports a `scripts
<http://docs.python.org/3.4/distutils/setupscript.html#installing-scripts>`_
keyword for pointing to pre-made scripts, the recommended approach to achieve
cross-platform compatibility, is to use "console_script" `entry points
<http://pythonhosted.org/setuptools/setuptools.html#dynamic-discovery-of-services-and-plugins>`_
that register your script interfaces, and let the toolchain handle the work of
turning these interfaces into actual scripts [2]_.  The scripts will be
generated during the install of your :term:`distribution <Distribution>`.

For more information, see `Automatic Script Creation
<http://pythonhosted.org/setuptools/setuptools.html#automatic-script-creation>`_
from the `setuptools docs <http://pythonhosted.org/setuptools/setuptools.html>`_.


MANIFEST.in
-----------

A ``MANIFEST.in`` file is needed in certain cases where you need to package
additional files that ``python setup.py sdist (or bdist_wheel)`` don't
automatically include.

To see a list of what's included by default, see the `Specifying the files to
distribute
<https://docs.python.org/3.4/distutils/sourcedist.html#specifying-the-files-to-distribute>`_
section from the :ref:`distutils` documentation.

For details on writing a ``MANIFEST.in`` file, see the `The MANIFEST.in template
<https://docs.python.org/2/distutils/sourcedist.html#the-manifest-in-template>`_
section from the :ref:`distutils` documentation.


Developing your project
=======================

Although not required, it's common to locally install your project in "develop"
or "editable" mode, while you're working on it.  This allows the project to be
both installed and editable in project form.

::

 cd myproject
 python setup.py develop    # the setuptools way
 pip install -e .           # the pip way (which just calls "setup.py develop")


For more information, see the `Development Mode
<http://pythonhosted.org/setuptools/setuptools.html#development-mode>`_ section
of the `setuptools docs <http://pythonhosted.org/setuptools/setuptools.html>`_.


Packaging your Project
======================

To have your project installable from a :term:`Package Index` like :term:`PyPI
<Python Package Index (PyPI)>`, you'll need to create a :term:`Distribution`
(aka ":term:`Package <Package (Meaning #2)>`" ) for your project.



Source Distributions
--------------------

Minimally, you should create a :term:`Source Distribution <Source Distribution (or
"sdist")>`:

::

 python setup.py sdist


A "source distribution" is unbuilt (i.e, it's not a :term:`Built Distribution`),
and requires a build step when installed by pip.  Even if the distribution is
pure python (i.e. contains no extensions), it still involves a build step to
build out the installation metadata from "``setup.py``".

.. _`Universal Wheels`:

Universal Wheels
----------------

Additionally, if your project is pure python (i.e. contains no compiled
extensions) and is version agnostic, then you should also create what's called a
"Universal Wheel". This is a wheel that can be installed anywhere by :ref:`pip`.

To build a Universal Wheel:

::

 python setup.py bdist_wheel --universal


You can also permanently set the ``--universal`` flag in "setup.cfg" (e.g., see
`sampleproject/setup.cfg
<https://github.com/pypa/sampleproject/blob/master/setup.cfg>`_)

::

 [bdist_wheel]
 universal=1


Only use the ``--universal`` setting, if:

1. Your project runs on Python 2 and 3 with no changes (i.e. it does not
   require 2to3).
2. Your project does not have any C extensions.

Beware that ``bdist_wheel`` does not currently have any checks to warn you if
use the setting inappropriately.

If your project has optional C extensions, it is recommended not to publish a
universal wheel, because pip will prefer the wheel over a source installation,
and prevent the possibility of building the extension.


Platform Wheels
---------------

"Platform Wheels" are wheels that are specific to a certain platform like linux,
OSX, or Windows, usually due to containing compiled extensions.

"Platform Wheels" are built the same as "Universal Wheels", but without the
``--universal`` flag:

::

 python setup.py bdist_wheel


.. note::

  :term:`PyPI <Python Package Index (PyPI)>` currently only allows uploads of
  platform wheels for Windows and OS X, NOT linux.  Currently, the wheel tag
  specification (:ref:`PEP425 <PEP425s>`) does not handle the variation that can
  exist across linux distros.


Uploading your Project to PyPI
==============================

First, you need a :term:`PyPI <Python Package Index (PyPI)>` user
account. There are two options:

1. Create an account manually `using the form on the PyPI website
   <https://pypi.python.org/pypi?%3Aaction=register_form>`_.

2. Have an account created as part of registering your first project (see option
   #2 below).

Next, you need to register your project.  There are two ways to do this:

1. **(Recommended):** Use `the form on the PyPI website
   <https://pypi.python.org/pypi?%3Aaction=submit_form>`_.  Although the form is
   cumbersome, it's a secure option over using #2 below, which passes your
   credentials over plaintext.
2. Run ``python setup.py register``.  If you don't have a user account already,
   a wizard will create one for you.


If you created your account using option #1 (the form), you'll need to manually
write a ``~/.pypirc`` file like so.

   ::

    [distutils]
    index-servers=pypi

    [pypi]
    repository = https://pypi.python.org/pypi
    username = <username>
    password = <password>

You can leave out the password line if below you use twine with its
``-p PASSWORD`` argument.

Finally, you can upload your distributions to :term:`PyPI <Python Package Index
(PyPI)>`. There are two options.

1. **(Recommended):** Use :ref:`twine`

   ::

     twine upload dist/*

   The biggest reason to use twine is that ``python setup.py upload`` (option #2
   below) uploads files over plaintext. This means anytime you use it you expose
   your username and password to a MITM attack. Twine uses only verified TLS to
   upload to PyPI protecting your credentials from theft.

   Secondly it allows you to precreate your distribution files.  ``python
   setup.py upload`` only allows you to upload something that you've created in
   the same command invocation. This means that you cannot test the exact file
   you're going to upload to PyPI to ensure that it works before uploading it.

   Finally it allows you to pre-sign your files and pass the .asc files into the
   command line invocation (``twine upload twine-1.0.1.tar.gz
   twine-1.0.1.tar.gz.asc``). This enables you to be assured that you're typing
   your gpg passphrase into gpg itself and not anything else since *you* will be
   the one directly executing ``gpg --detach-sign -a <filename>``.


2. Use :ref:`setuptools`:

   ::

    python setup.py sdist bdist_wheel upload


----

.. [1] Depending on your platform, this may require root or Administrator
       access. :ref:`pip` is currently considering changing this by `making user
       installs the default behavior
       <https://github.com/pypa/pip/issues/1668>`_.


.. [2] Specifically, the "console_script" approach generates ``.exe`` files on
       Windows, which are necessary because the OS special-cases ``.exe`` files.
       Script-execution features like ``PATHEXT`` and the `Python Launcher for
       Windows <http://legacy.python.org/dev/peps/pep-0397/>`_ allow scripts to
       be used in many cases, but not all.
