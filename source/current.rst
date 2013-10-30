
=====================
Quick Recommendations
=====================

:Page Status: Complete
:Last Reviewed: 10-29-2013

If you're familiar with Python packaging and installation, and just want to know
what toolset is currently recommended, then here it is:

* Use :ref:`pip` to install Python packages from :term:`PyPI
  <Python Package Index (PyPI)>`. [1]_

* Use :ref:`setuptools` to package and publish Python :term:`distributions <Distribution>` (or
  "packages") to the :term:`PyPI <Python Package Index (PyPI)>`. [2]_

* Use :ref:`virtualenv` to isolate application specific dependencies from the
  system Python installation.

* Use the ``bdist_wheel`` :ref:`setuptools` extension available from the :ref:`wheel
  project <wheel>`, to create :term:`wheel distributions <wheel>` for your
  project.

* Use `pip wheel
  <http://www.pip-installer.org/en/latest/usage.html#pip-wheel>`_ to create a
  cache of :term:`wheel` distributions, for the purpose of speeding up
  installation. [3]_

* If you're looking for fully intregrated software stacks, consider
  :ref:`buildout` (primarily focused on the web development community) or
  :ref:`hashdist`, or :ref:`conda` (primarily focused on the scientific
  community).


If you're not so familiar with Python packaging or installation, then proceed to
the  :doc:`packaging` and :doc:`installation`.

If you want to learn about what's coming later, see :doc:`future`.


.. [1] If you need to install from the :term:`Egg` format (which pip doesn't
       support), you can use ``easy_install`` (from :ref:`setuptools`) or
       :ref:`buildout`.  :term:`Eggs <Egg>` are intended to be replaced by
       :term:`Wheels <Wheel>`, so they should become less common over time.

.. [2] :ref:`distribute` (a fork of setuptools) was merged back into setuptools
       in June 2013, thereby making setuptools the primary choice for packaging.

.. [3] For more information, see the pip guide to `Building and Installing Wheels
       <http://www.pip-installer.org/en/latest/cookbook.html#building-and-installing-wheels>`_.

