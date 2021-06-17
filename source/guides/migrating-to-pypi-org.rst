.. _`Migrating to PyPI.org`:

Migrating to PyPI.org
=====================

:term:`pypi.org` is the new, rewritten version of PyPI that has replaced the
legacy PyPI code base. It is the default version of PyPI that people are
expected to use. These are the tools and processes that people will need to
interact with ``PyPI.org``.

Publishing releases
-------------------

``pypi.org`` is the default upload platform as of September 2016.

Uploads through ``pypi.python.org`` were *switched off* on **July 3, 2017**.
As of April 13th, 2018, ``pypi.org`` is the URL for PyPI.

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
configured in a file located at :file:`$HOME/.pypirc`. If you see a file like:

.. code::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository = https://pypi.python.org/pypi
    username = <your PyPI username>
    password = <your PyPI username>


Then simply delete the line starting with ``repository`` and you will use
your upload tool's default URL.

If for some reason you're unable to upgrade the version of your tool
to a version that defaults to using PyPI.org, then you may edit
:file:`$HOME/.pypirc` and include the ``repository:`` line, but use the
value ``https://upload.pypi.org/legacy/`` instead:

.. code::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository = https://upload.pypi.org/legacy/
    username = <your PyPI username>
    password = <your PyPI password>

(``legacy`` in this URL refers to the fact that this is the new server
implementation's emulation of the legacy server implementation's upload API.)

For more details, see the :ref:`specification <pypirc>` for :file:`.pypirc`.

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

Legacy TestPyPI (testpypi.python.org) is no longer available; use
`test.pypi.org <https://test.pypi.org>`_ instead. If you use TestPyPI,
you must update your :file:`$HOME/.pypirc` to handle TestPyPI's new
location, by replacing ``https://testpypi.python.org/pypi`` with
``https://test.pypi.org/legacy/``, for example:

.. code::

    [distutils]
    index-servers=
        pypi
        testpypi

    [testpypi]
    repository = https://test.pypi.org/legacy/
    username = <your TestPyPI username>
    password = <your TestPyPI password>

For more details, see the :ref:`specification <pypirc>` for :file:`.pypirc`.


Registering new user accounts
-----------------------------

In order to help mitigate spam attacks against PyPI, new user registration
through ``pypi.python.org`` was *switched off* on **February 20, 2018**.
New user registrations at ``pypi.org`` are open.


Browsing packages
-----------------

While ``pypi.python.org`` is may still be used in links from other PyPA
documentation, etc, the default interface for browsing packages is
``pypi.org``. The domain pypi.python.org now redirects to pypi.org,
and may be disabled sometime in the future.


Downloading packages
--------------------

``pypi.org`` is the default host for downloading packages.

Managing published packages and releases
----------------------------------------

``pypi.org`` provides a fully functional interface for logged in users to
manage their published packages and releases.
