.. _inline-script-metadata:

======================
Inline script metadata
======================

This specification defines a metadata format that can be embedded in single-file
Python scripts to assist launchers, IDEs and other external tools which may need
to interact with such scripts.


Specification
=============

This specification defines a metadata comment block format (loosely inspired by
`reStructuredText Directives`__).

__ https://docutils.sourceforge.io/docs/ref/rst/directives.html

Any Python script may have top-level comment blocks that MUST start with the
line ``# /// TYPE`` where ``TYPE`` determines how to process the content. That
is: a single ``#``, followed by a single space, followed by three forward
slashes, followed by a single space, followed by the type of metadata. Block
MUST end with the line ``# ///``. That is: a single ``#``, followed by a single
space, followed by three forward slashes. The ``TYPE`` MUST only consist of
ASCII letters, numbers and hyphens.

Every line between these two lines (``# /// TYPE`` and ``# ///``) MUST be a
comment starting with ``#``. If there are characters after the ``#`` then the
first character MUST be a space. The embedded content is formed by taking away
the first two characters of each line if the second character is a space,
otherwise just the first character (which means the line consists of only a
single ``#``).

Precedence for an ending line ``# ///`` is given when the next line is not
a valid embedded content line as described above. For example, the following
is a single fully valid block:

.. code:: python

    # /// some-toml
    # embedded-csharp = """
    # /// <summary>
    # /// text
    # ///
    # /// </summary>
    # public class MyClass { }
    # """
    # ///

A starting line MUST NOT be placed between another starting line and its ending
line. In such cases tools MAY produce an error. Unclosed blocks MUST be ignored.

When there are multiple comment blocks of the same ``TYPE`` defined, tools MUST
produce an error.

Tools reading embedded metadata MAY respect the standard Python encoding
declaration. If they choose not to do so, they MUST process the file as UTF-8.

This is the canonical regular expression that MAY be used to parse the
metadata:

.. code:: text

    (?m)^# /// (?P<type>[a-zA-Z0-9-]+)$\s(?P<content>(^#(| .*)$\s)+)^# ///$

In circumstances where there is a discrepancy between the text specification
and the regular expression, the text specification takes precedence.

Tools MUST NOT read from metadata blocks with types that have not been
standardized by this specification.

script type
-----------

The first type of metadata block is named ``script``, which contains
script metadata (dependency data and tool configuration).

This document MAY include the top-level fields ``dependencies`` and ``requires-python``,
and MAY optionally include a ``[tool]`` table.

The ``[tool]`` MAY be used by any tool, script runner or otherwise, to configure
behavior. It has the same semantics as the :ref:`[tool] table in pyproject.toml
<pyproject-tool-table>`.

The top-level fields are:

* ``dependencies``: A list of strings that specifies the runtime dependencies
  of the script. Each entry MUST be a valid
  :ref:`dependency specifier <dependency-specifiers>`.
* ``requires-python``: A string that specifies the Python version(s) with which
  the script is compatible. The value of this field MUST be a valid
  :ref:`version specifier <version-specifiers>`.

Script runners MUST error if the specified ``dependencies`` cannot be provided.
Script runners SHOULD error if no version of Python that satisfies the specified
``requires-python`` can be provided.

Example
-------

The following is an example of a script with embedded metadata:

.. code:: python

    # /// script
    # requires-python = ">=3.11"
    # dependencies = [
    #   "requests<3",
    #   "rich",
    # ]
    # ///

    import requests
    from rich.pretty import pprint

    resp = requests.get("https://peps.python.org/api/peps.json")
    data = resp.json()
    pprint([(k, v["title"]) for k, v in data.items()][:10])


Reference Implementation
========================

The following is an example of how to read the metadata on Python 3.11 or
higher.

.. code:: python

   import re
   import tomllib

   REGEX = r'(?m)^# /// (?P<type>[a-zA-Z0-9-]+)$\s(?P<content>(^#(| .*)$\s)+)^# ///$'

   def read(script: str) -> dict | None:
       name = 'script'
       matches = list(
           filter(lambda m: m.group('type') == name, re.finditer(REGEX, script))
       )
       if len(matches) > 1:
           raise ValueError(f'Multiple {name} blocks found')
       elif len(matches) == 1:
           content = ''.join(
               line[2:] if line.startswith('# ') else line[1:]
               for line in matches[0].group('content').splitlines(keepends=True)
           )
           return tomllib.loads(content)
       else:
           return None

Often tools will edit dependencies like package managers or dependency update
automation in CI. The following is a crude example of modifying the content
using the ``tomlkit`` library__.

__ https://tomlkit.readthedocs.io/en/latest/

.. code:: python

   import re

   import tomlkit

   REGEX = r'(?m)^# /// (?P<type>[a-zA-Z0-9-]+)$\s(?P<content>(^#(| .*)$\s)+)^# ///$'

   def add(script: str, dependency: str) -> str:
       match = re.search(REGEX, script)
       content = ''.join(
           line[2:] if line.startswith('# ') else line[1:]
           for line in match.group('content').splitlines(keepends=True)
       )

       config = tomlkit.parse(content)
       config['dependencies'].append(dependency)
       new_content = ''.join(
           f'# {line}' if line.strip() else f'#{line}'
           for line in tomlkit.dumps(config).splitlines(keepends=True)
       )

       start, end = match.span('content')
       return script[:start] + new_content + script[end:]

Note that this example used a library that preserves TOML formatting. This is
not a requirement for editing by any means but rather is a "nice to have"
feature.

The following is an example of how to read a stream of arbitrary metadata
blocks.

.. code:: python

   import re
   from typing import Iterator

   REGEX = r'(?m)^# /// (?P<type>[a-zA-Z0-9-]+)$\s(?P<content>(^#(| .*)$\s)+)^# ///$'

   def stream(script: str) -> Iterator[tuple[str, str]]:
       for match in re.finditer(REGEX, script):
           yield match.group('type'), ''.join(
               line[2:] if line.startswith('# ') else line[1:]
               for line in match.group('content').splitlines(keepends=True)
           )


Recommendations
===============

Tools that support managing different versions of Python should attempt to use
the highest available version of Python that is compatible with the script's
``requires-python`` metadata, if defined.


History
=======

- October 2023: This specification was conditionally approved through :pep:`723`.
- January 2024: Through amendments to :pep:`723`, the ``pyproject`` metadata
  block type was renamed to ``script``, and the ``[run]`` table was dropped,
  making the ``dependencies`` and ``requires-python`` keys
  top-level. Additionally, the specification is no longer provisional.
