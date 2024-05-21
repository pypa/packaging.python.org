.. _`Installing pip/setuptools/wheel with Linux Package Managers`:

===========================================================
Installing pip/setuptools/wheel with Linux Package Managers
===========================================================

:Page Status: Incomplete
:Last Reviewed: 2021-07-26

This section covers how to install :ref:`pip`, :ref:`setuptools`, and
:ref:`wheel` using Linux package managers.

If you're using a Python that was downloaded from `python.org
<https://www.python.org>`_, then this section does not apply.  See the
:ref:`installing_requirements` section instead.

Note that it's common for the versions of :ref:`pip`, :ref:`setuptools`, and
:ref:`wheel` supported by a specific Linux Distribution to be outdated by the
time it's released to the public, and updates generally only occur for security
reasons, not for feature updates.  For certain Distributions, there are
additional repositories that can be enabled to provide newer versions.  The
repositories we know about are explained below.

Also note that it's somewhat common for Distributions to apply patches for the
sake of security and normalization to their own standards.  In some cases, this
can lead to bugs or unexpected behaviors that vary from the original unpatched
versions.  When this is known, we will make note of it below.


Fedora
~~~~~~

.. code-block:: bash

  sudo dnf install python3-pip python3-wheel

To learn more about Python in Fedora, please visit the `official Fedora docs`_,
`Python Classroom`_ or `Fedora Loves Python`_.

.. _official Fedora docs: https://developer.fedoraproject.org/tech/languages/python/python-installation.html
.. _Python Classroom: https://labs.fedoraproject.org/en/python-classroom/
.. _Fedora Loves Python: https://fedoralovespython.org

CentOS/RHEL
~~~~~~~~~~~

CentOS and RHEL don't offer :ref:`pip` or :ref:`wheel` in their core repositories,
although :ref:`setuptools` is installed by default.

To install pip and wheel for the system Python, there are two options:

1. Enable the `EPEL repository <https://fedoraproject.org/wiki/EPEL>`_ using
   `these instructions
   <https://docs.fedoraproject.org/en-US/epel/#how_can_i_use_these_extra_packages>`__.
   On EPEL 7, you can install pip and wheel like so:

   .. code-block:: bash

     sudo dnf install python3-pip python3-wheel

   Since EPEL only offers extra, non-conflicting packages, EPEL does not offer
   setuptools, since it's in the core repository.


2. Enable the `PyPA Copr Repo
   <https://copr.fedorainfracloud.org/coprs/pypa/pypa/>`_ using `these instructions
   <https://fedoraproject.org/wiki/Infrastructure/Fedorahosted-retirement>`__ [1]_. You can install
   pip and wheel like so:

   .. code-block:: bash

     sudo dnf install python3-pip python3-wheel

   To additionally upgrade setuptools, run:

   .. code-block:: bash

     sudo dnf upgrade python3-setuptools


To install pip, wheel, and setuptools, in a parallel, non-system environment
(using yum) then there are two options:


1. Use the "Software Collections" feature to enable a parallel collection that
   includes pip, setuptools, and wheel.

   * For Redhat, see here:
     https://developers.redhat.com/products/softwarecollections/overview
   * For CentOS, see here: https://github.com/sclorg

   Be aware that collections may not contain the most recent versions.

2. Enable the `IUS repository <https://ius.io/setup>`_ and
   install one of the `parallel-installable
   <https://ius.io/usage#parallel-installable-packages>`_
   Pythons, along with pip, setuptools, and wheel, which are kept fairly up to
   date.

   For example, for Python 3.4 on CentOS7/RHEL7:

   .. code-block:: bash

     sudo yum install python34u python34u-wheel


openSUSE
~~~~~~~~

.. code-block:: bash

   sudo zypper install python3-pip python3-setuptools python3-wheel


.. _debian-ubuntu:

Debian/Ubuntu and derivatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Firstly, update and refresh repository lists by running this command:

.. code-block:: bash

  sudo apt update
  sudo apt install python3-venv python3-pip

.. warning::

   Recent Debian/Ubuntu versions have modified pip to use the `"User Scheme"
   <https://pip.pypa.io/en/stable/user_guide/#user-installs>`_ by default, which
   is a significant behavior change that can be surprising to some users.


Arch Linux
~~~~~~~~~~

.. code-block:: bash

   sudo pacman -S python-pip

----

.. [1] Currently, there is no "copr" yum plugin available for CentOS/RHEL, so
       the only option is to manually place the repo files as described.
