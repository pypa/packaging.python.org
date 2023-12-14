.. _installing-packages:

===================
Installing Packages
===================

This section covers the basics of how to install Python :term:`packages
<Distribution Package>`.

It's important to note that the term "package" in this context is being used to
describe a bundle of software to be installed (i.e. as a synonym for a
:term:`distribution <Distribution Package>`). It does not refer to the kind
of :term:`package <Import Package>` that you import in your Python source code
(i.e. a container of modules). It is common in the Python community to refer to
a :term:`distribution <Distribution Package>` using the term "package".  Using
the term "distribution" is often not preferred, because it can easily be
confused with a Linux distribution, or another larger software distribution
like Python itself.


.. _installing_requirements:

Requirements for Installing Packages
====================================

This section describes the steps to follow before installing other Python
packages.


Ensure you can run Python from the command line
-----------------------------------------------

Before you go any further, make sure you have Python and that the expected
version is available from your command line. You can check this by running:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 --version

.. tab:: Windows

    .. code-block:: bat

        py --version


You should get some output like ``Python 3.6.3``. If you do not have Python,
please install the latest 3.x version from `python.org`_ or refer to the
:ref:`Installing Python <python-guide:installation>` section of the Hitchhiker's Guide to Python.

.. Note:: If you're a newcomer and you get an error like this:

    .. code-block:: pycon

        >>> python3 --version
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'python3' is not defined

    It's because this command and other suggested commands in this tutorial
    are intended to be run in a *shell* (also called a *terminal* or
    *console*). See the Python for Beginners `getting started tutorial`_ for
    an introduction to using your operating system's shell and interacting with
    Python.

.. Note:: If you're using an enhanced shell like IPython or the Jupyter
   notebook, you can run system commands like those in this tutorial by
   prefacing them with a ``!`` character:

   .. code-block:: text

        In [1]: import sys
                !{sys.executable} --version
        Python 3.6.3

   It's recommended to write ``{sys.executable}`` rather than plain ``python`` in
   order to ensure that commands are run in the Python installation matching
   the currently running notebook (which may not be the same Python
   installation that the ``python`` command refers to).

.. Note:: Due to the way most Linux distributions are handling the Python 3
   migration, Linux users using the system Python without creating a virtual
   environment first should replace the ``python`` command in this tutorial
   with ``python3`` and the ``python -m pip`` command with ``python3 -m pip --user``. Do *not*
   run any of the commands in this tutorial with ``sudo``: if you get a
   permissions error, come back to the section on creating virtual environments,
   set one up, and then continue with the tutorial as written.

.. _getting started tutorial: https://opentechschool.github.io/python-beginners/en/getting_started.html#what-is-python-exactly
.. _python.org: https://www.python.org

Ensure you can run pip from the command line
--------------------------------------------

Additionally, you'll need to make sure you have :ref:`pip` available. You can
check this by running:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip --version

.. tab:: Windows

    .. code-block:: bat

        py -m pip --version

If you installed Python from source, with an installer from `python.org`_, or
via `Homebrew`_ you should already have pip. If you're on Linux and installed
using your OS package manager, you may have to install pip separately, see
:doc:`/guides/installing-using-linux-tools`.

.. _Homebrew: https://brew.sh

If ``pip`` isn't already installed, then first try to bootstrap it from the
standard library:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m ensurepip --default-pip

.. tab:: Windows

    .. code-block:: bat

        py -m ensurepip --default-pip

If that still doesn't allow you to run ``python -m pip``:

* Securely Download `get-pip.py
  <https://bootstrap.pypa.io/get-pip.py>`_ [1]_

* Run ``python get-pip.py``. [2]_  This will install or upgrade pip.
  Additionally, it will install :ref:`setuptools` and :ref:`wheel` if they're
  not installed already.

  .. warning::

     Be cautious if you're using a Python install that's managed by your
     operating system or another package manager. get-pip.py does not
     coordinate with those tools, and may leave your system in an
     inconsistent state. You can use ``python get-pip.py --prefix=/usr/local/``
     to install in ``/usr/local`` which is designed for locally-installed
     software.


