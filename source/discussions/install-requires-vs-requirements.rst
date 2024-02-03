.. _`install_requires vs requirements files`:

============================================
Metadata dependencies vs. requirements files
============================================

There are two main places where you will find list of "needed packages to
install", perhaps with version constraints, like ``requests`` or
``requests==2.31.0``. These are metadata dependencies, typically in a
``pyproject.toml`` (or ``setup.py``) file, and requirements files, often called
``requirements.txt``. This page breaks down the differences.

Metadata dependencies
=====================

Packages can declare dependencies, i.e. other packages that they need to
function. The standard method to do so is to set the :ref:`dependencies key
<writing-pyproject-toml-dependencies>` in the ``[project]`` section of a
``pyproject.toml`` file -- although other :term:`build backends <build backend>`
may use different methods. There can also be groups of optional dependencies,
also called "extras", which are typically specified in the
``optional-dependencies`` key of the ``[project]`` table. Both dependencies and
extras are ultimately written by the build backend to the package's distribution
metadata. On this page, we'll refer to these as "metadata dependencies".

When installing a package, installers like :ref:`pip` will automatically install
the metadata dependencies. They should be used for packages that the project
**minimally** needs to run correctly.

For example, suppose the project requires A and B. When using the ``[project]``
table to declare metadata, the ``pyproject.toml`` would be like so:

.. code-block:: toml

   [project]
   dependencies = ["A", "B"]

Additionally, it's best practice to indicate any known lower or upper bounds.

For example, it may be known, that your project requires at least v1 of 'A', and
v2 of 'B'.

.. code-block:: toml

   [project]
   dependencies = [
     "A >= 1",
     "B >= 2"
   ]

It may also be known that project 'A' introduced a change in its v2
that breaks the compatibility of your project with v2 of 'A' and later,
so it makes sense to not allow v2:

.. code-block:: toml

   [project]
   dependencies = [
     "A >= 1, < 2",
     "B >= 2"
    ]

It is not considered best practice to use metadata dependencies to pin
dependencies to specific versions, or to specify transitive dependencies
(i.e. dependencies of your dependencies).  This is overly restrictive, and
prevents the user from gaining the benefit of dependency upgrades.

Lastly, it's important to understand that metadata dependencies are "abstract"
requirements, i.e. just names and version restrictions, but don't determine
where the dependencies will be fulfilled from (from what package index or
source). The where (i.e. how they are to be made "concrete") is to be determined
at install time, e.g., using :ref:`pip` options. [1]_


Requirements files
==================

:ref:`Requirements Files <pip:Requirements Files>`, described most simply, are
just a list of :ref:`pip:pip install` arguments placed into a file.

Whereas metadata dependencies define the dependencies for a single
project, requirements files are often used to define the requirements
for a complete Python environment.

Whereas metadata dependencies requirements are minimal, requirements files
often contain an exhaustive listing of pinned versions for the purpose of
achieving :ref:`repeatable installations <pip:Repeatability>` of a complete
environment.

Whereas metadata dependencies are "abstract", i.e. not associated with any
particular index, requirements files often contain pip options like
``--index-url`` or ``--find-links`` to make requirements "concrete", i.e.
associated with a particular index or directory of packages. [1]_

Whereas metadata dependencies are automatically analyzed by pip during an
install, requirements files are not, and only are used when a user specifically
installs them using :samp:`python -m pip install -r {requirement_file.txt}`.

----

.. [1] For more on "abstract" vs "concrete" requirements, see
       https://caremad.io/posts/2013/07/setup-vs-requirement/.
