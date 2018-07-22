===================================
An Overview of Packaging for Python
===================================

Python is a general-purpose programming language, meaning you can use
it for many things. You can build robots or server software or a game
for your friends to play. For this reason, the first step in every
Python project must be to think about the project's audience and the
corresponding target environment. Using this information, this
overview will guide you to the packaging technologies best suited to
your project.

It might seem strange to think about packaging before writing code,
but this process does wonders for avoiding headaches later on. Some of
the questions you'll want to answer are:

* Who are your software's users? Are they other developers doing
  software development, operations people in a datacenter, or some
  less software-savvy group?
* Is your software meant for servers, desktops, or embedded devices?
* Is your software installed individually, or to many computers at once?

Packaging is all about target environment and deployment
experience. There are many answers to the questions above and each
combination of circumstances has its own solutions.

Packaging libraries and tools
-----------------------------

You may have heard about PyPI, ``setup.py``, and wheel files. These
are just a few of the tools Python's ecosystem provides for
distributing Python code to developers.

The following classes of code are libraries and tools, meant for a
technical audience, in a development setting. Skip ahead to
Application packaging if you're looking for ways to package Python for
a production setting.

Python modules
^^^^^^^^^^^^^^

A Python file, provided it only relies on the standard library, can be
redistributed and reused. You will also need to ensure it's written
for the right version of Python.

Python source distributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your code consists of multiple Python files, it's usually organized
into a directory structure. Any directory containing Python files,
provided one of those files is named ``__init__.py``, comprises an
:term:`import package`.

Because packages consist of multiple files, they are harder to
distribute. Most protocols support transferring only one file at a
time (when was the last time you clicked a link and it downloaded
multiple files?). It's easier to get incomplete transfers, and harder
to guarantee code integrity at the destination.

So long as your code contains nothing but pure Python code, and you
know your deployment environment supports your version of Python, then
you can use Python's native packaging tools to create a *source*
:term:`distribution package`, or *sdist* for short.

Python's *sdists* are compressed archives (``.tar.gz`` files)
containing one or more packages or modules. If your code is
pure-Python, and you only depend on other Python packages, you can `go
here to learn more <TODO>`_.

If you rely on any non-Python code, or non-Python packages (such as
libxml2 in the case of lxml, or BLAS libraries in the case of numpy),
you will want to read on.

.. TODO: "Did you know?" about distributions providing multiple
   versions of the same package. Python packaging superpower!

Python binary distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^

So much of Python's practical power comes from its ability to
integrate with the software ecosystem, in particular libraries written
in C, C++, Fortran, Rust, and other languages.

(TODO: This is why wheels exist, etc.)

Binary distributions are best when they come with source distributions
to match. This way, even if you don't upload pre-built versions of
your code for every operating system, users of other platforms can
still build it for themselves. Python and PyPI make it easy to upload
both.


Packaging Applications
----------------------

So far we've only discussed Python's native distribution tools. Based
on our introduction, you would be correct to infer we're only
targeting environments which have Python. More importantly we're
assuming an audience who knows how to install Python packages.

With the variety of operating systems, configurations, and people out
there, this assumption is only safe when targeting a developer
audience.

Python's native packaging is mostly built for distributing reusable
code, called libraries, between developers. We can piggyback
**tools**, or basic applications for developers, on top of Python's
library packaging, using technologies like `setuptools entry_points
<http://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation>`_.

Generally libraries are building blocks, and not complete
applications. For distributing applications, there's a whole world of
technologies out there.

The best way to organize these application packaging options is by the
way they depend on the target environment. That's how we'll approach
the coming sections.

.. TODO: Another way of thinking about packaging solutions is by how
   much they include. All solutions include your code, plus some
   amount of your code's library and service dependencies. PEX
   includes Python libraries. RPM includes a list of dependencies on
   libraries and local services. Images can be built to include
   everything.

Depending on a framework
^^^^^^^^^^^^^^^^^^^^^^^^

Some types of Python applications, like web sites and services, are
common enough that they have frameworks to enable their development
and packaging. Other types of applications, like web and mobile
clients, are advanced enough that the framework is more or less a
necessity.

In all these cases, it makes sense to work backwards, from the
framework's packaging and deployment story. Some frameworks include a
deployment system which wraps the technologies outlined in the rest of
the guide. In these cases, you'll want to defer to your framework's
packaging guide for the easiest and most reliable production experience.

