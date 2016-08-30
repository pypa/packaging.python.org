=======================
Documenting the Package
=======================

:Page Status: Draft
:Last Reviewed: 2016-08

A well-rounded project should also provide documentation to its users
to provide a narrative description of the purpose and use of the
package. This section describes the best practices for maintaining
and publishing documentation for a typical package.

.. contents:: Contents
   :local:


Layout
======

Author your documentation as ReStructuredText in ./docs.


Publishing
==========

The PyPA recommends that the project maintainers publish through
`Read The Docs <https://readthedocs.org>`_ (RTD). RTD requires
that your project be hosted in a publically-accessible SCM repository,
although `work is underway
<https://github.com/rtfd/readthedocs.org/issues/1957>`_ to
support an integrated experience.

Create an Account
-----------------

If you do not already have an account with Read The Docs,
`sign up here <https://readthedocs.org/accounts/signup/>`_.

Link Your Account to Github or Bitbucket
----------------------------------------

If you host your projects in Github or Bitbucket, you may
optionally link
your RTD account to those services to help facilitate the
registration of your projects.

Import a Repository
-------------------

Follow the Web UI to import your repository into your account.

Grant Access to Collaborators
-----------------------------

If you maintain the project with others, consider also
asking them also to sign
up for accounts in RTD and then grant access to each of the
projects in RTD to those collaborators.

Configure Dependencies
----------------------

If your documentation relies on any dependencies other
than Sphinx itself, you will need to declare those in a
pip requirements file (e.g. ``docs/requirements.txt``)
and configured in the RTD advanced project settings.

If the docs rely on code in the project itself or its
dependencies, you will also want to configure the
"Install Project" option in Advanced Settings.

Porting from Distutils-built Documentation
------------------------------------------

There are a few actions you should consider when migrating
from Distutils-published documentation to RTD.

Although both RTD and Distutils builds use Sphinx under the hood,
Distutils documentation is typicially invoked from the root of the
repository, but RTD builds are invoked from the ``docs`` directory
in the repository. Some projects may need to account for this
discrepancy.

Additionally, the content on pythonhosted.org will grow stale
as it is no longer being updated. It should be removed or set
to redirect. If you have a technique you recommend for doing
so, please consider contributing that here.

Any dependencies that your project had for building
documentation (other than Sphinx itself), will need to be declared
in a new requirements file and configured in the RTD
project config.

Legacy Publishing to PythonHosted.org
=====================================

Formerly, the packaging ecosystem based on distutils supported
building and publishing documentation through the distutils commands.

This technique is deprecated as the Warehouse project has dropped
support publishing and advertising documentation. Therefore, use
of pythonhosted.org for documentation is discouraged.

Sphinx itself supplies a ``build_sphinx`` command and Setuptools
supplies an ``upload_docs`` command.

Together, these commands enable the building and publishing of
documentation as part of the package release process. One can
create an alias, such as ``release`` below, which will upload the
package assets and publish the documentation in one command::

    # setup.cfg
    [aliases]
    release = sdist sphinx_build upload upload-docs

Next, ensure that sphinx is available during the build process by
including it in the ``setup_requires`` of the setup script::

    # setup.py
    needs_sphinx = {'release', 'sphinx_build'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []

    setup(
    	...
    	setup_requires=[...] + sphinx,
    )

Note that you could simply declare sphinx as a constant setup_requires
dependency, but then it would be required for any distutils operation
and not just a release or doc build.

With that configuration, a simple invocation of::

    python setup.py release

will upload the source dist and publish the documentation for the
project.

This technique had some advantages that the RTD process does not::

 - Source code did not need to be published in a public SCM repository.
 - Authentication and Authorization of maintainers in PyPI was re-used
   for authorization to publish documentation.
 - Uniform API that required no additional manual steps.
