
.. _`PEP Summaries`:

PEP Summaries
==============

:Page Status: Incomplete [1]_
:Last Reviewed: 10-29-2013


Summaries for the most relevant PEPs in the space of Python installation and packaging.

.. _PEP376s:

PEP376 Database of Installed Python Distributions
*************************************************

`PEP376`_ describes a new ``.dist-info`` directory structure to be used when
installing distributions.  Currently, only the ``bdist_wheel`` extension from
the :ref:`wheel` project creates distributions using this structure, although
:ref:`setuptools` and :ref:`pip` are equipped to manage distributions installed
in this way. This has very little implication for users, except that it might
help users to be aware of this directory format if they go hunting through their
`site-packages` for some reason, which we all end up doing from time to time.


.. _PEP425s:

PEP425 Compatibility Tags for Built Distributions
*************************************************

`PEP425`_ specifies a tagging system to use in :term:`Binary Distribution` file
names.  The system is composed of a set of three tags that indicate which Python
implementation and language version, ABI, and platform a :term:`Binary
Distribution` requires.  The motivation for the system was to tag wheel
distributions, which are covered in `PEP427`_.


.. _PEP427s:

PEP427 The Wheel Binary Package Format 1.0
******************************************

`PEP427`_


.. _PEP438s:

PEP438 Transitioning to release-file hosting on PyPI
****************************************************

`PEP438`_


.. _PEP453s:

PEP453 Explicit bootstrapping of pip in Python installations
************************************************************

`PEP453`_ proposes the inclusion of a method for explicitly bootstrapping pip as
the default package manager for Python. It also proposes that the distributions
of Python available via Python.org will automatically run this explicit
bootstrapping method and a recommendation to third party redistributors of
Python to also provide pip by default (in a way reasonable for their
distributions).

The impact for users, is that pip would be immediately
available without user installation.


.. _PEP426s:

PEP426 Metadata for Python Software Packages 2.0
************************************************

`PEP426`_


.. _PEP440s:

PEP440 Version Identification and Dependency Specification
**********************************************************

`PEP440`_


.. _PEP376: http://www.python.org/dev/peps/pep-0376/
.. _PEP425: http://www.python.org/dev/peps/pep-0425/
.. _PEP427: http://www.python.org/dev/peps/pep-0427/
.. _PEP438: http://www.python.org/dev/peps/pep-0438/
.. _PEP453: http://www.python.org/dev/peps/pep-0453/
.. _PEP426: http://www.python.org/dev/peps/pep-0426
.. _PEP440: http://www.python.org/dev/peps/pep-0440//


.. [1] See `Issue #31
       <https://bitbucket.org/pypa/python-packaging-user-guide/issue/31/what-to-cover-in-the-pep-summaries>`_
       about how these entries need to be expanded.
