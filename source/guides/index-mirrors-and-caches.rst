.. _`PyPI mirrors and caches`:

================================
Package index mirrors and caches
================================

:Page Status: Incomplete
:Last Reviewed: 2014-12-24

.. contents:: Contents
   :local:


Mirroring or caching of PyPI (and other package indexes) can be used to speed
up local package installation, allow offline work, work with corporate
firewalls or handle just plain internet flakiness.

There are multiple classes of options in this area:

1. local/hosted caching of package indexes.

2. local/hosted mirroring of a package index. A mirror is a (whole or
   partial) copy of a package index, which can be used in place of the
   original index.

3. private package index with fall-through to public package indexes (for
   example, to mitigate dependency confusion attacks), also known as a
   proxy.


Caching with pip
----------------

pip provides a number of facilities for speeding up installation by using local
cached copies of :term:`packages <Distribution Package>`:

1. :ref:`Fast & local installs <pip:installing from local packages>`
   by downloading all the requirements for a project and then pointing pip at
   those downloaded files instead of going to PyPI.
2. A variation on the above which pre-builds the installation files for
   the requirements using :ref:`python -m pip wheel <pip:pip wheel>`:

   .. code-block:: bash

      python -m pip wheel --wheel-dir=/tmp/wheelhouse SomeProject
      python -m pip install --no-index --find-links=/tmp/wheelhouse SomeProject


Caching with devpi
------------------

devpi is a caching proxy server which you run on your laptop, or some other
machine you know will always be available to you. See the `devpi
documentation for getting started`__.

__ https://devpi.net/docs/devpi/devpi/latest/+d/quickstart-pypimirror.html

devpi has additional funcionality, such as mirroring package indexes, running
multiple indexes with a concept of inheritance, syncing between multiple
servers, index replication and fail-over, and package upload.

* `devpi on PyPI <https://pypi.org/project/devpi/>`_
* `devpi source <https://github.com/devpi/devpi>`_


Complete mirror with bandersnatch
----------------------------------

bandersnatch will set up a complete local (or `AWS S3`_) mirror of all PyPI
:term:`packages
<Distribution Package>` (externally-hosted packages are not mirrored). See
the `bandersnatch documentation for getting that going`__.

__ https://bandersnatch.readthedocs.io/en/latest/

A benefit of devpi is that it will create a mirror which includes
:term:`packages <Distribution Package>` that are external to PyPI, unlike
bandersnatch which will only cache :term:`packages <Distribution Package>`
hosted on PyPI.

* `bandersnatch on PyPI <https://pypi.org/project/bandersnatch/>`_
* `bandersnatch source <https://github.com/pypa/bandersnatch/>`_


Other package index servers
---------------------------

simpleindex
^^^^^^^^^^^

Routes URLs to multiple package indexes (including PyPI), serves local (or
`AWS S3`_, with a plugin) directory of packages, no caching without custom
plugins, no mirroring.

* `simpleindex on PyPI <https://pypi.org/project/simpleindex/>`_
* `simpleindex source / documentation
  <https://github.com/uranusjr/simpleindex>`_

pypiserver
^^^^^^^^^^

Serves local directory of packages, no fall-through to package indexes
(including PyPI), supports package upload.

* `pypiserver on PyPI <https://pypi.org/project/pypiserver/>`_
* `pypiserver source / documentation
  <https://github.com/pypiserver/pypiserver>`_

pypiprivate
^^^^^^^^^^^

Serves local (or `AWS S3`_-hosted) directory of packages, no fall-through to
package indexes (including PyPI).

* `pypiprivate on PyPI <https://pypi.org/project/pypiprivate/>`_
* `pypiprivate source / documentation
  <https://github.com/helpshift/pypiprivate>`_

PyPI Cloud
^^^^^^^^^^

PyPI server, backed by `AWS S3`_, another cloud storage service, or local
files. Supports redirect/cached proxying, authentication and authorisation, no
mirroring.

* `PyPI Cloud on PyPI <https://pypi.org/project/pypicloud/>`_
* `PyPI Cloud source <https://github.com/stevearc/pypicloud>`_
* `PyPI Cloud documentation <https://pypicloud.readthedocs.io>`_

pywharf
^^^^^^^

.. warning:: Not maintained, project archived

PyPI server, backed by GitHub or local files. No proxy or mirror.

* `pywharf on PyPI <https://pypi.org/project/pywharf/>`_
* `pywharf source <https://github.com/pywharf/pywharf>`_

Python package index plugin for Pulp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Supports local/`AWS S3`_ mirrors, package upload, proxying to multiple indexes,
no caching.

