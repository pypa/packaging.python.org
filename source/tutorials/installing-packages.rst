.. _installing-packages:

===================
Installing Packages
===================

This section covers the basics of how to install Python :term:`packages
<Distribution Package>`.

It's important to note that the term "package" in this context is being used to
describe a bundle of software to be installed (i.e. as a synonym for a
:term:`distribution <Distribution Package>`). It does not refer to the kind
of :term:`package <Import Package>` that you import in your Python source code
(i.e. a container of modules). It is common in the Python community to refer to
a :term:`distribution <Distribution Package>` using the term "package".  Using
the term "distribution" is often not preferred, because it can easily be
confused with a Linux distribution, or another larger software distribution
like Python itself.


.. _installing_requirements:

Requirements for Installing Packages
====================================

This section describes the steps to follow before installing other Python
packages.


Ensure you can run Python from the command line
-----------------------------------------------

Before you go any further, make sure you have Python and that the expected
version is available from your command line. You can check this by running:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 --version

.. tab:: Windows

    .. code-block:: bat

        py --version


You should get some output like ``Python 3.6.3``. If you do not have Python,
please install the latest 3.x version from `python.org`_ or refer to the
:ref:`Installing Python <python-guide:installation>` section of the Hitchhiker's Guide to Python.

.. Note:: If you're a newcomer and you get an error like this:

    .. code-block:: pycon

        >>> python3 --version
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'python3' is not defined

    It's because this command and other suggested commands in this tutorial
    are intended to be run in a *shell* (also called a *terminal* or
    *console*). See the Python for Beginners `getting started tutorial`_ for
    an introduction to using your operating system's shell and interacting with
    Python.

.. Note:: If you're using an enhanced shell like IPython or the Jupyter
   notebook, you can run system commands like those in this tutorial by
   prefacing them with a ``!`` character:

   .. code-block:: text

        In [1]: import sys
                !{sys.executable} --version
        Python 3.6.3

   It's recommended to write ``{sys.executable}`` rather than plain ``python`` in
   order to ensure that commands are run in the Python installation matching
   the currently running notebook (which may not be the same Python
   installation that the ``python`` command refers to).

.. Note:: Due to the way most Linux distributions are handling the Python 3
   migration, Linux users using the system Python without creating a virtual
   environment first should replace the ``python`` command in this tutorial
   with ``python3`` and the ``python -m pip`` command with ``python3 -m pip --user``. Do *not*
   run any of the commands in this tutorial with ``sudo``: if you get a
   permissions error, come back to the section on creating virtual environments,
   set one up, and then continue with the tutorial as written.

.. _getting started tutorial: https://opentechschool.github.io/python-beginners/en/getting_started.html#what-is-python-exactly
.. _python.org: https://www.python.org

Ensure you can run pip from the command line
--------------------------------------------

Additionally, you'll need to make sure you have :ref:`pip` available. You can
check this by running:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip --version

.. tab:: Windows

    .. code-block:: bat

        py -m pip --version

If you installed Python from source, with an installer from `python.org`_, or
via `Homebrew`_ you should already have pip. If you're on Linux and installed
using your OS package manager, you may have to install pip separately, see
:doc:`/guides/installing-using-linux-tools`.

.. _Homebrew: https://brew.sh

If ``pip`` isn't already installed, then first try to bootstrap it from the
standard library:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m ensurepip --default-pip

.. tab:: Windows

    .. code-block:: bat

        py -m ensurepip --default-pip

If that still doesn't allow you to run ``python -m pip``:

* Securely Download `get-pip.py
  <https://bootstrap.pypa.io/get-pip.py>`_ [1]_

* Run ``python get-pip.py``. [2]_  This will install or upgrade pip.
  Additionally, it will install :ref:`setuptools` and :ref:`wheel` if they're
  not installed already.

  .. warning::

     Be cautious if you're using a Python install that's managed by your
     operating system or another package manager. get-pip.py does not
     coordinate with those tools, and may leave your system in an
     inconsistent state. You can use ``python get-pip.py --prefix=/usr/local/``
     to install in ``/usr/local`` which is designed for locally-installed
     software.


Ensure pip, setuptools, and wheel are up to date
------------------------------------------------

While ``pip`` alone is sufficient to install from pre-built binary archives,
up to date copies of the ``setuptools`` and ``wheel`` projects are useful
to ensure you can also install from source archives:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --upgrade pip setuptools wheel

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --upgrade pip setuptools wheel

Optionally, create a virtual environment
----------------------------------------

See :ref:`section below <Creating and using Virtual Environments>` for details,
but here's the basic :doc:`venv <python:library/venv>` [3]_ command to use on a typical Linux system:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m venv tutorial_env
        source tutorial_env/bin/activate

.. tab:: Windows

    .. code-block:: bat

        py -m venv tutorial_env
        tutorial_env\Scripts\activate

This will create a new virtual environment in the ``tutorial_env`` subdirectory,
and configure the current shell to use it as the default ``python`` environment.


.. _Creating and using Virtual Environments:

Creating Virtual Environments
=============================

