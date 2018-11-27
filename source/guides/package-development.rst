===================
Package Development
===================

This guide documents the most common workflows that are available for
developing a Python package and how to structure the project.

There are 4 basic cases: the package can be at the root level of in the `src`
directory (``src`` / ``non-src``) and the tests can be part of the package itself
or separate (tests ``included`` / ``separate``):

* tests ``included``, ``non-src``
* tests ``separate``, ``non-src``
* tests ``included``, ``src``
* tests ``separate``, ``src``

We now examine each of these 4 cases and describe the possible workflows of
each and the pros/cons.

``non-src``
===========

tests ``included``
------------------

An example package in this cathegory is SymPy.

Prepare (once)
~~~~~~~~~~~~~~

::

    git clone https://github.com/sympy/sympy
    conda create -y -n sympy python=3.7 mpmath pytest

Develop (every day)
~~~~~~~~~~~~~~~~~~~

Start:

    cd sympy
    conda activate sympy

Workflow:

1. Modify some files, say, in the ``sympy/polys`` directory
2. Test these particular changes:

        pytest sympy/polys/tests/test_solvers.py

Repeat 1. and 2. The ``sympy`` environment only has the dependencies, it
doesn't get modified and doesn't have the ``sympy`` package.

Pros / Cons
~~~~~~~~~~~

Pros:

* One can import the package directly without extra tooling or configuration
  (e.g., no need to modify `PYTHONPATH` or to install and pollute some
  environment)
* One can still install the package to test it if one wants to
* Distributing the tests with the package allows easy testing of installed
  package by ``import sympy; sympy.test()``.

Cons:

* By installing the package and running ``pytest``, one will run the local
  version of ``sympy``. One has to go to a different directory and do either
  ``import sympy; sympy.test()`` or ``pytest --pyargs sympy`` to run tests of
  the installed package.


tests ``separate``
------------------

An example package in this cathegory is Flit, others are
https://github.com/bokeh/bokeh/ and https://github.com/plotly/dash.

Prepare (once)
~~~~~~~~~~~~~~

::

    git clone https://github.com/takluyver/flit
    conda create -y -n flit python=3.7 pytest requests requests_download testpath responses docutils pytoml pytest-cov

Develop (every day)
~~~~~~~~~~~~~~~~~~~

Start:

    cd flit
    conda activate flit

Workflow:

1. Modify some files, say, the ``flit/upload.py`` file
2. Test these particular changes:

        pytest tests/test_upload.py

Repeat 1. and 2. The ``flit`` environment only has the dependencies, it
doesn't get modified and doesn't have the ``flit`` package.

Pros / Cons
~~~~~~~~~~~

Pros:

* One can import the package locally, no need to install and pollute some
  environment

Cons:

* By installing the package and running ``pytest``, one will run the local
  version of ``flit``. One has to remove the ``flit`` directory with ``rm -r
  flit`` to test the installed version.

``src``
=======

tests ``included``
------------------

An example package in this category is Matplotlib.

Prepare (once)
~~~~~~~~~~~~~~

::

    git clone https://github.com/matplotlib/matplotlib
    conda create -y -n mpl python=3.7 pytest numpy cycler kiwisolver pyparsing python-dateutil six cython
    cd matplotlib
    conda activate mpl
    pip install -e .

Develop (every day)
~~~~~~~~~~~~~~~~~~~

Start::

    cd matplotlib
    conda activate mpl

Workflow:

1. Modify some files, say, the ``lib/matplotlib/colorbar.py`` file
2. Test these particular changes:

        pytest lib/matplotlib/tests/test_colorbar.py

Repeat 1. and 2. The ``mpl`` environment has both the dependencies and the
``matplotlib`` package in the development mode.

tests ``separate``
------------------

An example package in this cathegory is Flake8.

Prepare (once)
~~~~~~~~~~~~~~

::

    git clone https://gitlab.com/pycqa/flake8
    conda create -y -n flake8 python=3.7 pytest pyflakes pycodestyle mccabe
    cd flake8
    conda activate flake8
    pip install -e .

Develop (every day)
~~~~~~~~~~~~~~~~~~~

Start::

    cd flake8
    conda activate flake8

Workflow:

1. Modify some files, say, the ``src/flake8/statistics.py`` file
2. Test these particular changes:

        pytest tests/unit/test_statistics.py

Repeat 1. and 2. The ``flake8`` environment has both the dependencies and the
``flake8`` package in the development mode.

Pros / Cons
~~~~~~~~~~~

Pros:

* Unlike the tests ``non-src`` case (both ``separate`` and ``included``), one
  cannot accidentally run tests with the local package instead of the
  installed one in an environment

Cons:

* One cannot import the package without installing it into an environment using
  `pip install -e .` (one can do it by setting ``PYTHONPATH`` which is not as
  simple as importing the package directly). That means that one will have an
  environment with a development version of the package, causing possible
  issues down the road when the environment is used for another purpose.

Notes
=====

* It would be nice if ``pytest`` added an option to ignore the local package,
  so that one does not have to do the ugly ``rm -r flit`` hack for ``separate``
  / ``non-src``. See this `comment
  <https://github.com/pypa/python-packaging-user-guide/issues/320#issuecomment-426429307>`_
  for more details.
