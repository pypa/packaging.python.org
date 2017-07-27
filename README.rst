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

In order to build this guide locally, you'll need:

1. `Nox <https://nox.readthedocs.io/en/latest/>`_. You can install or upgrade
   nox using ``pip``::

      pip install --upgrade nox-automation

2. Python 3.6. Our build scripts are designed to work with Python 3.6 only.
   See the `Hitchhiker's Guide to Python installation instructions <http://docs.python-guide.org/en/latest/starting/installation/>`__
   to install Python 3.6 on your operating system.

* **Building the Guide**

To build the guide run below bash command in the source folder::

  nox -s build

After the process completed you can find the HTML output in the ``./build/html`
directory. You can open the ``index.html`` file to view the guide in web broswer,
bu it's recommendation to serve the guide using an http server.

* **Serve the guide using http server**

You can build the guide and serve it via an HTTP server using the following
command::

  nox -s preview

The guide will be browsable via http://localhost:8000.

License
-------

The Python Packaging User Guide is licensed under a Creative Commons
Attribution-ShareAlike license: http://creativecommons.org/licenses/by-sa/3.0 .


.. _PyPA Code of Conduct: https://www.pypa.io/en/latest/code-of-conduct/
