
.. _`PEP Summaries`:

PEP Summaries
==============

:Page Status: Complete
:Last Reviewed: 2014-08-25


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


:Implementation: Currently, the ``bdist_wheel`` extension from the
                :ref:`wheel` project creates distributions using this structure,
                and :ref:`setuptools` and :ref:`pip` are equipped to manage
                distributions installed in this way. There is also an
                implementation in :ref:`distlib`.

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
                 installer understands the scheme as of v1.4. The wheel builder
                 in :ref:`distlib` also implements this scheme.


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
                 supports installing wheels as of v1.4. There is also an
                 implementation in :ref:`distlib`, which allows both building
                 wheels and installing from wheels.


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

:Implementation:  Most of the PEP is implemented in :ref:`distlib`, including
                  the dependency metadata. Since the PEP is still in flux, the
                  ``distlib`` implementation lags behind the most recent PEP
                  changes, but most of the functionality in the PEP is covered.


.. _PEP440s:

PEP440 Version Identification and Dependency Specification
**********************************************************

:PEP Link: `PEP440`_

:PEP Status: Accepted

:Summary: Specifies a versioning system for Python projects that goes along with
          :ref:`PEP426 <PEP426s>`, and replaces `PEP386`_. This system will be
          mostly consistent with how most people version their
          projects today.

:User Impact: Users will have a clear specification for what's proper
              versioning for Python projects.

:Implementation: :ref:`distlib` has version classes that understand PEP440, and
                 pip relies on :ref:`distlib`'s implementation in specific
                 cases. pip also has a `work-in-progress PR
                 <https://github.com/pypa/pip/pull/1894>`_ that implements
                 PEP440.


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



.. _PEP70s:

PEP470 Using Multi Index Support for External to PyPI Package File Hosting
**************************************************************************

:PEP Link: `PEP470`_

:PEP Status: Draft

:Summary: PyPI would no longer support projects configuring external hosting
          links that pip crawls and installs from automatically.  Projects would
          be allowed to configure external index links, but pip would never
          install from them automatically, but instead, only give users an
          informational message about what command they would use to do the
          install.  This PEP effectively reverts :ref:`PEP438 <PEP438s>`.

:User Impact: This would obsolete pip's ``--allow-external`` and
               ``--allow-unverified`` links, because PyPI itself wouldn't
               contain external or unverified links.

:Implementation: Nothing at this time.



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
.. _PEP470: http://www.python.org/dev/peps/pep-0470/




