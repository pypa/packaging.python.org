Installing packages using pip and virtual environments
======================================================

This guide discusses how to install packages using :ref:`pip` and
a virtual environment manager: either :ref:`venv` for Python 3 or :ref:`virtualenv`
for Python 2. These are the lowest-level tools for managing Python
packages and are recommended if higher-level tools do not suit your needs.

.. note:: This doc uses the term **package** to refer to a
    :term:`Distribution Package`  which is different from an :term:`Import
    Package` that which is used to import modules in your Python source code.


Installing pip
--------------

:ref:`pip` is the reference Python package manager. It's used to install and
update packages. You'll need to make sure you have the latest version of pip
installed.


Windows
+++++++

The Python installers for Windows include pip. You should be able to access
pip using:

.. code-block:: bash

    py -m pip --version
    pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)

You can make sure that pip is up-to-date by running:

.. code-block:: bash

    py -m pip install --upgrade pip


Linux and macOS
++++++++++++++++

Debian and most other distributions include a `python-pip`_ package, if you
want to use the Linux distribution-provided versions of pip see
:doc:`/guides/installing-using-linux-tools`.

You can also install pip yourself to ensure you have the latest version. It's
recommended to use the system pip to bootstrap a user installation of pip:

.. code-block:: bash

    python3 -m pip install --user --upgrade pip

Afterwards, you should have the newest pip installed in your user site:

.. code-block:: bash

    python3 -m pip --version
    pip 9.0.1 from $HOME/.local/lib/python3.6/site-packages (python 3.6)

.. _python-pip: https://packages.debian.org/stable/python-pip


Installing virtualenv
---------------------

.. Note:: If you are using Python 3.3 or newer, the :mod:`venv` module is
    the preferred way to create and manage virtual environments.
    venv is included in the Python standard library and requires no additional installation.
    If you are using venv, you may skip this section.


:ref:`virtualenv` is used to manage Python packages for different projects.
Using virtualenv allows you to avoid installing Python packages globally
which could break system tools or other projects. You can install virtualenv
using pip.

On macOS and Linux:

.. code-block:: bash

    python3 -m pip install --user virtualenv

On Windows:

.. code-block:: bash

    py -m pip install --user virtualenv



Creating a virtual environment
------------------------------

:ref:`venv` (for Python 3) and :ref:`virtualenv` (for Python 2) allow
you to manage separate package installations for
different projects. They essentially allow you to create a "virtual" isolated
Python installation and install packages into that virtual installation. When
you switch projects, you can simply create a new virtual environment and not
have to worry about breaking the packages installed in the other environments.
It is always recommended to use a virtual environment while developing Python
applications.

To create a virtual environment, go to your project's directory and run
venv. If you are using Python 2, replace ``venv`` with ``virtualenv``
in the below commands.

On macOS and Linux:

.. code-block:: bash

    python3 -m venv env

On Windows:

.. code-block:: bash

    py -m venv env

The second argument is the location to create the virtual environment. Generally, you
can just create this in your project and call it ``env``.

venv will create a virtual Python installation in the ``env`` folder.

.. Note:: You should exclude your virtual environment directory from your version
    control system using ``.gitignore`` or similar.


Activating a virtual environment
--------------------------------

Before you can start installing or using packages in your virtual environment you'll
need to *activate* it. Activating a virtual environment will put the
virtual environment-specific
``python`` and ``pip`` executables into your shell's ``PATH``.

On macOS and Linux:

.. code-block:: bash

    source env/bin/activate

On Windows::

    .\env\Scripts\activate

You can confirm you're in the virtual environment by checking the location of your
Python interpreter, it should point to the ``env`` directory.

On macOS and Linux:

.. code-block:: bash

    which python
    .../env/bin/python

On Windows:

.. code-block:: bash

    where python
    .../env/bin/python.exe


As long as your virtual environment is activated pip will install packages into that
specific environment and you'll be able to import and use packages in your
Python application.


Leaving the virtual environment
-------------------------------

If you want to switch projects or otherwise leave your virtual environment, simply run:

.. code-block:: bash

    deactivate

If you want to re-enter the virtual environment just follow the same instructions above
about activating a virtual environment. There's no need to re-create the virtual environment.


Installing packages
-------------------

Now that you're in your virtual environment you can install packages. Let's install the
`Requests`_ library from the :term:`Python Package Index (PyPI)`:

.. code-block:: bash

    pip install requests

pip should download requests and all of its dependencies and install them:

