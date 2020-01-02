.. _`Using MANIFEST.in`:

============================================================
Including files in source distributions with ``MANIFEST.in``
============================================================

When building a :term:`source distribution <Source Distribution (or "sdist")>`
for your package, by default only a minimal set of files are included.  You may
find yourself wanting to include extra files in the source distribution, such
as an authors/contributors file, a :file:`docs/` directory, or a directory of
data files used for testing purposes.  There may even be extra files that you
*need* to include; for example, if your :file:`setup.py` computes your
project's ``long_description`` by reading from both a README and a changelog
file, you'll need to include both those files in the sdist so that people that
build or install from the sdist get the correct results.

Adding & removing files to & from the source distribution is done by writing a
:file:`MANIFEST.in` file at the project root.


How files are included in an sdist
==================================

The following files are included in a source distribution by default:

- all Python source files implied by the ``py_modules`` and ``packages``
  ``setup()`` arguments
- all C source files mentioned in the ``ext_modules`` or ``libraries``
  ``setup()`` arguments
- scripts specified by the ``scripts`` ``setup()`` argument
- all files specified by the ``package_data`` and ``data_files`` ``setup()``
  arguments
- the file specified by the ``license_file`` option in :file:`setup.cfg`
  (setuptools 40.8.0+)
- all files specified by the ``license_files`` option in :file:`setup.cfg`
  (setuptools 42.0.0+)
- all files matching the pattern :file:`test/test*.py`
- :file:`setup.py` (or whatever you called your setup script)
- :file:`setup.cfg`
- :file:`README`
- :file:`README.txt`
- :file:`README.rst` (Python 3.7+ or setuptools 0.6.27+)
- :file:`README.md` (setuptools 36.4.0+)
- :file:`pyproject.toml` (setuptools 43.0.0+)
- :file:`MANIFEST.in`

After adding the above files to the sdist, the commands in :file:`MANIFEST.in`
(if such a file exists) are executed in order to add and remove further files
to & from the sdist.  Default files can even be removed from the sdist with the
appropriate :file:`MANIFEST.in` command.

After processing the :file:`MANIFEST.in` file, setuptools removes the
:file:`build/` directory as well as any directories named :file:`RCS`,
:file:`CVS`, or :file:`.svn` from the sdist, and it adds a :file:`PKG-INFO`
file and an :file:`*.egg-info` directory.  This behavior cannot be changed with
:file:`MANIFEST.in`.


:file:`MANIFEST.in` commands
============================

A :file:`MANIFEST.in` file consists of commands, one per line, instructing
setuptools to add or remove some set of files from the sdist.  The commands
are:

===============================================  ==================================================================================================
Command                                          Description
===============================================  ==================================================================================================
``include pat1 pat2 ...``                        Include all files matching any of the listed patterns
``exclude pat1 pat2 ...``                        Exclude all files matching any of the listed patterns
``recursive-include dir-pattern pat1 pat2 ...``  Include all files under directories matching ``dir-pattern`` that match any of the listed patterns
``recursive-exclude dir-pattern pat1 pat2 ...``  Exclude all files under directories matching ``dir-pattern`` that match any of the listed patterns
``global-include pat1 pat2 ...``                 Include all files anywhere in the source tree matching any of the listed patterns
``global-exclude pat1 pat2 ...``                 Exclude all files anywhere in the source tree matching any of the listed patterns
``graft dir-pattern``                            Include all files under directories matching ``dir-pattern``
``prune dir-pattern``                            Exclude all files under directories matching ``dir-pattern``
===============================================  ==================================================================================================

The patterns here are glob-style patterns: ``*`` matches zero or more regular
filename characters (on Unix, everything except forward slash; on Windows,
everything except backslash and colon); ``?`` matches a single regular filename
character, and ``[chars]`` matches any one of the characters between the square
brackets (which may contain character ranges, e.g., ``[a-z]`` or
``[a-fA-F0-9]``).  Setuptools also has undocumented support for ``**`` matching
zero or more characters including forward slash, backslash, and colon.

Directory patterns are relative to the root of the project directory; e.g.,
``graft example*`` will include a directory named :file:`examples` in the
project root but will not include :file:`docs/examples/`.

File & directory names in :file:`MANIFEST.in` should be ``/``-separated;
setuptools will automatically convert the slashes to the local platform's
appropriate directory separator.

Commands are processed in the order they appear in the :file:`MANIFEST.in`
file.  For example, given the commands::

    graft tests
    global-exclude *.py[cod]

the contents of the directory tree :file:`tests` will first be added to the
sdist, and then after that all files in the sdist with a ``.pyc``, ``.pyo``, or
``.pyd`` extension will be removed from the sdist.  If the commands were in the
opposite order, then ``*.pyc`` files etc. would be only be removed from what
was already in the sdist before adding :file:`tests`, and if :file:`tests`
happened to contain any ``*.pyc`` files, they would end up included in the
sdist because the exclusion happened before they were included.
