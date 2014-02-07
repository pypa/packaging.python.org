===================================
Installation & Packaging Quickstart
===================================

:Page Status: Incomplete
:Last Reviewed: 2014-01-22


Install the Tools
=================

1. Securely Download `get-pip.py
   <https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_ [1]_
2. Run ``python get-pip.py`` (this will install pip and setuptools) [2]_ [3]_
3. Run ``pip install virtualenv``


Create and use a Virtual Environment
============================

::

 virtualenv myVE
 source myVE/bin/activate

Or, if you want to install packages globally, don't do this.


Install some Python packages
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


For more on installation, see `the pip docs <http://www.pip-installer.org/en/latest/>`_.


Cache and Install from Wheels
=============================

:term:`Wheel` is a new pre-built alternative to :term:`sdist <Source
Distribution (or "sdist")>` that provides faster installation, especially when a
project contains extensions.

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


.. warning::

   Currently, when ``pip wheel`` finds a wheel for one of your requirements
   already on PyPI, it does not rebuild, and it does not place the file in your
   wheelhouse directory.  This is fixed in the develop branch of pip, but is
   not due to be released until v1.6



Create your own Project
=======================

See the `PyPA sample project <https://github.com/pypa/sampleproject>`_.

You can can copy and edit from that to get your project going.

To install your project in "develop" or "editable" mode (i.e. to have your
project installed, but still editable for development)

::

 cd myproject
 python setup.py develop    # the setuptools way
 pip install -e .           # the pip way

For more information on creating projects, see:

 * `Setuptools Developer Guide
   <http://pythonhosted.org/setuptools/setuptools.html#developer-s-guide>`_
 * `Open Sourcing a Python Project the Right Way
   <http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/>`_


Build & Upload your Project to PyPI
===================================

Build a source distribution

::

 python setup.py sdist


Build a wheel (for advice on when, see :ref:`pip:Should you upload wheels to PyPI`)

::

 pip install wheel
 python setup.py bdist_wheel


Upload your distributions with `twine <https://pypi.python.org/pypi/twine>`_

::

 pip install twine
 twine upload dist/*


----

.. [1] "Secure" in this context means using a modern browser or a
       tool like `curl` that verifies SSL certificates when downloading from
       https URLs.

.. [2] Depending on your platform, this may require root or Administrator access.

.. [3] On Linux and OSX, these tools will usually be available for the system
       python from a system package manager (e.g. `yum` or `apt-get` for linux,
       or `homebrew` for OSX). Unfortunately, there is often delay in getting
       the latest version this way, so in most cases, you'll want to use the
       instructions.
