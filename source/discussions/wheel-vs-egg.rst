.. _`Wheel vs Egg`:

============
Wheel vs Egg
============

:term:`Wheel` and :term:`Egg` are both packaging formats that aim to support the
use case of needing an install artifact that doesn't require building or
compilation, which can be costly in testing and production workflows.

The :term:`Egg` format was introduced by :ref:`setuptools` in 2004, whereas the
:term:`Wheel` format was introduced by :pep:`427` in 2012.

:term:`Wheel` is currently considered the standard for :term:`built <Built
Distribution>` and :term:`binary <Binary Distribution>` packaging for Python.

Here's a breakdown of the important differences between :term:`Wheel` and :term:`Egg`.


* :term:`Wheel` has an :pep:`official PEP <427>`. :term:`Egg` did not.

* :term:`Wheel` is a :term:`distribution <Distribution Package>` format, i.e a packaging
  format. [1]_ :term:`Egg` was both a distribution format and a runtime
  installation format (if left zipped), and was designed to be importable.

* :term:`Wheel` archives do not include .pyc files. Therefore, when the
  distribution only contains Python files (i.e. no compiled extensions), and is
  compatible with Python 2 and 3, it's possible for a wheel to be "universal",
  similar to an :term:`sdist <Source Distribution (or "sdist")>`.

* :term:`Wheel` uses :pep:`PEP376-compliant <376>` ``.dist-info``
  directories. Egg used ``.egg-info``.

* :term:`Wheel` has a :pep:`richer file naming convention <425>`. A single
  wheel archive can indicate its compatibility with a number of Python language
  versions and implementations, ABIs, and system architectures.

* :term:`Wheel` is versioned. Every wheel file contains the version of the wheel
  specification and the implementation that packaged it.

* :term:`Wheel` is internally organized by `sysconfig path type
  <http://docs.python.org/2/library/sysconfig.html#installation-paths>`_,
  therefore making it easier to convert to other formats.

----

.. [1] Circumstantially, in some cases, wheels can be used as an importable
       runtime format, although :pep:`this is not officially supported at this time
       <427#is-it-possible-to-import-python-code-directly-from-a-wheel-file>`.
