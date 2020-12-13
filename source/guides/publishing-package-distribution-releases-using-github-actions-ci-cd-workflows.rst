=============================================================================
Publishing package distribution releases using GitHub Actions CI/CD workflows
=============================================================================

`GitHub Actions CI/CD`_ allows you to run a series of commands
whenever an event occurs on the GitHub platform. One
popular choice is having a workflow that's triggered by a
``push`` event.
This guide shows you how to publish a Python distribution
whenever a tagged commit is pushed.
It will use the `pypa/gh-action-pypi-publish GitHub Action`_.

.. attention::

   This guide *assumes* that you already have a project that
   you know how to build distributions for and *it lives on GitHub*.

Saving credentials on GitHub
============================

In this guide, we'll demonstrate uploading to both
PyPI and TestPyPI, meaning that we'll have two separate sets
of credentials. And we'll need to save them in the GitHub repository
settings.

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
3. Create a new secret called ``PYPI_API_TOKEN`` and copy-paste
   the token from the first step.
4. Now, go to https://test.pypi.org/manage/account/#api-tokens
   and repeat the steps. Save that TestPyPI token on GitHub
   as ``TEST_PYPI_API_TOKEN``.

   .. attention::

      If you don't have a TestPyPI account, you'll need to
      create it. It's not the same as a regular PyPI account.


Creating a workflow definition
==============================

GitHub CI/CD workflows are declared in YAML files stored in the
``.github/workflows/`` directory of your repository.

Let's create a ``.github/workflows/publish-to-test-pypi.yml``
file.

Start it with a meaningful name and define the event that
should make GitHub run this workflow:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :end-before: jobs:


Defining a workflow job environment
===================================

Now, let's add initial setup for our job. It's a process that
will execute commands that we'll define later.
In this guide, we'll use Ubuntu 18.04:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: on:
   :end-before: steps:


Checking out the project and building distributions
===================================================

Then, add the following under the ``build-n-publish`` section:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: runs-on:
   :end-before: Install pypa/build

This will download your repository into the CI runner and then
install and activate Python 3.7.

And now we can build dists from source. In this example, we'll
use ``build`` package, assuming that your project has a
``pyproject.toml`` properly set up (see
:pep:`517`/:pep:`518`).

.. tip::

   You can use any other method for building distributions as long as
   it produces ready-to-upload artifacts saved into the
   ``dist/`` folder.

So add this to the steps list:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: version: 3.7
   :end-before: Actually publish to PyPI/TestPyPI


Publishing the distribution to PyPI and TestPyPI
================================================

Finally, add the following steps at the end:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: Actually publish to PyPI/TestPyPI

These two steps use the `pypa/gh-action-pypi-publish`_ GitHub
Action: the first one uploads contents of the ``dist/`` folder
into TestPyPI unconditionally and the second does that to
PyPI, but only if the current commit is tagged.


That's all, folks!
==================

Now, whenever you push a tagged commit to your Git repository remote
on GitHub, this workflow will publish it to PyPI.
And it'll publish any push to TestPyPI which is useful for
providing test builds to your alpha users as well as making
sure that your release pipeline remains healthy! 


.. _API token: https://pypi.org/help/#apitoken
.. _GitHub Actions CI/CD: https://github.com/features/actions
.. _join the waitlist: https://github.com/features/actions/signup
.. _pypa/gh-action-pypi-publish:
   https://github.com/pypa/gh-action-pypi-publish
.. _`pypa/gh-action-pypi-publish GitHub Action`:
   https://github.com/marketplace/actions/pypi-publish
.. _Secrets:
   https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables
