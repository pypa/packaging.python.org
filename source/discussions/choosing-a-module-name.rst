Choosing a Module Name
=========================

This discussion is a complement to :doc:`tutorials/packaging-projects`.

Make sure to have a valid :ref:`Python identifier <python:identifiers>` for your module name.
The PyPI project/dist name and the Python module may differ slightly.
For example, your package in pyproject.toml and on PyPI may have the name abcd-1234.
But a module named abcd-1234 would be cumbersome to import in Python,
since it isn't a valid identifier.
(There is a way to import it anyway, see :doc:`importlib <python:library/importlib>` and this question_.)

.. code-block:: python

   >>> import abcd-1234
   >>> from abcd-1234 import something

would not work.
But having a directory structure with src/abcd_1234/ instead of src/abcd-1234/ has 2 consequences:

- The following works:

  .. code-block:: python

     >>> import abcd_1234
     >>> from abcd_1234 import something

- Hatch will recognize that the module corresponding to the package is abcd_1234 instead of defaulting to src and building a not working wheel.

More information about :doc:`Python imports <python:reference/import>` and its :doc:`grammar <python:reference/grammar>`.

.. _question: https://stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it

