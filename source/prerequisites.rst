Prerequisites for Creating Packages
==========================

In order to complete the following tutorial, you must have pip, setuptools and wheel installed. The section below describes the steps for installation.

Install pip, setuptools and wheel
=================================

*To install pip, setuptools and wheel, you must have a version of Python installed. You can verify if
there is a version of Python in your system by entering the following into your terminal or command prompt:

  python -V

Once you have verified a version of Python is installed in your system,
you may proceed verifying/installing/upgrading pip, setuptools and wheel in your system.

*pip

To verify if pip is installed in your system, enter 'pip -V' into your command prompt.
If a version number is returned (for example: pip 7.X.X), then pip is installed.

If pip is not installed, download 'get-pip.py <https://bootstrap.pypa.io/get-pip.py>'. After downloading,
run "python get-pip.py" in your command prompt as this will install pip.

If pip is installed and needs to be upgraded, enter the 'pip install --upgrade pip' command.

*setuptools

Once you have verified//upgraded pip in your system, you'll need to verify if you have setuptools installed.
To verify, enter 'pip list' in the command prompt and you'll see a list of packages managed by pip. Scroll through
the list, which is listed alphabetically, and locate setuptools.

If setuptool is not installed, enter 'pip install setuptools' into your command prompt.

If setuptools needs to be upgraded, enter the 'pip install --upgrade setuptools' command.

*wheel

Similar to setuptools verification, to verify if wheel is installed, enter 'pip list' and locate wheel.

If wheel is not installed already, enter 'pip install wheel' into your command prompt.

To upgrade, enter the 'pip install --upgrade wheel' into your command prompt.