Ensure pip, setuptools, and wheel are up to date
------------------------------------------------

While ``pip`` alone is sufficient to install from pre-built binary archives,
up to date copies of the ``setuptools`` and ``wheel`` projects are useful
to ensure you can also install from source archives:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --upgrade pip setuptools wheel

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --upgrade pip setuptools wheel

Optionally, create a virtual environment
----------------------------------------

See :ref:`section below <Creating and using Virtual Environments>` for details,
but here's the basic :doc:`venv <python:library/venv>` [3]_ command to use on a typical Linux system:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m venv tutorial_env
        source tutorial_env/bin/activate

.. tab:: Windows

    .. code-block:: bat

        py -m venv tutorial_env
        tutorial_env\Scripts\activate

This will create a new virtual environment in the ``tutorial_env`` subdirectory,
and configure the current shell to use it as the default ``python`` environment.


.. _Creating and using Virtual Environments:

Creating Virtual Environments
=============================

Python "Virtual Environments" allow Python :term:`packages <Distribution
Package>` to be installed in an isolated location for a particular application,
rather than being installed globally. If you are looking to safely install
global command line tools,
see :doc:`/guides/installing-stand-alone-command-line-tools`.

Imagine you have an application that needs version 1 of LibFoo, but another
application requires version 2. How can you use both these applications? If you
install everything into /usr/lib/python3.6/site-packages (or whatever your
platform’s standard location is), it’s easy to end up in a situation where you
unintentionally upgrade an application that shouldn’t be upgraded.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you can’t install :term:`packages <Distribution Package>` into the
global site-packages directory? For instance, on a shared host.

In all these cases, virtual environments can help you. They have their own
installation directories and they don’t share libraries with other virtual
environments.

Currently, there are two common tools for creating Python virtual environments:

* :doc:`venv <python:library/venv>` is available by default in Python 3.3 and later, and installs
  :ref:`pip` and :ref:`setuptools` into created virtual environments in
  Python 3.4 and later.
* :ref:`virtualenv` needs to be installed separately, but supports Python 2.7+
  and Python 3.3+, and :ref:`pip`, :ref:`setuptools` and :ref:`wheel` are
  always installed into created virtual environments by default (regardless of
  Python version).

The basic usage is like so:

Using :doc:`venv <python:library/venv>`:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m venv <DIR>
        source <DIR>/bin/activate

.. tab:: Windows

    .. code-block:: bat

        py -m venv <DIR>
        <DIR>\Scripts\activate

Using :ref:`virtualenv`:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m virtualenv <DIR>
        source <DIR>/bin/activate

.. tab:: Windows

    .. code-block:: bat

        virtualenv <DIR>
        <DIR>\Scripts\activate

For more information, see the :doc:`venv <python:library/venv>` docs or
the :doc:`virtualenv <virtualenv:index>` docs.

The use of :command:`source` under Unix shells ensures
that the virtual environment's variables are set within the current
shell, and not in a subprocess (which then disappears, having no
useful effect).

In both of the above cases, Windows users should *not* use the
:command:`source` command, but should rather run the :command:`activate`
script directly from the command shell like so:

.. code-block:: bat

   <DIR>\Scripts\activate



Managing multiple virtual environments directly can become tedious, so the
:ref:`dependency management tutorial <managing-dependencies>` introduces a
higher level tool, :ref:`Pipenv`, that automatically manages a separate
virtual environment for each project and application that you work on.


Use pip for Installing
======================

:ref:`pip` is the recommended installer.  Below, we'll cover the most common
usage scenarios. For more detail, see the :doc:`pip docs <pip:index>`,
which includes a complete :doc:`Reference Guide <pip:cli/index>`.


Installing from PyPI
====================

The most common usage of :ref:`pip` is to install from the :term:`Python Package
Index <Python Package Index (PyPI)>` using a :term:`requirement specifier
<Requirement Specifier>`. Generally speaking, a requirement specifier is
composed of a project name followed by an optional :term:`version specifier
<Version Specifier>`.  A full description of the supported specifiers can be
found in the :ref:`Version specifier specification <version-specifiers>`.
Below are some examples.

