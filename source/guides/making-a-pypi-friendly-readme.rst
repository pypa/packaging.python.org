Making a PyPI-friendly README
=============================

README files can help your users understand your project and can be used to set your project's description on PyPI.
This guide helps you create a README in a PyPI-friendly format and include your README in your package so it appears on PyPI.


Creating a README file
----------------------

README files for Python projects are often named ``README``, ``README.txt``, ``README.rst``, or ``README.md``.

For your README to display properly on PyPI, choose a markup language supported by PyPI.
Formats supported by `PyPI's README renderer <https://github.com/pypa/readme_renderer>`_ are:

* plain text
* `reStructuredText <http://docutils.sourceforge.net/rst.html>`_
* Markdown (`GitHub Flavored Markdown <https://github.github.com/gfm/>`_ by default,
  or `CommonMark <http://commonmark.org/>`_)

It's customary to save your README file in the root of your project, in the same directory as your :file:`setup.py` file.


Including your README in your package's metadata
------------------------------------------------

To include your README's contents as your package description,
set your project's ``Description`` and ``Description-Content-Type`` metadata,
typically in your project's :file:`setup.py` file.

.. seealso::

   * :ref:`description-optional`
   * :ref:`description-content-type-optional`

For example, to set these values in a package's :file:`setup.py` file,
use ``setup()``'s ``long_description`` and ``long_description_content_type``.

Set the value of ``long_description`` to the contents (not the path) of the README file itself.
Set the ``long_description_content_type`` to an accepted ``Content-Type``-style value for your README file's markup,
such as ``text/plain``, ``text/x-rst`` (for reStructuredText), or ``text/markdown``.

.. Note:: If you're using GitHub-flavored Markdown to write a project's description, ensure you upgrade
          the following tools:

          .. code-block:: bash

              python3 -m pip install --user --upgrade setuptools wheel twine

          The preferred versions:

          - ``setuptools>=38.6.0``
          - ``wheel>=0.31.0``
          - ``twine>=1.11.0``

          It's recommended that you use ``twine`` to upload the project's distribution packages:

          .. code-block:: bash

              twine upload dist/*



For example, see this :file:`setup.py` file,
which reads the contents of :file:`README.md` as ``long_description``
and identifies the markup as GitHub-flavored Markdown:

.. code-block:: python

   from setuptools import setup

   # read the contents of your README file
   from os import path
   this_directory = path.abspath(path.dirname(__file__))
   with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
       long_description = f.read()

   setup(
       name='an_example_package',
       # other arguments omitted
       long_description=long_description,
       long_description_content_type='text/markdown'
   )