Python "Virtual Environments" allow Python :term:`packages <Distribution
Package>` to be installed in an isolated location for a particular application,
rather than being installed globally. If you are looking to safely install
global command line tools,
see :doc:`/guides/installing-stand-alone-command-line-tools`.

Imagine you have an application that needs version 1 of LibFoo, but another
application requires version 2. How can you use both these applications? If you
install everything into /usr/lib/python3.6/site-packages (or whatever your
platform’s standard location is), it’s easy to end up in a situation where you
unintentionally upgrade an application that shouldn’t be upgraded.

Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.

Also, what if you can’t install :term:`packages <Distribution Package>` into the
global site-packages directory? For instance, on a shared host.

In all these cases, virtual environments can help you. They have their own
installation directories and they don’t share libraries with other virtual
environments.

Currently, there are two common tools for creating Python virtual environments:

* :doc:`venv <python:library/venv>` is available by default in Python 3.3 and later, and installs
  :ref:`pip` into created virtual environments in Python 3.4 and later
  (Python versions prior to 3.12 also installed :ref:`setuptools`).
* :ref:`virtualenv` needs to be installed separately, but supports Python 2.7+
  and Python 3.3+, and :ref:`pip`, :ref:`setuptools` and :ref:`wheel` are
  installed into created virtual environments by default. Note that ``setuptools`` is no longer
  included by default starting with Python 3.12 (and ``virtualenv`` follows this behavior).

The basic usage is like so:

Using :doc:`venv <python:library/venv>`:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m venv <DIR>
        source <DIR>/bin/activate

.. tab:: Windows

    .. code-block:: bat

        py -m venv <DIR>
        <DIR>\Scripts\activate

Using :ref:`virtualenv`:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m virtualenv <DIR>
        source <DIR>/bin/activate

.. tab:: Windows

    .. code-block:: bat

        virtualenv <DIR>
        <DIR>\Scripts\activate

For more information, see the :doc:`venv <python:library/venv>` docs or
the :doc:`virtualenv <virtualenv:index>` docs.

The use of :command:`source` under Unix shells ensures
that the virtual environment's variables are set within the current
shell, and not in a subprocess (which then disappears, having no
useful effect).

In both of the above cases, Windows users should *not* use the
:command:`source` command, but should rather run the :command:`activate`
script directly from the command shell like so:

.. code-block:: bat

   <DIR>\Scripts\activate



Managing multiple virtual environments directly can become tedious, so the
:ref:`dependency management tutorial <managing-dependencies>` introduces a
higher level tool, :ref:`Pipenv`, that automatically manages a separate
virtual environment for each project and application that you work on.


Use pip for Installing
======================

:ref:`pip` is the recommended installer.  Below, we'll cover the most common
usage scenarios. For more detail, see the :doc:`pip docs <pip:index>`,
which includes a complete :doc:`Reference Guide <pip:cli/index>`.


Installing from PyPI
====================

The most common usage of :ref:`pip` is to install from the :term:`Python Package
Index <Python Package Index (PyPI)>` using a :term:`requirement specifier
<Requirement Specifier>`. Generally speaking, a requirement specifier is
composed of a project name followed by an optional :term:`version specifier
<Version Specifier>`.  A full description of the supported specifiers can be
found in the :ref:`Version specifier specification <version-specifiers>`.
Below are some examples.

To install the latest version of "SomeProject":

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install "SomeProject"

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomeProject"

To install a specific version:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install "SomeProject==1.4"

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomeProject==1.4"

To install greater than or equal to one version and less than another:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install "SomeProject>=1,<2"

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomeProject>=1,<2"


To install a version that's :ref:`compatible <version-specifiers-compatible-release>`
with a certain version: [4]_

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install "SomeProject~=1.4.2"

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomeProject~=1.4.2"

In this case, this means to install any version "==1.4.*" version that's also
">=1.4.2".


Source Distributions vs Wheels
==============================

:ref:`pip` can install from either :term:`Source Distributions (sdist) <Source
Distribution (or "sdist")>` or :term:`Wheels <Wheel>`, but if both are present
on PyPI, pip will prefer a compatible :term:`wheel <Wheel>`. You can override
pip`s default behavior by e.g. using its :ref:`--no-binary
<pip:install_--no-binary>` option.

:term:`Wheels <Wheel>` are a pre-built :term:`distribution <Distribution
Package>` format that provides faster installation compared to :term:`Source
Distributions (sdist) <Source Distribution (or "sdist")>`, especially when a
project contains compiled extensions.

If :ref:`pip` does not find a wheel to install, it will locally build a wheel
and cache it for future installs, instead of rebuilding the source distribution
in the future.


Upgrading packages
==================

Upgrade an already installed ``SomeProject`` to the latest from PyPI.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --upgrade SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --upgrade SomeProject

.. _`Installing to the User Site`:

Installing to the User Site
===========================

To install :term:`packages <Distribution Package>` that are isolated to the
current user, use the ``--user`` flag:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --user SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --user SomeProject

For more information see the `User Installs
<https://pip.pypa.io/en/latest/user_guide/#user-installs>`_ section
from the pip docs.

