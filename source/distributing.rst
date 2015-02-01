===================================
Packaging and Distributing Projects
===================================

:Page Status: Complete
:Last Reviewed: 2014-12-31

This section covers the basics of how to configure, package and distribute your
own Python projects.  It assumes that you are already familiar with the contents
of the :doc:`installing`.

The section does *not* aim to cover best practices for Python project
development as a whole.  For example, it does not provide guidance or tool
recommendations for version control, documentation, or testing.

For a reference material on this topic, see the `Setuptools docs on Building and
Distributing Packages <http://pythonhosted.org/setuptools/setuptools.html>`_,
but note that some advisory content there may be outdated. In the event of
conflicts, prefer the advice in the Python Packaging User Guide.

.. contents:: Contents
   :local:


Requirements for Packaging and Distributing
===========================================

1. First, make sure you have already fulfilled the :ref:`requirements for
   installing packages <installing_requirements>`.

2. Install the "wheel" project [1]_:

   ::

    pip install wheel

   You'll need this to package your project into :term:`wheels <Wheel>` (see
   :ref:`below <Packaging Your Project>`).

3. Install the "twine" project [1]_:

   ::

    pip install twine

   You'll need this to upload your project :term:`distributions <Distribution
   Package>` to :term:`PyPI <Python Package Index (PyPI)>` (see :ref:`below
   <Uploading your Project to PyPI>`).


Configuring your Project
========================


Initial Files
-------------

setup.py
~~~~~~~~

The most important file is "setup.py" which exists at the root of your project
directory. For an example, see the `setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_ in the `PyPA
sample project <https://github.com/pypa/sampleproject>`_.

"setup.py" serves two primary functions:

1. It's the file where various aspects of your project are configured. The
   primary feature of ``setup.py`` is that it contains a global ``setup()``
   function.  The keyword arguments to this function are how specific details of
   your project are defined.  The most relevant arguments are explained in
   :ref:`the section below <setup() args>`.

2. It's the command line interface for running various commands that
   relate to packaging tasks. To get a listing of available commands, run
   ``python setup.py --help-commands``.


setup.cfg
~~~~~~~~~

"setup.cfg" is an ini file that contains option defaults for ``setup.py``
commands.  For an example, see the `setup.cfg
<https://github.com/pypa/sampleproject/blob/master/setup.cfg>`_ in the `PyPA
sample project <https://github.com/pypa/sampleproject>`_.


README.rst
~~~~~~~~~~

All projects should contain a readme file that covers the goal of the
project. The most common format is `reStructuredText
<http://docutils.sourceforge.net/rst.html>`_ with an "rst" extension, although
this is not a requirement.

For an example, see `README.rst
<https://github.com/pypa/sampleproject/blob/master/README.rst>`_ from the `PyPA
sample project <https://github.com/pypa/sampleproject>`_

MANIFEST.in
~~~~~~~~~~~

A "MANIFEST.in" is needed in certain cases where you need to package additional
files that ``python setup.py sdist (or bdist_wheel)`` don't automatically
include. To see a list of what's included by default, see the `Specifying the
files to distribute
<https://docs.python.org/3.4/distutils/sourcedist.html#specifying-the-files-to-distribute>`_
section from the :ref:`distutils` documentation.

For an example, see the `MANIFEST.in
<https://github.com/pypa/sampleproject/blob/master/MANIFEST.in>`_ from the `PyPA
sample project <https://github.com/pypa/sampleproject>`_


For details on writing a ``MANIFEST.in`` file, see the `The MANIFEST.in template
<https://docs.python.org/2/distutils/sourcedist.html#the-manifest-in-template>`_
section from the :ref:`distutils` documentation.


<your package>
~~~~~~~~~~~~~~

Although it's not required, the most common practice to is to include your
python modules and packages under a single top-level package that has the same
:ref:`name <setup() name>` as your project, or something very close.

For an example, see the `sample
<https://github.com/pypa/sampleproject/tree/master/sample>`_ package that's
include in the `PyPA sample project <https://github.com/pypa/sampleproject>`_


.. _`setup() args`:

setup() args
------------

As mentioned above, The primary feature of ``setup.py`` is that it contains a
global ``setup()`` function.  The keyword arguments to this function are how
specific details of your project are defined.

The most relevant arguments are explained below. The snippets given are taken
from the `setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_ contained in the
`PyPA sample project <https://github.com/pypa/sampleproject>`_.


