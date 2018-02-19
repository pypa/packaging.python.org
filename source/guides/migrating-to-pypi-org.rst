.. _`Migrating to PyPI.org`:

Migrating to PyPI.org
=====================

:term:`PyPI.org` is a new, rewritten version of PyPI that is replacing the
legacy code base located at `pypi.python.org`. As it becomes the default, and
eventually only, version of PyPI people are expected to interact with, there
will be a transition period where tooling and processes are expected to need to
update to deal with the new location.

This section covers how to migrate to the new PyPI.org for different tasks.


Publishing releases
-------------------

``pypi.org`` became the default upload platform in September 2016.

Uploads through ``pypi.python.org`` were *switched off* on **July 3, 2017**.

The recommended way to migrate to PyPI.org for uploading is to ensure that you
are using a new enough version of your upload tool.

The default upload settings switched to ``pypi.org`` in the following versions:

* ``twine`` 1.8.0
* ``setuptools`` 27.0.0
* Python 2.7.13 (``distutils`` update)
* Python 3.4.6 (``distutils`` update)
* Python 3.5.3 (``distutils`` update)
* Python 3.6.0 (``distutils`` update)

In addition to ensuring you're on a new enough version of the tool for the
tool's default to have switched, you must also make sure that you have not
configured the tool to override its default upload URL. Typically this is
configured in a file located at ``$HOME/.pypirc``. If you see a file like:

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

If for some reason you're unable to upgrade the version of your tool
to a version that defaults to using PyPI.org, then you may edit
``$HOME/.pypirc`` and include the ``repository:`` line, but use the
value ``https://upload.pypi.org/legacy/`` instead:

.. code::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository: https://upload.pypi.org/legacy/
    username: your username
    password: your password

(``legacy`` in this URL refers to the fact that this is the new server
implementation's emulation of the legacy server implementation's upload API)


Registering package names & metadata
------------------------------------

Explicit pre-registration of package names with the ``setup.py register``
command prior to the first upload is no longer required, and is not
currently supported by the legacy upload API emulation on PyPI.org.

As a result, attempting explicit registration after switching to using
PyPI.org for uploads will give the following error message::

    Server response (410): This API is no longer supported, instead simply upload the file.

The solution is to skip the registration step, and proceed directly to
uploading artifacts.


Using TestPyPI
--------------

If you use TestPyPI, you must update your ``$HOME/.pypirc`` to handle
TestPyPI's new location, by replacing ``https://testpypi.python.org/pypi``
with ``https://test.pypi.org/legacy/``, for example:

.. code::

    [distutils]
    index-servers=
        pypi
        testpypi

    [testpypi]
    repository: https://test.pypi.org/legacy/
    username: your testpypi username
    password: your testpypi password


Registering new user accounts
-----------------------------

In order to help mitigate spam attacks against PyPI, new user registration
through ``pypi.python.org`` was *switched off* on **February 20, 2018**.


Browsing packages
-----------------

``pypi.python.org`` is currently still the default interface for browsing packages
(used in links from other PyPA documentation, etc).

``pypi.org`` is fully functional for purposes of browsing available packages, and
some users may choose to opt in to using it.

``pypi.org`` is expected to become the default recommended interface for browsing
once the limitations in the next two sections are addressed (at which point
attempts to access ``pypi.python.org`` will automatically be redirected to
``pypi.org``).


Downloading packages
--------------------

``pypi.python.org`` is currently still the default host for downloading packages.

``pypi.org`` is fully functional for purposes of downloading packages, and some users
may choose to opt in to using it, but its current hosting setup isn't capable of
handling the full bandwidth requirements of being the default download source (even
after accounting for the Fastly CDN).

``pypi.org`` is expected to become the default host for downloading packages once
it has been redeployed into an environment capable of handling the associated
network load.


Managing published packages and releases
----------------------------------------

``pypi.python.org`` provides an interface for logged in users to manage their
published packages and releases.

``pypi.org`` does not currently provide such an interface.

The missing capabilities are being tracked as part of the
`Shut Down Legacy PyPI <https://github.com/pypa/warehouse/milestone/7>`_
milestone.