Note that the ``--user`` flag has no effect when inside a virtual environment
- all installation commands will affect the virtual environment.

If ``SomeProject`` defines any command-line scripts or console entry points,
``--user`` will cause them to be installed inside the `user base`_'s binary
directory, which may or may not already be present in your shell's
:envvar:`PATH`.  (Starting in version 10, pip displays a warning when
installing any scripts to a directory outside :envvar:`PATH`.)  If the scripts
are not available in your shell after installation, you'll need to add the
directory to your :envvar:`PATH`:

- On Linux and macOS you can find the user base binary directory by running
  ``python -m site --user-base`` and adding ``bin`` to the end. For example,
  this will typically print ``~/.local`` (with ``~`` expanded to the absolute
  path to your home directory) so you'll need to add ``~/.local/bin`` to your
  ``PATH``.  You can set your ``PATH`` permanently by `modifying ~/.profile`_.

- On Windows you can find the user base binary directory by running ``py -m
  site --user-site`` and replacing ``site-packages`` with ``Scripts``. For
  example, this could return
  ``C:\Users\Username\AppData\Roaming\Python36\site-packages`` so you would
  need to set your ``PATH`` to include
  ``C:\Users\Username\AppData\Roaming\Python36\Scripts``. You can set your user
  ``PATH`` permanently in the `Control Panel`_. You may need to log out for the
  ``PATH`` changes to take effect.

.. _user base: https://docs.python.org/3/library/site.html#site.USER_BASE
.. _modifying ~/.profile: https://stackoverflow.com/a/14638025
.. _Control Panel: https://docs.microsoft.com/en-us/windows/win32/shell/user-environment-variables?redirectedfrom=MSDN

Requirements files
==================

Install a list of requirements specified in a :ref:`Requirements File
<pip:Requirements Files>`.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install -r requirements.txt

.. tab:: Windows

    .. code-block:: bat

        py -m pip install -r requirements.txt

Installing from VCS
===================

Install a project from VCS in "editable" mode.  For a full breakdown of the
syntax, see pip's section on :ref:`VCS Support <pip:VCS Support>`.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git
        python3 -m pip install -e SomeProject @ hg+https://hg.repo/some_pkg                # from mercurial
        python3 -m pip install -e SomeProject @ svn+svn://svn.repo/some_pkg/trunk/         # from svn
        python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  # from a branch

.. tab:: Windows

    .. code-block:: bat

        py -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git
        py -m pip install -e SomeProject @ hg+https://hg.repo/some_pkg                # from mercurial
        py -m pip install -e SomeProject @ svn+svn://svn.repo/some_pkg/trunk/         # from svn
        py -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  # from a branch

Installing from other Indexes
=============================

Install from an alternate index

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --index-url http://my.package.repo/simple/ SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --index-url http://my.package.repo/simple/ SomeProject

Search an additional index during install, in addition to :term:`PyPI <Python
Package Index (PyPI)>`

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --extra-index-url http://my.package.repo/simple SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --extra-index-url http://my.package.repo/simple SomeProject

Installing from a local src tree
================================


Installing from local src in
:doc:`Development Mode <setuptools:userguide/development_mode>`,
i.e. in such a way that the project appears to be installed, but yet is
still editable from the src tree.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install -e <path>

.. tab:: Windows

    .. code-block:: bat

        py -m pip install -e <path>

You can also install normally from src

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install <path>

.. tab:: Windows

    .. code-block:: bat

        py -m pip install <path>

Installing from local archives
==============================

Install a particular source archive file.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install ./downloads/SomeProject-1.0.4.tar.gz

.. tab:: Windows

    .. code-block:: bat

        py -m pip install ./downloads/SomeProject-1.0.4.tar.gz

