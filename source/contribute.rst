.. |PyPUG| replace:: Python Packaging User Guide

************************
Contribute to this guide
************************

The |PyPUG| welcomes contributors! There are lots of ways to help out,
including:

* Reading the guide and giving feedback
* Reviewing new contributions
* Revising existing content
* Writing new content

Most of the work on the |PyPUG| takes place on the
`project's GitHub repository`__. To get started, check out the list of
`open issues`__ and `pull requests`__. If you're planning to write or edit
the guide, please read the :ref:`style guide <contributing_style_guide>`.

.. __: https://github.com/pypa/python-packaging-user-guide/
.. __: https://github.com/pypa/python-packaging-user-guide/issues
.. __: https://github.com/pypa/python-packaging-user-guide/pulls

By contributing to the |PyPUG|, you're expected to follow the PSF's
`Code of Conduct`__.

.. __: https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md


Documentation types
===================

This project consists of four distinct documentation types with specific
purposes. When proposing new additions to the project please pick the
appropriate documentation type.

Tutorials
---------

Tutorials are focused on teaching the reader new concepts by accomplishing a
goal. They are opinionated step-by-step guides. They do not include extraneous
warnings or information. `example tutorial-style document`_.

.. _example tutorial-style document: https://docs.djangoproject.com/en/1.11/intro/

Guides
------

Guides are focused on accomplishing a specific task and can assume some level of
pre-requisite knowledge. These are similar to tutorials, but have a narrow and
clear focus and can provide lots of caveats and additional information as
needed. They may also discuss multiple approaches to accomplishing the task.
:doc:`example guide-style document <guides/packaging-namespace-packages>`.

Discussions
-----------

Discussions are focused on understanding and information. These explore a
specific topic without a specific goal in mind. :doc:`example discussion-style
document <discussions/install-requires-vs-requirements>`.

Specifications
--------------

Specifications are reference documention focused on comprehensively documenting
an agreed-upon interface for interoperability between packaging tools.
:doc:`example specification-style document <specifications/core-metadata>`.




Building the guide locally
==========================

Though not required to contribute, it may be useful to build this guide locally
in order to test your changes. In order to build this guide locally, you'll
need:

1. `Nox <https://nox.readthedocs.io/en/latest/>`_. You can install or upgrade
   nox using ``pip``::

      pip install --user nox

2. Python 3.6. Our build scripts are designed to work with Python 3.6 only.
   See the `Hitchhiker's Guide to Python installation instructions`_ to install
   Python 3.6 on your operating system.

.. _Hitchhiker's Guide to Python installation instructions:
    http://docs.python-guide.org/en/latest/starting/installation/

To build the guide, run the following bash command in the source folder::

  nox -s build

After the process has completed you can find the HTML output in the
``./build/html`` directory. You can open the ``index.html`` file to view the
guide in web browser, but it's recommended to serve the guide using an HTTP
server.

You can build the guide and serve it via an HTTP server using the following
command::

  nox -s preview

The guide will be browsable via http://localhost:8000.


Where the guide is deployed
===========================

The guide is deployed via ReadTheDocs and the configuration lives at https://readthedocs.org/projects/python-packaging-user-guide/. It's served from a custom domain and fronted by Fast.ly.


.. _contributing_style_guide:

Style guide
===========

This style guide has recommendations for how you should write the |PyPUG|.
Before you start writing, please review it. By following the style guide, your
contributions will help add to a cohesive whole and make it easier for your
contributions to be accepted into the project.


Purpose
-------

The purpose of the |PyPUG| is to be the authoritative resource on how to
package, publish, and install Python projects using current tools.


Scope
-----

The guide is meant to answer questions and solve problems with accurate and
focused recommendations.

The guide isn't meant to be comprehensive and it's not meant to replace
individual projects' documentation. For example, pip has dozens of commands,
options, and settings. The pip documentation describes each of them in detail,
while this guide describes only the parts of pip that are needed to complete the
specific tasks described in this guide.


Audience
--------

The audience of this guide is anyone who uses Python with packages.

Don't forget that the Python community is big and welcoming. Readers may not
share your age, gender, education, culture, and more, but they deserve to learn
about packaging just as much as you do.

In particular, keep in mind that not all people who use Python see themselves as
programmers. The audience of this guide includes astronomers or painters or
students as well as professional software developers.


Voice and tone
--------------

When writing this guide, strive to write with a voice that's approachable and
humble, even if you have all the answers.

Imagine you're working on a Python project with someone you know to be smart and
skilled. You like working with them and they like working with you. That person
has asked you a question and you know the answer. How do you respond? *That* is
how you should write this guide.

Here's a quick check: try reading aloud to get a sense for your writing's voice
and tone. Does it sound like something you would say or does it sound like
you're acting out a part or giving a speech? Feel free to use contractions and
don't worry about sticking to fussy grammar rules. You are hereby granted
permission to end a sentence in a preposition, if that's what you want to end it
with.

When writing the guide, adjust your tone for the seriousness and difficulty of
the topic. If you're writing an introductory tutorial, it's OK to make a joke,
but if you're covering a sensitive security recommendation, you might want to
avoid jokes altogether.


Conventions and mechanics
-------------------------

**Write to the reader**
  When giving recommendations or steps to take, address the reader as *you*
  or use the imperative mood.

  | Wrong: To install it, the user runs…
  | Right: You can install it by running…
  | Right: To install it, run…

**State assumptions**
  Avoid making unstated assumptions. Reading on the web means that any page of
  the guide may be the first page of the guide that the reader ever sees.
  If you're going to make assumptions, then say what assumptions that you're
  going to make.

**Cross-reference generously**
  The first time you mention a tool or practice, link to the part of the
  guide that covers it, or link to a relevant document elsewhere. Save the
  reader a search.

**Respect naming practices**
  When naming tools, sites, people, and other proper nouns, use their preferred
  capitalization.

  | Wrong: Pip uses…
  | Right: pip uses…
  |
  | Wrong: …hosted on github.
  | Right: …hosted on GitHub.

**Use a gender-neutral style**
  Often, you'll address the reader directly with *you*, *your* and *yours*.
  Otherwise, use gender-neutral pronouns *they*, *their*, and *theirs* or avoid
  pronouns entirely.

  | Wrong: A maintainer uploads the file. Then he…
  | Right: A maintainer uploads the file. Then they…
  | Right: A maintainer uploads the file. Then the maintainer…

**Headings**
  Write headings that use words the reader is searching for. A good way to
  do this is to have your heading complete an implied question. For example, a
  reader might want to know *How do I install MyLibrary?* so a good heading
  might be *Install MyLibrary*.

  In section headings, use sentence case. In other words, write headings as you
  would write a typical sentence.

  | Wrong: Things You Should Know About Python
  | Right: Things you should know about Python

**Numbers**
  In body text, write numbers one through nine as words. For other numbers or
  numbers in tables, use numerals.
