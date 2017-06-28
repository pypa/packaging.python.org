.. _`Migrating to PyPI.org`:

Migrating to PyPI.org
=====================

PyPI.org is a new, rewritten version of PyPI that is replacing the legacy code
base located at pypi.python.org. As it becomes the default, and eventually only,
version of PyPI people are expected to interact with, there will be a transition
period where tooling and processes are expected to need to update to deal with
the new location.

This section covers how to migrate to the new PyPI.org for different tasks.


Uploading
---------

The recommended way to migrate to PyPI.org for uploading is to ensure that you
are using a new enough version of the upload tools. That would be twine v1.8.0+
(recommneded tool), Python 3.4.6+, Python 3.5.3+, Python 3.6+, 2.7.13+, or
setuptools 27+.

In addition to ensuring you're on a new enough version of the tool for the
tool's default to have switched. You must also make sure that you have not
configured the tool to override it' default value. Typically this is configured
in a file located at ``~/.pypirc``. If you see a file like:


.. code::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository:https://pypi.python.org/pypi
    username:yourusername
    password:yourpassword


Then simply delete the line starting with ``repository`` and you will utilize
the default version of your upload tool.

If for some reason you're unable to upgrade the version of your tool to a
version that defaults to using PyPI.org, then you may edit ``~/.pypirc`` and
include the ``repository:`` line, but use the value
``https://upload.pypi.org/legacy/`` instead.

In addition to regular PyPI, you must also update your ``~/.pypirc`` to handle
TestPyPI if you're using it. For that you must edit your ``~/.pypirc`` to
replace ``https://testpypi.python.org/pypi`` with
``https://test.pypi.org/legacy/``.
