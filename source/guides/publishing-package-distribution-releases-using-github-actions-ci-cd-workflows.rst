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

   This guide *assumes* that you already have a project that you know how to
   build distributions for and *it lives on GitHub*.  This guide also avoids
   details of building platform specific projects. If you have binary
   components, check out :ref:`cibuildwheel`'s GitHub Action examples.

Configuring trusted publishing
==============================

This guide relies on PyPI's `trusted publishing`_ implementation to connect
to `GitHub Actions CI/CD`_. This is recommended for security reasons, since 
the generated tokens are created for each of your projects
individually and expire automatically. Otherwise you'll need to generate an
`API token`_ for both PyPI and TestPyPI. In case of publishing to third-party
indexes like :doc:`devpi <devpi:index>`, you will need to provide a
username/password combination.

Since this guide will demonstrate uploading to both
PyPI and TestPyPI, we'll need two trusted publishers configured. 
The following steps will lead you through creating the "pending" publishers
for your new project. However it is also possible to add `trusted publishing`_
to any pre-existing project, if you are its owner.

Let's begin! 🚀

1. Go to https://pypi.org/manage/account/publishing/.
2. Fill in the name you wish to publish your new project under,
   your GitHub username and repository name and 
   the name of the release workflow file under 
   the ``.github/`` folder, see :ref:`workflow-definition`. 
   Finally add the name of the GitHub Actions environment
   running under your repository. 
   Register the trusted publisher.
3. Now, go to https://test.pypi.org/manage/account/publishing/ and repeat
   the second step.   
4. Your "pending" publishers are now ready for their first use and will 
   create your projects automatically once you use them 
   for the first time.

   .. attention::

      If you don't have a TestPyPI account, you'll need to
      create it. It's not the same as a regular PyPI account.


.. _workflow-definition:

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

We will have to define two jobs to publish to PyPI 
and TestPyPI respectively, and an additional job to 
build the distribution packages.

Now, let's add initial setup for our job that will publish to PyPI.
It's a process that will execute commands that we'll define later.
In this guide, we'll use the latest stable Ubuntu LTS version
provided by GitHub Actions:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: on:
   :end-before: environment:


Checking out the project and building distributions
===================================================

Then, add the following under the ``build-n-publish-pypi`` section:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: runs-on:
   :end-before: Install pypa/build

This will download your repository into the CI runner and then
install and activate the newest available Python 3 release. It 
also defines the package index to publish to, PyPI, and grants
a permission to the action that is mandatory for trusted 
publishing.

And now we can build dists from source. In this example, we'll
use ``build`` package.

.. tip::

   You can use any other method for building distributions as long as
   it produces ready-to-upload artifacts saved into the
   ``dist/`` folder. You can even use ``actions/upload-artifact`` and
   ``actions/download-artifact`` to tranfer files between jobs or make them
   accessable for download from the web CI interface.

So add this to the steps list:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: version: "3.x"
   :end-before: Actually publish to PyPI


Publishing the distribution to PyPI
===================================

Finally, add the following steps at the end:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: Actually publish to PyPI
   :end-before: build-n-publish-testpypi

This step uses the `pypa/gh-action-pypi-publish`_ GitHub
Action: It uploads the contents of the ``dist/`` folder
into PyPI unconditionally, but only if the current commit 
is tagged. It is recommended you use the latest release 
tag; a tool like GitHub's dependabot can keep
these updated regularly.

Separate workflow for publishing to TestPyPI
============================================

Now, repeat these steps and create another job for
publishing to the TestPyPI package index under the ``jobs``
section:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: uses: pypa/gh-action-pypi-publish@release/v1

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
   https://docs.github.com/en/actions/reference/encrypted-secrets
.. _trusted publishing: https://docs.pypi.org/trusted-publishers/