Install from a local directory containing archives (and don't check :term:`PyPI
<Python Package Index (PyPI)>`)

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --no-index --find-links=file:///local/dir/ SomeProject
        python3 -m pip install --no-index --find-links=/local/dir/ SomeProject
        python3 -m pip install --no-index --find-links=relative/dir/ SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --no-index --find-links=file:///local/dir/ SomeProject
        py -m pip install --no-index --find-links=/local/dir/ SomeProject
        py -m pip install --no-index --find-links=relative/dir/ SomeProject

Installing from other sources
=============================

To install from other data sources (for example Amazon S3 storage)
you can create a helper application that presents the data
in a format compliant with the :ref:`simple repository API <simple-repository-api>`:,
and use the ``--extra-index-url`` flag to direct pip to use that index.

.. code-block:: bash

   ./s3helper --port=7777
   python -m pip install --extra-index-url http://localhost:7777 SomeProject


Installing Prereleases
======================

Find pre-release and development versions, in addition to stable versions.  By
default, pip only finds stable versions.

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --pre SomeProject

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --pre SomeProject

Installing "Extras"
===================

Extras are optional "variants" of a package, which may include
additional dependencies, and thereby enable additional functionality
from the package.  If you wish to install an extra for a package which
you know publishes one, you can include it in the pip installation command:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install 'SomePackage[PDF]'
        python3 -m pip install 'SomePackage[PDF]==3.0'
        python3 -m pip install -e '.[PDF]'  # editable project in current directory

.. tab:: Windows

    .. code-block:: bat

        py -m pip install "SomePackage[PDF]"
        py -m pip install "SomePackage[PDF]==3.0"
        py -m pip install -e ".[PDF]"  # editable project in current directory

----

.. [1] "Secure" in this context means using a modern browser or a
       tool like :command:`curl` that verifies SSL certificates when
       downloading from https URLs.

.. [2] Depending on your platform, this may require root or Administrator
       access. :ref:`pip` is currently considering changing this by `making user
       installs the default behavior
       <https://github.com/pypa/pip/issues/1668>`_.Attribution-NonCommercial-NoDerivatives 4.0 International
Creative Commons Legal Code

Attribution-ShareAlike 3.0 Unported

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS LICENSE DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE INFORMATION PROVIDED, AND DISCLAIMS LIABILITY FOR
    DAMAGES RESULTING FROM ITS USE.

License

THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE
COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY
COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS
AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.

BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE
TO BE BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY
BE CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS
CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND
CONDITIONS.

1. Definitions

 a. "Adaptation" means a work based upon the Work, or upon the Work and
    other pre-existing works, such as a translation, adaptation,
    derivative work, arrangement of music or other alterations of a
    literary or artistic work, or phonogram or performance and includes
    cinematographic adaptations or any other form in which the Work may be
    recast, transformed, or adapted including in any form recognizably
    derived from the original, except that a work that constitutes a
    Collection will not be considered an Adaptation for the purpose of
    this License. For the avoidance of doubt, where the Work is a musical
    work, performance or phonogram, the synchronization of the Work in
    timed-relation with a moving image ("synching") will be considered an
    Adaptation for the purpose of this License.
 b. "Collection" means a collection of literary or artistic works, such as
    encyclopedias and anthologies, or performances, phonograms or
    broadcasts, or other works or subject matter other than works listed
    in Section 1(f) below, which, by reason of the selection and
    arrangement of their contents, constitute intellectual creations, in
    which the Work is included in its entirety in unmodified form along
    with one or more other contributions, each constituting separate and
    independent works in themselves, which together are assembled into a
    collective whole. A work that constitutes a Collection will not be
    considered an Adaptation (as defined below) for the purposes of this
    License.
 c. "Creative Commons Compatible License" means a license that is listed
    at https://creativecommons.org/compatiblelicenses that has been
    approved by Creative Commons as being essentially equivalent to this
    License, including, at a minimum, because that license: (i) contains
    terms that have the same purpose, meaning and effect as the License
    Elements of this License; and, (ii) explicitly permits the relicensing
    of adaptations of works made available under that license under this
    License or a Creative Commons jurisdiction license with the same
    License Elements as this License.
 d. "Distribute" means to make available to the public the original and
    copies of the Work or Adaptation, as appropriate, through sale or
    other transfer of ownership.
 e. "License Elements" means the following high-level license attributes
    as selected by Licensor and indicated in the title of this License:
    Attribution, ShareAlike.
 f. "Licensor" means the individual, individuals, entity or entities that
    offer(s) the Work under the terms of this License.
 g. "Original Author" means, in the case of a literary or artistic work,
    the individual, individuals, entity or entities who created the Work
    or if no individual or entity can be identified, the publisher; and in
    addition (i) in the case of a performance the actors, singers,
    musicians, dancers, and other persons who act, sing, deliver, declaim,
    play in, interpret or otherwise perform literary or artistic works or
    expressions of folklore; (ii) in the case of a phonogram the producer
    being the person or legal entity who first fixes the sounds of a
    performance or other sounds; and, (iii) in the case of broadcasts, the
    organization that transmits the broadcast.
 h. "Work" means the literary and/or artistic work offered under the terms
    of this License including without limitation any production in the
    literary, scientific and artistic domain, whatever may be the mode or
    form of its expression including digital form, such as a book,
    pamphlet and other writing; a lecture, address, sermon or other work
    of the same nature; a dramatic or dramatico-musical work; a
    choreographic work or entertainment in dumb show; a musical
    composition with or without words; a cinematographic work to which are
    assimilated works expressed by a process analogous to cinematography;
    a work of drawing, painting, architecture, sculpture, engraving or
    lithography; a photographic work to which are assimilated works
    expressed by a process analogous to photography; a work of applied
    art; an illustration, map, plan, sketch or three-dimensional work
    relative to geography, topography, architecture or science; a
    performance; a broadcast; a phonogram; a compilation of data to the
    extent it is protected as a copyrightable work; or a work performed by
    a variety or circus performer to the extent it is not otherwise
    considered a literary or artistic work.
 i. "You" means an individual or entity exercising rights under this
    License who has not previously violated the terms of this License with
    respect to the Work, or who has received express permission from the
    Licensor to exercise rights under this License despite a previous
    violation.
 j. "Publicly Perform" means to perform public recitations of the Work and
    to communicate to the public those public recitations, by any means or
    process, including by wire or wireless means or public digital
    performances; to make available to the public Works in such a way that
    members of the public may access these Works from a place and at a
    place individually chosen by them; to perform the Work to the public
    by any means or process and the communication to the public of the
    performances of the Work, including by public digital performance; to
    broadcast and rebroadcast the Work by any means including signs,
    sounds or images.
 k. "Reproduce" means to make copies of the Work by any means including
    without limitation by sound or visual recordings and the right of
    fixation and reproducing fixations of the Work, including storage of a
    protected performance or phonogram in digital form or other electronic
    medium.

2. Fair Dealing Rights. Nothing in this License is intended to reduce,
limit, or restrict any uses free from copyright or rights arising from
limitations or exceptions that are provided for in connection with the
copyright protection under copyright law or other applicable laws.

3. License Grant. Subject to the terms and conditions of this License,
Licensor hereby grants You a worldwide, royalty-free, non-exclusive,
perpetual (for the duration of the applicable copyright) license to
exercise the rights in the Work as stated below:

 a. to Reproduce the Work, to incorporate the Work into one or more
    Collections, and to Reproduce the Work as incorporated in the
    Collections;
 b. to create and Reproduce Adaptations provided that any such Adaptation,
    including any translation in any medium, takes reasonable steps to
    clearly label, demarcate or otherwise identify that changes were made
    to the original Work. For example, a translation could be marked "The
    original work was translated from English to Spanish," or a
    modification could indicate "The original work has been modified.";
 c. to Distribute and Publicly Perform the Work including as incorporated
    in Collections; and,
 d. to Distribute and Publicly Perform Adaptations.
 e. For the avoidance of doubt:

     i. Non-waivable Compulsory License Schemes. In those jurisdictions in
        which the right to collect royalties through any statutory or
        compulsory licensing scheme cannot be waived, the Licensor
        reserves the exclusive right to collect such royalties for any
        exercise by You of the rights granted under this License;
    ii. Waivable Compulsory License Schemes. In those jurisdictions in
        which the right to collect royalties through any statutory or
        compulsory licensing scheme can be waived, the Licensor waives the
        exclusive right to collect such royalties for any exercise by You
        of the rights granted under this License; and,
   iii. Voluntary License Schemes. The Licensor waives the right to
        collect royalties, whether individually or, in the event that the
        Licensor is a member of a collecting society that administers
        voluntary licensing schemes, via that society, from any exercise
        by You of the rights granted under this License.

The above rights may be exercised in all media and formats whether now
known or hereafter devised. The above rights include the right to make
such modifications as are technically necessary to exercise the rights in
other media and formats. Subject to Section 8(f), all rights not expressly
granted by Licensor are hereby reserved.

4. Restrictions. The license granted in Section 3 above is expressly made
subject to and limited by the following restrictions:

 a. You may Distribute or Publicly Perform the Work only under the terms
    of this License. You must include a copy of, or the Uniform Resource
    Identifier (URI) for, this License with every copy of the Work You
    Distribute or Publicly Perform. You may not offer or impose any terms
    on the Work that restrict the terms of this License or the ability of
    the recipient of the Work to exercise the rights granted to that
    recipient under the terms of the License. You may not sublicense the
    Work. You must keep intact all notices that refer to this License and
    to the disclaimer of warranties with every copy of the Work You
    Distribute or Publicly Perform. When You Distribute or Publicly
    Perform the Work, You may not impose any effective technological
    measures on the Work that restrict the ability of a recipient of the
    Work from You to exercise the rights granted to that recipient under
    the terms of the License. This Section 4(a) applies to the Work as
    incorporated in a Collection, but this does not require the Collection
    apart from the Work itself to be made subject to the terms of this
    License. If You create a Collection, upon notice from any Licensor You
    must, to the extent practicable, remove from the Collection any credit
    as required by Section 4(c), as requested. If You create an
    Adaptation, upon notice from any Licensor You must, to the extent
    practicable, remove from the Adaptation any credit as required by
    Section 4(c), as requested.
 b. You may Distribute or Publicly Perform an Adaptation only under the
    terms of: (i) this License; (ii) a later version of this License with
    the same License Elements as this License; (iii) a Creative Commons
    jurisdiction license (either this or a later license version) that
    contains the same License Elements as this License (e.g.,
    Attribution-ShareAlike 3.0 US)); (iv) a Creative Commons Compatible
    License. If you license the Adaptation under one of the licenses
    mentioned in (iv), you must comply with the terms of that license. If
    you license the Adaptation under the terms of any of the licenses
    mentioned in (i), (ii) or (iii) (the "Applicable License"), you must
    comply with the terms of the Applicable License generally and the
    following provisions: (I) You must include a copy of, or the URI for,
    the Applicable License with every copy of each Adaptation You
    Distribute or Publicly Perform; (II) You may not offer or impose any
    terms on the Adaptation that restrict the terms of the Applicable
    License or the ability of the recipient of the Adaptation to exercise
    the rights granted to that recipient under the terms of the Applicable
    License; (III) You must keep intact all notices that refer to the
    Applicable License and to the disclaimer of warranties with every copy
    of the Work as included in the Adaptation You Distribute or Publicly
    Perform; (IV) when You Distribute or Publicly Perform the Adaptation,
    You may not impose any effective technological measures on the
    Adaptation that restrict the ability of a recipient of the Adaptation
    from You to exercise the rights granted to that recipient under the
    terms of the Applicable License. This Section 4(b) applies to the
    Adaptation as incorporated in a Collection, but this does not require
    the Collection apart from the Adaptation itself to be made subject to
    the terms of the Applicable License.
 c. If You Distribute, or Publicly Perform the Work or any Adaptations or
    Collections, You must, unless a request has been made pursuant to
    Section 4(a), keep intact all copyright notices for the Work and
    provide, reasonable to the medium or means You are utilizing: (i) the
    name of the Original Author (or pseudonym, if applicable) if supplied,
    and/or if the Original Author and/or Licensor designate another party
    or parties (e.g., a sponsor institute, publishing entity, journal) for
    attribution ("Attribution Parties") in Licensor's copyright notice,
    terms of service or by other reasonable means, the name of such party
    or parties; (ii) the title of the Work if supplied; (iii) to the
    extent reasonably practicable, the URI, if any, that Licensor
    specifies to be associated with the Work, unless such URI does not
    refer to the copyright notice or licensing information for the Work;
    and (iv) , consistent with Ssection 3(b), in the case of an
    Adaptation, a credit identifying the use of the Work in the Adaptation
    (e.g., "French translation of the Work by Original Author," or
    "Screenplay based on original Work by Original Author"). The credit
    required by this Section 4(c) may be implemented in any reasonable
    manner; provided, however, that in the case of a Adaptation or
    Collection, at a minimum such credit will appear, if a credit for all
    contributing authors of the Adaptation or Collection appears, then as
    part of these credits and in a manner at least as prominent as the
    credits for the other contributing authors. For the avoidance of
    doubt, You may only use the credit required by this Section for the
    purpose of attribution in the manner set out above and, by exercising
    Your rights under this License, You may not implicitly or explicitly
    assert or imply any connection with, sponsorship or endorsement by the
    Original Author, Licensor and/or Attribution Parties, as appropriate,
    of You or Your use of the Work, without the separate, express prior
    written permission of the Original Author, Licensor and/or Attribution
    Parties.
 d. Except as otherwise agreed in writing by the Licensor or as may be
    otherwise permitted by applicable law, if You Reproduce, Distribute or
    Publicly Perform the Work either by itself or as part of any
    Adaptations or Collections, You must not distort, mutilate, modify or
    take other derogatory action in relation to the Work which would be
    prejudicial to the Original Author's honor or reputation. Licensor
    agrees that in those jurisdictions (e.g. Japan), in which any exercise
    of the right granted in Section 3(b) of this License (the right to
    make Adaptations) would be deemed to be a distortion, mutilation,
    modification or other derogatory action prejudicial to the Original
    Author's honor and reputation, the Licensor will waive or not assert,
    as appropriate, this Section, to the fullest extent permitted by the
    applicable national law, to enable You to reasonably exercise Your
    right under Section 3(b) of this License (right to make Adaptations)
    but not otherwise.

5. Representations, Warranties and Disclaimer

UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING, LICENSOR
OFFERS THE WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY
KIND CONCERNING THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE,
INCLUDING, WITHOUT LIMITATION, WARRANTIES OF TITLE, MERCHANTIBILITY,
FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF
LATENT OR OTHER DEFECTS, ACCURACY, OR THE PRESENCE OF ABSENCE OF ERRORS,
WHETHER OR NOT DISCOVERABLE. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION
OF IMPLIED WARRANTIES, SO SUCH EXCLUSION MAY NOT APPLY TO YOU.

6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE
LAW, IN NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR
ANY SPECIAL, INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES
ARISING OUT OF THIS LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS
BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

7. Termination

 a. This License and the rights granted hereunder will terminate
    automatically upon any breach by You of the terms of this License.
    Individuals or entities who have received Adaptations or Collections
    from You under this License, however, will not have their licenses
    terminated provided such individuals or entities remain in full
    compliance with those licenses. Sections 1, 2, 5, 6, 7, and 8 will
    survive any termination of this License.
 b. Subject to the above terms and conditions, the license granted here is
    perpetual (for the duration of the applicable copyright in the Work).
    Notwithstanding the above, Licensor reserves the right to release the
    Work under different license terms or to stop distributing the Work at
    any time; provided, however that any such election will not serve to
    withdraw this License (or any other license that has been, or is
    required to be, granted under the terms of this License), and this
    License will continue in full force and effect unless terminated as
    stated above.

8. Miscellaneous

 a. Each time You Distribute or Publicly Perform the Work or a Collection,
    the Licensor offers to the recipient a license to the Work on the same
    terms and conditions as the license granted to You under this License.
 b. Each time You Distribute or Publicly Perform an Adaptation, Licensor
    offers to the recipient a license to the original Work on the same
    terms and conditions as the license granted to You under this License.
 c. If any provision of this License is invalid or unenforceable under
    applicable law, it shall not affect the validity or enforceability of
    the remainder of the terms of this License, and without further action
    by the parties to this agreement, such provision shall be reformed to
    the minimum extent necessary to make such provision valid and
    enforceable.
 d. No term or provision of this License shall be deemed waived and no
    breach consented to unless such waiver or consent shall be in writing
    and signed by the party to be charged with such waiver or consent.
 e. This License constitutes the entire agreement between the parties with
    respect to the Work licensed here. There are no understandings,
    agreements or representations with respect to the Work not specified
    here. Licensor shall not be bound by any additional provisions that
    may appear in any communication from You. This License may not be
    modified without the mutual written agreement of the Licensor and You.
 f. The rights granted under, and the subject matter referenced, in this
    License were drafted utilizing the terminology of the Berne Convention
    for the Protection of Literary and Artistic Works (as amended on
    September 28, 1979), the Rome Convention of 1961, the WIPO Copyright
    Treaty of 1996, the WIPO Performances and Phonograms Treaty of 1996
    and the Universal Copyright Convention (as revised on July 24, 1971).
    These rights and subject matter take effect in the relevant
    jurisdiction in which the License terms are sought to be enforced
    according to the corresponding provisions of the implementation of
    those treaty provisions in the applicable national law. If the
    standard suite of rights granted under applicable copyright law
    includes additional rights not granted under this License, such
    additional rights are deemed to be included in the License; this
    License is not intended to restrict the license of any rights under
    applicable law.


