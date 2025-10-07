.. _dependency-groups:

=================
Dependency Groups
=================

This specification defines Dependency Groups, a mechanism for storing package
requirements in ``pyproject.toml`` files such that they are not included in
project metadata when it is built.

Dependency Groups are suitable for internal development use-cases like linting
and testing, as well as for projects which are not built for distribution, like
collections of related scripts.

Fundamentally, Dependency Groups should be thought of as being a standardized
subset of the capabilities of ``requirements.txt`` files (which are
``pip``-specific).

Specification
=============

Examples
--------

This is a simple table which shows ``docs`` and ``test`` groups::

    [dependency-groups]
    docs = ["sphinx"]
    test = ["pytest>7", "coverage"]

and a similar table which defines ``docs``, ``test``, and ``coverage`` groups::

    [dependency-groups]
    docs = ["sphinx"]
    coverage = ["coverage[toml]"]
    test = ["pytest>7", {include-group = "coverage"}]

The ``[dependency-groups]`` Table
---------------------------------

Dependency Groups are defined as a table in ``pyproject.toml`` named
``dependency-groups``. The ``dependency-groups`` table contains an arbitrary
number of user-defined keys, each of which has, as its value, a list of
requirements.

``[dependency-groups]`` keys, sometimes also called "group names", must be
:ref:`valid non-normalized names <name-format>`. Tools which handle Dependency
Groups MUST :ref:`normalize <name-normalization>` these names before
comparisons.

Tools SHOULD prefer to present the original, non-normalized name to users, and
if duplicate names are detected after normalization, tools SHOULD emit an
error.

Requirement lists, the values in ``[dependency-groups]``, may contain strings,
tables (``dict`` in Python), or a mix of strings and tables. Strings must be
valid :ref:`dependency specifiers <dependency-specifiers>`, and tables must be
valid Dependency Group Includes.

Dependency Group Include
------------------------

A Dependency Group Include includes another Dependency Group in the current
group.

An include is a table with exactly one key, ``"include-group"``, whose value is
a string, the name of another Dependency Group.

Includes are defined to be exactly equivalent to the contents of the named
Dependency Group, inserted into the current group at the location of the include.
For example, if ``foo = ["a", "b"]`` is one group, and
``bar = ["c", {include-group = "foo"}, "d"]`` is another, then ``bar`` should
evaluate to ``["c", "a", "b", "d"]`` when Dependency Group Includes are expanded.

Dependency Group Includes may specify the same package multiple times.
Tools SHOULD NOT deduplicate or otherwise alter the list contents produced by the
include. For example, given the following table:

.. code-block:: toml

    [dependency-groups]
    group-a = ["foo"]
    group-b = ["foo>1.0"]
    group-c = ["foo<1.0"]
    all = [
        "foo",
        {include-group = "group-a"},
        {include-group = "group-b"},
        {include-group = "group-c"},
    ]

The resolved value of ``all`` SHOULD be ``["foo", "foo", "foo>1.0", "foo<1.0"]``.
Tools should handle such a list exactly as they would handle any other case in
which they are asked to process the same requirement multiple times with
different version constraints.

Dependency Group Includes may include groups containing Dependency Group Includes,
in which case those includes should be expanded as well. Dependency Group Includes
MUST NOT include cycles, and tools SHOULD report an error if they detect a cycle.

Package Building
----------------

Build backends MUST NOT include Dependency Group data in built distributions as
package metadata. This means that sdist ``PKG-INFO`` and wheel ``METADATA``
files should not include referenceable fields containing Dependency Groups.

It is, however, valid to use Dependency Groups in the evaluation of dynamic
metadata, and ``pyproject.toml`` files included in sdists will still contain
``[dependency-groups]``. However, the table's contents are not part of a built
package's interfaces.

Installing Dependency Groups & Extras
-------------------------------------

There is no syntax or specification-defined interface for installing or
referring to Dependency Groups. Tools are expected to provide dedicated
interfaces for this purpose.

