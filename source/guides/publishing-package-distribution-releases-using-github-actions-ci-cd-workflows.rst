Publishing package distribution releases using GitHub Actions CI/CD workflows
=============================================================================

`GitHub Actions CI/CD`_ allow you to run a series of commands
whenever an event occurs on the GitHub platform. One
popular choice is having a workflow that's triggered by a
``push`` event.
This guide shows you how to publish a Python distribution
package whenever a tagged commit is pushed.

.. attention::

   This guide *assumes* that you already have a project that
   you know how to build dists for and *it lives on GitHub*.

.. warning::

   At the time of writing, `GitHub Actions CI/CD`_
   is in public beta. If you don't have it enabled,
   you should join the waitlist to gain access.

   GitHub Actions will be generally available on November 13th, 2019.


Saving credentials on GitHub
----------------------------

In this guide, we'll demonstrate uploading to both production
PyPI and Test PyPI meaning that we'll have two separate sets
of creds. And we'll need to save them in the GitHub repo settings.

Let's begin! 🚀

1. Go to https://pypi.org/manage/account/#api-tokens and
   create a new `API token`_. If you have the project on PyPI
   already, limit the token scope to just that project.
   You can call it something like
   ``GitHub Actions CI/CD — project-org/project-repo``
   in order for it to be easily distinguishable in the token
   list.
   **Don't close the page just yet — you won't see that token
   again.**
2. In a separate browser tab or window, go to the ``Settings``
   tab of your target repository and then click on `Secrets`_
   in the left sidebar.
3. Create a new secret called ``pypi_password`` and copy-paste
   the token from the fist step.
4. Now, go to https://test.pypi.org/manage/account/#api-tokens
   and repeat the steps. Save that Test PyPI token on GitHub
   as ``test_pypi_password``.


Creating a workflow definition
------------------------------

GitHub CI/CD workflows are declared in YAML files stored under
``.github/workflows/`` of your repository.

Start it with a meaningful name and define the event that
should make GitHub run this workflow:

.. code-block:: yaml

   name: Publish Python 🐍 distribution package 📦 to PyPIs

   on: push


Defining a workflow job environment
-----------------------------------

Now, let's add initial setup for our job. It's a process that
will execute commands that we'll define later.
In this guide, we'll choose to use Ubuntu 18.04:

.. code-block:: yaml

   build-n-publish:
     name: Build and publish Python 🐛 dist 📦 to PyPIs
     runs-on: ubuntu-18.04


Checking out the project and building dists
-------------------------------------------

Then, add the following under the ``build-n-publish`` section:

.. code-block:: yaml

     steps:
     - uses: actions/checkout@master
     - name: Set up Python 3.7
       uses: actions/setup-python@v1
       with:
         version: 3.7

This will download your repository into the CI runner and then
install and activate Python 3.7.

And now we can build dists from source. In this example, we'll
use ``pep517`` package, *assuming that your project has a ``pyproject.toml`` properly set up (see :pep:`517`/:pep:`518`)*.

.. tip::

   You can use any other method for building dists as long as
   it produces ready-to-upload artifacts saved into the ``dist/``
   folder.

So add this to the steps list:

.. code-block:: yaml

     - name: Install pep517
       run: >-
         python -m
         pip install
         pep517
         --user
     - name: Build a binary wheel and a source tarball
       run: >-
         python -m
         pep517.build
         --source
         --binary
         --out-dir dist/
         .


Publishing dist to Test PyPI and production PyPI
------------------------------------------------

Finally, add the following steps at the end:

.. code-block:: yaml

     - name: Publish 📦 to Test PyPI
       uses: pypa/gh-action-pypi-publish@master
       with:
         password: ${{ secrets.test_pypi_password }}
         repository_url: https://test.pypi.org/legacy/
     - name: Publish 📦 to production PyPI
       if: startsWith(github.event.ref, 'refs/tags')
       uses: pypa/gh-action-pypi-publish@master
       with:
         password: ${{ secrets.pypi_password }}

These two steps use the `pypa/gh-action-pypi-publish`_ GitHub
Action: the first one uploads contents of the ``dist/`` folder
into Test PyPI unconditionally and the second does that to
production PyPI but only if the current commit is tagged.


That's all, folks!
------------------

Now, whenever you push a tagged commit to your Git repo remote
on GitHub, this workflow will publish it to PyPI.
And it'll publish any push to Test PyPI which is useful for
providing test builds to your alpha users as well as making
sure that your release pipeline remains healthy! 


.. _API token: https://pypi.org/help/#apitoken
.. _GitHub Actions CI/CD: https://github.com/features/actions
.. _pypa/gh-action-pypi-publish:
.. _Secrets:
   https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables
