
.. _`History`:

====================
A Packaging Timeline
====================

:Page Status: Incomplete [#]_
:Last Reviewed: 2013-10-29


**2013-06-09**: The merge of :ref:`setuptools` and :ref:`distribute` was completed
and released to PyPI. [#]_

**2013-03-23**: :term:`PyPA <Python Packaging Authority (PyPA)>` became the
maintainer for the `Python Packaging User Guide`_, which was forked from the
"Hitchhiker's Guide to Packaging". [#]_

**2013-03-15**: Packaging Dev and User Summits were held at Pycon 2013 to share ideas on
the future of packaging. [#]_ [#]_

**2013-03-14**: The intention to merge :ref:`setuptools` and
:ref:`distribute` was announced by their respective maintainers, PJ Eby and Jason Coombs. [#]_

**2013-03-09**: :ref:`pip` began depending on :ref:`distlib`. [#]_

**2013-03-02**: :ref:`distlib` began releasing to `PyPI`_.

**2013-03-17**: `PEP425`_ and `PEP427`_ were accepted.  Together, they specify a
built-package format for Python called "wheel".

**2012-06-19**: The effort to include "Distutils2/Packaging" in Python 3.3 was
abandoned due lack of involvement. [#]_

**2008**: After some period of trying to open up the Setuptools project itself,
some of these developers led by Tarek Ziade decided to fork Setuptools.  The
fork was named Distribute.

**2008**: Ian Bicking created an alternative for easy_install called `pip`_, also
building on Setuptools.

**2007**: virtualenv was released. Ian Bicking drove one line of solutions:
virtual-python, which evolved into workingenv, which evolved into virtualenv
in 2007. The concept behind this approach is to allow the developer to create as
many fully working Python environments as they like from a central system
installation of Python. When the developer activates the virtualenv,
easy_install will install all packages into its the virtualenv's
site-packages. This allows you to create a virtualenv per project and thus
isolate each project from each other.

**2006**: Jim Fulton created Buildout, building on Setuptools and
easy_install. Buildout can create an isolated project environment like
virtualenv does, but is more ambitious: the goal is to create a system for
repeatable installations of potentially very complex projects. Instead of
writing an INSTALL.txt that tells others who to install the prerequites for a
package (Python or not), with Buildout these prerequisites can be installed
automatically.

**2004**: Phillip Eby started work on Setuptools in 2004. Setuptools is a whole
range of extensions to Distutils such as from a binary installation format
(eggs), an automatic package installation tool, and the definition and
declaration of scripts for installation. Work continued throughout 2005 and
2006, and feature after feature was added to support a whole range of advanced
usage scenarios.

**2003**: The Python package index was up and running. The Python world now had
a way to upload packages and metadata to a central index. If we then manually
downloaded a package we could install it using setup.py thanks to Distutils.

**2002**: Richard Jones started work on the Python Package Index, `PyPI`_.  `PyPI`_ is
also known as the Cheeseshop. The first work on an implementation started, and
PEP 301 that describes `PyPI`_ was also created then. Distutils was extended so the
metadata and packages themselves could be uploaded to this package index.

**2001**: The first step was to standardize the metadata that could be cataloged
by any index of Python packages. Andrew Kuchling drove the effort on this,
culminating in PEP 241, later updated by PEP 314:

**2000**: We didn't have a centralized index (or catalog) of packages yet,
however. To work on this, the Catalog SIG was started in the year

**2000**: Distutils was added to the Python standard library in Python 1.6. We
now had a way to distribute and install Python packages, if we did the
distribution ourselves.

**1998**: The Distutils SIG (special interest group) was created. Greg Ward in
the context of this discussion group started to create Distutils about this
time. Distutils allows you to structure your Python project so that it has a
setup.py. Through this setup.py you can issue a variety of commands, such as
creating a tarball out of your project, or installing your project. Distutils
importantly also has infrastructure to help compiling C extensions for your
Python package.


.. _PyPI: https://pypi.python.org
.. _pip: http://www.pip-installer.org/en/latest/
.. _`Python Packaging User Guide`: https://python-packaging-user-guide.readthedocs.org/en/latest/
.. _PEP425: http://www.python.org/dev/peps/pep-0425
.. _PEP427: http://www.python.org/dev/peps/pep-0427

.. [#] Missing some recent events. Some the older events could more brief.
.. [#] http://mail.python.org/pipermail/distutils-sig/2013-June/021160.html
.. [#] http://mail.python.org/pipermail/distutils-sig/2013-March/020224.html
.. [#] https://us.pycon.org/2013/community/openspaces/packaginganddistributionminisummit/
.. [#] http://www.pyvideo.org/video/1731/panel-directions-for-packaging
.. [#] http://mail.python.org/pipermail/distutils-sig/2013-March/020127.html
.. [#] https://github.com/pypa/pip/pull/834
.. [#] http://mail.python.org/pipermail/python-dev/2012-June/120430.html

