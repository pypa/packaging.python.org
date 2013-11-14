=====================
Quick Recommendations
=====================

:Page Status: Complete
:Last Reviewed: 2013-11-03

If you're familiar with Python packaging and installation, and just want to know
what toolset is currently recommended, then here it is.

If you're less familiar with Python packaging or installation, and would like
more details, then proceed to the  :doc:`packaging` and :doc:`installation`.

If you're interested in learning more about current areas of development,
see :doc:`future`.


Installation Tool Recommendations
=================================

* Use :ref:`pip` to install Python :term:`packages <Package (Meaning #2)>`
  from :term:`PyPI <Python Package Index (PyPI)>`. [1]_ [2]_

* Use :ref:`virtualenv` to isolate application specific dependencies from a
  shared Python installation. [3]_

* Use `pip wheel
  <http://www.pip-installer.org/en/latest/usage.html#pip-wheel>`_ to create a
  cache of :term:`wheel` distributions, for the purpose of speeding up
  subsequent installations. [4]_

* If you're looking for management of fully integrated cross-platform software
  stacks, consider :ref:`buildout` (primarily focused on the web development
  community) or :ref:`hashdist`, or :ref:`conda` (both primarily focused on
  the scientific community).


Packaging Tool Recommendations
==============================

* Use :ref:`setuptools` to package and publish Python :term:`packages <Package
  (Meaning #2)>` to :term:`PyPI <Python Package Index (PyPI)>`. [5]_ [6]_

* If your project includes binary extensions, use the ``bdist_wheel``
  :ref:`setuptools` extension available from the :ref:`wheel project
  <wheel>`, to create and publish :term:`wheel distributions <wheel>` for
  Windows and Mac OS X for your project on :term:`PyPI <Python Package Index
  (PyPI)>`. These wheel files should be compatible with the binary
  installers provided for download from python.org. [7]_

----

.. [1] If you need to install from the :term:`Egg` format (which pip doesn't
       support), you can use ``easy_install`` (from :ref:`setuptools`) or
       :ref:`buildout`.  :term:`Eggs <Egg>` are intended to be replaced by
       :term:`Wheels <Wheel>`, so they should become less common over time.

.. [2] The acceptance of :ref:`PEP453 <PEP453s>` means that :ref:`pip` will likely be
       available by default in most installations of Python 3.4 or later.

.. [3] The acceptance of :ref:`PEP453 <PEP453s>` means that users of Python 3.4 or later
       will likely be able to use the standard library's own ``pyvenv`` tool
       instead of :ref:`virtualenv`. However, using :ref:`virtualenv` will
       still be recommended for users that need cross-version consistency.

.. [4] For more information, see the pip guide to `Building and Installing
       Wheels
       <http://www.pip-installer.org/en/latest/cookbook.html#building-and-installing-wheels>`_.

.. [5] `distribute`_ (a fork of setuptools) was merged back into
       :ref:`setuptools` in June 2013, thereby making setuptools the default
       choice for packaging.

.. [6] When building from source (rather than installing from a :term:`wheel
       <Wheel>` file), :ref:`pip` ensures that packages that use the standard
       library's ``distutils`` module are built with :ref:`setuptools`
       instead.

.. [7] :ref:`pip` and the wheel format don't currently offer good tools for
       handling arbitrary external binary dependencies. Accordingly, PyPI
       currently only allows platform specific wheel distributions to be
       uploaded for Windows and Mac OS X. External binary dependencies are
       currently best handled by building custom wheel files with the correct
       dependencies, by using one of the fully integrated cross-platform
       software stack management systems mentioned in the installation tools
       section, or by using platform specific tools.

.. _distribute: https://pypi.python.org/pypi/distribute
