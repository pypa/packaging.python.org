Choosing a Package/Module Name
==============================

This discussion is a complement to :doc:`/tutorials/packaging-projects`.

Make sure to choose a valid :ref:`Python identifier <python:identifiers>` for the names of all your :term:`import packages <import package>` and :term:`modules <module>`.
The name of the :term:`project` and the name of the :term:`distribution package` are one and the same.
It is the name you will see on PyPI, for example.
The name of the project and the name of the top-level :term:`import package` (or :term:`module`) can be different.

Moreover, one PyPI project/dist may ship more than one module or importable package — it is only possible that one matches the name, others can't.
It is recommended to have only one importable package, with a name as similar as possible as the `dist-info` file in the installation folder.

Project names (usually found in :file:`pyproject.toml`) and import package names follow different rules and conventions.
The normalized form (and thus the preferred form) for project names
is the so-called "kebab case" (see :ref:`name normalization`), for example ``abcd-1234``.
But import packages and modules should have a valid Python identifier as a name.

With an import package name ``abcd-1234``, the following would not work:
.. code-block:: pycon

   >>> import abcd-1234
   >>> from abcd-1234 import something

Since ``abcd-1234`` is not a valid Python identifier.
(Importing such a module would be cumbersome, completely unnatural and against the long-established conventions in the Python community;
see, for example, :pep:`8#package-and-module-names`.
There is a way to import it anyway, see :doc:`importlib <python:library/importlib>` and this question_.)

:ref:`Python identifiers <python:identifiers>` follow the so-called "snake case".
The preferred form for an import package name is ``abcd_1234`` which is a valid Python identifier.
Note the underscore ``_`` as separation character instead of of the dash ``-`` seen in the project name.

Having a directory structure with ``src/abcd_1234/`` instead of ``src/abcd-1234/`` has 2 consequences:

- The following works:

  .. code-block:: pycon

     >>> import abcd_1234
     >>> from abcd_1234 import something

- All four build backends covered in the tutorial :doc:`/tutorials/packaging-projects` will work:

  - Flit will not crash with an error;
  - Hatch will recognize that the module corresponding to the package is ``abcd_1234`` instead of defaulting to ``src`` and building a not working wheel.

More information about :doc:`Python imports <python:reference/import>` and its :doc:`grammar <python:reference/grammar>`.

.. _question: https://stackoverflow.com/questions/8350853/how-to-import-module-when-module-name-has-a-dash-or-hyphen-in-it
