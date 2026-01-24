.. highlight:: text

.. _dependency-specifiers:

=====================
Dependency specifiers
=====================

This document defines the format used to specify dependencies on other projects.
The language defined is a compact line based format which was adapted from the
format originally used in ``pip`` requirements files.

The job of a dependency is to enable tools like pip [#pip]_ to find the right
package to install. Sometimes this is very loose - just specifying a name, and
sometimes very specific - referring to a specific file to install. Sometimes
dependencies are only relevant on one platform, or only some versions are
acceptable, so the language permits describing all these cases.

Whether tools should be strict or permissive in their processing of dependency
specifiers is largely dependent on the role of the tool in the wider ecosystem:

* publishing tools and index servers SHOULD be strict in their processing for
  new releases, encouraging the consistency of published specifiers to improve
  over time
* locking and installation tools MAY be permissive in their processing, allowing
  consumption of older packages which may contain dependency specifiers that are
  arguably nonsensical

Specification
=============

Examples
--------

All features of the language shown with a name based lookup::

    requests [security,tests] >= 2.8.1, == 2.8.* ; python_version < "3.7"

A minimal URL based lookup::

    pip @ https://github.com/pypa/pip/archive/1.3.1.zip#sha1=da9234ee9982d4bbb3c72346a6de940a148ea686

Concepts
--------

A dependency specification always specifies a distribution name. It may
include extras, which expand the dependencies of the named distribution to
enable optional features. The version installed can be controlled using
version limits, or giving the URL to a specific artifact to install. Finally
the dependency can be made conditional using environment markers.

Grammar
-------

We first cover the grammar briefly and then drill into the semantics of each
section later.

A distribution specification is written in ASCII text. We use a parsley
[#parsley]_ grammar to provide a precise grammar. It is expected that the
specification will be embedded into a larger system which offers framing such
as comments, multiple line support via continuations, or other such features.

The full grammar including annotations to build a useful parse tree is
included at the end of this document.

Versions may be specified according to the rules of the
:ref:`Version specifier specification <version-specifiers>`. (Note:
URI is defined in :rfc:`std-66 <3986>`)::

    version_cmp   = wsp* '<=' | '<' | '!=' | '===' | '==' | '>=' | '>' | '~='
    version       = wsp* ( letterOrDigit | '-' | '_' | '.' | '*' | '+' | '!' )+
    version_one   = version_cmp version wsp*
    version_many  = version_one (',' version_one)* (',' wsp*)?
    versionspec   = ( '(' version_many ')' ) | version_many
    urlspec       = '@' wsp* <URI_reference>

Environment markers allow making a specification only take effect in some
environments::

    marker_op     = version_cmp | (wsp+ 'in' wsp+) | (wsp+ 'not' wsp+ 'in' wsp+)
    python_str_c  = (wsp | letter | digit | '(' | ')' | '.' | '{' | '}' |
                     '-' | '_' | '*' | '#' | ':' | ';' | ',' | '/' | '?' |
                     '[' | ']' | '!' | '~' | '`' | '@' | '$' | '%' | '^' |
                     '&' | '=' | '+' | '|' | '<' | '>' )
    dquote        = '"'
    squote        = '\\''
    python_str    = (squote (python_str_c | dquote)* squote |
                     dquote (python_str_c | squote)* dquote)
    env_var       = ('python_version' | 'python_full_version' |
                     'os_name' | 'sys_platform' | 'platform_release' |
                     'platform_system' | 'platform_version' |
                     'platform_machine' | 'platform_python_implementation' |
                     'implementation_name' | 'implementation_version' |
                     'extra' | 'extras' | 'dependency_groups' # ONLY when defined by a containing layer
                     )
    marker_var    = wsp* (env_var | python_str)
    marker_expr   = marker_var marker_op marker_var
                  | wsp* '(' marker wsp* ')'
    marker_and    = marker_expr wsp* 'and' marker_expr
                  | marker_expr
    marker_or     = marker_and wsp* 'or' marker_and
                      | marker_and
    marker        = marker_or
    quoted_marker = ';' wsp* marker

Optional components of a distribution may be specified using the extras
field::

    identifier_end = letterOrDigit | (('-' | '_' | '.' )* letterOrDigit)
    identifier    = letterOrDigit identifier_end*
    name          = identifier
    extras_list   = identifier (wsp* ',' wsp* identifier)*
    extras        = '[' wsp* extras_list? wsp* ']'

Giving us a rule for name based requirements::

    name_req      = name wsp* extras? wsp* versionspec? wsp* quoted_marker?

And a rule for direct reference specifications::

    url_req       = name wsp* extras? wsp* urlspec (wsp+ quoted_marker?)?

Leading to the unified rule that can specify a dependency.::

    specification = wsp* ( url_req | name_req ) wsp*

Whitespace
----------

Non line-breaking whitespace is mostly optional with no semantic meaning. The
sole exceptions are detecting the end of a URL requirement and inside user
supplied constants in environment markers.

.. _dependency-specifiers-names:

Names
-----

Distribution names are defined in the :ref:`Core metadata <core-metadata-name>`.
Names act as the primary identifier for distributions. They are present in all
dependency specifications, and are sufficient to be a specification on their
own.

Valid distribution names are defined in the :ref:`name format specification
<name-format>`.


.. _dependency-specifiers-extras:

Extras
------

An extra is an optional part of a distribution. Distributions can specify as
many extras as they wish, and each extra results in the declaration of
additional dependencies of the distribution **when** the extra is used in a
dependency specification. For instance::

    requests[security,tests]

Extras union in the dependencies they define with the dependencies of the
distribution they are attached to. The example above would result in requests
being installed, and requests own dependencies, and also any dependencies that
are listed in the "security" extra of requests.

If multiple extras are listed, all the dependencies are unioned together.

Restrictions on names for extras are defined in the
:ref:`Core metadata specification <core-metadata-provides-extra>`. Publication
tools SHOULD enforce these restrictions in dependency specifiers, while locking
and installation tools MAY normalize invalid extra names in order to accept
published metadata using core metadata versions prior to 2.3.

.. _dependency-specifiers-versions:

Versions
--------

See the :ref:`Version specifier specification <version-specifiers>` for
more detail on both version numbers and version comparisons. Version
specifications limit the versions of a distribution that can be
used. They only apply to distributions looked up by name, rather than
via a URL. Version comparisons are also used in environment markers. The
optional brackets around a version are present for compatibility with
:pep:`345` but should not be generated, only accepted.

.. _dependency-specifiers-environment-markers:

Environment Markers
-------------------

Environment markers allow a dependency specification to provide a rule that
describes when the dependency should be used. For instance, consider a package
that needs ``pywin32`` when running on Windows. This can be expressed as::

    pywin32; sys_platform == "win32"

A marker expression evaluates to either True or False for a given deployment
environment. When it evaluates to False, the dependency should be ignored.

The marker language is inspired by Python itself, chosen for the ability to
safely evaluate it without running arbitrary code that could become a security
vulnerability.

Markers were first defined in :pep:`345`, formally specified in :pep:`508`,
then subsequently amended over time (amendments since :pep:`508` are recorded
:ref:`at the end of this specification <dependency-specifier-history>`).

Marker field types
''''''''''''''''''

Environment marker fields are each defined as one of the following types:

* ``String``: the contents of the field are always treated as an opaque string.
* ``Set of strings``: the contents of the field are always treated as a set
  containing opaque strings. In comparisons, the user supplied constant MUST
  still be a single string (as set literals are not part of the marker syntax).
* ``Version``: the contents of the field are always expected to be a valid
  :ref:`version specifier <version-specifiers>`. Publishing tools SHOULD emit
  an error if that is not the case, but installation tools MAY fall back to
  treating the field as a string field.
* ``Version | String``: the contents of the field are expected to be a valid
  :ref:`version specifier <version-specifiers>` on some platforms, but an
  opaque string on others. The specifics of this distinction are field dependent
  and whether or not tools actually make the distinction will be tool dependent.

Marker comparisons
''''''''''''''''''

All marker comparison expressions are expected to compare a named marker field
against a given user supplied constant. The type of the comparison is determined
by the comparison operator used and the type of the named field as given
in :ref:`the table below <environment-marker-fields>`. Tools MAY emit an
error if no marker field is referenced in a comparison (that is, both operands
are given as constants).

The follow comparison operations are defined in the marker expression grammar:

* ``==`` (for example, ``sys_platform == "win32"``)
* ``!=`` (for example, ``sys_platform != "win32"``)
* ``>`` (for example, ``python_version > "3.10"``)
* ``>=`` (for example, ``python_version >= "3.10"``)
* ``<`` (for example, ``python_version < "3.10"``)
* ``<=`` (for example, ``python_version <= "3.10"``)
* ``~=`` (for example, ``python_version ~= "3"``)
* ``===`` (for example, ``implementation_version === "not.a.valid.version"``)
* ``in`` (for example, ``"gui" in extras``, ``"SMP" in platform_version``)
* ``not in`` (for example, ``"dev" not in dependency_groups``)

For ``String`` fields, ``==``, ``!=``, ``in``, and ``not in`` are defined as
they are for Python strings (case sensitive, with no value normalization of any
kind). The use of ``~=`` or ``===`` with string fields is
explicitly discouraged, and publishing tools SHOULD emit an error, while locking
and installation tools MAY instead interpret them as equivalent to ``==``. The
use of ordered comparisons (``<``, ``<=``, ``>``, ``>=``) with string fields is
explicitly discouraged (as it makes no semantic sense in the packaging context),
and publishing tools SHOULD emit an error, while locking and installation tools
SHOULD implement the following behavior:

* treat ``>=`` and ``<=`` as equivalent to ``==``
* treat ``>`` and ``<`` as always being False

For ``Set of String`` fields, as there is no marker syntax for set literals,
the only valid operations are ``in`` and ``not in`` comparisons with a user
supplied string literal as the left operand.

For ``Version`` fields, the comparison operations are defined by the
:ref:`Version specifier specification <version-specifiers>` when either both
the marker field value and the user supplied constant can be parsed as valid
version specifiers or the ``===`` arbitrary equivalence comparison operator
is used. When an operator other than ``===`` is used, publishing tools SHOULD
emit an error if the user supplied constant cannot be parsed as a valid version
specifier, while locking and installation tools MAY either emit an error or else
fall back to ``String`` field comparison logic if either the marker field value
or the user supplied constant cannot be parsed as a valid version specifier.
Note that ``in`` and ``not in`` containment checks are NOT valid for ``Version``
fields.

For ``Version | String`` fields, comparison operations are defined as they are
for ``Version`` fields. However, there is no expectation that the parsing of
the marker field value or the user supplied constant as a valid version will
succeed, so tools MUST fall back to processing the field as a ``String`` field.
Alternatively, tools MAY unconditionally treat such fields as ``String`` fields.
Accordingly, comparisons that rely on these fields being processed as
``Version`` field SHOULD NOT be used in environment markers published to public
index servers, but they may be appropriate in more constrained environments.

Composing marker expressions
''''''''''''''''''''''''''''

More complex marker expressions may be composed using the ``and`` and ``or``
logical operators. Parentheses may be used as necessary to control operand
precedence (with all comparison operations having a higher precedence).

For example::

    sys_platform == "ios" or sys_platform == "darwin"
    sys_platform == "linux" and "SMP" in platform_version
    sys_platform == "darwin" and platform_version >= "12"

Python's comparison chaining (such as ``3.4 < python_version < 3.9``) is NOT
supported in environment markers (such expressions must instead be written out
as two separate comparisons joined by ``and``).

User supplied constants
'''''''''''''''''''''''

User supplied constants are always given as strings within either ``'`` or
``"`` quote marks. Triple-quoted multi-line strings are NOT permitted.

Backslash escapes are not specified, although tools MAY support them.
They are not included in the specification because they add complexity and
there is currently no known need for treating user supplied constants as
anything other than either opaque strings or valid version specifiers.

Similarly, non-ASCII character support is not specified, but tools MAY accept
them (usually based on the text encoding of the file or stream containing the
dependency specifier). This may be revisited in the future if it becomes more
common for the runtime variables typically referenced in environment markers to
contain non-ASCII text that users wish to perform comparisons against.

Unknown marker fields
'''''''''''''''''''''

References to unknown marker fields MUST raise an error rather than resulting
in a comparison that evaluates to True or False.

Variables whose value cannot be calculated on a given Python implementation
should evaluate to ``0`` for ``Version`` fields, and an empty string for all
other variables (including ``Version | String`` fields).

.. _dependency-specifiers-environment-marker-fields:
.. _environment-marker-fields:

Defined environment marker fields
'''''''''''''''''''''''''''''''''

Unless otherwise noted below, marker evaluation environments MUST support all
of the following marker fields:

.. list-table::
   :header-rows: 1

   * - Marker
     - Python equivalent
     - Type
     - Sample values
   * - ``os_name``
     - :py:data:`os.name`
     - String
     - ``posix``, ``java``
   * - ``sys_platform``
     - :py:data:`sys.platform`
     - String
     - ``linux``, ``linux2``, ``darwin``, ``java1.8.0_51`` (note that "linux"
       is from Python3 and "linux2" from Python2)
   * - ``platform_machine``
     - :py:func:`platform.machine()`
     - String
     - ``x86_64``
   * - ``platform_python_implementation``
     - :py:func:`platform.python_implementation()`
     - String
     - ``CPython``, ``Jython``
   * - ``platform_release``
     - :py:func:`platform.release()`
     - Version | String
     - ``3.14.1-x86_64-linode39``, ``14.5.0``, ``1.8.0_51``
   * - ``platform_system``
     - :py:func:`platform.system()`
     - String
     - ``Linux``, ``Windows``, ``Java``
   * - ``platform_version``
     - :py:func:`platform.version()`
     - String
     - ``#1 SMP Fri Apr 25 13:07:35 EDT 2014``
       ``Java HotSpot(TM) 64-Bit Server VM, 25.51-b03, Oracle Corporation``
       ``Darwin Kernel Version 14.5.0: Wed Jul 29 02:18:53 PDT 2015; root:xnu-2782.40.9~2/RELEASE_X86_64``
   * - ``python_version``
     - ``'.'.join(platform.python_version_tuple()[:2])``
     - :ref:`Version <version-specifiers>`
     - ``3.4``, ``2.7``
   * - ``python_full_version``
     - :py:func:`platform.python_version()`
     - :ref:`Version <version-specifiers>`
     - ``3.4.0``, ``3.5.0b1``
   * - ``implementation_name``
     - :py:data:`sys.implementation.name <sys.implementation>`
     - String
     - ``cpython``
   * - ``implementation_version``
     - see definition below
     - :ref:`Version <version-specifiers>`
     - ``3.4.0``, ``3.5.0b1``
   * - ``extra``
     - Used to indicate optional dependencies in project dependency metadata.
       An error except when defined by the context interpreting the
       specifier. Publishing tools SHOULD permit use of this field.
     - Special (see below)
     - ``toml``
   * - ``extras``
     - Used to indicate optional public dependencies in lock files. An error
       except when defined by the context interpreting the specifier.
       Publishing tools SHOULD NOT permit use of this field.
     - Set of strings
     - ``{"toml"}``
   * - ``dependency_groups``
     - Used to indicate optional project internal dependencies in lock files.
       An error except when defined by the context interpreting the
       specifier. Publishing tools SHOULD NOT permit use of this field.
     - Set of strings
     - ``{"test"}``

For backwards compatibility with older locking and installation tools, the
``extras`` and ``dependency_groups`` fields are currently only considered
valid in :ref:`lock files <lock-file-spec>` (where they allow consumers of the
lock file to selectively install optional parts of the locked dependency tree).
Publishing tools SHOULD emit an error if projects attempt to use them in their
published metadata, and index servers SHOULD NOT accept uploads referencing
these fields. Outside lock file processing, marker evaluation environments
DO NOT need to define these fields.

The ``extra`` field is also special, as it expects set-like behaviour, but
predates the addition of ``Set of strings`` as a defined marker field type.
Accordingly, for this field only, ``extra == "name"`` is equivalent to
``"name" in extras``, while ``extra != "name"`` is equivalent to
``"name" not in extras``. Other comparison operations on ``extra`` are not
defined and publishing tools SHOULD emit an error, while locking and
installation tools may evaluate them as False. Unlike the newer ``extras``
field, this field SHOULD be accepted by both publishing tools and index
servers. Marker evaluation environments intended for project dependency
declarations will typically need to handle evaluation of ``extra`` field
comparisons, while other evaluations of environment markers will not generally
need to do so.

The ``implementation_version`` marker variable is derived from
:py:data:`sys.implementation.version <sys.implementation>`:

.. code-block:: python

    def format_full_version(info):
        version = '{0.major}.{0.minor}.{0.micro}'.format(info)
        kind = info.releaselevel
        if kind != 'final':
            version += kind[0] + str(info.serial)
        return version

    if hasattr(sys, 'implementation'):
        implementation_version = format_full_version(sys.implementation.version)
    else:
        implementation_version = "0"

.. _dependency-specifiers-grammar:

Complete Grammar
================

The complete parsley grammar::

    wsp           = ' ' | '\t'
    version_cmp   = wsp* <'<=' | '<' | '!=' | '===' | '==' | '>=' | '>' | '~='>
    version       = wsp* <( letterOrDigit | '-' | '_' | '.' | '*' | '+' | '!' )+>
    version_one   = version_cmp:op version:v wsp* -> (op, v)
    version_many  = version_one:v1 (',' version_one)*:v2 (',' wsp*)? -> [v1] + v2
    versionspec   = ('(' version_many:v ')' ->v) | version_many
    urlspec       = '@' wsp* <URI_reference>
    marker_op     = version_cmp | (wsp* 'in') | (wsp* 'not' wsp+ 'in')
    python_str_c  = (wsp | letter | digit | '(' | ')' | '.' | '{' | '}' |
                     '-' | '_' | '*' | '#' | ':' | ';' | ',' | '/' | '?' |
                     '[' | ']' | '!' | '~' | '`' | '@' | '$' | '%' | '^' |
                     '&' | '=' | '+' | '|' | '<' | '>' )
    dquote        = '"'
    squote        = '\\''
    python_str    = (squote <(python_str_c | dquote)*>:s squote |
                     dquote <(python_str_c | squote)*>:s dquote) -> s
    env_var       = ('python_version' | 'python_full_version' |
                     'os_name' | 'sys_platform' | 'platform_release' |
                     'platform_system' | 'platform_version' |
                     'platform_machine' | 'platform_python_implementation' |
                     'implementation_name' | 'implementation_version' |
                     'extra' | 'extras' | 'dependency_groups' # ONLY when defined by a containing layer
                     ):varname -> lookup(varname)
    marker_var    = wsp* (env_var | python_str)
    marker_expr   = marker_var:l marker_op:o marker_var:r -> (o, l, r)
                  | wsp* '(' marker:m wsp* ')' -> m
    marker_and    = marker_expr:l wsp* 'and' marker_expr:r -> ('and', l, r)
                  | marker_expr:m -> m
    marker_or     = marker_and:l wsp* 'or' marker_and:r -> ('or', l, r)
                      | marker_and:m -> m
    marker        = marker_or
    quoted_marker = ';' wsp* marker
    identifier_end = letterOrDigit | (('-' | '_' | '.' )* letterOrDigit)
    identifier    = < letterOrDigit identifier_end* >
    name          = identifier
    extras_list   = identifier:i (wsp* ',' wsp* identifier)*:ids -> [i] + ids
    extras        = '[' wsp* extras_list?:e wsp* ']' -> e
    name_req      = (name:n wsp* extras?:e wsp* versionspec?:v wsp* quoted_marker?:m
                     -> (n, e or [], v or [], m))
    url_req       = (name:n wsp* extras?:e wsp* urlspec:v (wsp+ | end) quoted_marker?:m
                     -> (n, e or [], v, m))
    specification = wsp* ( url_req | name_req ):s wsp* -> s
    # The result is a tuple - name, list-of-extras,
    # list-of-version-constraints-or-a-url, marker-ast or None


    URI_reference = <URI | relative_ref>
    URI           = scheme ':' hier_part ('?' query )? ( '#' fragment)?
    hier_part     = ('//' authority path_abempty) | path_absolute | path_rootless | path_empty
    absolute_URI  = scheme ':' hier_part ( '?' query )?
    relative_ref  = relative_part ( '?' query )? ( '#' fragment )?
    relative_part = '//' authority path_abempty | path_absolute | path_noscheme | path_empty
    scheme        = letter ( letter | digit | '+' | '-' | '.')*
    authority     = ( userinfo '@' )? host ( ':' port )?
    userinfo      = ( unreserved | pct_encoded | sub_delims | ':')*
    host          = IP_literal | IPv4address | reg_name
    port          = digit*
    IP_literal    = '[' ( IPv6address | IPvFuture) ']'
    IPvFuture     = 'v' hexdig+ '.' ( unreserved | sub_delims | ':')+
    IPv6address   = (
                      ( h16 ':'){6} ls32
                      | '::' ( h16 ':'){5} ls32
                      | ( h16 )?  '::' ( h16 ':'){4} ls32
                      | ( ( h16 ':')? h16 )? '::' ( h16 ':'){3} ls32
                      | ( ( h16 ':'){0,2} h16 )? '::' ( h16 ':'){2} ls32
                      | ( ( h16 ':'){0,3} h16 )? '::' h16 ':' ls32
                      | ( ( h16 ':'){0,4} h16 )? '::' ls32
                      | ( ( h16 ':'){0,5} h16 )? '::' h16
                      | ( ( h16 ':'){0,6} h16 )? '::' )
    h16           = hexdig{1,4}
    ls32          = ( h16 ':' h16) | IPv4address
    IPv4address   = dec_octet '.' dec_octet '.' dec_octet '.' dec_octet
    nz            = ~'0' digit
    dec_octet     = (
                      digit # 0-9
                      | nz digit # 10-99
                      | '1' digit{2} # 100-199
                      | '2' ('0' | '1' | '2' | '3' | '4') digit # 200-249
                      | '25' ('0' | '1' | '2' | '3' | '4' | '5') )# %250-255
    reg_name = ( unreserved | pct_encoded | sub_delims)*
    path = (
            path_abempty # begins with '/' or is empty
            | path_absolute # begins with '/' but not '//'
            | path_noscheme # begins with a non-colon segment
            | path_rootless # begins with a segment
            | path_empty ) # zero characters
    path_abempty  = ( '/' segment)*
    path_absolute = '/' ( segment_nz ( '/' segment)* )?
    path_noscheme = segment_nz_nc ( '/' segment)*
    path_rootless = segment_nz ( '/' segment)*
    path_empty    = pchar{0}
    segment       = pchar*
    segment_nz    = pchar+
    segment_nz_nc = ( unreserved | pct_encoded | sub_delims | '@')+
                    # non-zero-length segment without any colon ':'
    pchar         = unreserved | pct_encoded | sub_delims | ':' | '@'
    query         = ( pchar | '/' | '?')*
    fragment      = ( pchar | '/' | '?')*
    pct_encoded   = '%' hexdig
    unreserved    = letter | digit | '-' | '.' | '_' | '~'
    reserved      = gen_delims | sub_delims
    gen_delims    = ':' | '/' | '?' | '#' | '(' | ')?' | '@'
    sub_delims    = '!' | '$' | '&' | '\\'' | '(' | ')' | '*' | '+' | ',' | ';' | '='
    hexdig        = digit | 'a' | 'A' | 'b' | 'B' | 'c' | 'C' | 'd' | 'D' | 'e' | 'E' | 'f' | 'F'

A test program - if the grammar is in a string ``grammar``:

.. code-block:: python

    import os
    import sys
    import platform

    from parsley import makeGrammar

    grammar = """
        wsp ...
        """
    tests = [
        "A",
        "A.B-C_D",
        "aa",
        "name",
        "name<=1",
        "name>=3",
        "name>=3,",
        "name>=3,<2",
        "name@http://foo.com",
        "name [fred,bar] @ http://foo.com ; python_version=='2.7'",
        "name[quux, strange];python_version<'2.7' and platform_version=='2'",
        "name; os_name=='a' or os_name=='b'",
        # Should parse as (a and b) or c
        "name; os_name=='a' and os_name=='b' or os_name=='c'",
        # Overriding precedence -> a and (b or c)
        "name; os_name=='a' and (os_name=='b' or os_name=='c')",
        # should parse as a or (b and c)
        "name; os_name=='a' or os_name=='b' and os_name=='c'",
        # Overriding precedence -> (a or b) and c
        "name; (os_name=='a' or os_name=='b') and os_name=='c'",
        ]

    def format_full_version(info):
        version = '{0.major}.{0.minor}.{0.micro}'.format(info)
        kind = info.releaselevel
        if kind != 'final':
            version += kind[0] + str(info.serial)
        return version

    if hasattr(sys, 'implementation'):
        implementation_version = format_full_version(sys.implementation.version)
        implementation_name = sys.implementation.name
    else:
        implementation_version = '0'
        implementation_name = ''
    bindings = {
        'implementation_name': implementation_name,
        'implementation_version': implementation_version,
        'os_name': os.name,
        'platform_machine': platform.machine(),
        'platform_python_implementation': platform.python_implementation(),
        'platform_release': platform.release(),
        'platform_system': platform.system(),
        'platform_version': platform.version(),
        'python_full_version': platform.python_version(),
        'python_version': '.'.join(platform.python_version_tuple()[:2]),
        'sys_platform': sys.platform,
    }

    compiled = makeGrammar(grammar, {'lookup': bindings.__getitem__})
    for test in tests:
        parsed = compiled(test).specification()
        print("%s -> %s" % (test, parsed))


.. _dependency-specifier-history:

History
=======

- November 2015: This specification was approved through :pep:`508`.
- July 2019: The definition of ``python_version`` was `changed
  <python-version-change_>`_ from ``platform.python_version()[:3]`` to
  ``'.'.join(platform.python_version_tuple()[:2])``, to accommodate potential
  future versions of Python with 2-digit major and minor versions
  (e.g. 3.10). [#future_versions]_
- March 2022: Standardised the normalization of extra names at publication time
  (for core metadata 2.3 and later) through :pep:`685`
- June 2024: The definition of ``version_many`` was changed to allow trailing
  commas, matching with the behavior of the Python implementation that has been
  in use since late 2022.
- April 2025: Added ``extras`` and ``dependency_groups`` marker field for
  :ref:`lock-file-spec` as approved through :pep:`751`.
- August 2025: The suggested name validation regex was fixed to match the field
  specification (it previously finished with ``$`` instead of ``\Z``,
  incorrectly permitting trailing newlines)
- December 2025: Ensure ``===`` is before ``==`` in grammar, to allow arbitrary
  equality comparisons to be parsed.
- January 2026: Amend the definition of environment marker comparison operations
  to restrict version comparison semantics to fields where they make sense,
  make extra name restrictions more explicit, adjust the way ordered comparisons
  are defined for strings, and make the fallback from version comparisons to
  string comparisons when version parsing fails optional. Also provide different
  tool behaviour recommendations for publishing tools vs installation tools.
  This brought the nominal specification into line with the way tools actually
  work. [#marker_comparison_logic]_
- January 2026: fix outdated references inadvertently retained from :pep:`508`


References
==========

.. [#pip] pip, the recommended installer for Python packages
   (http://pip.readthedocs.org/en/stable/)

.. [#parsley] The parsley PEG library.
   (https://pypi.python.org/pypi/parsley/)

.. [#future_versions] Future Python versions might be problematic with the
   definition of Environment Marker Variable ``python_version``
   (https://github.com/python/peps/issues/560)

.. [#marker_comparison_logic] Resolving inconsistencies between actual tool
   behavior and the nominal definitions of environment marker field comparisons
   (https://discuss.python.org/t/spec-change-bugfix-dependency-specifiers-simplification-pep-508/105203)


.. _python-version-change: https://mail.python.org/pipermail/distutils-sig/2018-January/031920.html
