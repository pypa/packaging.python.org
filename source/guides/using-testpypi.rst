.. _using-test-pypi:

==============
Using TestPyPI
==============

``TestPyPI`` is a separate instance of the :term:`Python Package Index (PyPI)`
that allows you to try out the distribution tools and process without worrying
about affecting the real index. TestPyPI is hosted at
`test.pypi.org <https://test.pypi.org>`_

Registering your account
------------------------

Because TestPyPI has a separate database from the live PyPI, you'll need a
separate user account specifically for TestPyPI. Go to
https://test.pypi.org/account/register/ to register your account.

.. note:: The database for TestPyPI may be periodically pruned, so it is not
    unusual for user accounts to be deleted.


Using TestPyPI with Twine
-------------------------

You can upload your distributions to TestPyPI using :ref:`twine` by specifying
the ``--repository`` flag:

.. code-block:: bash

    twine upload --repository testpypi dist/*

You can see if your package has successfully uploaded by navigating to the URL
``https://test.pypi.org/project/<sampleproject>`` where ``sampleproject`` is
the name of your project that you uploaded. It may take a minute or two for
your project to appear on the site.

Using TestPyPI with pip
-----------------------

You can use :ref:`pip` to install a wheel that you uploaded to TestPyPI:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps --only-binary=:all: your-package

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --index-url https://test.pypi.org/simple/ --no-deps --only-binary=:all: your-package

The ``--index-url`` flag selects TestPyPI instead of PyPI. The ``--no-deps``
flag prevents installing runtime dependencies, while ``--only-binary=:all:``
requires a wheel, avoiding installation of build dependencies. If your package
has dependencies, install them separately from PyPI before running these commands.

.. warning::

    TestPyPI is a separate index, and packages there may be missing or unrelated
    to packages with the same name on PyPI. Installing dependencies from TestPyPI
    could install unintended or malicious packages. Avoid combining the two
    indexes with ``--extra-index-url``: pip does not prioritize one index over
    the other, so dependencies could still be downloaded from TestPyPI.

Setting up TestPyPI in :file:`.pypirc`
--------------------------------------

If you want to avoid being prompted for your username and password every time,
you can configure TestPyPI in your :file:`$HOME/.pypirc`:

.. code:: ini

    [testpypi]
    username = __token__
    password = <your TestPyPI API Token>

For more details, see the :ref:`specification <pypirc>` for :file:`.pypirc`.
