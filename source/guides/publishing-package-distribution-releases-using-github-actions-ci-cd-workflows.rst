=============================================================================
Publishing package distribution releases using GitHub Actions CI/CD workflows
=============================================================================

`GitHub Actions CI/CD`_ allows you to run a series of commands
whenever an event occurs on the GitHub platform. One
popular choice is having a workflow that's triggered by a
``push`` event.
This guide shows you how to publish a Python distribution
whenever a tagged commit is pushed.
It will use the `pypa/gh-action-pypi-publish GitHub Action`_ for
publishing. It also uses GitHub's `upload-artifact`_ and `download-artifact`_ actions
for temporarily storing and downloading the source packages.

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
individually and expire automatically. Otherwise, you'll need to generate an
`API token`_ for both PyPI and TestPyPI. In case of publishing to third-party
indexes like :doc:`devpi <devpi:index>`, you may need to provide a
username/password combination.

Since this guide will demonstrate uploading to both
PyPI and TestPyPI, we'll need two trusted publishers configured.
The following steps will lead you through creating the "pending" publishers
for your new :term:`PyPI project <Project>`.
However it is also possible to add `trusted publishing`_ to any
pre-existing project, if you are its owner.

.. attention::

   If you followed earlier versions of this guide, you
   have created the secrets ``PYPI_API_TOKEN`` and ``TEST_PYPI_API_TOKEN``
   for direct PyPI and TestPyPI access. These are obsolete now and
   you should remove them from your GitHub repository and revoke
   them in your PyPI and TestPyPI account settings in case you are replacing your old setup with the new one.


Let's begin! 🚀

1. Go to https://pypi.org/manage/account/publishing/.
2. Fill in the name you wish to publish your new
   :term:`PyPI project <Project>` under
   (the ``name`` value in your ``setup.cfg`` or ``pyproject.toml``),
   the GitHub repository owner's name (org or user),
   and repository name, and the name of the release workflow file under
   the ``.github/`` folder, see :ref:`workflow-definition`.
   Finally, add the name of the GitHub Environment
   (``pypi``) we're going set up under your repository.
   Register the trusted publisher.
3. Now, go to https://test.pypi.org/manage/account/publishing/ and repeat
   the second step, but this time, enter ``testpypi`` as the name of the
   GitHub Environment.
4. Your "pending" publishers are now ready for their first use and will
   create your projects automatically once you use them
   for the first time.

   .. note::

      If you don't have a TestPyPI account, you'll need to
      create it. It's not the same as a regular PyPI account.


   .. attention::

      For security reasons, you must require `manual approval <https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#deployment-protection-rules>`_
      on each run for the ``pypi`` environment.


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

Checking out the project and building distributions
===================================================

We will have to define two jobs to publish to PyPI
and TestPyPI respectively, and an additional job to
build the distribution packages.

First, we'll define the job for building the dist packages of
your project and storing them for later use:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-at: jobs:
   :end-before: Install pypa/build

This will download your repository into the CI runner and then
install and activate the newest available Python 3 release.

And now we can build the dists from source and store them.
In this example, we'll use the ``build`` package.
So add this to the steps list:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-at: Install pypa/build
   :end-before: publish-to-pypi

Defining a workflow job environment
===================================

Now, let's add initial setup for our job that will publish to PyPI.
It's a process that will execute commands that we'll define later.
In this guide, we'll use the latest stable Ubuntu LTS version
provided by GitHub Actions. This also defines a GitHub Environment
for the job to run in its context and a URL to be displayed in GitHub's
UI nicely. Additionally, it allows acquiring an OpenID Connect token
that the ``pypi-publish`` actions needs to implement secretless
trusted publishing to PyPI.

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: path: dist/
   :end-before: steps:

This will also ensure that the PyPI publishing workflow is only triggered
if the current commit is tagged.

Publishing the distribution to PyPI
===================================

Finally, add the following steps at the end:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-after: id-token: write
   :end-before:  github-release:

This step uses the `pypa/gh-action-pypi-publish`_ GitHub
Action: after the stored distribution package has been
downloaded by the `download-artifact`_ action, it uploads
the contents of the ``dist/`` folder into PyPI unconditionally.

Signing the distribution packages
=================================

The following job signs the distribution packages with `Sigstore`_,
the same artifact signing system `used to sign CPython <https://www.python.org/download/sigstore/>`_.

Firstly, it uses the `sigstore/gh-action-sigstore-python GitHub Action`_
to sign the distribution packages. In the next step, an empty GitHub Release
from the current tag is created using the ``gh`` CLI. Note this step can be further
customised. See the `gh release documentation <https://cli.github.com/manual/gh_release>`_
as a reference.

Finally, the signed distributions are uploaded to the GitHub Release.

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-at: github-release:
   :end-before:  publish-to-testpypi


.. note::

   This is a replacement for GPG signatures, for which support has been
   `removed from PyPI <https://blog.pypi.org/posts/2023-05-23-removing-pgp/>`_.
   However, this job is not mandatory for uploading to PyPI and can be omitted.


Separate workflow for publishing to TestPyPI
============================================

Now, repeat these steps and create another job for
publishing to the TestPyPI package index under the ``jobs``
section:

.. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
   :language: yaml
   :start-at: publish-to-testpypi

.. tip::

   Requiring manual approvals in the ``testpypi`` GitHub Environment is typically unnecessary as it's designed to run on each commit to the main branch and is often used to indicate a healthy release publishing pipeline.


The whole CI/CD workflow
========================

This paragraph showcases the whole workflow after following the above guide.

.. collapse:: Click here to display the entire GitHub Actions CI/CD workflow definition

    .. literalinclude:: github-actions-ci-cd-sample/publish-to-test-pypi.yml
       :language: yaml

That's all, folks!
==================

Now, whenever you push a tagged commit to your Git repository remote
on GitHub, this workflow will publish it to PyPI.
And it'll publish any push to TestPyPI which is useful for
providing test builds to your alpha users as well as making
sure that your release pipeline remains healthy!

.. attention::

  If your repository has frequent commit activity and every push is uploaded
  to TestPyPI as described, the project might exceed the
  `PyPI project size limit <https://pypi.org/help/#project-size-limit>`_.
  The limit could be increased, but a better solution may constitute to
  use a PyPI-compatible server like :ref:`pypiserver` in the CI for testing purposes.

.. note::

   It is recommended to keep the integrated GitHub Actions at their latest
   versions, updating them frequently.


.. _API token: https://pypi.org/help/#apitoken
.. _GitHub Actions CI/CD: https://github.com/features/actions
.. _join the waitlist: https://github.com/features/actions/signup
.. _pypa/gh-action-pypi-publish:
   https://github.com/pypa/gh-action-pypi-publish
.. _`pypa/gh-action-pypi-publish GitHub Action`:
   https://github.com/marketplace/actions/pypi-publish
.. _`download-artifact`:
   https://github.com/actions/download-artifact
.. _`upload-artifact`:
   https://github.com/actions/upload-artifact
.. _Sigstore: https://www.sigstore.dev/
.. _`sigstore/gh-action-sigstore-python GitHub Action`:
   https://github.com/marketplace/actions/gh-action-sigstore-python
.. _Secrets:
   https://docs.github.com/en/actions/reference/encrypted-secrets
.. _trusted publishing: https://docs.pypi.org/trusted-publishers/
