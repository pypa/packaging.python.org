
.. _`Multi-version installs`:

Multi-version installs
======================


easy_install allows simultaneous installation of different versions of the same
project into a single environment shared by multiple programs which must
``require`` the appropriate version of the project at run time (using
``pkg_resources``).

For many use cases, virtual environments address this need without the
complication of the ``require`` directive. However, the advantage of
parallel installations within the same environment is that it works for an
environment shared by multiple applications, such as the system Python in a
Linux distribution.

The major limitation of ``pkg_resources`` based parallel installation is
that as soon as you import ``pkg_resources`` it locks in the *default*
version of everything which is already available on sys.path. This can
cause problems, since ``setuptools`` created command line scripts
use ``pkg_resources`` to find the entry point to execute. This means that,
for example, you can't use ``require`` tests invoked through ``nose`` or a
WSGI application invoked through ``gunicorn`` if your application needs a
non-default version of anything that is available on the standard
``sys.path`` - the script wrapper for the main application will lock in the
version that is available by default, so the subsequent ``require`` call
in your own code fails with a spurious version conflict.

This can be worked around by setting all dependencies in
``__main__.__requires__`` before importing ``pkg_resources`` for the first
time, but that approach does mean that standard command line invocations of
the affected tools can't be used - it's necessary to write a custom
wrapper script or use ``python -c '<command>'`` to invoke the application's
main entry point directly.

Refer to the `pkg_resources documentation
<https://setuptools.readthedocs.io/en/latest/pkg_resources.html#workingset-objects>`__
for more details.
