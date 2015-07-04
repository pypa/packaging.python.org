.. _`On-demand Package Resolution`:

On-demand Package Resolution
============================

Setuptools, via easy_install, allows for packages to be
resolved and made available for import at runtime. The
canonical example of this functionality can be seen in
the `test command
<https://pythonhosted.org/setuptools/setuptools.html#test-build-package-and-run-a-unittest-suite>`_
or in `pytest-runner <https://pypi.python.org/pypi/pytest-runner>`_.

In these distutils commands, packages that are not already
available in the current environment are downloaded
and "installed" in a transient manner, made available
for the running application without prior intervention by
the user (such as creating a virtual environment).

This functionality along with ``sys.path modification``
enables features like :ref:`Multi-version Installs`.
