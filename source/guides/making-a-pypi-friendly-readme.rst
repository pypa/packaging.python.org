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

.. note::

   If you're using GitHub-flavored Markdown to write a project's description, ensure you upgrade
   the following tools:

   .. tab:: Unix/macOS

      .. code-block:: bash

         python3 -m pip install --user --upgrade setuptools wheel twine

   .. tab:: Windows

      .. code-block:: bat

         py -m pip install --user --upgrade setuptools wheel twine

   The minimum required versions of the respective tools are:

   - ``setuptools >= 38.6.0``
   - ``wheel >= 0.31.0``
   - ``twine >= 1.11.0``

   It's recommended that you use ``twine`` to upload the project's distribution packages:

   .. code-block:: bash

      twine upload dist/*

For example, see this :file:`setup.py` file,
which reads the contents of :file:`README.md` as ``long_description``
and identifies the markup as GitHub-flavored Markdown:

.. code-block:: python

   from setuptools import setup

   # read the contents of your README file
   from pathlib import Path
   this_directory = Path(__file__).parent
   long_description = (this_directory / "README.md").read_text()

   setup(
       name='an_example_package',
       # other arguments omitted
       long_description=long_description,
       long_description_content_type='text/markdown'
   )


Validating reStructuredText markup
----------------------------------

If your README is written in reStructuredText, any invalid markup will prevent
it from rendering, causing PyPI to instead just show the README's raw source.

Note that Sphinx extensions used in docstrings, such as
:doc:`directives <sphinx:usage/restructuredtext/directives>` and :doc:`roles <sphinx:usage/restructuredtext/roles>`
(e.g., "``:py:func:`getattr```" or "``:ref:`my-reference-label```"), are not allowed here and will result in error
messages like "``Error: Unknown interpreted text role "py:func".``".

You can check your README for markup errors before uploading as follows:

1. Install the latest version of `twine <https://github.com/pypa/twine>`_;
   version 1.12.0 or higher is required:

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
