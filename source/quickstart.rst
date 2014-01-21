==========
Quickstart
==========

:Page Status: Complete
:Last Reviewed: 2014-01-20

No explanations or justifications here, just the snippets to get going.

Install the Tools
=================

1. Download `ez_setup.py
   <https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py>`_ for
   installing :ref:`setuptools`.
2. Run ``python ez_setup.py``
3. Download `get-pip.py
   <https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_ for installing
   :ref:`pip`.
4. Run ``python get-pip.py``
5. Run ``pip install virtualenv``


For more explanation, see :doc:`setup`.


Create a Virtual Environment
============================

::

 virtualenv myVE
 source myVE/bin/activate

Or, if you want to install packages globally, don't do this.

For more information on virtualenv environments and global installs, see :doc:`installation`.


Install Python Packages
=======================

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


Find pre-release and development versions, in addition to stable versions.  By default, pip only finds stable versions.

::

 pip install --pre SomePackage



For more on installation and pip, see :doc:`installation`.


Create your own Project
=======================

See the `PyPA sample project <https://github.com/pypa/sampleproject>`__.

You can can copy and edit from that to get your project going.

To install your project in "develop" or "editable" mode (i.e. to have your
project installed, but still editable for development)

::

 cd myproject
 python setup.py develop    # the setuptools way
 pip install -e .           # the pip way

For more on creating projects, see :doc:`packaging`.


Build & Upload your Project to PyPI
===================================

Build a source distribution

::

 python setup.py sdist


Build a wheel (for details on when and why, see :ref:`Getting started with wheel`)

::

 pip install wheel
 python setup.py bdist_wheel


Upload your distributions with :ref:`twine <Getting started with twine>`

::

 pip install twince
 twine upload dist/*