To install the latest version of "SomeProject":

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install "SomeProject"

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomeProject"

To install a specific version:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install "SomeProject==1.4"

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomeProject==1.4"

To install greater than or equal to one version and less than another:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install "SomeProject>=1,<2"

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomeProject>=1,<2"


To install a version that's :ref:`compatible <version-specifiers-compatible-release>`
with a certain version: [4]_

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install "SomeProject~=1.4.2"

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomeProject~=1.4.2"

In this case, this means to install any version "==1.4.*" version that's also
">=1.4.2".


Source Distributions vs Wheels
==============================

:ref:`pip` can install from either :term:`Source Distributions (sdist) <Source
Distribution (or "sdist")>` or :term:`Wheels <Wheel>`, but if both are present
on PyPI, pip will prefer a compatible :term:`wheel <Wheel>`. You can override
pip`s default behavior by e.g. using its :ref:`--no-binary
<pip:install_--no-binary>` option.

:term:`Wheels <Wheel>` are a pre-built :term:`distribution <Distribution
Package>` format that provides faster installation compared to :term:`Source
Distributions (sdist) <Source Distribution (or "sdist")>`, especially when a
project contains compiled extensions.

If :ref:`pip` does not find a wheel to install, it will locally build a wheel
and cache it for future installs, instead of rebuilding the source distribution
in the future.


Upgrading packages
==================

Upgrade an already installed ``SomeProject`` to the latest from PyPI.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --upgrade SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --upgrade SomeProject

.. _`Installing to the User Site`:

Installing to the User Site
===========================

To install :term:`packages <Distribution Package>` that are isolated to the
current user, use the ``--user`` flag:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --user SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --user SomeProject

For more information see the `User Installs
<https://pip.pypa.io/en/latest/user_guide/#user-installs>`_ section
from the pip docs.

Note that the ``--user`` flag has no effect when inside a virtual environment
- all installation commands will affect the virtual environment.

If ``SomeProject`` defines any command-line scripts or console entry points,
``--user`` will cause them to be installed inside the `user base`_'s binary
directory, which may or may not already be present in your shell's
:envvar:`PATH`.  (Starting in version 10, pip displays a warning when
installing any scripts to a directory outside :envvar:`PATH`.)  If the scripts
are not available in your shell after installation, you'll need to add the
directory to your :envvar:`PATH`:

- On Linux and macOS you can find the user base binary directory by running
  ``python -m site --user-base`` and adding ``bin`` to the end. For example,
  this will typically print ``~/.local`` (with ``~`` expanded to the absolute
  path to your home directory) so you'll need to add ``~/.local/bin`` to your
  ``PATH``.  You can set your ``PATH`` permanently by `modifying ~/.profile`_.

- On Windows you can find the user base binary directory by running ``py -m
  site --user-site`` and replacing ``site-packages`` with ``Scripts``. For
  example, this could return
  ``C:\Users\Username\AppData\Roaming\Python36\site-packages`` so you would
  need to set your ``PATH`` to include
  ``C:\Users\Username\AppData\Roaming\Python36\Scripts``. You can set your user
  ``PATH`` permanently in the `Control Panel`_. You may need to log out for the
  ``PATH`` changes to take effect.

.. _user base: https://docs.python.org/3/library/site.html#site.USER_BASE
.. _modifying ~/.profile: https://stackoverflow.com/a/14638025
.. _Control Panel: https://docs.microsoft.com/en-us/windows/win32/shell/user-environment-variables?redirectedfrom=MSDN

Requirements files
==================

Install a list of requirements specified in a :ref:`Requirements File
<pip:Requirements Files>`.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install -r requirements.txt

.. tab:: Windows

    .. code-block:: bat

        py -m pip install -r requirements.txt

Installing from VCS
===================

