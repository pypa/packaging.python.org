.. _`Hosting your Own Simple Repository`:

==================================
Hosting your own simple repository
==================================


If you wish to host your own simple repository [1]_, you can either use a
software package like :doc:`devpi <devpi:index>` or you can simply create the proper
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


Existing projects
=================

.. list-table::
   :header-rows: 1

   * - Project
     - Package upload
     - PyPI fall-through [2]_
     - Additional notes

   * - :ref:`devpi`
     - ✔
     - ✔
     - multiple indexes with inheritance, with syncing, replication, fail-over;
       mirroring

   * - :ref:`simpleindex`
     -
     - ✔
     -

   * - :ref:`pypiserver`
     - ✔
     -
     -

   * - :ref:`pypiprivate`
     -
     -
     -

   * - :ref:`pypicloud`
     -
     -
     - unmaintained; also cached proxying; authentication, authorisation

   * - :ref:`pywharf`
     -
     -
     - unmaintained; serve files in GitHub

   * - :ref:`pulppython`
     - ✔
     -
     - also mirroring, proxying; plugin for Pulp

   * - :ref:`pip2pi`
     -
     -
     - also mirroring; manual synchronisation

   * - :ref:`dumb-pypi`
     -
     -
     - not a server, but a static file site generator

   * - :ref:`httpserver`
     -
     -
     - standard-library

   * - `Apache <https://httpd.apache.org/>`_
     -
     - ✔
     - using
       `mod_rewrite
       <https://httpd.apache.org/docs/current/mod/mod_rewrite.html>`_
       and
       `mod_cache_disk
       <https://httpd.apache.org/docs/current/mod/mod_cache_disk.html>`_,
       you can cache requests to package indexes through an Apache server

----

.. [1] For complete documentation of the simple repository protocol, see
       :ref:`simple repository API <simple-repository-api>`.

.. [2] Can be configured to fall back to PyPI (or another package index)
       if a requested package is missing.

.. _Twisted: https://twistedmatrix.com/