Creative Commons Notice

    Creative Commons is not a party to this License, and makes no warranty
    whatsoever in connection with the Work. Creative Commons will not be
    liable to You or any party on any legal theory for any damages
    whatsoever, including without limitation any general, special,
    incidental or consequential damages arising in connection to this
    license. Notwithstanding the foregoing two (2) sentences, if Creative
    Commons has expressly identified itself as the Licensor hereunder, it
    shall have all rights and obligations of Licensor.

    Except for the limited purpose of indicating to the public that the
    Work is licensed under the CCPL, Creative Commons does not authorize
    the use by either party of the trademark "Creative Commons" or any
    related trademark or logo of Creative Commons without the prior
    written consent of Creative Commons. Any permitted use will be in
    compliance with Creative Commons' then-current trademark usage
    guidelines, as may be published on its website or otherwise made
    available upon request from time to time. For the avoidance of doubt,
    this trademark restriction does not form part of the License.

    Creative Commons may be contacted at https://creativecommons.org/.
git clone --depth 1 https://github.com/pypa/packaging.python.org.git . 0sgit fetch origin --force --prune --prune-tags --depth 50 refs/heads/main:refs/remotes/origin/main 0sgit checkout --force origin/main 0scat .readthedocs.yaml 0sasdf global python 3.11.12 0spython -mvirtualenv $READTHEDOCS_VIRTUALENV_PATH 0spython -m pip install --upgrade --no-cache-dir pip setuptools 4spython -m pip install --upgrade --no-cache-dir sphinx 4spython -m pip install --exists-action=w --no-cache-dir -r requirements.txt 6spython -m sphinx -T -b dirhtml -d _build/doctrees -D language=en . $READTHEDOCS_OUTPUT/html 9spip install llm-github-copilotllm install llm-github-copilotgit clone https://github.com/yourusername/llm-github-copilot.git
cd llm-github-copilotbrew install worktrunk && wt config shell installpowershell -ExecutionPolicy Bypass -c "irm https://github.com/max-sixty/worktrunk/releases/download/v0.29.0/worktrunk-installer.ps1 | iex"; git-wt config shell installcurl --proto '=https' --tlsv1.2 -LsSf https://github.com/max-sixty/worktrunk/releases/download/v0.29.0/worktrunk-installer.sh | sh && wt config shell install
=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
    wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public:
    wiki.creativecommons.org/Considerations_for_licensees

