.. _licensing-examples-and-user-scenarios:


=====================================
Licensing examples and user scenarios
=====================================


:pep:`639` has specified the way to declare a project's license and paths to
license files and other legally required information.
This document aims to provide clear guidance how to migrate from the legacy
to the standardized way of declaring licenses.
Make sure your preferred build backend supports :pep:`639` before
trying to apply the newer guidelines.


Licensing Examples
==================

.. _licensing-example-basic:

Basic example
-------------

The Setuptools project itself, as of `version 75.6.0 <setuptools7560_>`__,
does not use the ``License`` field in its own project source metadata.
Further, it no longer explicitly specifies ``license_file``/``license_files``
as it did previously, since Setuptools relies on its own automatic
inclusion of license-related files matching common patterns,
such as the :file:`LICENSE` file it uses.

It includes the following license-related metadata in its
:file:`pyproject.toml`:

.. code-block:: toml

    [project]
    classifiers = [
        "License :: OSI Approved :: MIT License"
    ]

The simplest migration to PEP 639 would consist of using this instead:

.. code-block:: toml

    [project]
    license = "MIT"

Or, if the project used :file:`setup.cfg`, in its ``[metadata]`` table:

.. code-block:: ini

    [metadata]
    license = MIT

The output Core Metadata for the distribution packages would then be:

.. code-block:: email

    License-Expression: MIT
    License-File: LICENSE

The :file:`LICENSE` file would be stored at :file:`/setuptools-{VERSION}/LICENSE`
in the sdist and :file:`/setuptools-{VERSION}.dist-info/licenses/LICENSE`
in the wheel, and unpacked from there into the site directory (e.g.
:file:`site-packages/`) on installation; :file:`/` is the root of the respective archive
and ``{VERSION}`` the version of the Setuptools release in the Core Metadata.


.. _licensing-example-advanced:

Advanced example
----------------

Suppose Setuptools were to include the licenses of the third-party projects
that are vendored in the :file:`setuptools/_vendor/` and :file:`pkg_resources/_vendor/`
directories; specifically:

.. code-block:: text

    packaging==21.2
    pyparsing==2.2.1
    ordered-set==3.1.1
    more_itertools==8.8.0

The license expressions for these projects are:

.. code-block:: text

    packaging: Apache-2.0 OR BSD-2-Clause
    pyparsing: MIT
    ordered-set: MIT
    more_itertools: MIT

A comprehensive license expression covering both Setuptools
proper and its vendored dependencies would contain these metadata,
combining all the license expressions into one. Such an expression might be:

.. code-block:: text

    MIT AND (Apache-2.0 OR BSD-2-Clause)

In addition, per the requirements of the licenses, the relevant license files
must be included in the package. Suppose the :file:`LICENSE` file contains the text
of the MIT license and the copyrights used by Setuptools, ``pyparsing``,
``more_itertools`` and ``ordered-set``; and the :file:`LICENSE*` files in the
:file:`setuptools/_vendor/packaging/` directory contain the Apache 2.0 and
2-clause BSD license text, and the Packaging copyright statement and
`license choice notice <packaginglicense_>`__.

Specifically, we assume the license files are located at the following
paths in the project source tree (relative to the project root and
:file:`pyproject.toml`):

.. code-block:: text

    LICENSE
    setuptools/_vendor/packaging/LICENSE
    setuptools/_vendor/packaging/LICENSE.APACHE
    setuptools/_vendor/packaging/LICENSE.BSD

Putting it all together, our :file:`pyproject.toml` would be:

.. code-block:: toml

    [project]
    license = "MIT AND (Apache-2.0 OR BSD-2-Clause)"
    license-files = [
        "LICENSE*",
        "setuptools/_vendor/LICENSE*",
    ]

Or alternatively, the license files can be specified explicitly (paths will be
interpreted as glob patterns):

.. code-block:: toml

    [project]
    license = "MIT AND (Apache-2.0 OR BSD-2-Clause)"
    license-files = [
        "LICENSE",
        "setuptools/_vendor/LICENSE",
        "setuptools/_vendor/LICENSE.APACHE",
        "setuptools/_vendor/LICENSE.BSD",
    ]

If our project used :file:`setup.cfg`, we could define this in :

.. code-block:: ini

    [metadata]
    license = MIT AND (Apache-2.0 OR BSD-2-Clause)
    license_files =
        LICENSE
        setuptools/_vendor/packaging/LICENSE
        setuptools/_vendor/packaging/LICENSE.APACHE
        setuptools/_vendor/packaging/LICENSE.BSD

