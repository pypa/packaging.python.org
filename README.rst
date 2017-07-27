Python Packaging User Guide
===========================

http://packaging.python.org

The "Python Packaging User Guide" (PyPUG) aims to be the authoritative resource on
how to package and install distributions in Python using current tools.

To follow the development of Python packaging, see the `Python
Packaging Authority <https://www.pypa.io>`_.


Code of Conduct
---------------

Everyone interacting in the Python Packaging User Guide project's codebases,
issue trackers, chat rooms, and mailing lists is expected to follow the
`PyPA Code of Conduct`_.

History
-------

This Guide was forked from the “Hitchhiker's Guide to Packaging” in March 2013,
which was maintained by Tarek Ziadé. Thank you Tarek for all your efforts in
Python packaging.

How to build this guide
-----------------------



* **Pre-requirements**

.. _`Pre requirements`:
Before you start to build guide you need below packages installed in your computer.

1. `Nox <https://nox.readthedocs.io/en/latest/>`_

you can install nox by below command or upgrade your nox to latest.

  `pip install --upgrade nox-automation`

2. Relavent python version

To build the guide using nox you need to install relavent python version. In Operating Systems like Ubuntu by default installed 2.7 and 3.x version.
You can findout which version you have by using

  `python -V`

or

  `python3 -V`

You can find your relavent python version in nox.py file, assign to *session.interpreter* attribute. Current version is python 3.6.
If your python version lower than 3.6 you need to install 3.6 using below commands

 sudo add-apt-repository ppa:jonathonf/python-3.6

 sudo apt-get update

 sudo apt-get install python3.6

Now you're ready to build the guide.

* **Building the Guide**

To build the guide run below bash command in the source folder

  nox -s build

After the process completed you can find the HTML version in the

**/python-packaging-user-guide/build/html**

open index.html file to view the guide in web broswer.

* **Serve the guide using http server**

Other than access locally build guide you can serve the guide through http server. To that run below command in project folder.

  nox -s preview

To access guide access localhost using web browser using port 8000.

  http://localhost:8000

  or

  http://0.0.0.0:8000

License
-------

The Python Packaging User Guide is licensed under a Creative Commons
Attribution-ShareAlike license: http://creativecommons.org/licenses/by-sa/3.0 .


.. _PyPA Code of Conduct: https://www.pypa.io/en/latest/code-of-conduct/