Tools MAY choose to provide the same or similar interfaces for interacting
with Dependency Groups as they do for managing extras. Tools authors are
advised that the specification does not forbid having an extra whose name
matches a Dependency Group. Separately, users are advised to avoid creating
Dependency Groups whose names match extras, and tools MAY treat such matching
as an error.

Validation and Compatibility
----------------------------

Tools supporting Dependency Groups may want to validate data before using it.
When implementing such validation, authors should be aware of the possibility
of future extensions to the specification, so that they do not unnecessarily
emit errors or warnings.

Tools SHOULD error when evaluating or processing unrecognized data in
Dependency Groups.

Tools SHOULD NOT eagerly validate the contents of *all* Dependency Groups
unless they have a need to do so.

This means that in the presence of the following data, most tools should allow
the ``foo`` group to be used and only error if the ``bar`` group is used:

.. code-block:: toml

    [dependency-groups]
    foo = ["pyparsing"]
    bar = [{set-phasers-to = "stun"}]

.. note::

    There are several known cases of tools which have good cause to be
    stricter. Linters and validators are an example, as their purpose is to
    validate the contents of all Dependency Groups.

Reference Implementation
========================

The following Reference Implementation prints the contents of a Dependency
Group to stdout, newline delimited.
The output is therefore valid ``requirements.txt`` data.

.. code-block:: python

    import re
    import sys
    import tomllib
    from collections import defaultdict

    from packaging.requirements import Requirement


    def _normalize_name(name: str) -> str:
        return re.sub(r"[-_.]+", "-", name).lower()


    def _normalize_group_names(dependency_groups: dict) -> dict:
        original_names = defaultdict(list)
        normalized_groups = {}

        for group_name, value in dependency_groups.items():
            normed_group_name = _normalize_name(group_name)
            original_names[normed_group_name].append(group_name)
            normalized_groups[normed_group_name] = value

        errors = []
        for normed_name, names in original_names.items():
            if len(names) > 1:
                errors.append(f"{normed_name} ({', '.join(names)})")
        if errors:
            raise ValueError(f"Duplicate dependency group names: {', '.join(errors)}")

        return normalized_groups


    def _resolve_dependency_group(
        dependency_groups: dict, group: str, past_groups: tuple[str, ...] = ()
    ) -> list[str]:
        if group in past_groups:
            raise ValueError(f"Cyclic dependency group include: {group} -> {past_groups}")

        if group not in dependency_groups:
            raise LookupError(f"Dependency group '{group}' not found")

        raw_group = dependency_groups[group]
        if not isinstance(raw_group, list):
            raise ValueError(f"Dependency group '{group}' is not a list")

        realized_group = []
        for item in raw_group:
            if isinstance(item, str):
                # packaging.requirements.Requirement parsing ensures that this is a valid
                # PEP 508 Dependency Specifier
                # raises InvalidRequirement on failure
                Requirement(item)
                realized_group.append(item)
            elif isinstance(item, dict):
                if tuple(item.keys()) != ("include-group",):
                    raise ValueError(f"Invalid dependency group item: {item}")

                include_group = _normalize_name(next(iter(item.values())))
                realized_group.extend(
                    _resolve_dependency_group(
                        dependency_groups, include_group, past_groups + (group,)
                    )
                )
            else:
                raise ValueError(f"Invalid dependency group item: {item}")

        return realized_group


    def resolve(dependency_groups: dict, group: str) -> list[str]:
        if not isinstance(dependency_groups, dict):
            raise TypeError("Dependency Groups table is not a dict")
        if not isinstance(group, str):
            raise TypeError("Dependency group name is not a str")
        return _resolve_dependency_group(dependency_groups, group)


    if __name__ == "__main__":
        with open("pyproject.toml", "rb") as fp:
            pyproject = tomllib.load(fp)

        dependency_groups_raw = pyproject["dependency-groups"]
        dependency_groups = _normalize_group_names(dependency_groups_raw)
        print("\n".join(resolve(pyproject["dependency-groups"], sys.argv[1])))

History
=======

- October 2024: This specification was approved through :pep:`735`.
