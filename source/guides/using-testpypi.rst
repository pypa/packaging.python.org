.. _using-test-pypi:

==============
Using TestPyPI
==============

`TestPyPI` is a separate instance of the :term:`Python Package Index (PyPI)`
that allows you to try out the distribution tools and process without worrying
about affecting the real index. TestPyPI is hosted at
`test.pypi.org <https://test.pypi.org>`_

Registering your account
------------------------

Because TestPyPI has a separate database from the live PyPI, you'll need a
separate user account for specifically for TestPyPI. Go to
https://test.pypi.org/account/register/ to register your account.

.. Note:: The database for TestPyPI may be periodically pruned, so it is not
    unusual for user accounts to be deleted.


Using TestPyPI with Twine
-------------------------

You can upload your distributions to TestPyPI using :ref:`twine` by passing
in the ``--repository-url`` flag

.. code::

    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*

The ``legacy`` in the URL above refers to the legacy API for PyPI, which may
change as the Warehouse project progresses.

You can see if your package has successfully uploaded by navigating to the URL
``https://test.pypi.org/project/<sampleproject>`` where ``sampleproject`` is
the name of your project that you uploaded. It may take a minute or two for
your project to appear on the site.

Using TestPyPI with pip
-----------------------

You can tell pip to download packages from TestPyPI instead of PyPI by
specifying the ``--index-url`` flag

.. code::

    $ pip install --index-url https://test.pypi.org/simple/ your-package

If you want to allow pip to also pull other packages from PyPI you can
specify ``--extra-index-url`` to point to PyPI. This is useful when the package
you're testing has dependencies:

.. code::

    pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple your-package

Setting up TestPyPI in pypirc
-----------------------------

If you want to avoid entering the TestPyPI url and your username
you can configure TestPyPI in your ``$HOME/.pypirc``.

Create or modify ``$HOME/.pypirc`` with the following:

.. code::

    [distutils]
    index-servers=
        pypi
        testpypi

    [testpypi]
    repository: https://test.pypi.org/legacy/
    username: your testpypi username


.. Warning:: Do not store passwords in the pypirc file.
    Storing passwords in plain text is never a good idea.

You can then tell :ref:`twine` to upload to TestPyPI by specifying the
``--repository`` flag:

.. code::

    $ twine upload --repository testpypi dist/*
