===================================
Packaging and Distributing Projects
===================================

:Page Status: Complete
:Last Reviewed: 2015-09-08

This section covers the basics of how to configure, package and distribute your
own Python projects.  It assumes that you are already familiar with the contents
of the :doc:`installing` page.

The section does *not* aim to cover best practices for Python project
development as a whole.  For example, it does not provide guidance or tool
recommendations for version control, documentation, or testing.

For more reference material, see `Building and Distributing Packages
<https://setuptools.readthedocs.io/en/latest/setuptools.html>`_ in the
:ref:`setuptools` docs, but note that some advisory content there may be
outdated. In the event of conflicts, prefer the advice in the Python
Packaging User Guide.

.. contents:: Contents
   :local:


Requirements for Packaging and Distributing
===========================================

1. First, make sure you have already fulfilled the :ref:`requirements for
   installing packages <installing_requirements>`.

2. Install "twine" [1]_:

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

Although it's not required, the most common practice is to include your
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

  name='sample',

This is the name of your project, and will determine how your project is listed
on :term:`PyPI <Python Package Index (PyPI)>`. For details on permitted
characters, see the :pep:`name <426#name>`
section from :pep:`426`.


version
~~~~~~~

::

  version='1.2.0',

This is the current version of your project, allowing your users to determine whether or not
they have the latest version, and to indicate which specific versions they've tested their own
software against.

Versions are displayed on :term:`PyPI <Python Package Index (PyPI)>` for each release if you
publish your project.

See :ref:`Choosing a versioning scheme` for more information on ways to use versions to convey
compatibility information to your users.

If the project code itself needs run-time access to the version, the simplest
way is to keep the version in both ``setup.py`` and your code. If you'd rather
not duplicate the value, there are a few ways to manage this. See the
":ref:`Single sourcing the version`" Advanced Topics section.


description
~~~~~~~~~~~

::

  description='A sample Python project',
  long_description=long_description,

Give a short and long description for you project.  These values will be
displayed on :term:`PyPI <Python Package Index (PyPI)>` if you publish your
project.


url
~~~

::

  url='https://github.com/pypa/sampleproject',


Give a homepage url for your project.


author
~~~~~~

::

  author='The Python Packaging Authority',
  author_email='pypa-dev@googlegroups.com',

Provide details about the author.


license
~~~~~~~

::

  license='MIT',

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
  ],

Provide a list of classifiers that categorize your project. For a full listing,
see https://pypi.python.org/pypi?%3Aaction=list_classifiers.


keywords
~~~~~~~~

::

  keywords='sample setuptools development',

List keywords that describe your project.


packages
~~~~~~~~

::

  packages=find_packages(exclude=['contrib', 'docs', 'tests*']),


It's required to list the :term:`packages <Import Package>` to be included
in your project.  Although they can be listed manually,
``setuptools.find_packages`` finds them automatically.  Use the ``exclude``
keyword argument to omit packages that are not intended to be released and
installed.


install_requires
~~~~~~~~~~~~~~~~

::

 install_requires=['peppercorn'],

"install_requires" should be used to specify what dependencies a project
minimally needs to run. When the project is installed by :ref:`pip`, this is the
specification that is used to install its dependencies.

For more on using "install_requires" see :ref:`install_requires vs Requirements files`.


.. _`Package Data`:

package_data
~~~~~~~~~~~~

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

For more information, see `Including Data Files
<https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files>`_
from the `setuptools docs <https://setuptools.readthedocs.io>`_.


.. _`Data Files`:

data_files
~~~~~~~~~~

::

    data_files=[('my_data', ['data/data_file'])],

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
  },


Use this keyword to specify any plugins that your project provides for any named
entry points that may be defined by your project or others that you depend on.

For more information, see the section on `Dynamic Discovery of Services and
Plugins
<https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins>`_
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
  },

Use "console_script" `entry points
<https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins>`_
to register your script interfaces. You can then let the toolchain handle the
work of turning these interfaces into actual scripts [2]_.  The scripts will be
generated during the install of your :term:`distribution <Distribution
Package>`.

For more information, see `Automatic Script Creation
<https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation>`_
from the `setuptools docs <https://setuptools.readthedocs.io>`_.