.. _`setup() name`:

name
~~~~

::

  name = 'sample'

This is the name of your project, and will determine how your project is listed
on :term:`PyPI <Python Package Index (PyPI)>`. For details on permitted
characters, see the `name <http://legacy.python.org/dev/peps/pep-0426/#name>`_
section from :ref:`PEP426 <pypa:PEP426s>`.


version
~~~~~~~

::

  version = '1.2.0'


Projects should comply with the `version scheme
<http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
specified in :ref:`PEP440 <pypa:PEP440s>`.  Here are some examples:

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


description
~~~~~~~~~~~

::

  description='A sample Python project',
  long_description=long_description

Give a short and long description for you project.  These values will be
displayed on :term:`PyPI <Python Package Index (PyPI)>` if you publish your
project.


url
~~~

::

  url='https://github.com/pypa/sampleproject'


Give a homepage url for your project.


author
~~~~~~

::

  author='The Python Packaging Authority',
  author_email='pypa-dev@googlegroups.com'

Provide details about the author.


license
~~~~~~~

::

  license='MIT'

Provide the type of license you are using.


classifiers
~~~~~~~~~~~

::

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
  ]

Provide a list of classifiers the categorize your project. For a full listing,
see https://pypi.python.org/pypi?%3Aaction=list_classifiers.


keywords
~~~~~~~~

::

  keywords='sample setuptools development'

List keywords that describe your project.


packages
~~~~~~~~

::

  packages=find_packages(exclude=['contrib', 'docs', 'tests*'])


It's required to list the :term:`packages <Import Package>` to be included
in your project.  Although they can be listed manually,
``setuptools.find_packages`` finds them automatically.  Use the ``exclude``
keyword argument to omit packages that are not intended to be released and
installed.


install_requires
~~~~~~~~~~~~~~~~

::

 install_requires = ['peppercorn']

"install_requires" should be used to specify what dependences a project
minimally needs to run. When the project is installed by :ref:`pip`, this is the
specification that is used to install its dependencies.

For more on using "install_requires" see :ref:`install_requires vs Requirements files`.


.. _`Package Data`:

package_data
~~~~~~~~~~~~

::

 package_data={
     'sample': ['package_data.dat'],
 }


Often, additional files need to be installed into a :term:`package <Import
Package>`. These files are often data that’s closely related to the package’s
implementation, or text files containing documentation that might be of interest
to programmers using the package. These files are called "package data".

The value must be a mapping from package name to a list of relative path names
that should be copied into the package. The paths are interpreted as relative to
the directory containing the package.

For more information, see `Including Data Files
<http://pythonhosted.org/setuptools/setuptools.html#including-data-files>`_ from
the `setuptools docs <http://pythonhosted.org/setuptools/setuptools.html>`_.


.. _`Data Files`:

data_files
~~~~~~~~~~

::

    data_files=[('my_data', ['data/data_file'])]

Although configuring :ref:`Package Data` is sufficient for most needs, in some
cases you may need to place data files *outside* of your :term:`packages
<Import Package>`.  The ``data_files`` directive allows you to do that.

Each (directory, files) pair in the sequence specifies the installation
directory and the files to install there. If directory is a relative path, it is
interpreted relative to the installation prefix (Python’s sys.prefix for
pure-Python :term:`distributions <Distribution Package>`, sys.exec_prefix for
distributions that contain extension modules). Each file name in files is
interpreted relative to the ``setup.py`` script at the top of the project source
distribution.

For more information see the distutils section on `Installing Additional Files
<http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files>`_.

.. note::

  :ref:`setuptools` allows absolute "data_files" paths, and pip honors them as
  absolute, when installing from :term:`sdist <Source Distribution (or
  "sdist")>`.  This is not true when installing from :term:`wheel`
  distributions. Wheels don't support absolute paths, and they end up being
  installed relative to "site-packages".  For discussion see `wheel Issue #92
  <https://bitbucket.org/pypa/wheel/issue/92>`_.


scripts
~~~~~~~

Although ``setup()`` supports a `scripts
<http://docs.python.org/3.4/distutils/setupscript.html#installing-scripts>`_
keyword for pointing to pre-made scripts to install, the recommended approach to
achieve cross-platform compatibility is to use :ref:`console_scripts` entry
points (see below).


entry_points
~~~~~~~~~~~~

