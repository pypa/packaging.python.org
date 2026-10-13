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
* `reStructuredText <https://docutils.sourceforge.io/rst.html>`_ (without Sphinx extensions)
* Markdown (`GitHub Flavored Markdown <https://github.github.com/gfm/>`_ by default,
  or `CommonMark <https://commonmark.org/>`_)

It's customary to save your README file in the root of your project, in the same directory as your :file:`pyproject.toml` file.


Including your README in your package's metadata
------------------------------------------------

To include your README as your project's long description on PyPI, declare
the ``readme`` key in the ``[project]`` table of :file:`pyproject.toml`.
Build backends use this value to populate the distribution's ``Description``
and ``Description-Content-Type`` core metadata fields.

.. seealso::

   * :ref:`declaring-project-metadata`
   * :ref:`description-optional`
   * :ref:`description-content-type-optional`

For Markdown or reStructuredText files, the simplest form is the README path:

.. code-block:: toml

   [project]
   name = "an-example-package"
   # other project metadata omitted
   readme = "README.md"

When the file name has a recognized ``.md`` or ``.rst`` extension, the
content type is inferred automatically. For another file name or format,
provide both the file path and content type explicitly:

.. code-block:: toml

   [project]
   readme = { file = "README", content-type = "text/plain" }

The referenced README should remain in the project source tree so the build
backend can read it when producing package metadata.

Validating reStructuredText markup
----------------------------------

If your README is written in reStructuredText, any invalid markup will prevent
it from rendering, causing PyPI to instead just show the README's raw source.

Note that Sphinx extensions used in docstrings, such as
:doc:`directives <sphinx:usage/restructuredtext/directives>` and :doc:`roles <sphinx:usage/restructuredtext/roles>`
(e.g., "``:py:func:`getattr```" or "``:ref:`my-reference-label```"), are not allowed here and will result in error
messages like "``Error: Unknown interpreted text role "py:func".``".

You can check your README for markup errors before uploading as follows:

1. Install or upgrade `twine <https://github.com/pypa/twine>`_:

   .. tab:: Unix/macOS

      .. code-block:: bash

            python3 -m pip install --upgrade twine

   .. tab:: Windows

      .. code-block:: bat

            py -m pip install --upgrade twine

2. Build the sdist and wheel for your project as described under
   :ref:`Packaging Your Project`.

3. Run ``twine check`` on the sdist and wheel:

   .. code-block:: bash

      twine check dist/*

   This command will report any problems rendering your README.  If your markup
   renders fine, the command will output ``Checking distribution FILENAME:
   Passed``.
