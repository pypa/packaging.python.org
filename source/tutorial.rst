=================================
Installation & Packaging Tutorial
=================================

:Page Status: Incomplete
:Last Reviewed: 2014-01-22


Installing the Tools
====================

For Installation or Packaging, you'll minimally want :ref:`pip` and
:ref:`setuptools`, and in most cases, :ref:`virtualenv` [5]_.  Additionally, for
building wheels, you'll need :ref:`wheel`, and for uploading to :term:`PyPI
<Python Package Index (PyPI)>`, you'll need :ref:`twine`.

We recommend the following sequence for installation:

1. Securely Download `get-pip.py
   <https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_ [1]_

2. Run ``python get-pip.py``.  This will install or upgrade pip.  Additionally,
   it will install setuptools if it's not installed already. To upgrade an
   existing setuptools, run ``pip install -U setuptools`` [2]_ [3]_

3. Run ``pip install virtualenv`` [2]_ [5]_

4. Optionally, Create a virtual environment (See :ref:`section below <Creating
   and using Virtual Environments>` for details):

   ::

    virtualenv <DIR>
    source <DIR>/bin/activate

5. For building wheels: ``pip install wheel`` [2]_

6. For uploading distributions: ``pip install twine`` [2]_


.. _`Creating and using Virtual Environments`:

Creating and using Virtual Environments
=======================================

:ref:`virtualenv` is a tool to create isolated Python environments. [5]_

The basic problem being addressed is one of dependencies and versions, and
indirectly permissions. Imagine you have an application that needs version 1 of
LibFoo, but another application requires version 2. How can you use both these
applications? If you install everything into /usr/lib/python2.7/site-packages
(or whatever your platform’s standard location is), it’s easy to end up in a
situation where you unintentionally upgrade an application that shouldn’t be
upgraded.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you can’t install packages into the global site-packages
directory? For instance, on a shared host.

In all these cases, virtualenv can help you. It creates an environment that has
its own installation directories, that doesn’t share libraries with other
virtualenv environments (and optionally doesn’t access the globally installed
libraries either).

For more information, see the `virtualenv docs <http://www.virtualenv.org>`_.

Note that in some cases, the `user installation scheme
<http://docs.python.org/install/index.html#alternate-installation-the-user-scheme>`_
can offer similar benefits as Virtual Environments. For more information see the
`User Installs
<https://pip.readthedocs.org/en/latest/user_guide.html#user-installs>`_ section
from the pip docs.


Installing Python packages
==========================

Install `SomePackage` and it's dependencies from :term:`PyPI <Python Package
Index (PyPI)>` using :ref:`pip:Requirement Specifiers`

::

 pip install SomePackage           # latest version
 pip install SomePackage==1.0.4    # specific version
 pip install 'SomePackage>=1.0.4'  # minimum version


Install a list of requirements specified in a :ref:`Requirements File
<pip:Requirements Files>`.

::

 pip install -r requirements.txt


Upgrade an already installed `SomePackage` to the latest from PyPI.

::

 pip install --upgrade SomePackage


Install a project from VCS in "editable" mode.  For a full breakdown of the
syntax, see pip's section on :ref:`VCS Support <pip:VCS Support>`.

::

 pip install -e git+https://git.repo/some_pkg.git#egg=SomePackage          # from git
 pip install -e hg+https://hg.repo/some_pkg.git#egg=SomePackage            # from mercurial
 pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomePackage         # from svn
 pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomePackage  # from a branch


Install a particular source archive file.

::

 pip install ./downloads/SomePackage-1.0.4.tar.gz
 pip install http://my.package.repo/SomePackage-1.0.4.zip


Install from an alternate index

::

 pip install --index-url http://my.package.repo/simple/ SomePackage


Search an additional index during install, in addition to :term:`PyPI <Python
Package Index (PyPI)>`

::

 pip install --extra-index-url http://my.package.repo/simple SomePackage


Install from a local directory containing archives (and don't check :term:`PyPI
<Python Package Index (PyPI)>`)

::

 pip install --no-index --find-links=file:///local/dir/ SomePackage
 pip install --no-index --find-links=/local/dir/ SomePackage
 pip install --no-index --find-links=relative/dir/ SomePackage


Find pre-release and development versions, in addition to stable versions.  By
default, pip only finds stable versions.

::

 pip install --pre SomePackage


For more on installation, see `the pip docs <http://www.pip-installer.org/en/latest/>`_.