.. _`Choosing a versioning scheme`:

Choosing a versioning scheme
----------------------------

Standards compliance for interoperability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Different Python projects may use different versioning schemes based on the needs of that
particular project, but all of them are required to comply with the flexible :pep:`public version
scheme <440#public-version-identifiers>` specified
in :pep:`440` in order to be supported in tools and libraries like ``pip``
and ``setuptools``.

Here are some examples of compliant version numbers::

  1.2.0.dev1  # Development release
  1.2.0a1     # Alpha Release
  1.2.0b1     # Beta Release
  1.2.0rc1    # Release Candidate
  1.2.0       # Final Release
  1.2.0.post1 # Post Release
  15.10       # Date based release
  23          # Serial release

To further accommodate historical variations in approaches to version numbering,
:pep:`440` also defines a comprehensive technique for :pep:`version
normalisation <440#normalization>` that maps
variant spellings of different version numbers to a standardised canonical form.

Scheme choices
~~~~~~~~~~~~~~

Semantic versioning (preferred)
*******************************

For new projects, the recommended versioning scheme is based on `Semantic Versioning
<http://semver.org>`_, but adopts a different approach to handling pre-releases and
build metadata.

The essence of semantic versioning is a 3-part MAJOR.MINOR.MAINTENANCE numbering scheme,
where the project author increments:

1. MAJOR version when they make incompatible API changes,
2. MINOR version when they add functionality in a backwards-compatible manner, and
3. MAINTENANCE version when they make backwards-compatible bug fixes.

Adopting this approach as a project author allows users to make use of :pep:`"compatible release"
<440#compatible-release>` specifiers, where
``name ~= X.Y`` requires at least release X.Y, but also allows any later release with
a matching MAJOR version.

Python projects adopting semantic versioning should abide by clauses 1-8 of the
`Semantic Versioning 2.0.0 specification <http://semver.org>`_.

Date based versioning
*********************

Semantic versioning is not a suitable choice for all projects, such as those with a regular
time based release cadence and a deprecation process that provides warnings for a number of
releases prior to removal of a feature.

A key advantage of date based versioning is that it is straightforward to tell how old the
base feature set of a particular release is given just the version number.

Version numbers for date based projects typically take the form of YEAR.MONTH (for example,
``12.04``, ``15.10``).

Serial versioning
*****************

This is the simplest possible versioning scheme, and consists of a single number which is
incremented every release.

While serial versioning is very easy to manage as a developer, it is the hardest to track
as an end user, as serial version numbers convey little or no information regarding API
backwards compatibility.

Hybrid schemes
**************

Combinations of the above schemes are possible. For example, a project may combine date
based versioning with serial versioning to create a YEAR.SERIAL numbering scheme that
readily conveys the approximate age of a release, but doesn't otherwise commit to a particular
release cadence within the year.

Pre-release versioning
~~~~~~~~~~~~~~~~~~~~~~

Regardless of the base versioning scheme, pre-releases for a given final release may be
published as:

* zero or more dev releases (denoted with a ".devN" suffix)
* zero or more alpha releases (denoted with a ".aN" suffix)
* zero or more beta releases (denoted with a ".bN" suffix)
* zero or more release candidates (denoted with a ".rcN" suffix)

``pip`` and other modern Python package installers ignore pre-releases by default when
deciding which versions of dependencies to install.


Local version identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~

Public version identifiers are designed to support distribution via
:term:`PyPI <Python Package Index (PyPI)>`. Python's software distribution tools also support
the notion of a :pep:`local version identifier
<440#local-version-identifiers>`, which can be used to
identify local development builds not intended for publication, or modified variants of a release
maintained by a redistributor.

A local version identifier takes the form ``<public version identifier>+<local version label>``.
For example::

   1.2.0.dev1+hg.5.b11e5e6f0b0b  # 5th VCS commmit since 1.2.0.dev1 release
   1.2.1+fedora.4                # Package with downstream Fedora patches applied


Working in "Development Mode"
=============================

Although not required, it's common to locally install your project in "editable"
or "develop" mode while you're working on it.  This allows your project to be
both installed and editable in project form.

Assuming you're in the root of your project directory, then run:

::

 pip install -e .