Install a project from VCS in "editable" mode.  For a full breakdown of the
syntax, see pip's section on :ref:`VCS Support <pip:VCS Support>`.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git
        python3 -m pip install -e SomeProject @ hg+https://hg.repo/some_pkg                # from mercurial
        python3 -m pip install -e SomeProject @ svn+svn://svn.repo/some_pkg/trunk/         # from svn
        python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  # from a branch

.. tab:: Windows

    .. code-block:: bat

        py -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git
        py -m pip install -e SomeProject @ hg+https://hg.repo/some_pkg                # from mercurial
        py -m pip install -e SomeProject @ svn+svn://svn.repo/some_pkg/trunk/         # from svn
        py -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  # from a branch

Installing from other Indexes
=============================

Install from an alternate index

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --index-url http://my.package.repo/simple/ SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --index-url http://my.package.repo/simple/ SomeProject

Search an additional index during install, in addition to :term:`PyPI <Python
Package Index (PyPI)>`

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --extra-index-url http://my.package.repo/simple SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --extra-index-url http://my.package.repo/simple SomeProject

Installing from a local src tree
================================


Installing from local src in
:doc:`Development Mode <setuptools:userguide/development_mode>`,
i.e. in such a way that the project appears to be installed, but yet is
still editable from the src tree.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install -e <path>

.. tab:: Windows

    .. code-block:: bat

        py -m pip install -e <path>

You can also install normally from src

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install <path>

.. tab:: Windows

    .. code-block:: bat

        py -m pip install <path>

Installing from local archives
==============================

Install a particular source archive file.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install ./downloads/SomeProject-1.0.4.tar.gz

.. tab:: Windows

    .. code-block:: bat

        py -m pip install ./downloads/SomeProject-1.0.4.tar.gz

Install from a local directory containing archives (and don't check :term:`PyPI
<Python Package Index (PyPI)>`)

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --no-index --find-links=file:///local/dir/ SomeProject
        python3 -m pip install --no-index --find-links=/local/dir/ SomeProject
        python3 -m pip install --no-index --find-links=relative/dir/ SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --no-index --find-links=file:///local/dir/ SomeProject
        py -m pip install --no-index --find-links=/local/dir/ SomeProject
        py -m pip install --no-index --find-links=relative/dir/ SomeProject

Installing from other sources
=============================

To install from other data sources (for example Amazon S3 storage)
you can create a helper application that presents the data
in a format compliant with the :ref:`simple repository API <simple-repository-api>`:,
and use the ``--extra-index-url`` flag to direct pip to use that index.

.. code-block:: bash

   ./s3helper --port=7777
   python -m pip install --extra-index-url http://localhost:7777 SomeProject


Installing Prereleases
======================

Find pre-release and development versions, in addition to stable versions.  By
default, pip only finds stable versions.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --pre SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --pre SomeProject

Installing "Extras"
===================

Extras are optional "variants" of a package, which may include
additional dependencies, and thereby enable additional functionality
from the package.  If you wish to install an extra for a package which
you know publishes one, you can include it in the pip installation command:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install 'SomePackage[PDF]'
        python3 -m pip install 'SomePackage[PDF]==3.0'
        python3 -m pip install -e '.[PDF]'  # editable project in current directory

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomePackage[PDF]"
        py -m pip install "SomePackage[PDF]==3.0"
        py -m pip install -e ".[PDF]"  # editable project in current directory

----

.. [1] "Secure" in this context means using a modern browser or a
       tool like :command:`curl` that verifies SSL certificates when
       downloading from https URLs.

.. [2] Depending on your platform, this may require root or Administrator
       access. :ref:`pip` is currently considering changing this by `making user
       installs the default behavior
       <https://github.com/pypa/pip/issues/1668>`_.

.. [3] Beginning with Python 3.4, ``venv`` (a stdlib alternative to
       :ref:`virtualenv`) will create virtualenv environments with ``pip``
       pre-installed, thereby making it an equal alternative to
       :ref:`virtualenv`.

.. [4] The compatible release specifier was accepted in :pep:`440`
       and support was released in :ref:`setuptools` v8.0 and
       :ref:`pip` v6.0
