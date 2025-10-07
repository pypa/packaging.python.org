==================
License Expression
==================

:pep:`639` defined a new :ref:`pyproject.toml's license <pyproject-toml-license>`
value and added a corresponding :ref:`core metadata License-Expression field
<core-metadata-license-expression>`.
This specification defines which license expressions are acceptable.


Specification
=============

License can be defined as a text string that is a valid SPDX
:term:`license expression <License Expression>`,
as documented in the `SPDX specification <spdxpression_>`__,
either Version 2.2 or a later compatible version.

A license expression can use the following license identifiers:

- Any SPDX-listed license short-form identifiers that are published in
  the `SPDX License List <spdxlist_>`__,
  version 3.17 or any later compatible version.

- The custom ``LicenseRef-[idstring]`` string(s), where ``[idstring]`` is
  a unique string containing letters, numbers, ``.`` and/or ``-``,
  to identify licenses that are not included in the SPDX license list.
  The custom identifiers must follow the SPDX specification,
  `clause 10.1 <spdxcustom_>`__ of the given specification version.


Examples of valid license expressions:

.. code-block:: yaml

    MIT
    BSD-3-Clause
    MIT AND (Apache-2.0 OR BSD-2-Clause)
    MIT OR GPL-2.0-or-later OR (FSFUL AND BSD-2-Clause)
    GPL-3.0-only WITH Classpath-Exception-2.0 OR BSD-3-Clause
    LicenseRef-Special-License OR CC0-1.0 OR Unlicense
    LicenseRef-Proprietary


Examples of invalid license expressions:

.. code-block:: yaml

    Use-it-after-midnight  # No `LicenseRef` prefix
    Apache-2.0 OR 2-BSD-Clause  # 2-BSD-Clause is not a valid SPDX identifier
    LicenseRef-License with spaces  # spaces are not allowed
    LicenseRef-License_with_underscores  # underscore are not allowed

.. _spdxcustom: https://spdx.github.io/spdx-spec/v2.2.2/other-licensing-information-detected/
.. _spdxlist: https://spdx.org/licenses/
.. _spdxpression: https://spdx.github.io/spdx-spec/v2.2.2/SPDX-license-expressions/
