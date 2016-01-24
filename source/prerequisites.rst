Prerequisites for Creating Packages
==========================

In order to create or install packages, you must have pip, setuptools and wheel installed. The section below describe the steps for installation.

Install pip, setuptools and wheel
=================================

*In order to install pip, setuptools and wheel, you must have a version of Python installed. You can verify if
there is a version of Python in your system by entering the following into your Treminal or Command Prompt:

  Linux, OS X or Windows:

  python -V or python --version

Once you have verified a version of Python is installed in your system,
you may proceed installing/verifying pip, setuptools and wheel in your system.

*If you have Python 2 >=2.7.9 or Python 3 >=3.4 installed from python.org, you will already have pip and setuptools, but will need to upgrade to the latest version:

  On Linux or OS X:
  pip install -U pip setuptools

  On Windows:
  python -m pip install -U pip setuptools

You will not have wheel, so you’ll need to run: pip install wheel

* If you're using a verison of Python which didn't install pip, setuptools and wheel, follow the steps below.

*If you’re using a Python install on Linux that’s managed by the system package manager (e.g “yum”, “apt-get” etc...), and you want to use the system package manager to install or upgrade pip, then see 'Installing pip/setuptools/wheel with Linux Package Managers <https://packaging.python.org/en/latest/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers>'

*Otherwise:

  1. Download 'get-pip.py <https://bootstrap.pypa.io/get-pip.py>'
  2. Run "python get-pip.py" in your Terminal or Command Prompt. This command will install or upgrade pip. Also, it will install setuptools and wheel if they’re not installed already.