With either approach, the output Core Metadata in the distribution
would be:

.. code-block:: email

    License-Expression: MIT AND (Apache-2.0 OR BSD-2-Clause)
    License-File: LICENSE
    License-File: setuptools/_vendor/packaging/LICENSE
    License-File: setuptools/_vendor/packaging/LICENSE.APACHE
    License-File: setuptools/_vendor/packaging/LICENSE.BSD

In the resulting sdist, with :file:`/` as the root of the archive and ``{VERSION}``
the version of the Setuptools release specified in the Core Metadata,
the license files would be located at the paths:

.. code-block:: text

    /setuptools-{VERSION}/LICENSE
    /setuptools-{VERSION}/setuptools/_vendor/packaging/LICENSE
    /setuptools-{VERSION}/setuptools/_vendor/packaging/LICENSE.APACHE
    /setuptools-{VERSION}/setuptools/_vendor/packaging/LICENSE.BSD

In the built wheel, with :file:`/` being the root of the archive and
``{VERSION}`` as the previous, the license files would be stored at:

.. code-block:: text

    /setuptools-{VERSION}.dist-info/licenses/LICENSE
    /setuptools-{VERSION}.dist-info/licenses/setuptools/_vendor/packaging/LICENSE
    /setuptools-{VERSION}.dist-info/licenses/setuptools/_vendor/packaging/LICENSE.APACHE
    /setuptools-{VERSION}.dist-info/licenses/setuptools/_vendor/packaging/LICENSE.BSD

Finally, in the installed project, with :file:`site-packages/` being the site dir
and ``{VERSION}`` as the previous, the license files would be installed to:

.. code-block:: text

    site-packages/setuptools-{VERSION}.dist-info/licenses/LICENSE
    site-packages/setuptools-{VERSION}.dist-info/licenses/setuptools/_vendor/packaging/LICENSE
    site-packages/setuptools-{VERSION}.dist-info/licenses/setuptools/_vendor/packaging/LICENSE.APACHE
    site-packages/setuptools-{VERSION}.dist-info/licenses/setuptools/_vendor/packaging/LICENSE.BSD


Expression examples
'''''''''''''''''''

Some additional examples of valid ``License-Expression`` values:

.. code-block:: email

    License-Expression: MIT
    License-Expression: BSD-3-Clause
    License-Expression: MIT AND (Apache-2.0 OR BSD-2-Clause)
    License-Expression: MIT OR GPL-2.0-or-later OR (FSFUL AND BSD-2-Clause)
    License-Expression: GPL-3.0-only WITH Classpath-Exception-2.0 OR BSD-3-Clause
    License-Expression: LicenseRef-Public-Domain OR CC0-1.0 OR Unlicense
    License-Expression: LicenseRef-Proprietary
    License-Expression: LicenseRef-Custom-License


User Scenarios
==============

The following covers the range of common use cases from a user perspective,
providing guidance for each. Do note that the following
should **not** be considered legal advice, and readers should consult a
licensed legal practitioner in their jurisdiction if they are unsure about
the specifics for their situation.


I have a private package that won't be distributed
--------------------------------------------------

If your package isn't shared publicly, i.e. outside your company,
organization or household, it *usually* isn't strictly necessary to include
a formal license, so you wouldn't necessarily have to do anything extra here.

However, it is still a good idea to include ``LicenseRef-Proprietary``
as a license expression in your package configuration, and/or a
copyright statement and any legal notices in a :file:`LICENSE.txt` file
in the root of your project directory, which will be automatically
included by packaging tools.


I just want to share my own work without legal restrictions
-----------------------------------------------------------