* `pulp_python on PyPI <https://pypi.org/project/pulp-python/>`_
* `pulp_python documentation <https://docs.pulpproject.org/pulp_python/>`_
* `pulp_python source <https://github.com/pulp/pulp_python>`_

pip2pi
^^^^^^

Manual syncing of specific packages, no proxy.

* `pip2pi on PyPI <https://pypi.org/project/pip2pi/>`_
* `pip2pi source / documenation <https://github.com/wolever/pip2pi>`_

proxpi
^^^^^^

Package index caching proxy, supports multiple indexes, no mirroring.

* `proxpi on PyPI <https://pypi.org/project/proxpi/>`_
* `proxpi source <https://github.com/EpicWink/proxpi>`_

Flask-Pypi-Proxy
^^^^^^^^^^^^^^^^

.. warning:: Not maintained, project archived

Caches PyPI. No cache size limit, no caching index pages.

* `Flask-Pypi-Proxy on PyPI <https://pypi.org/project/Flask-Pypi-Proxy/>`_
* `Flask-Pypi-Proxy documentation
  <https://flask-pypi-proxy.readthedocs.io/en/latest/index.html>`_
* `Flask-Pypi-Proxy source <https://github.com/tzulberti/Flask-PyPi-Proxy>`_

http.server
^^^^^^^^^^^

Standard-library, hosts directory exactly as laid out, no proxy to package
indexes (eg PyPI). See more in :ref:`Hosting your Own Simple Repository`.

* `http.server documentation
  <https://docs.python.org/3/library/http.server.html>`_

Apache
^^^^^^

Using
`mod_rewrite <https://httpd.apache.org/docs/current/mod/mod_rewrite.html>`_ and
`mod_cache_disk
<https://httpd.apache.org/docs/current/mod/mod_cache_disk.html>`_,
you can cache requests to package indexes through an Apache server.

Gemfury
^^^^^^^

Hosted and managed solution. Private indexes are not free, documentation
doesn't say anything about fall-through.

* `Host Python packages on Gemfury <https://fury.co/l/pypi-server>`_
* `Gemfure PyPI documentation <https://gemfury.com/help/pypi-server>`_

Artifactory
^^^^^^^^^^^

Hosted and managed solution. Proxy (with caching) multiple package indexes, and
host a new package index (supporting upload) with fall-through. Can be
self-hosted (not for free).

* `JFrog Artifactory <https://jfrog.com/artifactory/>`_
* `PyPI Repositories on Artifactory documentation
  <https://www.jfrog.com/confluence/display/JFROG/PyPI+Repositories>`_

Nexus Repository Manager
^^^^^^^^^^^^^^^^^^^^^^^^

Hosted and managed solution. Proxy (with caching) multiple package indexes, and
host a new package index (supporting upload) with fall-through.

* `Sonatype Nexus repository
  <https://www.sonatype.com/products/nexus-repository>`_
* `PyPI documentation for Nexus
  <https://help.sonatype.com/repomanager3/nexus-repository-administration/formats/pypi-repositories>`_

Coherent Minds PyPI Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^

Hosted and managed solution. Only filters requests, redirecting to PyPI if not
filtered, and blocking requests otherwise.

* `Coherent Minds PyPI filter <https://pypi.coherentminds.de/redoc>`_

GitLab Package Registry
^^^^^^^^^^^^^^^^^^^^^^^

Hosted and managed solution. Private and public package index with
optional fall-through, permissioning.

* `GitLab documentation
  <https://docs.gitlab.com/ee/user/packages/pypi_repository/>`_

AWS CodeArtifact
^^^^^^^^^^^^^^^^

Hosted and managed solution. Private package index with optional cached
fall-through to PyPI.

* `AWS CodeArtifact <https://aws.amazon.com/codeartifact/>`_
* `Python packages on CodeArtifact documentation
  <https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html>`_

Azure Artifacts
^^^^^^^^^^^^^^^

Hosted and managed solution. Private package index with optional fall-through.

* `Azure Artifacts
  <https://azure.microsoft.com/en-us/products/devops/artifacts/>`_
* `Python packages on Azure Artifacts documentation
  <https://learn.microsoft.com/en-us/azure/devops/artifacts/quickstarts/python-packages>`_

Google Artifact Registry
^^^^^^^^^^^^^^^^^^^^^^^^

Hosted and managed solution. Private package index with no fall-through nor
mirroring.

* `Google Artifact Registry <https://cloud.google.com/artifact-registry/>`_
* `Python packages on Artifact Registry documentation
  <https://cloud.google.com/artifact-registry/docs/python>`_

.. _`AWS S3`: https://aws.amazon.com/s3/
