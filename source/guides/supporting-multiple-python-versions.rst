:orphan:

.. _`Supporting multiple Python versions`:

===================================
Supporting multiple Python versions
===================================

:Page Status: Obsolete
:Last Reviewed: 2014-12-24


::

  FIXME

  Useful projects/resources to reference:

  - DONE six
  - DONE python-future (http://python-future.org)
  - tox
  - DONE Travis and Shining Panda CI (Shining Panda no longer available)
  - DONE Appveyor
  - DONE Ned Batchelder's "What's in Which Python"
    - http://nedbatchelder.com/blog/201310/whats_in_which_python_3.html
      - http://nedbatchelder.com/blog/201109/whats_in_which_python.html
  - Lennart Regebro's "Porting to Python 3"
  - Greg Hewgill's script to identify the minimum version of Python
    required to run a particular script:
    https://github.com/ghewgill/pyqver
  - the Python 3 porting how to in the main docs
  - cross reference to the stable ABI discussion
    in the binary extensions topic (once that exists)
  - mention version classifiers for distribution metadata

In addition to the work required to create a Python package, it is often
necessary that the package must be made available on different versions of
Python.  Different Python versions may contain different (or renamed) standard
library packages, and the changes between Python versions 2.x and 3.x include
changes in the language syntax.

Performed manually, all the testing required to ensure that the package works
correctly on all the target Python versions (and OSs!) could be very
time-consuming. Fortunately, several tools are available for dealing with
this, and these will briefly be discussed here.

Automated testing and continuous integration
--------------------------------------------

Several hosted services for automated testing are available. These services
will typically monitor your source code repository (e.g. at
`GitHub <https://github.com>`_ or `Bitbucket <https://bitbucket.org>`_)
and run your project's test suite every time a new commit is made.

These services also offer facilities to run your project's test suite on
*multiple versions of Python*, giving rapid feedback about whether the code
will work, without the developer having to perform such tests themselves.

Wikipedia has an extensive `comparison
<https://en.wikipedia.org/wiki/Comparison_of_continuous_integration_software>`_
of many continuous-integration systems. There are two hosted services which
when used in conjunction provide automated testing across Linux, Mac and
Windows:

  - `Travis CI <https://travis-ci.org>`_ provides both a Linux and a macOS
    environment. The Linux environment is Ubuntu 12.04 LTS Server Edition 64 bit
    while the macOS is 10.9.2 at the time of writing.
  - `Appveyor <https://www.appveyor.com/>`_ provides a Windows environment
    (Windows Server 2012).

::

    TODO Either link to or provide example .yml files for these two
    services.

    TODO How do we keep the Travis Linux and macOS versions up-to-date in this
    document?

Both `Travis CI`_ and Appveyor_ require a `YAML
<https://yaml.org>`_-formatted file as specification for the instructions
for testing. If any tests fail, the output log for that specific configuration
can be inspected.

For Python projects that are intended to be deployed on both Python 2 and 3
with a single-source strategy, there are a number of options.

Tools for single-source Python packages
----------------------------------------

`six <https://pypi.org/project/six/>`_ is a tool developed by Benjamin Peterson
for wrapping over the differences between Python 2 and Python 3. The six_
package has enjoyed widespread use and may be regarded as a reliable way to
write a single-source Python module that can be use in both Python 2 and 3.
The six_ module can be used from as early as Python 2.5. A tool called
`modernize <https://pypi.org/project/modernize>`_, developed by Armin
Ronacher, can be used to automatically apply the code modifications provided
by six_.

Similar to six_, `python-future <http://python-future.org/overview.html>`_ is
a package that provides a compatibility layer between Python 2 and Python 3
source code; however, unlike six_, this package aims to provide
interoperability between Python 2 and Python 3 with a language syntax that
matches one of the two Python versions: one may
use

  - a Python 2 (by syntax) module in a Python 3 project.
  - a Python 3 (by syntax) module in a *Python 2* project.

Because of the bi-directionality, python-future_ offers a pathway to
converting a Python 2 package to Python 3 syntax module-by-module. However, in
contrast to six_, python-future_ is supported only from Python 2.6. Similar to
modernize_ for six_, python-future_ comes with two scripts called ``futurize``
and ``pasteurize`` that can be applied to either a Python 2 module or a Python
3 module respectively.

Use of six_ or python-future_ adds an additional runtime dependency to your
package: with python-future_, the ``futurize`` script can be called with the
``--stage1`` option to apply only the changes that Python 2.6+ already
provides for forward-compatibility to Python 3. Any remaining compatibility
problems would require manual changes.

What's in which Python?
-----------------------

Ned Batchelder provides a list of changes in each Python release for
`Python 2 <https://nedbatchelder.com/blog/201109/whats_in_which_python.html>`__,
`Python 3.0-3.3 <https://nedbatchelder.com/blog/201310/whats_in_which_python_3.html>`__ and
`Python 3.4-3.6 <https://nedbatchelder.com/blog/201803/whats_in_which_python_3436.html>`__.
These lists may be used to check whether any changes between Python versions
may affect your package.

::

    TODO These lists should be reproduced here (with permission).

    TODO The py3 list should be updated to include 3.4
