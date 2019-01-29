Installing stand alone command line tools
=========================================

Many packages have command line entry points. Examples of this type of application are
`mypy <https://github.com/python/mypy>`_,
`flake8 <https://github.com/PyCQA/flake8>`_,
`pipenv <https://github.com/pypa/pipenv>`_,and
`black <https://github.com/ambv/black>`_.

Usually you want to be able to access these from anywhere,
but installing packages and their dependencies to the same global environment
can cause version conflicts and break dependencies the operating system has
on Python packages.

``pipx-app`` solves this by creating a virtual environment for
each package. It then makes the entry points globally accessible by adding them
to your $PATH. This allows each package to be upgraded or uninstalled without
causing conflicts with other packages, and allows you to safely run the program
from anywhere.

.. Note:: ``pipx`` only works with Python 3.6+.

``pipx`` is installed with ``pipx-bootstrap``:

::

  $ pip install --user pipx-bootstrap
  $ pipx-bootstrap
  $ pip uninstall pipx-bootstrap

.. Note:: You may need to restart your terminal for the path updates to take effect.

Now you can install packages and access their entry points from anywhere.

::

  $ pipx install PACKAGE
  $ ENTRYPOINT_OF_PACKAGE

To upgrade or uninstall

::

  $ pipx upgrade PACKAGE
  $ pipx uninstall PACKAGE

``pipx`` can modify itself too. To upgrade or uninstall ``pipx``

::

  $ pipx upgrade pipx-app
  $ pipx uninstall pipx-app

``pipx`` also allows you to install and run the latest version of a cli tool
in a temporary, ephemeral environment.

::

  $ pipx run PACKAGE [ARGS]

To see the full list of commands ``pipx`` offers, run

::

  $ pipx --help

You can learn more about ``pipx`` at its homepage, https://github.com/cs01/pipx.