Installing Wheels
=================

:term:`Wheel` is a new pre-built alternative to :term:`sdist <Source
Distribution (or "sdist")>` that provides faster installation, especially when a
project contains extensions.

As of v1.5, :ref:`pip` prefers :term:`wheels <Wheel>` over :term:`sdists <Source
Distribution (or "sdist")>` when searching indexes.

Although wheels are `becoming more common <http://pythonwheels.com>`_ on
:term:`PyPI <Python Package Index (PyPI)>`, if you want all of your dependencies
converted to wheel, do the following (assuming you're using a :ref:`Requirements
File <pip:Requirements Files>`):

::

 pip install wheel
 pip wheel --wheel-dir=/local/wheels -r requirements.txt

And then to install those requirements just using your local directory of wheels
(and not from PyPI):

::

 pip install --no-index --find-links=/local/wheels -r requirements.txt



Creating your own Project
=========================

See the `PyPA sample project <https://github.com/pypa/sampleproject>`_. You can
use that as an example to get started.

Let's cover the critical features below: [4]_


Project Structure
-----------------

Project Name
------------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

  name = 'sample'

This will determine how your project is listed on :term:`PyPI <Python Package
Index (PyPI)>`. It's recommended to only use letters, decimal digits, ``-``, ``.``, and ``_``.


Project Version
---------------

from `sampleproject/sample/__init__.py
<https://github.com/pypa/sampleproject/blob/master/sample/__init__.py>`_

::

  __version__ = '1.2.0'

Projects should aim to comply with the `scheme
<http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
specified in :ref:`PEP440 <PEP440s>`.

Some Examples:

::

  1.2.0.dev1  # Development release
  1.2.0a1     # Alpha Release
  1.2.0b1     # Beta Release
  1.2.0       # Final Release
  1.2.0.post1 # Post Release


Dependencies
------------

from `sampleproject/setup.py
<https://github.com/pypa/sampleproject/blob/master/setup.py>`_

::

 install_requires = ['SomeDependency']


Data Files
----------

Scripts
-------

Universal Wheels
----------------

from `sampleproject/setup.cfg
<https://github.com/pypa/sampleproject/blob/master/setup.cfg>`_

::

 [wheel]
 universal=1

The benefit of this setting, is that ``python setup.py bdist_wheel`` will then
generate a wheel that will be installable anywhere (i.e. be "Universal"),
similar to an :term:`sdist <Source Distribution (or "sdist")>`.

Only use this setting, if:

1. You're project runs on Python 2 and 3 with no changes (i.e. it does not
   require 2to3).
2. You're project does not have any C extensions.

Beware that ``bdist_wheel`` does not currently have any checks to warn you if
use the setting inappropriately.


Installing your project in Editable mode
========================================

To install your project in "develop" or "editable" mode (i.e. to have your
project installed, but still editable for development)

::

 cd myproject
 python setup.py develop    # the setuptools way
 pip install -e .           # the pip way



Building & Uploading your Project to PyPI
=========================================

Build a source distribution

::

 python setup.py sdist


Build a wheel

::

 python setup.py bdist_wheel


Upload your distributions with :ref:`twine`

::

 twine upload dist/*


----

.. [1] "Secure" in this context means using a modern browser or a
       tool like `curl` that verifies SSL certificates when downloading from
       https URLs.

.. [2] Depending on your platform, this may require root or Administrator access.

.. [3] On Linux and OSX, pip and setuptools will usually be available for the system
       python from a system package manager (e.g. `yum` or `apt-get` for linux,
       or `homebrew` for OSX). Unfortunately, there is often delay in getting
       the latest version this way, so in most cases, you'll want to use the
       instructions.

.. [4] For more information on creating projects, see the `Setuptools Docs
       <http://pythonhosted.org/setuptools/setuptools.html>`_

.. [5] Beginning with Python 3.4, ``pyvenv`` (a stdlib alternative to
       :ref:`virtualenv`) will create virtualenv environments with ``pip``
       pre-installed, thereby making it an equal alternative to
       :ref:`virtualenv`.
