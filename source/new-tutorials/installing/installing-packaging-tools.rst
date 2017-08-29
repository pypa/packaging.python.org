Installing packaging tools
==========================

This tutorial will show you how to install the Python package manager and
associated tools.

Make sure you've got Python
---------------------------

Before you go any further, make sure you have Python and that it's avalable
from your command line. You can check this by simply running:

.. code-block:: bash

    python --version

You should get some output like ``3.6.1``. If you do not have Python, please
install the latest 3.x version from `python.org`_ or refer to the
`Installing Python`_ section of the Hitchhiker's Guide to Python.

.. Note:: This guide is written for Python 3, however, these instructions
    should work fine on Python 2. If there are any caveats for Python 2 this
    guide will call it out with a note just like this one.

.. _python.org: https://python.org
.. _Installing Python: http://docs.python-guide.org/en/latest/starting/installation/


Installing pip
--------------

:ref:`pip` is the the Python package manager. It's used to install and update
packages. You'll need to make sure you have the latest version of pip
installed.


Windows
+++++++

The Python installers for Windows include pip. If you setup Python to be in
your ``PATH`` you should have access to pip already:

.. code-block:: bash

    pip version
    pip 9.0.1 from  c:\python36\lib\site-packages (Python 3.6.1)

.. Note:: If Python and pip aren't in your PATH, If you you'll need to add
    Python's installation directory as well as the Scripts folder to your path,
    for example: ``C:\Python36\;C:\Python36\Scripts\``.

You should make sure that pip is up-to-date by running:

.. code-block:: bash

    pip install --upgrade pip


Linux and macOS
++++++++++++++++

While Debian and most other distributions include a `python-pip`_ package, it's
recommended that you install pip yourself to get the latest version. This
also applies to Python on OS X (both system and Homebrew Python):

.. code-block:: bash

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python get-pip.py

.. _python-pip: https://packages.debian.org/stable/python-pip

Afterwards, you should have pip:

.. code-block:: bash

    pip --version
    pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)


Installing virtualenv
---------------------

:ref:`virtualenv` is used to manage Python packages for different projects.
Using virtualenv allows you to avoid installing Python packages globally
which could break system tools or other projects.

Since you now have pip, you can install virtualenv by running:

.. code-block:: bash

    pip install --upgrade virtualenv

.. Note:: If you're on Linux or macOS, you may need to run this with ``sudo``.
    In general, you should avoid invoking pip with ``sudo`` as this installs
    packages globally. However, virtualenv and pip are core utilities that
    make sense to be installed globally.


Next step
---------

Now that you've got the tools installed, continue on to
:doc:`installing-and-using-packages`.
