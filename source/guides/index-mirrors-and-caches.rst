.. _`PyPI mirrors and caches`:

================================
Package index mirrors and caches
================================

:Page Status: Incomplete
:Last Reviewed: 2023-11-08

Mirroring or caching of PyPI (and other
:term:`package indexes <Package Index>`) can be used to speed up local
package installation,
allow offline work, handle corporate firewalls or just plain Internet flakiness.

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
   the requirements using :ref:`python3 -m pip wheel <pip:pip wheel>`:

   .. code-block:: bash

      python3 -m pip wheel --wheel-dir=/tmp/wheelhouse SomeProject
      python3 -m pip install --no-index --find-links=/tmp/wheelhouse SomeProject


Existing projects
-----------------

.. list-table::
   :header-rows: 1

   * - Project
     - Cache
     - Mirror
     - Proxy
     - Additional notes

   * - :ref:`devpi`
     - ✔
     - ✔
     -
     - multiple indexes with inheritance; syncing, replication, fail-over;
       package upload

   * - :ref:`bandersnatch`
     - ✔
     - ✔
     -
     -

   * - :ref:`simpleindex`
     -
     -
     - ✔
     - custom plugin enables caching; re-routing to other package indexes

   * - :ref:`pypicloud`
     - ✔
     -
     - ✔
     - unmaintained; authentication, authorisation

   * - :ref:`pulppython`
     -
     - ✔
     - ✔
     - plugin for Pulp; multiple proxied indexes; package upload

   * - :ref:`proxpi`
     - ✔
     -
     - ✔
     - multiple proxied indexes

   * - :ref:`nginx_pypi_cache`
     - ✔
     -
     - ✔
     - multiple proxied indexes

   * - :ref:`flaskpypiproxy`
     - ✔
     -
     - ✔
     - unmaintained

   * - `Apache <https://httpd.apache.org/>`_
     - ✔
     -
     - ✔
     - using
       `mod_rewrite
       <https://httpd.apache.org/docs/current/mod/mod_rewrite.html>`_
       and
       `mod_cache_disk
       <https://httpd.apache.org/docs/current/mod/mod_cache_disk.html>`_,
       you can cache requests to package indexes through an Apache server
