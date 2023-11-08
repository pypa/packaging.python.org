.. _`Hosting your Own Simple Repository`:

==================================
Hosting your own simple repository
==================================


If you wish to host your own simple repository [1]_, you can either use a
software package like :doc:`devpi <devpi:index>` or you can use simply create the proper
directory structure and use any web server that can serve static files and
generate an autoindex.

In either case, since you'll be hosting a repository that is likely not in
your user's default repositories, you should instruct them in your project's
description to configure their installer appropriately. For example with pip:

.. tab:: Unix/macOS

    .. code-block:: bash

        python3 -m pip install --extra-index-url https://python.example.com/ foobar

.. tab:: Windows

    .. code-block:: bat

        py -m pip install --extra-index-url https://python.example.com/ foobar

In addition, it is **highly** recommended that you serve your repository with
valid HTTPS. At this time, the security of your user's installations depends on
all repositories using a valid HTTPS setup.


"Manual" repository
===================

The directory layout is fairly simple, within a root directory you need to
create a directory for each project. This directory should be the :ref:`normalized name <name-normalization>` of the project. Within each of these directories
simply place each of the downloadable files. If you have the projects "Foo"
(with the versions 1.0 and 2.0) and "bar" (with the version 0.1) You should
end up with a structure that looks like::

    .
    ├── bar
    │   └── bar-0.1.tar.gz
    └── foo
        ├── Foo-1.0.tar.gz
        └── Foo-2.0.tar.gz

Once you have this layout, simply configure your webserver to serve the root
directory with autoindex enabled. For an example using the built in Web server
in `Twisted`_, you would simply run ``twistd -n web --path .`` and then
instruct users to add the URL to their installer's configuration.


Hosted and managed solutions
============================

These options are provided by third-party organisations, and are generally
not open-source nor free.

Gemfury
^^^^^^^

`Product page <https://fury.co/l/pypi-server/>`__ |
`Documentation <https://gemfury.com/help/pypi-server/>`__

Private indexes are paid.

Artifactory
^^^^^^^^^^^

`Product page <https://jfrog.com/artifactory/>`__ |
`Documentation
<https://www.jfrog.com/confluence/display/JFROG/PyPI+Repositories/>`__

Cached proxy for multiple package indexes (including PyPI), and hosting a
new package index (supporting upload) with fall-through. Can be self-hosted
(not for free).

Nexus Repository Manager
^^^^^^^^^^^^^^^^^^^^^^^^

`Product page <https://www.sonatype.com/products/nexus-repository/>`__ |
`Documentation
<https://help.sonatype.com/repomanager3/nexus-repository-administration/formats/pypi-repositories/>`__

Cached proxy for multiple package indexes (including PyPI), and hosting a
new package index (supporting upload) with fall-through.

Coherent Minds PyPI Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Documentation <https://pypi.coherentminds.de/redoc/>`__

Only filters requests, redirecting to PyPI if not filtered, and blocking
requests otherwise.

GitLab Package Registry
^^^^^^^^^^^^^^^^^^^^^^^

`Documentation
<https://docs.gitlab.com/ee/user/packages/pypi_repository/>`__

Private and public package index with optional fall-through, permissioning.

AWS CodeArtifact
^^^^^^^^^^^^^^^^

`Product page <https://aws.amazon.com/codeartifact/>`__ |
`Documentation
<https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html>`__

Private package index with optional cached fall-through to PyPI.

Azure Artifacts
^^^^^^^^^^^^^^^

`Product page
<https://azure.microsoft.com/en-us/products/devops/artifacts/>`__ |
`Documentation
<https://learn.microsoft.com/en-us/azure/devops/artifacts/quickstarts/python-packages/>`__

Private package index with optional fall-through.

Google Artifact Registry
^^^^^^^^^^^^^^^^^^^^^^^^

`Product page
<https://cloud.google.com/artifact-registry/>`__ |
`Documentation
<https://cloud.google.com/artifact-registry/docs/python/>`__

Private package index with no fall-through nor mirroring.

----

.. [1] For complete documentation of the simple repository protocol, see
       :ref:`simple repository API <simple-repository-api>`.


.. _Twisted: https://twistedmatrix.com/
