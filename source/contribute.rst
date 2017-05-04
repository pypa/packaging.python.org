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

By contributing to the |PyPUG|, you're expected to follow the Python Packaging
Authority's `Contributor Code of Conduct`__. Harassment, personal attacks, and
other unprofessional conduct is not acceptable.

.. __: https://www.pypa.io/en/latest/code-of-conduct/


.. _contributing_style_guide:

Style guide
===========

This style guide has recommendations for how you should write the |PyPUG|.
Before you start writing, please review it. By following the style guide, your
contributions will help add to a cohesive whole and make it easier for your
contributions to be accepted into the project.


Purpose
-------

The purpose of the |PyPUG| is

    to be the authoritative resource on how to package, publish, and install
    Python projects using current tools.


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
