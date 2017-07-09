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
are using a new enough version of your upload tool. Tools that support PyPI.org
by default are twine v1.8.0+ (recommended tool), setuptools 27+, or the distutils
included with Python 3.4.6+, Python 3.5.3+, Python 3.6+, and 2.7.13+.

In addition to ensuring you're on a new enough version of the tool for the
tool's default to have switched, you must also make sure that you have not
configured the tool to override its default upload URL. Typically this is
configured in a file located at ``~/.pypirc``. If you see a file like:


.. code::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository:https://pypi.python.org/pypi
    username:yourusername
    password:yourpassword


Then simply delete the line starting with ``repository`` and you will use
your upload tool's default URL.

If for some reason you're unable to upgrade the version of your tool to a
version that defaults to using PyPI.org, then you may edit ``~/.pypirc`` and
include the ``repository:`` line, but use the value
``https://upload.pypi.org/legacy/`` instead::


.. code::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository:https://upload.pypi.org/legacy/
    username:yourusername
    password:yourpassword

If you use TestPyPI, you must update your ``~/.pypirc`` to handle
TestPyPI's new location, by replacing ``https://testpypi.python.org/pypi``
with ``https://test.pypi.org/legacy/``.


Registering package names & metadata
------------------------------------

Explicit pre-registration of package names with the `setup.py register`
command prior to the first upload is no longer required, and is not
currently supported by the legacy upload API emulation on `pypi.org`.

As a result, attempting explicit registration after switching to using
`pypi.org` for uploads will give the follow error message::

    Server response (410): This API is no longer supported, instead simply upload the file.

The solution is to skip the registration step, and proceed directly to
uploading artifacts.