While you aren't required to include a license, if you don't, no one has
`any permission to download, use or improve your work <dontchoosealicense_>`__,
so that's probably the *opposite* of what you actually want.
The `MIT license <chooseamitlicense_>`__ is a great choice instead, as it's simple,
widely used and allows anyone to do whatever they want with your work
(other than sue you, which you probably also don't want).

To apply it, just paste `the text <chooseamitlicense_>`__ into a file named
:file:`LICENSE.txt` at the root of your repo, and add the year and your name to
the copyright line. Then, just add ``license = "MIT"`` under
``[project]`` in your :file:`pyproject.toml` if your packaging tool supports it,
or in its config file/section. You're done!


I want to distribute my project under a specific license
--------------------------------------------------------

To use a particular license, simply paste its text into a :file:`LICENSE.txt`
file at the root of your repo, if you don't have it in a file starting with
:file:`LICENSE` or :file:`COPYING` already, and add
``license = "LICENSE-ID"`` under ``[project]`` in your
:file:`pyproject.toml` if your packaging tool supports it, or else in its
config file. You can find the ``LICENSE-ID``
and copyable license text on sites like
`ChooseALicense <choosealicenselist_>`__ or `SPDX <spdxlist_>`__.

Many popular code hosts, project templates and packaging tools can add the
license file for you, and may support the expression as well in the future.


I maintain an existing package that's already licensed
------------------------------------------------------

If you already have license files and metadata in your project, you
should only need to make a couple of tweaks to take advantage of the new
functionality.

In your project config file, enter your license expression under
``license`` (``[project]`` table in :file:`pyproject.toml`),
or the equivalent for your packaging tool,
and make sure to remove any legacy ``license`` table subkeys or
``License ::`` classifiers. Your existing ``license`` value may already
be valid as one (e.g. ``MIT``, ``Apache-2.0 OR BSD-2-Clause``, etc);
otherwise, check the `SPDX license list <spdxlist_>`__ for the identifier
that matches the license used in your project.

Make sure to list your license files under ``license-files``
under ``[project]`` in :file:`pyproject.toml`
or else in your tool's configuration file.

See the :ref:`licensing-example-basic` for a simple but complete real-world demo
of how this works in practice.
See also the best-effort guidance on how to translate license classifiers
into license expression provided by the :pep:`639` authors:
`Mapping License Classifiers to SPDX Identifiers <mappingclassifierstospdx_>`__.
Packaging tools may support automatically converting legacy licensing
metadata; check your tool's documentation for more information.


My package includes other code under different licenses
-------------------------------------------------------

If your project includes code from others covered by different licenses,
such as vendored dependencies or files copied from other open source
software, you can construct a license expression
to describe the licenses involved and the relationship
between them.

In short, ``License-1 AND License-2`` mean that *both* licenses apply
to your project, or parts of it (for example, you included a file
under another license), and ``License-1 OR License-2`` means that
*either* of the licenses can be used, at the user's option (for example,
you want to allow users a choice of multiple licenses). You can use
parenthesis (``()``) for grouping to form expressions that cover even the most
complex situations.

In your project config file, enter your license expression under
``license`` (``[project]`` table of :file:`pyproject.toml`),
or the equivalent for your packaging tool,
and make sure to remove any legacy ``license`` table subkeys
or ``License ::`` classifiers.

Also, make sure you add the full license text of all the licenses as files
somewhere in your project repository. List the
relative path or glob patterns to each of them under ``license-files``
under ``[project]`` in :file:`pyproject.toml`
(if your tool supports it), or else in your tool's configuration file.

As an example, if your project was licensed MIT but incorporated
a vendored dependency (say, ``packaging``) that was licensed under
either Apache 2.0 or the 2-clause BSD, your license expression would
be ``MIT AND (Apache-2.0 OR BSD-2-Clause)``. You might have a
:file:`LICENSE.txt` in your repo root, and a :file:`LICENSE-APACHE.txt` and
:file:`LICENSE-BSD.txt` in the :file:`_vendor/` subdirectory, so to include
all of them, you'd specify ``["LICENSE.txt", "_vendor/packaging/LICENSE*"]``
as glob patterns, or
``["LICENSE.txt", "_vendor/LICENSE-APACHE.txt", "_vendor/LICENSE-BSD.txt"]``
as literal file paths.

See a fully worked out :ref:`licensing-example-advanced` for an end-to-end
application of this to a real-world complex project, with many technical
details, and consult a `tutorial <spdxtutorial_>`__ for more help and examples
using SPDX identifiers and expressions.


.. _chooseamitlicense: https://choosealicense.com/licenses/mit/
.. _choosealicenselist: https://choosealicense.com/licenses/
.. _dontchoosealicense: https://choosealicense.com/no-permission/
.. _mappingclassifierstospdx: https://peps.python.org/pep-0639/appendix-mapping-classifiers/
.. _packaginglicense: https://github.com/pypa/packaging/blob/21.2/LICENSE
.. _setuptools7560: https://github.com/pypa/setuptools/blob/v75.6.0/pyproject.toml
.. _spdxlist: https://spdx.org/licenses/
.. _spdxtutorial: https://github.com/david-a-wheeler/spdx-tutorial
