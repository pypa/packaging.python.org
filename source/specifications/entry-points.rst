.. _entry-points:

==========================
Entry points specification
==========================

*Entry points* are a mechanism for an installed distribution to advertise
components it provides to be discovered and used by other code. For
example:

- Distributions can specify ``console_scripts`` entry points, each referring to
  a function. When *pip* (or another console_scripts aware installer) installs
  the distribution, it will create a command-line wrapper for each entry point.
- Applications can use entry points to load plugins; e.g. Pygments (a syntax
  highlighting tool) can use additional lexers and styles from separately
  installed packages. For more about this, see
  :doc:`/guides/creating-and-discovering-plugins`.

The entry point file format was originally developed to allow packages built
with setuptools to provide integration point metadata that would be read at
runtime with ``pkg_resources``. It is now defined as a PyPA interoperability
specification in order to allow build tools other than setuptools to publish
``pkg_resources`` compatible entry point metadata, and runtime libraries other
than ``pkg_resources`` to portably read published entry point metadata
(potentially with different caching and conflict resolution strategies).

Data model
==========

Conceptually, an entry point is defined by three required properties:

- The **group** that an entry point belongs to indicates what sort of object it
  provides. For instance, the group ``console_scripts`` is for entry points
  referring to functions which can be used as a command, while
  ``pygments.styles`` is the group for classes defining pygments styles.
  The consumer typically defines the expected interface. To avoid clashes,
  consumers defining a new group should use names starting with a PyPI name
  owned by the consumer project, followed by ``.``. Group names must be one or
  more groups of letters, numbers and underscores, separated by dots (regex
  ``^\w+(\.\w+)*$``).

- The **name** identifies this entry point within its group. The precise meaning
  of this is up to the consumer. For console scripts, the name of the entry point
  is the command that will be used to launch it. Within a distribution, entry
  point names should be unique. If different distributions provide the same
  name, the consumer decides how to handle such conflicts. The name may contain
  any characters except ``=``, but it cannot start or end with any whitespace
  character, or start with ``[``. For new entry points, it is recommended to
  use only letters, numbers, underscores, dots and dashes (regex ``[\w.-]+``).

- The **object reference** points to a Python object. It is either in the form
  ``importable.module``, or ``importable.module:object.attr``. Each of the parts
  delimited by dots and the colon is a valid Python identifier.
  It is intended to be looked up like this::

    import importlib
    modname, qualname_separator, qualname = object_ref.partition(':')
    obj = importlib.import_module(modname)
    if qualname_separator:
        for attr in qualname.split('.'):
            obj = getattr(obj, attr)

.. note::
   Some tools call this kind of object reference by itself an 'entry point', for
   want of a better term, especially where it points to a function to launch a
   program.

There is also an optional property: the **extras** are a set of strings
identifying optional features of the distribution providing the entry point.
If these are specified, the entry point requires the dependencies of those
'extras'. See the metadata field :ref:`metadata_provides_extra`.

Using extras for an entry point is no longer recommended. Consumers should
support parsing them from existing distributions, but may then ignore them.
New publishing tools need not support specifying extras. The functionality of
handling extras was tied to setuptools' model of managing 'egg' packages, but
newer tools such as pip and virtualenv use a different model.

File format
===========

Entry points are defined in a file called :file:`entry_points.txt` in the
:file:`*.dist-info` directory of the distribution. This is the directory
described in :pep:`376` for installed distributions, and in :pep:`427` for
wheels.  The file uses the UTF-8 character encoding.

The file contents are in INI format, as read by Python's :mod:`configparser`
module. However, configparser treats names as case-insensitive by default,
whereas entry point names are case sensitive. A case-sensitive config parser
can be made like this::

    import configparser

    class CaseSensitiveConfigParser(configparser.ConfigParser):
        optionxform = staticmethod(str)

The entry points file must always use ``=`` to delimit names from values
(whereas configparser also allows using ``:``).

The sections of the config file represent entry point groups, the names are
names, and the values encode both the object reference and the optional extras.
If extras are used, they are a comma-separated list inside square brackets.

Within a value, readers must accept and ignore spaces (including multiple
consecutive spaces) before or after the colon, between the object reference and
the left square bracket, between the extra names and the square brackets and
colons delimiting them, and after the right square bracket. The syntax for
extras is formally specified as part of :pep:`508` (as ``extras``).
For tools writing the file, it is recommended only to insert a space between the
object reference and the left square bracket.

For example::

    [console_scripts]
    foo = foomod:main
    # One which depends on extras:
    foobar = foomod:main_bar [bar,baz]

    # pytest plugins refer to a module, so there is no ':obj'
    [pytest11]
    nbval = nbval.plugin

Use for scripts
===============

Two groups of entry points have special significance in packaging:
``console_scripts`` and ``gui_scripts``. In both groups, the name of the entry
point should be usable as a command in a system shell after the package is
installed. The object reference points to a function which will be called with
no arguments when this command is run. The function may return an integer to be
used as a process exit code, and returning ``None`` is equivalent to returning
``0``.

For instance, the entry point ``mycmd = mymod:main`` would create a command
``mycmd`` launching a script like this::

    import sys
    from mymod import main
    sys.exit(main())

The difference between ``console_scripts`` and ``gui_scripts`` only affects
Windows systems. ``console_scripts`` are wrapped in a console executable,
so they are attached to a console and can use ``sys.stdin``, ``sys.stdout`` and
``sys.stderr`` for input and output. ``gui_scripts`` are wrapped in a GUI
executable, so they can be started without a console, but cannot use standard
streams unless application code redirects them. Other platforms do not have the
same distinction.

Install tools are expected to set up wrappers for both ``console_scripts`` and
``gui_scripts`` in the scripts directory of the install scheme. They are not
responsible for putting this directory in the ``PATH`` environment variable
which defines where command-line tools are found.

As files are created from the names, and some filesystems are case-insensitive,
packages should avoid using names in these groups which differ only in case.
The behaviour of install tools when names differ only in case is undefined.
