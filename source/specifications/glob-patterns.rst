=================
``glob`` patterns
=================

Some PyPA specifications, e.g. :ref:`pyproject.toml's license-files
<pyproject-toml-license-files>`, accept certain types of *glob patterns*
to match a given string containing wildcards and character ranges against
files and directories. This specification defines which patterns are acceptable
and how they should be handled.


Valid glob patterns
===================

For PyPA purposes, a *valid glob pattern* MUST be a string matched against
filesystem entries as specified below:

- Alphanumeric characters, underscores (``_``), hyphens (``-``) and dots (``.``)
  MUST be matched verbatim.

- Special glob characters: ``*``, ``?``, ``**`` and character ranges: ``[]``
  containing only the verbatim matched characters MUST be supported.
  Within ``[...]``, the hyphen indicates a locale-agnostic range (e.g. ``a-z``,
  order based on Unicode code points).
  Hyphens at the start or end are matched literally.

- Path delimiters MUST be the forward slash character (``/``).

- Patterns always refer to *relative paths*,
  e.g., when used in :file:`pyproject.toml`, patterns should always be
  relative to the directory containing that file.
  Therefore the leading slash character MUST NOT be used.

- Parent directory indicators (``..``) MUST NOT be used.

Any characters or character sequences not covered by this specification are
invalid. Projects MUST NOT use such values.
Tools consuming glob patterns SHOULD reject invalid values with an error.

Literal paths (e.g. :file:`LICENSE`) are valid globs which means they
can also be defined.

Tools consuming glob patterns:

- MUST treat each value as a glob pattern, and MUST raise an error if the
  pattern contains invalid glob syntax.
- MUST raise an error if any individual user-specified pattern does not match
  at least one file.

Examples of valid glob patterns:

.. code-block:: python

   "LICEN[CS]E*"
   "AUTHORS*"
   "licenses/LICENSE.MIT"
   "licenses/LICENSE.CC0"
   "LICENSE.txt"
   "licenses/*"

Examples of invalid glob patterns:

.. code-block:: python

   "..\LICENSE.MIT"
   # .. must not be used.
   # \ is an invalid path delimiter, / must be used.

   "LICEN{CSE*"
   # the { character is not allowed


Reference implementation in Python
==================================

It is possible to defer the majority of the pattern matching against the file
system to the :mod:`glob` module in Python's standard library. It is necessary
however to perform additional validations.

The code below is as a simple reference implementation:

.. code-block:: python

   import os
   import re
   from glob import glob


   def find_pattern(pattern: str) -> list[str]:
       """
       >>> find_pattern("/LICENSE.MIT")
       Traceback (most recent call last):
       ...
       ValueError: Pattern '/LICENSE.MIT' should be relative...
       >>> find_pattern("../LICENSE.MIT")
       Traceback (most recent call last):
       ...
       ValueError: Pattern '../LICENSE.MIT' cannot contain '..'...
       >>> find_pattern("LICEN{CSE*")
       Traceback (most recent call last):
       ...
       ValueError: Pattern 'LICEN{CSE*' contains invalid characters...
       """
       if ".." in pattern:
           raise ValueError(f"Pattern {pattern!r} cannot contain '..'")
       if pattern.startswith((os.sep, "/")) or ":\\" in pattern:
           raise ValueError(
               f"Pattern {pattern!r} should be relative and must not start with '/'"
           )
       if re.match(r'^[\w\-\.\/\*\?\[\]]+$', pattern) is None:
           raise ValueError(f"Pattern '{pattern}' contains invalid characters.")
       found = glob(pattern, recursive=True)
       if not found:
           raise ValueError(f"Pattern '{pattern}' did not match any files.")
       return found
