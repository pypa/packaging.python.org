
.. _`PEP Summaries`:

PEP Summaries
==============

:Page Status: Complete
:Last Reviewed: 2014-01-22


Summaries for the currently relevant `PEPs <http://www.python.org/dev/peps/>`_
in the space of Python installation and packaging.

.. _PEP376s:

PEP376 Database of Installed Python Distributions
*************************************************

:PEP Link: `PEP376`_

:PEP Status: Accepted

:Summary: Describes a new ``.dist-info`` directory structure and system of
          metadata to be used when installing distributions.

:User Impact: This has very little implication for users, except to be aware of
              the format if they go hunting through their `site-packages`.

              .. note::

                :ref:`PEP426 <PEP426s>` will likely spawn a child PEP that
                updates this to use a json-based system of metadata.


:Implementation: Currently, only the ``bdist_wheel`` extension from the
                :ref:`wheel` project creates distributions using this structure,
                although :ref:`setuptools` and :ref:`pip` are equipped to manage
                distributions installed in this way.

.. _PEP425s:

PEP425 Compatibility Tags for Built Distributions
*************************************************

:PEP Link: `PEP425`_

:PEP Status: Accepted

:Summary: Specifies a tagging system to use in :term:`Built Distribution` file
          names. The motivation for the system was to tag wheel distributions,
          which are covered in `PEP427`_

          .. note::

             A revision to this PEP is likely due to simple tags like
             "linux_x86_64" not handling the variation within linux
             platforms. Because of this, PyPI currently blocks uploading linux
             platform-specific wheels and pip won't install linux
             platform-specific wheels from PyPI.

:User Impact: As :term:`wheels <Wheel>` become more common, users will notice
              the new tagging scheme in wheel filenames.

:Implementation: The ``bdist_wheel`` :ref:`setuptools` extensions generates
                 :term:`wheels <Wheel>` using this scheme, and pip's wheel
                 installer understands the scheme as of v1.4.


.. _PEP427s:

PEP427 The Wheel Binary Package Format 1.0
******************************************

:PEP Link: `PEP427`_

:PEP Status: Accepted

:Summary: Specifies a :term:`Built Distribution` format, that is based on, but
          modernizes the :term:`Egg` format. Wheel filenames conform to
          :ref:`PEP425 <PEP425s>`

          .. note::

             :ref:`PEP426 <PEP426s>` will likely spawn a child PEP that
             updates this to use a json-based system of metadata.


:User Impact: Built distributions are *fast* to install.

:Implementation: The ``bdist_wheel`` :ref:`setuptools` extension (available from
                 :ref:`wheel`) generates :term:`wheels <Wheel>`, and :ref:`pip`
                 supports installing wheels as of v1.4.


.. _PEP438s:

PEP438 Transitioning to release-file hosting on PyPI
****************************************************

:PEP Link: `PEP438`_

:PEP Status: Accepted

:Summary: Specifies a two-step plan to phase out the primary use of external download
          links on PyPI, for the sake of security and installation speed.

:User Impact:  :ref:`pip` (as of v1.5) will be faster and more secure by default.

:Implementation: Both :ref:`pip` and PyPI made changes during 2013 to implement
                 this PEP.


.. _PEP453s:

PEP453 Explicit bootstrapping of pip in Python installations
************************************************************

:PEP Link: `PEP453`_

:PEP Status: Accepted

:Summary: Proposes the inclusion of a method for explicitly bootstrapping pip as
          the default package manager for Python.

:User Impact: ``pip`` will be available in some Python installations without
               users having to install it.

:Implementation: The goal is to have this for Python 3.4.  PEP453 includes an
                 `integration timeline
                 <http://www.python.org/dev/peps/pep-0453/#integration-timeline>`_.


.. _PEP426s:

PEP426 Metadata for Python Software Packages 2.0
************************************************

:PEP Link: `PEP426`_

:PEP Status: Draft

:Summary: Specifies version 2.0 of the metadata format. Version 1.0 is specified
          in `PEP241`_. Version 1.1 is specified in `PEP314`_. Version 1.2 is
          specified in `PEP345`_.  This is a work in progress, and represents a
          major upgrade to the Packaging ecosystem. :ref:`PEP440 <PEP440s>` is a
          child of this PEP, and more PEPs are likely to grow out of this, as it
          evolves.

:User Impact: When this is accepted, users themselves will *not* do anything to
              adopt the new system, but rather projects like pip, setuptools,
              and PyPI will make changes to conform to it, and then surface new
              features and functionality to users that are based on top of the
              new system.

:Implementation:  Nothing at this time.


.. _PEP440s:

PEP440 Version Identification and Dependency Specification
**********************************************************

:PEP Link: `PEP440`_

:PEP Status: Draft

:Summary: Specifies a versioning system for Python projects that goes along with
          :ref:`PEP426 <PEP440s>`, and replaces `PEP386`_. This system will be
          consistent with how most people version their projects today.

:User Impact: Once accepted, users will have a clear specification for what's
              "correct" versioning for Python projects.

:Implementation:  Nothing at this time.


.. _PEP458s:

PEP458 Surviving a Compromise of PyPI
*************************************

:PEP Link: `PEP458`_

:PEP Status: Draft

:Summary: Specifies an integration of PyPI with the `"The Update Framework"
          (TUF) <http://www.updateframework.com/projects/project>`_.

:User Impact: pip will be more secure against various types of security attacks
              on PyPI and protect users against them.

:Implementation:  Nothing at this time.


.. _PEP241: http://www.python.org/dev/peps/pep-0241/
.. _PEP314: http://www.python.org/dev/peps/pep-0314/
.. _PEP345: http://www.python.org/dev/peps/pep-0345/
.. _PEP376: http://www.python.org/dev/peps/pep-0376/
.. _PEP425: http://www.python.org/dev/peps/pep-0425/
.. _PEP427: http://www.python.org/dev/peps/pep-0427/
.. _PEP438: http://www.python.org/dev/peps/pep-0438/
.. _PEP453: http://www.python.org/dev/peps/pep-0453/
.. _PEP426: http://www.python.org/dev/peps/pep-0426/
.. _PEP386: http://www.python.org/dev/peps/pep-0386/
.. _PEP440: http://www.python.org/dev/peps/pep-0440/
.. _PEP458: http://www.python.org/dev/peps/pep-0458/




