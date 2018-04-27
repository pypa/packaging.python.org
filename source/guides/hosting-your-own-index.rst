.. _`Hosting your Own Simple Repository`:

==================================
Hosting your own simple repository
==================================


If you wish to host your own simple repository [1]_, you can either use a
software package like `devpi`_ or you can use simply create the proper
directory structure and use any web server that can serve static files and
generate an autoindex.

In either case, since you'll be hosting a repository that is likely not in
your user's default repositories, you should instruct them in your project's
description to configure their installer appropriately. For example with pip::

    pip install --extra-index-url https://python.example.com/ foobar

In addition, it is **highly** recommended that you serve your repository with
valid HTTPS. At this time, the security of your user's installations depends on
all repositories using a valid HTTPS setup.


"Manual" repository
===================

The directory layout is fairly simple, within a root directory you need to
create a directory for each project. This directory should be the normalized
name (as defined by PEP 503) of the project. Within each of these directories
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

----

.. [1] For complete documentation of the simple repository protocol, see
       PEP 503.


.. _devpi: http://doc.devpi.net/latest/
.. _Twisted: https://twistedmatrix.com/
