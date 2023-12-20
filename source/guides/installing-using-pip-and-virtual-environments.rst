Install packages in a virtual environment using pip and venv
============================================================

This guide discusses how to create and activate a virtual environment using
the standard library's virtual environment tool :ref:`venv` and install packages.
The guide covers how to:

* Create and activate a virtual environment
* Prepare pip
* Install packages into a virtual environment using the ``pip`` command
* Use and create a requirements file


.. note:: This guide applies to supported versions of Python, currently 3.8
    and higher.


.. note:: This guide uses the term **package** to refer to a
    :term:`Distribution Package`, which commonly is installed from an external
    host. This differs from the term :term:`Import Package` which refers to
    import modules in your Python source code.


.. important::
    This guide has the prerequisite that you are using an official Python version obtained from
    <https://www.python.org/downloads/>. If you are using your operating
    system's package manager to install Python, please ensure that Python is
    installed before proceeding with these steps.


Create and Use Virtual Environments
-----------------------------------

Create a new virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`venv` (for Python 3) allows you to manage separate package installations for
different projects. It creates a "virtual" isolated Python installation. When
you switch projects, you can create a new virtual environment which is isolated
from other virtual environments. You benefit from the virtual environment
since packages can be installed confidently and will not interfere with
another project's environment.

.. tip::
   It is recommended to use a virtual environment when working with third
   party packages.

To create a virtual environment, go to your project's directory and run the
following command. This will create a new virtual environment in a local folder
named ``.venv``:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m venv .venv

.. tab:: Windows

    .. code-block:: bat

        py -m venv .venv

The second argument is the location to create the virtual environment. Generally, you
can just create this in your project and call it ``.venv``.

``venv`` will create a virtual Python installation in the ``.venv`` folder.

.. Note:: You should exclude your virtual environment directory from your version
    control system using ``.gitignore`` or similar.


Activate a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you can start installing or using packages in your virtual environment you'll
need to ``activate`` it. Activating a virtual environment will put the
virtual environment-specific ``python`` and ``pip`` executables into your
shell's ``PATH``.

.. tab:: Unix/macOS

    .. code-block:: bash

        source .venv/bin/activate

.. tab:: Windows

    .. code-block:: bat

        .venv\Scripts\activate

To confirm the virtual environment is activated, check the location of your
Python interpreter:

.. tab:: Unix/macOS

    .. code-block:: bash

        which python

.. tab:: Windows

    .. code-block:: bat

        where python

While the virtual environment is active, the above command will output a
filepath that includes the ``.venv`` directory, by ending with the following:

.. tab:: Unix/macOS

    .. code-block:: bash

        .venv/bin/python

.. tab:: Windows

    .. code-block:: bat

        .venv\Scripts\python


While a virtual environment is activated, pip will install packages into that
specific environment. This enables you to import and use packages in your
Python application.


Deactivate a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to switch projects or leave your virtual environment,
``deactivate`` the environment:

.. code-block:: bash

    deactivate

.. note::
    Closing your shell will deactivate the virtual environment. If
    you open a new shell window and want to use the virtual environment,
    reactivate it.

Reactivate a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to reactivate an existing virtual environment, follow the same
instructions about activating a virtual environment. There's no need to create
a new virtual environment.


Prepare pip
-----------

:ref:`pip` is the reference Python package manager.
It's used to install and update packages into a virtual environment.


.. tab:: Unix/macOS

    The Python installers for macOS include pip. On Linux, you may have to install
    an additional package such as ``python3-pip``. You can make sure that pip is
    up-to-date by running:

    .. code-block:: bash

        python3 -m pip install --upgrade pip
        python3 -m pip --version

    Afterwards, you should have the latest version of pip installed in your
    user site:

    .. code-block:: text

        pip 23.3.1 from .../.venv/lib/python3.9/site-packages (python 3.9)

.. tab:: Windows

    The Python installers for Windows include pip. You can make sure that pip is
    up-to-date by running:

    .. code-block:: bat

        py -m pip install --upgrade pip
        py -m pip --version

    Afterwards, you should have the latest version of pip:

    .. code-block:: text

        pip 23.3.1 from .venv\lib\site-packages (Python 3.9.4)