::

  entry_points={
    ...
  }


Use this keyword to specify any plugins that your project provides for any named
entry points that may be defined by your project or others that you depend on.

For more information, see the section on `Dynamic Discovery of Services and
Plugins
<http://pythonhosted.org/setuptools/setuptools.html#dynamic-discovery-of-services-and-plugins>`_
from the :ref:`setuptools` docs.

The most commonly used entry point is "console_scripts" (see below).

.. _`console_scripts`:

console_scripts
***************

::

  entry_points={
      'console_scripts': [
          'sample=sample:main',
      ],
  }

Use "console_script" `entry points
<http://pythonhosted.org/setuptools/setuptools.html#dynamic-discovery-of-services-and-plugins>`_
to register your script interfaces. You can then let the toolchain handle the
work of turning these interfaces into actual scripts [2]_.  The scripts will be
generated during the install of your :term:`distribution <Distribution
Package>`.

For more information, see `Automatic Script Creation
<http://pythonhosted.org/setuptools/setuptools.html#automatic-script-creation>`_
from the `setuptools docs <http://pythonhosted.org/setuptools/setuptools.html>`_.



Working in "Development Mode"
=============================

Although not required, it's common to locally install your project in "develop"
or "editable" mode while you're working on it.  This allows the project to be
both installed and editable in project form.

Using "setup.py", run the following:

::

 python setup.py develop


Or you can achieve the same result using :ref:`pip`:

::

 pip install -e .


Note that both commands will install any dependencies declared with
"install_requires" and also any scripts declared with "console_scripts".


For more information, see the `Development Mode
<http://pythonhosted.org/setuptools/setuptools.html#development-mode>`_ section
of the `setuptools docs <http://pythonhosted.org/setuptools/setuptools.html>`_.


.. _`Packaging Your Project`:

Packaging your Project
======================

To have your project installable from a :term:`Package Index` like :term:`PyPI
<Python Package Index (PyPI)>`, you'll need to create a :term:`Distribution
<Distribution Package>` (aka ":term:`Package <Distribution Package>`" ) for your
project.



Source Distributions
--------------------

Minimally, you should create a :term:`Source Distribution <Source Distribution (or
"sdist")>`:

::

 python setup.py sdist


A "source distribution" is unbuilt (i.e, it's not a :term:`Built Distribution`),
and requires a build step when installed by pip.  Even if the distribution is
pure python (i.e. contains no extensions), it still involves a build step to
build out the installation metadata from ``setup.py``.

.. _`Wheels`:

Wheels
------

You should also create a wheel for your project. A wheel is an installable
binary package of your project which can be installed without needing to go
through the "build" process. Installing wheels is substantially faster for
the end user than installing from a source distribution.

To build a Wheel:

::

 python setup.py bdist_wheel

Assuming that your project does not contain any C extensions, this will build
a "Pure Python Wheel". It will be usable on any Python installation with the
same major version (Python 2 or Python 3) as the version you used to build
the wheel.

If your project will run on both Python 2 and Python 3 with the same source,
you should produce a "Universal Wheel" (see below). If your project includes
C extensions, you should produce "Platform Wheels" for the platforms you
support.

If your code supports both Python 2 and 3, but with different code (e.g., you
use ``2to3``) you can run ``setup.py bdist_wheel`` twice, once with Python 2
and once with Python 3. This will produce wheels for each version.


.. _`Universal Wheels`:

Universal Wheels
----------------

Additionally, if your project is pure python (i.e. contains no compiled
extensions) and is version agnostic, then you should create what's called a
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

The ``bdist_wheel`` command will detect automatically whether your code contains
a C extension, and build a pure Python wheel or a platform wheel as appropriate.

.. note::

  :term:`PyPI <Python Package Index (PyPI)>` currently only allows uploads of
  platform wheels for Windows and OS X, NOT linux.  Currently, the wheel tag
  specification (:ref:`PEP425 <pypa:PEP425s>`) does not handle the variation that can
  exist across linux distros.


.. _`Uploading your Project to PyPI`:

Uploading your Project to PyPI
==============================

.. note::

  Before releasing on main PyPI repo, you might prefer training with
  `PyPI test site <https://testpypi.python.org/pypi>`_
  which is cleaned on a semi regular basis. See
  `these instructions <https://wiki.python.org/moin/TestPyPI>`_ on how
  to setup your configuration in order to use it.


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