Although somewhat cryptic, ``-e`` is short for ``--editable``, and ``.`` refers
to the current working directory, so together, it means to install the current
directory (i.e. your project) in editable mode.  This will also install any
dependencies declared with "install_requires" and any scripts declared with
"console_scripts".  Dependencies will be installed in the usual, non-editable mode.

It's fairly common to also want to install some of your dependencies in editable
mode as well. For example, supposing your project requires "foo" and "bar", but
you want "bar" installed from vcs in editable mode, then you could construct a
requirements file like so::

  -e .
  -e git+https://somerepo/bar.git#egg=bar

The first line says to install your project and any dependencies. The second
line overrides the "bar" dependency, such that it's fulfilled from vcs, not
PyPI.

If, however, you want "bar" installed from a local directory in editable mode, the requirements file should look like this, with the local paths at the top of the file::

  -e /path/to/project/bar
  -e .

Otherwise, the dependency will be fulfilled from PyPI, due to the installation order of the requirements file.  For more on requirements files, see the :ref:`Requirements File
<pip:Requirements Files>` section in the pip docs.  For more on vcs installs,
see the :ref:`VCS Support <pip:VCS Support>` section of the pip docs.

Lastly, if you don't want to install any dependencies at all, you can run::

   pip install -e . --no-deps


For more information, see the `Development Mode
<https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode>`_ section
of the `setuptools docs <https://setuptools.readthedocs.io>`_.

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


Wheels
------

You should also create a wheel for your project. A wheel is a :term:`built
package <Built Distribution>` that can be installed without needing to go
through the "build" process. Installing wheels is substantially faster for the
end user than installing from a source distribution.

If your project is pure python (i.e. contains no compiled extensions) and
natively supports both Python 2 and 3, then you'll be creating what's called a
:ref:`"Universal Wheel" (see section below) <Universal Wheels>`.

If your project is pure python but does not natively support both Python 2 and
3, then you'll be creating a :ref:`"Pure Python Wheel" (see section below) <Pure
Python Wheels>`.

If you project contains compiled extensions, then you'll be creating what's
called a :ref:`"Platform Wheel" (see section below) <Platform Wheels>`.


.. _`Universal Wheels`:

Universal Wheels
~~~~~~~~~~~~~~~~

"Universal Wheels" are wheels that are pure python (i.e. contains no compiled
extensions) and support Python 2 and 3. This is a wheel that can be installed
anywhere by :ref:`pip`.

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

Beware that ``bdist_wheel`` does not currently have any checks to warn if you
use the setting inappropriately.

If your project has optional C extensions, it is recommended not to publish a
universal wheel, because pip will prefer the wheel over a source installation,
and prevent the possibility of building the extension.


.. _`Pure Python Wheels`:

Pure Python Wheels
~~~~~~~~~~~~~~~~~~

"Pure Python Wheels" that are not "universal" are wheels that are pure python
(i.e. contains no compiled extensions), but don't natively support both Python 2
and 3.

To build the wheel:

::

 python setup.py bdist_wheel


`bdist_wheel` will detect that the code is pure Python, and build a wheel that's
named such that it's usable on any Python installation with the same major
version (Python 2 or Python 3) as the version you used to build the wheel.  For
details on the naming of wheel files, see :pep:`425`

If your code supports both Python 2 and 3, but with different code (e.g., you
use `"2to3" <https://docs.python.org/2/library/2to3.html>`_) you can run
``setup.py bdist_wheel`` twice, once with Python 2 and once with Python 3. This
will produce wheels for each version.



.. _`Platform Wheels`:

Platform Wheels
~~~~~~~~~~~~~~~

"Platform Wheels" are wheels that are specific to a certain platform like linux,
OSX, or Windows, usually due to containing compiled extensions.

To build the wheel:

::

 python setup.py bdist_wheel


`bdist_wheel` will detect that the code is not pure Python, and build a wheel
that's named such that it's only usable on the platform that it was built
on. For details on the naming of wheel files, see :pep:`425`

.. note::

  :term:`PyPI <Python Package Index (PyPI)>` currently supports uploads of
  platform wheels for Windows, OS X, and the multi-distro ``manylinux1`` ABI.
  Details of the latter are defined in :pep:`513`.


