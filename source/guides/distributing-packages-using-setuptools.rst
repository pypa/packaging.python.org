:orphan:

.. _distributing-packages:

===================================
Packaging and distributing projects
===================================

The guidance previously provided here is now covered by the following resources.

.. _requirements-for-packaging-and-distributing:
.. _initial-files:
.. _readme-rst-readme-md:
.. _license-txt:
.. _install-requires:
.. _choosing-a-versioning-scheme:

Configuring your project
========================

* :doc:`/tutorials/packaging-projects` walks through creating, building, and
  publishing a Python project.
* :doc:`writing-pyproject-toml` explains how to configure project metadata,
  dependencies, and the build backend.
* :doc:`making-a-pypi-friendly-readme` explains how to display your README on PyPI.
* :doc:`/discussions/versioning` covers choosing a versioning scheme.

.. _setup-py:
.. _setup-cfg:
.. _`setup() args`:
.. _your-package:
.. _packages:
.. _py-modules:
.. _manifest-in:
.. _`Package Data`:
.. _`Data Files`:
.. _scripts:

Setuptools configuration
========================

For configuration specific to :ref:`setuptools`, see its documentation:

* :doc:`Configuring setuptools using pyproject.toml
  <setuptools:userguide/pyproject_config>`
* :doc:`Package discovery <setuptools:userguide/package_discovery>`
* :doc:`Data files support <setuptools:userguide/datafiles>`
* :doc:`Entry points <setuptools:userguide/entry_point>`

For existing projects, see :doc:`modernize-setup-py-project` and
:doc:`/discussions/setup-py-deprecated`.

.. _working-in-development-mode:

Editable installs
=================

See :doc:`installing-using-pip-and-virtual-environments` for installing a local
project in editable mode, and :doc:`Development Mode
<setuptools:userguide/development_mode>` for details specific to setuptools.

.. _`Packaging your project`:
.. _source-distributions:
.. _wheels:
.. _`Pure Python Wheels`:
.. _`Platform Wheels`:
.. _`Uploading your Project to PyPI`:
.. _create-an-account:
.. _register-your-project:
.. _upload-your-distributions:

Building and publishing
=======================

* :doc:`/tutorials/packaging-projects` explains how to build source distributions
  and wheels, and upload them to PyPI.
* :doc:`packaging-binary-extensions` covers projects with compiled extensions.
* :doc:`publishing-package-distribution-releases-using-github-actions-ci-cd-workflows`
  covers publishing releases with GitHub Actions.
