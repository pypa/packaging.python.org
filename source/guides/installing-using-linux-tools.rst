.. _`Installing pip/setuptools/wheel with Linux Package Managers`:

===========================================================
Installing pip/setuptools/wheel with Linux Package Managers
===========================================================

:Page Status: Incomplete
:Last Reviewed: 2015-09-17


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

* Fedora 21:

  * Python 2::

      sudo yum upgrade python-setuptools
      sudo yum install python-pip python-wheel

  * Python 3: ``sudo yum install python3 python3-wheel``

* Fedora 22:

  * Python 2::

      sudo dnf upgrade python-setuptools
      sudo dnf install python-pip python-wheel

  * Python 3: ``sudo dnf install python3 python3-wheel``


To get newer versions of pip, setuptools, and wheel for Python 2, you can enable
the `PyPA Copr Repo <https://copr.fedoraproject.org/coprs/pypa/pypa/>`_ using
the `Copr Repo instructions
<https://fedorahosted.org/copr/wiki/HowToEnableRepo>`__, and then run::

  sudo yum|dnf upgrade python-setuptools
  sudo yum|dnf install python-pip python-wheel


CentOS/RHEL
~~~~~~~~~~~

CentOS and RHEL don't offer :ref:`pip` or :ref:`wheel` in their core repositories,
although :ref:`setuptools` is installed by default.

To install pip and wheel for the system Python, there are two options:

1. Enable the `EPEL repository <https://fedoraproject.org/wiki/EPEL>`_ using
   `these instructions
   <https://fedoraproject.org/wiki/EPEL#How_can_I_use_these_extra_packages.3F>`__. On
   EPEL 6 and EPEL7, you can install pip like so::

     sudo yum install python-pip

   On EPEL 7 (but not EPEL 6), you can install wheel like so::

     sudo yum install python-wheel

   Since EPEL only offers extra, non-conflicting packages, EPEL does not offer
   setuptools, since it's in the core repository.


2. Enable the `PyPA Copr Repo
   <https://copr.fedoraproject.org/coprs/pypa/pypa/>`_ using `these instructions
   <https://fedorahosted.org/copr/wiki/HowToEnableRepo>`__ [1]_. You can install
   pip and wheel like so::

     sudo yum install python-pip python-wheel

   To additionally upgrade setuptools, run::

     sudo yum upgrade python-setuptools


To install pip, wheel, and setuptools, in a parallel, non-system environment
(using yum) then there are two options:


1. Use the "Software Collections" feature to enable a parallel collection that
   includes pip, setuptools, and wheel.

   * For Redhat, see here:
     http://developers.redhat.com/products/softwarecollections/overview/
   * For CentOS, see here: https://www.softwarecollections.org/en/

   Be aware that collections may not contain the most recent versions.

2. Enable the `IUS repository <https://ius.io/GettingStarted/>`_ and
   install one of the `parallel-installable
   <https://ius.io/SafeRepo/#parallel-installable-package>`_
   Pythons, along with pip, setuptools, and wheel, which are kept fairly up to
   date.

   For example, for Python 3.4 on CentOS7/RHEL7::

     sudo yum install python34u python34u-wheel


openSUSE
~~~~~~~~

* Python 2::

    sudo zypper install python-pip python-setuptools python-wheel


* Python 3::
 
    sudo zypper install python3-pip python3-setuptools python3-wheel


Debian/Ubuntu
~~~~~~~~~~~~~


* Python 2::

    sudo apt install python-pip


* Python 3::

    sudo apt install python3-venv python3-pip


.. warning::

   Recent Debian/Ubuntu versions have modified pip to use the `"User Scheme"
   <https://pip.pypa.io/en/stable/user_guide/#user-installs>`_ by default, which
   is a significant behavior change that can be surprising to some users.


Arch Linux
~~~~~~~~~~

* Python 2::

    sudo pacman -S python2-pip

* Python 3::

    sudo pacman -S python-pip

----

.. [1] Currently, there is no "copr" yum plugin available for CentOS/RHEL, so
       the only option is to manually place the repo files as described.
