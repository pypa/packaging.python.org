Prerequisites for Creating Packages
===================================

In order to complete the following tutorial, you must have pip, setuptools
and wheel installed. The section below describes the steps for installation.
Please note the latest versions of Python include pip.


Install pip, setuptools and wheel
---------------------------------

To install pip, setuptools and wheel, you must have a version of Python
installed. You can verify if there is a version of Python in your
system by entering the following into your terminal or command prompt.

.. code-block:: shell

  python --version

If a version number is returned (for example: python 3.5.0), then
Python is installed.

Once you have verified a version of Python is installed in your system,
you may proceed verifying/installing/upgrading pip, setuptools and
wheel in your system.


pip
----

To verify if pip is installed in your system, enter
the following into your command prompt.

.. code-block:: shell

  pip --version

If a version number is returned (for example: pip 7.X.X), then
pip is installed.

If pip is not installed, download get-pip.py from here_.

.. _here: https://bootstrap.pypa.io/get-pip.py

After downloading, run the following command in
your prompt as this will install pip.

.. code-block:: shell

  python get-pip.py

If pip is installed and needs to be upgraded, enter the following command.

.. code-block:: shell

  pip install --upgrade pip


setuptools
-----------

Once you have verified/upgraded pip in your system, you'll need to
verify if you have setuptools installed. To verify, enter the following into
your command prompt and you'll see a list of packages managed by pip.

.. code-block:: shell

  pip list

Scroll through the list, which is listed alphabetically, and locate setuptools.

If setuptools is not installed, enter the following into your command prompt.

.. code-block:: shell

  pip install setuptools

If setuptools needs to be upgraded, enter the following command.

.. code-block:: shell

  pip install --upgrade setuptools


wheel
-----

Similar to setuptools verification, to verify if wheel
is installed, enter the following and locate wheel.

.. code-block:: shell

  pip list

If wheel is not installed already, enter the following
into your command prompt.

.. code-block:: shell

  pip install wheel

To upgrade, enter the following into your command prompt.

.. code-block:: shell

  pip install --upgrade wheel
