
.. _`PEP Summaries`:

PEP Summaries
==============

:Page Status: Incomplete [1]_
:Last Reviewed: 2013-11-01


Summaries for the most relevant PEPs in the space of Python installation and
packaging.

.. _PEP376s:

PEP376 Database of Installed Python Distributions
*************************************************

:PEP Link: `PEP376`_

:PEP Status: Accepted

:Summary: Describes a new ``.dist-info`` directory structure to be used when
          installing distributions.

:User Impact: This has very little implication for users, except that it might
              help users to be aware of this directory format if they go hunting
              through their `site-packages` for some reason, which we all end up
              doing from time to time.

:Implementation: Currently, only the ``bdist_wheel`` extension from the
                :ref:`wheel` project creates distributions using this structure,
                although :ref:`setuptools` and :ref:`pip` are equipped to manage
                distributions installed in this way.

.. _PEP425s:

PEP425 Compatibility Tags for Built Distributions
*************************************************

:PEP Link: `PEP425`_

:PEP Status: Accepted

             .. note::

                 A revision to this PEP is likely due to it not handling the
                 variation within a specific platform, e.g. the linux variation
                 we see across the linux distros is not covered with the simple
                 tag "linux_x86_64".  Because of this, PyPI currently blocks
                 uploading platform-specific wheels (except for windows), and
                 pip currently won't install platform-specific wheels from PyPI
                 (except for windows).


:Summary: Specifies a tagging system to use in :term:`Binary Distribution` file
          names. The motivation for the system was to tag wheel distributions,
          which are covered in `PEP427`_

:User Impact: As :term:`wheels <Wheel>` become more common, users will notice
              the new tagging scheme in wheel filenames.

:Implementation: The ``bdist_wheel`` setuptools extensions generates
                 :term:`wheels <Wheel>` using this scheme, and pip's wheel
                 installer understands the scheme as of v1.4.


.. _PEP427s:

PEP427 The Wheel Binary Package Format 1.0
******************************************

:PEP Link: `PEP427`_

:PEP Status: Accepted

:Summary:

:User Impact:

:Implementation:


.. _PEP438s:

PEP438 Transitioning to release-file hosting on PyPI
****************************************************

:PEP Link: `PEP438`_

:PEP Status: Accepted

:Summary:

:User Impact:

:Implementation:


.. _PEP453s:

PEP453 Explicit bootstrapping of pip in Python installations
************************************************************

:PEP Link: `PEP453`_

:PEP Status: Accepted

:Summary: Proposes the inclusion of a method for explicitly bootstrapping pip as
          the default package manager for Python.

:User Impact: ``pip`` will be available without users having to install it.

:Implementation: The goal is to have this for Python 3.4.  PEP453 includes an
                 `integration timeline
                 <http://www.python.org/dev/peps/pep-0453/#integration-timeline>`_.


.. _PEP426s:

PEP426 Metadata for Python Software Packages 2.0
************************************************

:PEP Link: `PEP426`_

:PEP Status: Draft

:Summary:

:User Impact:

:Implementation:


.. _PEP440s:

PEP440 Version Identification and Dependency Specification
**********************************************************

:PEP Link: `PEP427`_

:PEP Status: Draft

:Summary:

:User Impact:

:Implementation:


.. _PEP376: http://www.python.org/dev/peps/pep-0376/
.. _PEP425: http://www.python.org/dev/peps/pep-0425/
.. _PEP427: http://www.python.org/dev/peps/pep-0427/
.. _PEP438: http://www.python.org/dev/peps/pep-0438/
.. _PEP453: http://www.python.org/dev/peps/pep-0453/
.. _PEP426: http://www.python.org/dev/peps/pep-0426
.. _PEP440: http://www.python.org/dev/peps/pep-0440//


.. [1] Need to fill in missing information.
