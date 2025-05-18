.. _creating-command-line-tools:

=========================================
Creating and packaging command-line tools
=========================================

This guide will walk you through creating and packaging a standalone command-line application
that can be installed with :ref:`pipx`, a tool for creating and managing :term:`Python Virtual Environments <Virtual Environment>`
and exposing the executable scripts of packages (and available manual pages) for use on the command-line.

Creating the package
====================

First of all, create a source tree for the :term:`project <Project>`. For the sake of an example, we'll
build a simple tool outputting a greeting (a string) for a person based on arguments given on the command-line.

.. todo:: Advise on the optimal structure of a Python package in another guide or discussion and link to it here.

This project will adhere to :ref:`src-layout <src-layout-vs-flat-layout>` and in the end be alike this file tree,
with the top-level folder and package name ``greetings``:

::

    .
    ├── pyproject.toml
    └── src
        └── greetings
            ├── cli.py
            ├── greet.py
            ├── __init__.py
            └── __main__.py

The actual code responsible for the tool's functionality will be stored in the file :file:`greet.py`,
named after the main module:

.. code-block:: python

    import typer
    from typing_extensions import Annotated


    def greet(
        name: Annotated[str, typer.Argument(help="The (last, if --gender is given) name of the person to greet")] = "",
        gender: Annotated[str, typer.Option(help="The gender of the person to greet")] = "",
        knight: Annotated[bool, typer.Option(help="Whether the person is a knight")] = False,
        count: Annotated[int, typer.Option(help="Number of times to greet the person")] = 1
    ):
        greeting = "Greetings, dear "
        masculine = gender == "masculine"
        feminine = gender == "feminine"
        if gender or knight:
            salutation = ""
            if knight:
                salutation = "Sir "
            elif masculine:
                salutation = "Mr. "
            elif feminine:
                salutation = "Ms. "
            greeting += salutation
            if name:
                greeting += f"{name}!"
            else:
                pronoun = "her" if feminine else "his" if masculine or knight else "its"
                greeting += f"what's-{pronoun}-name"
        else:
            if name:
                greeting += f"{name}!"
            elif not gender:
                greeting += "friend!"
        for i in range(0, count):
            print(greeting)

The above function receives several keyword arguments that determine how the greeting to output is constructed.
Now, construct the command-line interface to provision it with the same, which is done
in :file:`cli.py`:

.. code-block:: python

    import typer

    from .greet import greet


    app = typer.Typer()
    app.command()(greet)


    if __name__ == "__main__":
        app()

The command-line interface is built with typer_, an easy-to-use CLI parser based on Python type hints. It provides
auto-completion and nicely styled command-line help out of the box. Another option would be :py:mod:`argparse`,
a command-line parser which is included in Python's standard library. It is sufficient for most needs, but requires
a lot of code, usually in ``cli.py``, to function properly. Alternatively, docopt_ makes it possible to create CLI
interfaces based solely on docstrings; advanced users are encouraged to make use of click_ (on which ``typer`` is based).

Now, add an empty :file:`__init__.py` file, to define the project as a regular :term:`import package <Import Package>`.

The file :file:`__main__.py` marks the main entry point for the application when running it via :mod:`runpy`
(i.e. ``python -m greetings``, which works immediately with flat layout, but requires installation of the package with src layout),
so initialize the command-line interface here:

.. code-block:: python

	if __name__ == "__main__":
	    from greetings.cli import app
	    app()

.. note::

    In order to enable calling the command-line interface directly from the :term:`source tree <Project Source Tree>`,
    i.e. as ``python src/greetings``, a certain hack could be placed in this file; read more at
    :ref:`running-cli-from-source-src-layout`.


``pyproject.toml``
------------------

The project's :term:`metadata <Pyproject Metadata>` is placed in :term:`pyproject.toml`. The :term:`pyproject metadata keys <Pyproject Metadata Key>` and the ``[build-system]`` table may be filled in as described in :ref:`writing-pyproject-toml`, adding a dependency
on ``typer`` (this tutorial uses version *0.12.3*).

For the project to be recognised as a command-line tool, additionally a ``console_scripts`` :ref:`entry point <entry-points>` (see :ref:`console_scripts`) needs to be added as a :term:`subkey <Pyproject Metadata Subkey>`:

.. code-block:: toml

	[project.scripts]
	greet = "greetings.cli:app"

Now, the project's source tree is ready to be transformed into a :term:`distribution package <Distribution Package>`,
which makes it installable.


Installing the package with ``pipx``
====================================

After installing ``pipx`` as described in :ref:`installing-stand-alone-command-line-tools`, install your project:

.. code-block:: console

    $ cd path/to/greetings/
    $ pipx install .

This will expose the executable script we defined as an entry point and make the command ``greet`` available.
Let's test it:

.. code-block:: console

	$ greet --knight Lancelot
	Greetings, dear Sir Lancelot!
	$ greet --gender feminine Parks
	Greetings, dear Ms. Parks!
	$ greet --gender masculine
	Greetings, dear Mr. what's-his-name!

Since this example uses ``typer``, you could now also get an overview of the program's usage by calling it with
the ``--help`` option, or configure completions via the ``--install-completion`` option.

To just run the program without installing it permanently, use ``pipx run``, which will create a temporary
(but cached) virtual environment for it:

.. code-block:: console

	$ pipx run --spec . greet --knight

This syntax is a bit impractical, however; as the name of the entry point we defined above does not match the package name,
we need to state explicitly which executable script to run (even though there is only on in existence).

There is, however, a more practical solution to this problem, in the form of an entry point specific to ``pipx run``.
The same can be defined as follows in :file:`pyproject.toml`:

.. code-block:: toml

    [project.entry-points."pipx.run"]
    greetings = "greetings.cli:app"


Thanks to this entry point (which *must* match the package name), ``pipx`` will pick up the executable script as the
default one and run it, which makes this command possible:

.. code-block:: console

    $ pipx run . --knight

Conclusion
==========

You know by now how to package a command-line application written in Python. A further step could be to distribute your package,
meaning uploading it to a :term:`package index <Package Index>`, most commonly :term:`PyPI <Python Package Index (PyPI)>`. To do that, follow the instructions at :ref:`Packaging your project`. And once you're done, don't forget to :ref:`do some research <analyzing-pypi-package-downloads>` on how your package is received!

.. _click: https://click.palletsprojects.com/
.. _docopt: https://docopt.readthedocs.io/en/latest/
.. _typer: https://typer.tiangolo.com/
