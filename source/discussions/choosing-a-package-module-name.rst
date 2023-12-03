Choosing a Package/Module Name
=========================

This discussion is a complement to :doc:`/tutorials/packaging-projects`.

Make sure to have a valid :ref:`Python identifier <python:identifiers>` for your import package/module name.
The PyPI project/dist name and the Python package/module may differ slightly.
Moreover, one PyPI project/dist may ship more than one module or importable package — it is only possible that one matches the name, others can't.
For example, your package in :file:`pyproject.toml` and on PyPI may have the name ``abcd-1234``.
But a module named ``abcd-1234`` would be cumbersome to import in Python,
since it isn't a valid identifier.
(It would be cumbersone, completely unnatural and against the long-established conventions in the Python community;
see, for example, :pep:`8#package-and-module-names`.
There is a way to import it anyway, see :doc:`importlib <python:library/importlib>` and this question_.)

.. code-block:: pycon

   >>> import abcd-1234
   >>> from abcd-1234 import something

would not work.
But having a directory structure with ``src/abcd_1234/`` instead of ``src/abcd-1234/`` has 2 consequences:

- The following works:

  .. code-block:: pycon

     >>> import abcd_1234
     >>> from abcd_1234 import something

- Hatch will recognize that the module corresponding to the package is ``abcd_1234`` instead of defaulting to ``src`` and building a not working wheel.

More information about :doc:`Python imports <python:reference/import>` and its :doc:`grammar <python:reference/grammar>`.

.. _question: https://stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it
