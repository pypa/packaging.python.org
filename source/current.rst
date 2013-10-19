
=====================
Quick Recommendations
=====================

If all you're after is clear, simple advice for what to use right now, here it
is:

* Use :ref:`setuptools` to build and package Python distributions and publish
  them to the `Python Package Index`_ (PyPI). :ref:`distribute` (a fork of
  setuptools) was recently merged back into setuptools, thereby making
  setuptools the primary choice for packaging.
* Use :ref:`pip` to install Python distributions from PyPI
* Use :ref:`virtualenv` to isolate application specific dependencies from the
  system Python installation
* Use :ref:`buildout` (primarily focused on the web development community) or
  `hashdist`_ and `conda`_ (primarily focused on the scientific community) if
  you want fully intregrated software stacks, without worrying about
  interoperability with platform provided package management systems
* If you're on Linux, the versions of these tools provided as platform specific
  packages should be fine for most purposes, but may be missing some of the
  latest features described on the project websites.

Unfortunately, there are a couple of qualifications required on that simple
advice:

* Use ``easy_install`` or :ref:`buildout` if you need to install from the binary
  ``egg`` format, which :ref:`pip` can't currently handle
* Aside from using :ref:`pip` over ``easy_install`` whenever possible, try to
  ignore the confusing leftovers of slanging matches between developers of
  competing tools, as well as information about upcoming tools that are likely
  still months or years away from being meaningful to anyone not directly
  involved in developing packaging tools.

.. _Python Package Index: https://pypi.python.org
.. _hashdist: http://hashdist.readthedocs.org/en/latest/
.. _conda: http://docs.continuum.io/conda/


Step-by-step Guide
==================

For those looking for a more comprehensive guide to "How do I publish my
Python project in a way that will make it as easy as possible for me to
maintain and for others to contribute?", then Jeff Knupp's
`Open Sourcing a Python Project the Right Way
<http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/>`__
is an excellent guide that is up to date with the currently available tools
(as of September, 2013). Even for those not looking for a step-by-step
guide, Jeff's post provides some links to some excellent resources.
