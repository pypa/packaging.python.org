
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

  * Python 2: ``sudo yum install python-pip python-wheel``
  * Python 3: ``sudo yum install python3 python3-wheel``

* Fedora 22:

  * Python 2: ``sudo dnf install python-pip python-wheel``
  * Python 3: ``sudo dnf install python3 python3-wheel``


To get newer versions of pip, setuptools, and wheel, you can enable the
`PyPA Copr Repo <https://copr.fedoraproject.org/coprs/pypa/pypa/>`_ using the
`Copr Repo instructions <https://fedorahosted.org/copr/wiki/HowToEnableRepo>`__.


CentOS/RHEL
~~~~~~~~~~~

CentOS and RHEL don't offer :ref:`pip` or :ref:`wheel` in their core repositories,
although :ref:`setuptools` is installed by default.

There's three options available to fill in :ref:`pip` and :ref:`wheel`, and to
upgrade :ref:`setuptools`:

1. Use the "Sofware Collections" feature to enable a collection that includes
   pip, setuptools, and wheel.

   * For Redhat, see here:
     http://developers.redhat.com/products/softwarecollections/overview/
   * For CentOS, see here: https://www.softwarecollections.org/en/

   Although this has promise to be the preferred method in the future, as it is,
   you can't count on finding a collection that has recent versions.

2. You can install pip from the `EPEL repository
   <https://fedoraproject.org/wiki/EPEL>`_. Enable EPEL using `these
   instructions
   <https://fedoraproject.org/wiki/EPEL#How_can_I_use_these_extra_packages.3F>`__,
   and install like so::

     sudo yum install python-pip

   Although EPEL tends to maintain a pretty recent version of :ref:`pip`, it
   does not maintain :ref:`setuptools` or :ref:`wheel`, so you'd have to settle
   for the distro version of setuptools, and use pip itself to install
   wheel.

3. You can enable the `PyPA Copr Repo
   <https://copr.fedoraproject.org/coprs/pypa/pypa/>`_ using `these instructions
   <https://fedorahosted.org/copr/wiki/HowToEnableRepo>`__ [1]_, and run::

     sudo yum install python-pip python-setuptools python-wheel


Also, note that if you're using the `IUS repository
<https://iuscommunity.org/pages/Repos.html>`_ to install alternative Python
versions, IUS also maintains corresponding versions versions of pip, setuptools,
and wheel that are usually up to date.


Debian/Ubuntu
~~~~~~~~~~~~~

::

  sudo apt-get install python-pip

Replace "python" with "python3" for Python 3.


.. warning::

   Recent Debian/Ubuntu versions have modified pip to use the `"User Scheme"
   <https://pip.pypa.io/en/stable/user_guide/#user-installs>`_ by default, which
   is a significant behavior change that can be surprising to some users.


----

.. [1] Currently, there is no "copr" yum plugin available for CentOS/RHEL, so
       the only option is to manually place the repo files as described.