.. _`Uploading your Project to PyPI`:

Uploading your Project to PyPI
==============================

.. note::

  Before releasing on main PyPI repo, you might prefer training with
  `PyPI test site <https://testpypi.python.org/pypi>`_
  which is cleaned on a semi regular basis. See
  `these instructions <https://wiki.python.org/moin/TestPyPI>`_ on how
  to setup your configuration in order to use it.

When you ran the command to create your distribution, a new directory dist/ was created under your project's root directory. That's where you'll find your distribution file(s) to upload.

Create an account
-----------------

First, you need a :term:`PyPI <Python Package Index (PyPI)>` user
account. There are two options:

1. Create an account manually `using the form on the PyPI website
   <https://pypi.python.org/pypi?%3Aaction=register_form>`_.

2. **(Not recommended):** Have an account created as part of
   registering your first project (not recommended due to the
   related security concerns, see option #3 below).

If you created your account using option #1 (the form), you'll need to manually
write a ``~/.pypirc`` file like so.

   ::

    [distutils]
    index-servers=pypi

    [pypi]
    repository = https://upload.pypi.org/legacy/
    username = <username>
    password = <password>

You can leave out the password line if you use twine with its
``-p PASSWORD`` argument or prefer to simply enter your password
when prompted.


Register your project
---------------------

Next, if this is the first release, you currently need to explicitly register your
project prior to uploading.

There are three ways to do this:

1. Use `the form on the PyPI website
   <https://pypi.python.org/pypi?%3Aaction=submit_form>`_, to upload your
   ``PKG-INFO`` info located in your local project tree at
   ``myproject.egg-info/PKG-INFO``.  If you don't have that file or directory,
   then run ``python setup.py egg_info`` to have it generated.
2. Run ``twine register dist/mypkg.whl``, and :ref:`twine` will register your project
   based on the package metadata in the specified files. Your ``~/.pypirc``
   must already be appropriately configured for twine to work.
3. **(Not recommended):** Run ``python setup.py register``.  If you don't have
   a user account already, a wizard will create one for you. This approach is
   covered here due to it being mentioned in other guides, but it is not
   recommended as it may use a plaintext HTTP or unverified HTTPS connection
   on some Python versions, allowing your username and password to be intercepted
   during transmission.


Upload your distributions
-------------------------

Finally, you can upload your distributions to :term:`PyPI <Python Package Index
(PyPI)>`.

There are two options:

1. Use :ref:`twine`

   ::

     twine upload dist/*

   The biggest reason to use twine is that ``python setup.py upload`` (option #2
   below) uploads files over plaintext. This means anytime you use it you expose
   your username and password to a MITM attack. Twine uses only verified TLS to
   upload to PyPI in order to protect your credentials from theft.

   Secondly it allows you to precreate your distribution files.  ``python
   setup.py upload`` only allows you to upload something that you've created in
   the same command invocation. This means that you cannot test the exact file
   you're going to upload to PyPI to ensure that it works before uploading it.

   Finally it allows you to pre-sign your files and pass the .asc files into the
   command line invocation (``twine upload twine-1.0.1.tar.gz
   twine-1.0.1.tar.gz.asc``). This enables you to be assured that you're typing
   your gpg passphrase into gpg itself and not anything else since *you* will be
   the one directly executing ``gpg --detach-sign -a <filename>``.


2. **(Not recommended):** Use :ref:`setuptools`:

   ::

    python setup.py bdist_wheel sdist upload

   This approach is covered here due to it being mentioned in other guides, but it
   is not recommended as it may use a plaintext HTTP or unverified HTTPS connection
   on some Python versions, allowing your username and password to be intercepted
   during transmission.

----

.. [1] Depending on your platform, this may require root or Administrator
       access. :ref:`pip` is currently considering changing this by `making user
       installs the default behavior
       <https://github.com/pypa/pip/issues/1668>`_.


.. [2] Specifically, the "console_script" approach generates ``.exe`` files on
       Windows, which are necessary because the OS special-cases ``.exe`` files.
       Script-execution features like ``PATHEXT`` and the :pep:`Python Launcher for
       Windows <397>` allow scripts to
       be used in many cases, but not all.
