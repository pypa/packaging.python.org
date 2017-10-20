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

Entry points were developed as part of setuptools. This document aims to
describe the mechanism that is already a de-facto standard.

Data model
==========

Conceptually, an entry point is defined by three required properties:

- The **group** that an entry point belongs to indicates what sort of object it
  provides. For instance, the group ``console_scripts`` is for entry points
  referring to functions which can be used as a command, while
  ``pygments.styles`` is the group for classes defining pygments styles.
  The consumer typically defines the expected interface. To avoid clashes,
  consumers defining a new group should use names starting with a PyPI name
  owned by the consumer project, followed by ``.``.

- The **name** identifies this entry point within its group. The precise meaning
  of this is up to the consumer. For console scripts, the name of the entry point
  is the command that will be used to launch it. Within a distribution, entry
  point names should be unique. If different distributions provide the same
  name, the consumer decides how to handle that.

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

The precise functionality of entry points with extras is tied to setuptools'
model of adding ``.egg`` directories to ``sys.path`` at runtime. Other
installation mechanisms (such as pip and virtualenv) work differently. Packages
declaring entry points should not assume that extras have any particular effect
on the environment of the code using the entry points.

File format
===========

Entry points are defined in a file called ``entry_points.txt`` in the
``*.dist-info`` directory of the distribution. This is the directory described
in :pep:`376` for installed distributions, and in :pep:`427` for wheels.
The file uses the UTF-8 character encoding.

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