.. code-block:: text

    Collecting requests
      Using cached requests-2.18.4-py2.py3-none-any.whl
    Collecting chardet<3.1.0,>=3.0.2 (from requests)
      Using cached chardet-3.0.4-py2.py3-none-any.whl
    Collecting urllib3<1.23,>=1.21.1 (from requests)
      Using cached urllib3-1.22-py2.py3-none-any.whl
    Collecting certifi>=2017.4.17 (from requests)
      Using cached certifi-2017.7.27.1-py2.py3-none-any.whl
    Collecting idna<2.7,>=2.5 (from requests)
      Using cached idna-2.6-py2.py3-none-any.whl
    Installing collected packages: chardet, urllib3, certifi, idna, requests
    Successfully installed certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

.. _Requests: https://pypi.org/project/requests/


Installing specific versions
-----------------------------

pip allows you to specify which version of a package to install using
:term:`version specifiers <Version Specifier>`. For example, to install
a specific version of ``requests``:

.. code-block:: bash

    pip install requests==2.18.4

To install the latest ``2.x`` release of requests:

.. code-block:: bash

    pip install requests>=2.0.0,<3.0.0

To install pre-release versions of packages, use the ``--pre`` flag:

.. code-block:: bash

    pip install --pre requests


Installing extras
-----------------

Some packages have optional `extras`_. You can tell pip to install these by
specifying the extra in brackets:

.. code-block:: bash

    pip install requests[security]

.. _extras:
    https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies


Installing from source
----------------------

pip can install a package directly from source, for example:

.. code-block:: bash

    cd google-auth
    pip install .

Additionally, pip can install packages from source in `development mode`_,
meaning that changes to the source directory will immediately affect the
installed package without needing to re-install:

.. code-block:: bash

    pip install --editable .


.. _development mode:
    https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode


Installing from version control systems
---------------------------------------

pip can install packages directly from their version control system. For
example, you can install directly from a git repository:

.. code-block:: bash

    git+https://github.com/GoogleCloudPlatform/google-auth-library-python.git#egg=google-auth

For more information on supported version control systems and syntax, see pip's
documentation on :ref:`VCS Support <pip:VCS Support>`.


Installing from local archives
------------------------------

If you have a local copy of a :term:`Distribution Package`'s archive (a zip,
wheel, or tar file) you can install it directly with pip:

.. code-block:: bash

    pip install requests-2.18.4.tar.gz

If you have a directory containing archives of multiple packages, you can tell
pip to look for packages there and not to use the
:term:`Python Package Index (PyPI)` at all:

.. code-block:: bash

    pip install --no-index --find-links=/local/dir/ requests

This is useful if you are installing packages on a system with limited
connectivity or if you want to strictly control the origin of distribution
packages.


Using other package indexes
---------------------------

If you want to download packages from a different index than the
:term:`Python Package Index (PyPI)`, you can use the ``--index-url`` flag:

.. code-block:: bash

    pip install --index-url http://index.example.com/simple/ SomeProject

If you want to allow packages from both the :term:`Python Package Index (PyPI)`
and a separate index, you can use the ``--extra-index-url`` flag instead:


.. code-block:: bash

    pip install --extra-index-url http://index.example.com/simple/ SomeProject


Upgrading packages
------------------

pip can upgrade packages in-place using the ``--upgrade`` flag. For example, to
install the latest version of ``requests`` and all of its dependencies:

.. code-block:: bash

    pip install --upgrade requests


Using requirements files
------------------------

Instead of installing packages individually, pip allows you to declare all
dependencies in a :ref:`Requirements File <pip:Requirements Files>`. For
example you could create a :file:`requirements.txt` file containing:

.. code-block:: text

    requests==2.18.4
    google-auth==1.1.0

And tell pip to install all of the packages in this file using the ``-r`` flag:

.. code-block:: bash

    pip install -r requirements.txt


Freezing dependencies
---------------------

Pip can export a list of all installed packages and their versions using the
``freeze`` command:

.. code-block:: bash

    pip freeze

Which will output a list of package specifiers such as:

.. code-block:: text

    cachetools==2.0.1
    certifi==2017.7.27.1
    chardet==3.0.4
    google-auth==1.1.1
    idna==2.6
    pyasn1==0.3.6
    pyasn1-modules==0.1.4
    requests==2.18.4
    rsa==3.4.2
    six==1.11.0
    urllib3==1.22

This is useful for creating :ref:`pip:Requirements Files` that can re-create
the exact versions of all packages installed in an environment.