If you ever wonder how these platforms and frameworks work under the
hood, you can always read the sections beyond.

Service platforms
*****************

If you're developing for a "Platform-as-a-Service" or "PaaS" like
Heroku or Google App Engine, you are going to want to follow their
respective packaging guides.

* Heroku
* Google App Engine
* PythonAnywhere
* OpenShift
* "Serverless" frameworks like Zappa

In all these setups, the platform takes care of packaging and
deployment, as long as you follow their patterns. Most software does
not fit one of these templates, hence the existence of all the other
options below.

If you're developing software that will be deployed to machines you
own, users' personal computers, or any other arrangement, read on.

Web browsers and mobile applications
************************************

Python's steady advances are leading it into new spaces. These days
you can write a mobile app or web application frontend in
Python. While the language may be familiar, the packaging and
deployment practices are brand new.

If you're planning on releasing to these new frontiers, you'll want to
check out the following frameworks, and refer to their packaging
guides:

* Kivy
* Beeware
* Brython
* Flexx

If you are *not* interested in using a framework or platform, or just
wonder about some of the technologies and techniques utilized by the
frameworks above, continue reading below.

Depending on a pre-installed Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pick an arbitrary computer, and depending the context, there's a very
good chance Python is already installed. Included by default in most
Linux and Mac operating systems for many years now, you can reasonably
depend on Python preexisting in your data centers or on the personal
machines of developers and data scientists.

Technologies which support this model:

* `PEX <https://github.com/pantsbuild/pex#pex>`_ (Python EXecutable)
* `zipapp <https://docs.python.org/3/library/zipapp.html>`_ (does not help manage dependencies, requires Python 3.5+)
* `shiv <https://github.com/linkedin/shiv#shiv>`_ (requires Python 3)

Depending on a new Python ecosystem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a long time many operating systems, including Mac and Windows,
lacked built-in package management. Only recently did these OSes gain
so-called "app stores", but even those focus on consumer applications
and offer little for developers.

Developers long sought remedies, and in this struggle, emerged with
new their own package management solutions -- with some notable
benefits for Python developers in particular. The most prominent, an
alternative package ecosystem called Anaconda is built around Python
and is increasingly common in academic, analytical, and other
data-oriented environments, even making its way into server-oriented
environments.

Instructions on building for the Anaconda ecosystem:

* `Building libraries and applications with conda <https://conda.io/docs/user-guide/tutorials/index.html>`_
* `Transitioning a native Python package to Anaconda <https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html>`_

A similar model involves installing an alternative Python
distribution, but does not support arbitrary operating system-level
packages:

* `Enthought Canopy <https://www.enthought.com/product/canopy/>`_
* `ActiveState ActivePython <https://www.activestate.com/activepython>`_
* `WinPython <http://winpython.github.io/>`_

Bringing your own Python
^^^^^^^^^^^^^^^^^^^^^^^^

Computing as we know it is defined by the ability to execute
programs. Every operating system natively supports one or more formats
of program they can natively execute.

There are many techniques and technologies which turn your Python
program into one of these formats, most of which involve embedding the
Python interpreter and any other dependencies into a single executable
file.

This approach offers wide compatiblity and seamless user experience,
though often through a panel of technologies, and a good amount of
effort.

* Freezers (Links TODO, maybe separate doc?)

For server applications, see `Chef Omnibus
<https://github.com/chef/omnibus#-omnibus>`_.


Bringing your own userspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the host system to be able to run a lightweight image in
a relatively modern arrangement often referred to as containerization.

* AppImage
* Flatpak
* Snappy
* Docker

Bringing your own kernel
^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the host system to have a hypervisor and run a virtual
machine. This type of virtualization is mature and widespread in data
center environments.

* Vagrant
* AMIs
* OpenStack

Bringing your own hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on your host to have electricity.

Embed your code on an Adafruit or a Micropython, or some other
hardware, and just ship it to the datacenter, or your users' homes,
and call it good.

What about...
-------------

* Operating-system packages (deb/rpm)
* virtualenv
* Security considerations

Summary
-------

Packaging in Python has a bit of a reputation for being a bumpy
ride. This is mostly a confused side effect of Python's
versatility. Once you understand the natural boundaries between each
packaging solution, you begin to realize that the varied landscape is
a small price Python programmers pay for using the most balanced,
flexible language available.
