.. _`Tool Recommendations`:

====================
Tool recommendations
====================

If you're familiar with Python packaging and installation, and just want to know
what tools are currently recommended, then here it is.


Installation Tool Recommendations
=================================

* Use :ref:`pip` to install Python :term:`packages <Distribution Package>` from
  :term:`PyPI <Python Package Index (PyPI)>`. [1]_ [2]_ Depending on how :ref:`pip`
  is installed, you may need to also install :ref:`wheel` to get the benefit
  of wheel caching. [3]_

* Use :ref:`virtualenv`, or `venv`_ to isolate application specific
  dependencies from a shared Python installation. [4]_

* If you're looking for management of fully integrated cross-platform software
  stacks, consider:

  * :ref:`buildout`: primarily focused on the web development community

  * :ref:`spack`, :ref:`hashdist`, or :ref:`conda`: primarily focused
    on the scientific community.



Packaging Tool Recommendations
==============================

* Use :ref:`setuptools` to define projects and create :term:`Source Distributions
  <Source Distribution (or "sdist")>`. [5]_ [6]_

* Use the ``bdist_wheel`` :ref:`setuptools` extension available from the
  :ref:`wheel project <wheel>` to create :term:`wheels <Wheel>`.  This is
  especially beneficial, if your project contains binary extensions. [7]_

* Use `twine <https://pypi.python.org/pypi/twine>`_ for uploading distributions
  to :term:`PyPI <Python Package Index (PyPI)>`.


Publishing Platform Migration
=============================

The original Python Package Index implementation (hosted at
`pypi.python.org <https://pypi.python.org>`_) is being phased out in favour
of an updated implementation hosted at `pypi.org <https://pypi.org>`_. Both
interfaces share a common database backend and file store, allowing the latter
to assume more default responsibilities as it becomes more capable.

Users consistently using the latest versions of the recommended tools above
with their default settings don't need to worry about this migration, but
users running older versions, or not using the default settings, will need
to update their configurations in line with the recommendations below.


Publishing releases
-------------------

``pypi.org`` became the default upload platform in September 2016

Uploads through ``pypi.python.org`` will be *switched off* on **July 3, 2017**

The default upload settings switched to ``pypi.org`` in the following versions:

* ``twine`` 1.8.0
* ``setuptools`` 27.0.0
* Python 3.4.6 (``distutils`` update)
* Python 3.5.3 (``distutils`` update)
* Python 3.6.0 (``distutils`` update)


Browsing packages
-----------------

``pypi.python.org`` is currently still the default interface for browsing packages
(used in links from other PyPA documentation, etc)

``pypi.org`` is fully functional for purposes of browsing available packages, and
some users may choose to opt in to using it

``pypi.org`` is expected to become the default recommended interface for browsing
once the limitations in the next two sections are addressed (at which point
attempts to access ``pypi.python.org`` will automatically be redirected to
``pypi.org``)


Downloading packages
--------------------

``pypi.python.org`` is currently still the default host for downloading packages

``pypi.org`` is fully functional for purposes of downloading packages, and some users
may choose to opt in to using it, but its current hosting setup isn't capable of
handling the full bandwidth requirements of being the default download source (even
after accounting for the Fastly CDN)

``pypi.org`` is expected to become the default host for downloading packages once
it has been redeployed into an environment capable of handling the associated
network load


Managing published packages and releases
----------------------------------------

``pypi.python.org`` provides an interface for logged in users to manage their
published packages and releases

``pypi.org`` does not currently provide such an interface

The missing capabilities are being tracked as part of the
`Shut Down Legacy PyPI <https://github.com/pypa/warehouse/milestone/7>`_
milestone

----

.. [1] There are some cases where you might choose to use ``easy_install`` (from
       :ref:`setuptools`), e.g. if you need to install from :term:`Eggs <Egg>`
       (which pip doesn't support).  For a detailed breakdown, see :ref:`pip vs
       easy_install`.

.. [2] The acceptance of :pep:`453` means that :ref:`pip`
       will be available by default in most installations of Python 3.4 or
       later.  See the :pep:`rationale section <453#rationale>` from :pep:`453`
       as for why pip was chosen.

.. [3] :ref:`get-pip.py <pip:get-pip>` and :ref:`virtualenv` install
       :ref:`wheel`, whereas :ref:`ensurepip` and :ref:`venv <venv>` do not
       currently.  Also, the common "python-pip" package that's found in various
       linux distros, does not depend on "python-wheel" currently.

.. [4] Beginning with Python 3.4, ``venv`` will create virtualenv environments
       with ``pip`` installed, thereby making it an equal alternative to
       :ref:`virtualenv`. However, using :ref:`virtualenv` will still be
       recommended for users that need cross-version consistency.

.. [5] Although you can use pure ``distutils`` for many projects, it does not
       support defining dependencies on other projects and is missing several
       convenience utilities for automatically populating distribution metadata
       correctly that are provided by ``setuptools``. Being outside the
       standard library, ``setuptools`` also offers a more consistent feature
       set across different versions of Python, and (unlike ``distutils``),
       ``setuptools`` will be updated to produce the upcoming "Metadata 2.0"
       standard formats on all supported versions.

       Even for projects that do choose to use ``distutils``, when :ref:`pip`
       installs such projects directly from source (rather than installing
       from a prebuilt :term:`wheel <Wheel>` file), it will actually build
       your project using :ref:`setuptools` instead.

.. [6] `distribute`_ (a fork of setuptools) was merged back into
       :ref:`setuptools` in June 2013, thereby making setuptools the default
       choice for packaging.

.. [7] :term:`PyPI <Python Package Index (PyPI)>` currently only allows
       uploading Windows and Mac OS X wheels, and they should be compatible with
       the binary installers provided for download from python.org. Enhancements
       will have to be made to the :pep:`wheel compatibility tagging scheme
       <425>` before linux wheels will be allowed.

.. _distribute: https://pypi.python.org/pypi/distribute
.. _venv: https://docs.python.org/3/library/venv.html
