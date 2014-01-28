
.. _`Tool Recommendations`:

====================
Tool Recommendations
====================

:Page Status: Incomplete
:Last Reviewed: 2014-01-22

If you're familiar with Python packaging and installation, and just want to know
what tools are currently recommended, then here it is.

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

* Use :ref:`setuptools` to define projects and build distributions. [5]_ [6]_

* If your project includes binary extensions, use the ``bdist_wheel``
  :ref:`setuptools` extension available from the :ref:`wheel project
  <wheel>`, to create and publish :term:`wheel distributions <wheel>` for
  Windows and Mac OS X for your project on :term:`PyPI <Python Package Index
  (PyPI)>`. These wheel files should be compatible with the binary
  installers provided for download from python.org. [7]_

* Use `twine <https://pypi.python.org/pypi/twine>`_ for uploading distributions
  to :term:`PyPI <Python Package Index (PyPI)>`.


----

.. [1] There are some cases where you might choose to use ``easy_install`` (from
       :ref:`setuptools`), e.g. if you need to install from :term:`Eggs <Egg>`
       (which pip doesn't support).  For a detailed breakdown, see :ref:`pip vs
       easy_install`.

.. [2] The acceptance of :ref:`PEP453 <PEP453s>` means that :ref:`pip` will be
       available by default in most installations of Python 3.4 or later.  See
       the `rationale section
       <http://www.python.org/dev/peps/pep-0453/#rationale>`_ from :ref:`PEP453
       <PEP453s>` as for why pip was chosen.

.. [3] The acceptance of :ref:`PEP453 <PEP453s>` means that users of Python 3.4
       or later will likely be able to use the standard library's own ``pyvenv``
       tool instead of :ref:`virtualenv`. However, using :ref:`virtualenv` will
       still be recommended for users that need cross-version consistency.

.. [4] For more information, see the pip guide to `Building and Installing
       Wheels
       <http://www.pip-installer.org/en/latest/cookbook.html#building-and-installing-wheels>`_.

.. [5] `distribute`_ (a fork of setuptools) was merged back into
       :ref:`setuptools` in June 2013, thereby making setuptools the default
       choice for packaging.

.. [6] Although you can use pure ``distutils``, for most projects, that's
       insufficient, due it lacking support for defining dependencies. If do you
       use ``distutils``, realize that when :ref:`pip` installs your project
       source (rather than installing from a :term:`wheel <Wheel>` file), it
       will actually build your project using :ref:`setuptools` instead.

.. [7] :ref:`pip` and the wheel format don't currently offer good tools for
       handling arbitrary external binary dependencies. Accordingly, PyPI
       currently only allows platform specific wheel distributions to be
       uploaded for Windows and Mac OS X. External binary dependencies are
       currently best handled by building custom wheel files with the correct
       dependencies, by using one of the fully integrated cross-platform
       software stack management systems mentioned in the installation tools
       section, or by using platform specific tools.

.. _distribute: https://pypi.python.org/pypi/distribute
