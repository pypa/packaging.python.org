
.. _pypirc:

========================
The :file:`.pypirc` file
========================

A :file:`.pypirc` file allows you to define the configuration for :term:`package
indexes <Package Index>` (referred to here as "repositories"), so that you don't
have to enter the URL, username, or password whenever you upload a package with
:ref:`twine` or :ref:`flit`.

The format (originally defined by the :ref:`distutils` package) is:

.. code-block:: ini

    [distutils]
    index-servers =
        first-repository
        second-repository

    [first-repository]
    repository = <first-repository URL>
    username = <first-repository username>
    password = <first-repository password>

    [second-repository]
    repository = <second-repository URL>
    username = <second-repository username>
    password = <second-repository password>

The ``distutils`` section defines an ``index-servers`` field that lists the
name of all sections describing a repository.

Each section describing a repository defines three fields:

- ``repository``: The URL of the repository.
- ``username``: The registered username on the repository.
- ``password``: The password that will used to authenticate the username.

.. warning::

    Be aware that this stores your password in plain text. For better security,
    consider an alternative like `keyring`_, setting environment variables, or
    providing the password on the command line.

    Otherwise, set the permissions on :file:`.pypirc` so that only you can view
    or modify it. For example, on Linux or macOS, run:

    .. code-block:: bash

        chmod 600 ~/.pypirc

.. _keyring: https://pypi.org/project/keyring/

Common configurations
=====================

.. note::

    These examples apply to :ref:`twine`, and projects like :ref:`hatch` that
    use it under the hood. Other projects (e.g. :ref:`flit`) also use
    :file:`.pypirc`, but with different defaults. Please refer to each project's
    documentation for more details and usage instructions.

Twine's default configuration mimics a :file:`.pypirc` with repository sections
for PyPI and TestPyPI:

.. code-block:: ini

    [distutils]
    index-servers =
        pypi
        testpypi

    [pypi]
    repository = https://upload.pypi.org/legacy/

    [testpypi]
    repository = https://test.pypi.org/legacy/

Twine will add additional configuration from :file:`$HOME/.pypirc`, the command
line, and environment variables to this default configuration.

Using a PyPI token
------------------

To set your `API token`_ for PyPI, you can create a :file:`$HOME/.pypirc`
similar to:

.. code-block:: ini

    [pypi]
    username = __token__
    password = <PyPI token>

For :ref:`TestPyPI <using-test-pypi>`, add a ``[testpypi]`` section, using the
API token from your TestPyPI account.

.. _API token: https://pypi.org/help/#apitoken

Using another package index
---------------------------

To configure an additional repository, you'll need to redefine the
``index-servers`` field to include the repository name. Here is a complete
example of a :file:`$HOME/.pypirc` for PyPI, TestPyPI, and a private repository:

.. code-block:: ini

    [distutils]
    index-servers =
        pypi
        testpypi
        private-repository

    [pypi]
    username = __token__
    password = <PyPI token>

    [testpypi]
    username = __token__
    password = <TestPyPI token>

    [private-repository]
    repository = <private-repository URL>
    username = <private-repository username>
    password = <private-repository password>

.. warning::

    Instead of using the ``password`` field, consider saving your API tokens
    and passwords securely using `keyring`_ (which is installed by Twine):

    .. code-block:: bash

        keyring set https://upload.pypi.org/legacy/ __token__
        keyring set https://test.pypi.org/legacy/ __token__
        keyring set <private-repository URL> <private-repository username>
