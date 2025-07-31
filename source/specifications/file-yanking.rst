.. _file-yanking:

============
File Yanking
============

.. note::

    This specification was originally defined in
    :pep:`592`.

.. note::

    :pep:`592` includes changes to the HTML and JSON index APIs.
    These changes are documented in the :ref:`simple-repository-api`
    under :ref:`HTML - Project Detail <simple-repository-html-project-detail>`
    and :ref:`JSON - Project Detail <simple-repository-json-project-detail>`.

Specification
=============

Links in the simple repository **MAY** have a ``data-yanked`` attribute
which may have no value, or may have an arbitrary string as a value. The
presence of a ``data-yanked`` attribute **SHOULD** be interpreted as
indicating that the file pointed to by this particular link has been
"Yanked", and should not generally be selected by an installer, except
under specific scenarios.

The value of the ``data-yanked`` attribute, if present, is an arbitrary
string that represents the reason for why the file has been yanked. Tools
that process the simple repository API **MAY** surface this string to
end users.

The yanked attribute is not immutable once set, and may be rescinded in
the future (and once rescinded, may be reset as well). Thus API users
**MUST** be able to cope with a yanked file being "unyanked" (and even
yanked again).

Installers
----------

The desirable experience for users is that once a file is yanked, when
a human being is currently trying to directly install a yanked file, that
it fails as if that file had been deleted. However, when a human did that
awhile ago, and now a computer is just continuing to mechanically follow
the original order to install the now yanked file, then it acts as if it
had not been yanked.

An installer **MUST** ignore yanked releases, if the selection constraints
can be satisfied with a non-yanked version, and **MAY** refuse to use a
yanked release even if it means that the request cannot be satisfied at all.
An implementation **SHOULD** choose a policy that follows the spirit of the
intention above, and that prevents "new" dependencies on yanked
releases/files.

What this means is left up to the specific installer, to decide how to best
fit into the overall usage of their installer. However, there are two
suggested approaches to take:

1. Yanked files are always ignored, unless they are the only file that
   matches a version specifier that "pins" to an exact version using
   either ``==`` (without any modifiers that make it a range, such as
   ``.*``) or ``===``. Matching this version specifier should otherwise
   be done as per :ref:`the version specifiers specification
   <version-specifiers>` for things like local versions, zero padding,
   etc.
2. Yanked files are always ignored, unless they are the only file that
   matches what a lock file (such as ``Pipfile.lock`` or ``poetry.lock``)
   specifies to be installed. In this case, a yanked file **SHOULD** not
   be used when creating or updating a lock file from some input file or
   command.

Regardless of the specific strategy that an installer chooses for deciding
when to install yanked files, an installer **SHOULD** emit a warning when
it does decide to install a yanked file. That warning **MAY** utilize the
value of the ``data-yanked`` attribute (if it has a value) to provide more
specific feedback to the user about why that file had been yanked.


Mirrors
-------

Mirrors can generally treat yanked files one of two ways:

1. They may choose to omit them from their simple repository API completely,
   providing a view over the repository that shows only "active", unyanked
   files.
2. They may choose to include yanked files, and additionally mirror the
   ``data-yanked`` attribute as well.

Mirrors **MUST NOT** mirror a yanked file without also mirroring the
``data-yanked`` attribute for it.