=======================================================================

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
International Public License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International Public
License ("Public License"). To the extent this Public License may be
interpreted as a contract, You are granted the Licensed Rights in
consideration of Your acceptance of these terms and conditions, and the
Licensor grants You such rights in consideration of benefits the
Licensor receives from making the Licensed Material available under
these terms and conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.

  c. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  d. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  e. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  f. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  g. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  h. NonCommercial means not primarily intended for or directed towards
     commercial advantage or monetary compensation. For purposes of
     this Public License, the exchange of the Licensed Material for
     other material subject to Copyright and Similar Rights by digital
     file-sharing or similar means is NonCommercial provided there is
     no payment of monetary compensation in connection with the
     exchange.

  i. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  j. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  k. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part, for NonCommercial purposes only; and

            b. produce and reproduce, but not Share, Adapted Material
               for NonCommercial purposes only.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties, including when
          the Licensed Material is used other than for NonCommercial
          purposes.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material, You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

          For the avoidance of doubt, You do not have permission under
          this Public License to Share Adapted Material.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.

       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database for NonCommercial purposes
     only and provided You do not Share Adapted Material;

  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material; and

  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.

  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, THE LICENSOR OFFERS THE LICENSED MATERIAL AS-IS
     AND AS-AVAILABLE, AND MAKES NO REPRESENTATIONS OR WARRANTIES OF
     ANY KIND CONCERNING THE LICENSED MATERIAL, WHETHER EXPRESS,
     IMPLIED, STATUTORY, OR OTHER. THIS INCLUDES, WITHOUT LIMITATION,
     WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR
     PURPOSE, NON-INFRINGEMENT, ABSENCE OF LATENT OR OTHER DEFECTS,
     ACCURACY, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT
     KNOWN OR DISCOVERABLE. WHERE DISCLAIMERS OF WARRANTIES ARE NOT
     ALLOWED IN FULL OR IN PART, THIS DISCLAIMER MAY NOT APPLY TO YOU.

  b. TO THE EXTENT POSSIBLE, IN NO EVENT WILL THE LICENSOR BE LIABLE
     TO YOU ON ANY LEGAL THEORY (INCLUDING, WITHOUT LIMITATION,
     NEGLIGENCE) OR OTHERWISE FOR ANY DIRECT, SPECIAL, INDIRECT,
     INCIDENTAL, CONSEQUENTIAL, PUNITIVE, EXEMPLARY, OR OTHER LOSSES,
     COSTS, EXPENSES, OR DAMAGES ARISING OUT OF THIS PUBLIC LICENSE OR
     USE OF THE LICENSED MATERIAL, EVEN IF THE LICENSOR HAS BEEN
     ADVISED OF THE POSSIBILITY OF SUCH LOSSES, COSTS, EXPENSES, OR
     DAMAGES. WHERE A LIMITATION OF LIABILITY IS NOT ALLOWED IN FULL OR
     IN PART, THIS LIMITATION MAY NOT APPLY TO YOU.

  c. The disclaimer of warranties and limitation of liability provided
     above shall be interpreted in a manner that, to the extent
     possible, most closely approximates an absolute disclaimer and
     waiver of all liability.


Section 6 -- Term and Termination.

  a. This Public License applies for the term of the Copyright and
     Similar Rights licensed here. However, if You fail to comply with
     this Public License, then Your rights under this Public License
     terminate automatically.

  b. Where Your right to use the Licensed Material has terminated under
     Section 6(a), it reinstates:

       1. automatically as of the date the violation is cured, provided
          it is cured within 30 days of Your discovery of the
          violation; or

       2. upon express reinstatement by the Licensor.

     For the avoidance of doubt, this Section 6(b) does not affect any
     right the Licensor may have to seek remedies for Your violations
     of this Public License.

  c. For the avoidance of doubt, the Licensor may also offer the
     Licensed Material under separate terms or conditions or stop
     distributing the Licensed Material at any time; however, doing so
     will not terminate this Public License.

  d. Sections 1, 5, 6, 7, and 8 survive termination of this Public
     License.


Section 7 -- Other Terms and Conditions.

  a. The Licensor shall not be bound by any additional or different
     terms or conditions communicated by You unless expressly agreed.

  b. Any arrangements, understandings, or agreements regarding the
     Licensed Material not stated herein are separate from and
     independent of the terms and conditions of this Public License.


Section 8 -- Interpretation.

  a. For the avoidance of doubt, this Public License does not, and
     shall not be interpreted to, reduce, limit, restrict, or impose
     conditions on any use of the Licensed Material that could lawfully
     be made without permission under this Public License.

  b. To the extent possible, if any provision of this Public License is
     deemed unenforceable, it shall be automatically reformed to the
     minimum extent necessary to make it enforceable. If the provision
     cannot be reformed, it shall be severed from this Public License
     without affecting the enforceability of the remaining terms and
     conditions.

  c. No term or condition of this Public License will be waived and no
     failure to comply consented to unless expressly agreed to by the
     Licensor.

  d. Nothing in this Public License constitutes or may be interpreted
     as a limitation upon, or waiver of, any privileges and immunities
     that apply to the Licensor or You, including from the legal
     processes of any jurisdiction or authority.

=======================================================================

Creative Commons is not a party to its public
licenses. Notwithstanding, Creative Commons may elect to apply one of
its public licenses to material it publishes and in those instances
will be considered the “Licensor.” The text of the Creative Commons
public licenses is dedicated to the public domain under the CC0 Public
Domain Dedication. Except for the limited purpose of indicating that
material is shared under a Creative Commons public license or as
otherwise permitted by the Creative Commons policies published at
creativecommons.org/policies, Creative Commons does not authorize the
use of the trademark "Creative Commons" or any other trademark or logo
of Creative Commons without its prior written consent including,
without limitation, in connection with any unauthorized modifications
to any of its public licenses or any other arrangements,
understandings, or agreements concerning use of licensed material. For
the avoidance of doubt, this paragraph does not form part of the
public licenses.

Creative Commons may be contacted at creativecommons.org.


.. [3] Beginning with Python 3.4, ``venv`` (a stdlib alternative to
       :ref:`virtualenv`) will create virtualenv environments with ``pip``
       pre-installed, thereby making it an equal alternative to
       :ref:`virtualenv`.

.. [4] The compatible release specifier was accepted in :pep:`440`
       and support was released in :ref:`setuptools` v8.0 and
       :ref:`pip` v6.0