Install packages using pip
--------------------------

When your virtual environment is activated, you can install packages. Use the
``pip install`` command to install packages.

Install a package
~~~~~~~~~~~~~~~~~

For example,let's install the
`Requests`_ library from the :term:`Python Package Index (PyPI)`:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install requests

.. tab:: Windows

    .. code-block:: bat

        py -m pip install requests

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


Install a specific package version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pip allows you to specify which version of a package to install using
:term:`version specifiers <Version Specifier>`. For example, to install
a specific version of ``requests``:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install 'requests==2.18.4'

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "requests==2.18.4"

To install the latest ``2.x`` release of requests:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install 'requests>=2.0.0,<3.0.0'

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "requests>=2.0.0,<3.0.0"

To install pre-release versions of packages, use the ``--pre`` flag:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --pre requests

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --pre requests


Install extras
~~~~~~~~~~~~~~

Some packages have optional `extras`_. You can tell pip to install these by
specifying the extra in brackets:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install 'requests[security]'

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "requests[security]"

.. _extras:
    https://setuptools.readthedocs.io/en/latest/userguide/dependency_management.html#optional-dependencies


Install a package from source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pip can install a package directly from its source code. For example, to install
the source code in the ``google-auth`` directory:

.. tab:: Unix/macOS

    .. code-block:: bash

        cd google-auth
        python3 -m pip install .

.. tab:: Windows

    .. code-block:: bat

        cd google-auth
        py -m pip install .

Additionally, pip can install packages from source in
:doc:`development mode <setuptools:userguide/development_mode>`,
meaning that changes to the source directory will immediately affect the
installed package without needing to re-install:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --editable .

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --editable .


Install from version control systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pip can install packages directly from their version control system. For
example, you can install directly from a git repository:

.. code-block:: bash

    google-auth @ git+https://github.com/GoogleCloudPlatform/google-auth-library-python.git

For more information on supported version control systems and syntax, see pip's
documentation on :ref:`VCS Support <pip:VCS Support>`.


Install from local archives
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a local copy of a :term:`Distribution Package`'s archive (a zip,
wheel, or tar file) you can install it directly with pip:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install requests-2.18.4.tar.gz

.. tab:: Windows

    .. code-block:: bat

        py -m pip install requests-2.18.4.tar.gz

If you have a directory containing archives of multiple packages, you can tell
pip to look for packages there and not to use the
:term:`Python Package Index (PyPI)` at all:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --no-index --find-links=/local/dir/ requests

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --no-index --find-links=/local/dir/ requests

This is useful if you are installing packages on a system with limited
connectivity or if you want to strictly control the origin of distribution
packages.


Install from other package indexes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to download packages from a different index than the
:term:`Python Package Index (PyPI)`, you can use the ``--index-url`` flag:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --index-url http://index.example.com/simple/ SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --index-url http://index.example.com/simple/ SomeProject

If you want to allow packages from both the :term:`Python Package Index (PyPI)`
and a separate index, you can use the ``--extra-index-url`` flag instead:


.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --extra-index-url http://index.example.com/simple/ SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --extra-index-url http://index.example.com/simple/ SomeProject

Upgrading packages
------------------

pip can upgrade packages in-place using the ``--upgrade`` flag. For example, to
install the latest version of ``requests`` and all of its dependencies:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --upgrade requests

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --upgrade requests

Using a requirements file
-------------------------

Instead of installing packages individually, pip allows you to declare all
dependencies in a :ref:`Requirements File <pip:Requirements Files>`. For
example you could create a :file:`requirements.txt` file containing:

.. code-block:: text

    requests==2.18.4
    google-auth==1.1.0

And tell pip to install all of the packages in this file using the ``-r`` flag:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install -r requirements.txt

.. tab:: Windows

    .. code-block:: bat

        py -m pip install -r requirements.txt

Freezing dependencies
---------------------

Pip can export a list of all installed packages and their versions using the
``freeze`` command:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip freeze

.. tab:: Windows

    .. code-block:: bat

        py -m pip freeze

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

The ``pip freeze`` command is useful for creating :ref:`pip:Requirements Files`
that can re-create the exact versions of all packages installed in an environment.
