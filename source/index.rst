===========================
Python Packaging User Guide
===========================

.. meta::
   :description: The Python Packaging User Guide (PyPUG) is a collection of tutorials and guides for packaging Python software.
   :keywords: python, packaging, guide, tutorial

.. toctree::
   :maxdepth: 2
   :hidden:

   overview
   basics
   tutorials/index
   guides/index
   discussions/index
   specifications/index
   key_projects
   glossary
   support
   contribute
   news

Welcome to the *Python Packaging User Guide*, a collection of tutorials and
references to help you distribute and install Python packages with modern
tools.

This guide is maintained on `GitHub`_ by the `Python Packaging Authority`_. We
happily accept any :doc:`contributions and feedback <contribute>`. 😊

.. _GitHub: https://github.com/pypa/python-packaging-user-guide
.. _Python Packaging Authority: https://pypa.io


.. note:: **Navigating the User Guide**

   The *Python Packaging User Guide* is organized into several sections:

   - :doc:`tutorials/index` introduce packaging concepts through opinionated,
     step-by-step guides, such as *Installing Packages* and *Packaging Projects*.
   - :doc:`guides/index` focus on accomplishing a specific task, such as *Making a
     PyPI friendly README* and *Installing Scientific Packages*.
   - :doc:`discussions/index` provide comprehensive information about a specific topic
     such as *install_requires vs requirements files* and *Wheel vs Egg*.
   - :doc:`specifications/index` document interoperability and standards, such as
     *Entry points specification* and *Platform compatibility tags*.
   - :doc:`key_projects` highlights PyPA maintained projects and mentions notable
     third-party maintained projects.

   The :doc:`glossary` also helps the reader understand any unfamiliar terms or
   jargon.


Get started
===========

Many readers will find the :doc:`tutorials/index` section a good starting place
to learn more about Python packaging. It provides step-by-step information about
the essential tools and concepts of installing and packaging Python projects:

* :doc:`tutorial on Installing Packages <tutorials/installing-packages>`
* :doc:`tutorial on Managing Application Dependencies <tutorials/managing-dependencies>`
  in a version controlled project
* :doc:`tutorial on Packaging and Distributing <tutorials/packaging-projects>`
  your projects

The :doc:`Basics of Installation <basics>` discusses the methods of
installing a Python package for different use cases, such as web, scientific
applications, devops, and more. New developers are encouraged to read this
section before the :doc:`tutorial on Installing Packages <tutorials/installing-packages>`.

Intermediate to advanced Python developers interested in creating a Python
package will benefit from reviewing the :doc:`Overview of Python Packaging <overview>`
and its guidance on planning development for packaging.


Learn more
==========

Beyond our :doc:`tutorials/index`, this User Guide has several resource
sections with topical and in-depth information:

* the :doc:`guides/index` section for walk throughs, such as
  :doc:`guides/installing-using-linux-tools` or :doc:`guides/packaging-binary-extensions`
* the :doc:`discussions/index` section for in-depth references on topics such as
  :doc:`discussions/deploying-python-applications` or :doc:`discussions/pip-vs-easy-install`
* the :doc:`specifications/index` section for packaging interoperability specifications

Additionally, there is a list of :doc:`other projects <key_projects>` maintained
by members of the Python Packaging Authority.
