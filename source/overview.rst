================
Packaging Python
================

Python is a general-purpose programming lanaguage, meaning you can use
it for many things. You can build robots or server software or a game
for your friends to play.

For this reason, the first step in every Python project must be to
think about the project's audience and the corresponding target
environment. Using this information, this overview will guide you to
the packaging technologies best suited to your project.

It might seem strange to think about packaging before writing code,
but this process does wonders for avoiding headaches later on.

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

You may have heard about PyPI and ``setup.py`` and wheel files. These
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
into a *package*. A package is any directory containing Python files,
as long as one of those files is named ``__init__.py``.

Because packages consist of multiple files, they are harder to
distribute. Most protocols support transferring only one file at a
time (when was the last time you clicked a link and it downloaded
multiple files?). It's easier to get incomplete transfers, and harder
to guarantee code integrity at the destination.

So long as your code contains nothing but pure Python code, and you
know your deployment environment supports your version of Python, then
you can use Python's native packaging tools to create a *source
distribution*, or *sdist* for short.

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

Python's real power comes from its ability to integrate with the
software ecosystem, in particular libraries written in C, C++,
Fortran, Rust, and other languages. This is why wheels exist.


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
framework's packaging and deployment story. Frameworks wrap the
technologies outlined in the rest of the guide, and can make your
production experience easier and more reliable.

Service platforms
*****************

If you're developing a "Platform-as-a-Service" or "PaaS" like Heroku
or Google App Engine, you are going to want to follow their respective
packaging guides.

* Heroku
* Google App Engine
* PythonAnywhere
* OpenShift

In all these setups, the platform takes care of packaging and
deployment, as long as you follow their patterns. Most software does
not fit these templates, hence the existence of all the other options
below.

If you're developing software that will be deployed to machines you
own, users' personal computers, or any other arrangement, read on.

Web and mobile platforms
************************

Python's advances are leading it into new spaces. These days you can
write a mobile app or web application frontend in Python. While the
language may be familiar, the packaging and deployment practices are
brand new.

If you're using one of the following frameworks, you'll want to refer
to their packaging guides:

* Kivy
* Brython
* Beeware

If you are *not* interested in using a framework or platform, or just
wonder about some of the technologies and techniques utilized by the
frameworks above, continue reading below.

Depending on a pre-installed Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the host system to have Python installed. Common in
controlled environments like data centers, and local environments of
tech savvy people. Technically includes pretty much every major Linux
and Mac OS version for many years now.

* PEX
* zipapp (doesn't include library dependencies, requires Python 3.5+)
* shiv (requires Python 3)

Depending on a new Python ecosystem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the host system to have an alternative ecosystem
installed, like Anaconda. Increasingly common in academic, analytical,
and other data-oriented environments. Also used in production services.

* conda/Anaconda

Bringing your own Python
^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the host system to be able to run a program in which
we've embedded Python. Operating systems have been designed to run
programs for a very long time, so this approach offers wide
compatibility, if you're willing to work at it.

* Freezers
* Omnibus

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
