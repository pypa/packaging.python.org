Installing stand alone command line tools
=========================================

Many packages provide command line applications. Examples of such packages are
`mypy <https://github.com/python/mypy>`_,
`flake8 <https://github.com/PyCQA/flake8>`_,
`black <https://github.com/psf/black>`_, and
:ref:`pipenv`.

Usually you want to be able to access these applications from anywhere on your
system, but installing packages and their dependencies to the same global
environment can cause version conflicts and break dependencies the operating
system has on Python packages.

:ref:`pipx` solves this by creating a virtual environment for each package,
while also ensuring that its applications are accessible through a directory
that is on your ``$PATH``. This allows each package to be upgraded or
uninstalled without causing conflicts with other packages, and allows you to
safely run the applications from anywhere.

.. note:: pipx only works with Python 3.6+.

pipx is installed with pip:

.. tab:: Unix/macOS

  .. code-block:: bash

      python3 -m pip install --user pipx
      python3 -m pipx ensurepath

.. tab:: Windows

  .. code-block:: bat

      py -m pip install --user pipx
      py -m pipx ensurepath

.. note::

   ``ensurepath`` ensures that the application directory is on your ``$PATH``.
   You may need to restart your terminal for this update to take effect.

Now you can install packages with ``pipx install`` and run the package's
applications(s) from anywhere.

.. code-block:: console

  $ pipx install PACKAGE
  $ PACKAGE_APPLICATION [ARGS]

For example:

.. code-block:: console

  $ pipx install cowsay
    installed package cowsay 2.0, Python 3.6.2+
    These binaries are now globally available
      - cowsay
  done! ✨ 🌟 ✨
  $ cowsay moo
    ___
  < moo >
    ===
          \
           \
             ^__^
             (oo)\_______
             (__)\       )\/
                 ||     ||
                 ||----w |


To see a list of packages installed with pipx and which applications are
available, use ``pipx list``:

.. code-block:: console

  $ pipx list
  venvs are in /Users/user/.local/pipx/venvs
  symlinks to binaries are in /Users/user/.local/bin
     package black 18.9b0, Python 3.6.2+
      - black
      - blackd
     package cowsay 2.0, Python 3.6.2+
      - cowsay
     package mypy 0.660, Python 3.6.2+
      - dmypy
      - mypy
      - stubgen
     package nox 2018.10.17, Python 3.6.2+
      - nox
      - tox-to-nox

To upgrade or uninstall a package:

.. code-block:: bash

  pipx upgrade PACKAGE
  pipx uninstall PACKAGE

pipx can be upgraded or uninstalled with pip:

.. tab:: Unix/macOS

  .. code-block:: bash

      python3 -m pip install --upgrade pipx
      python3 -m pip uninstall pipx

.. tab:: Windows

  .. code-block:: bat

      py -m pip install --upgrade pipx
      py -m pip uninstall pipx

pipx also allows you to install and run the latest version of an application
in a temporary, ephemeral environment. For example:

.. code-block:: bash

  pipx run cowsay moooo

To see the full list of commands pipx offers, run:

.. code-block:: bash

  pipx --help

You can learn more about pipx at https://pipx.pypa.io/.
