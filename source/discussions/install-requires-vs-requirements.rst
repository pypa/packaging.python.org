.. _`install_requires vs requirements files`:

======================================
install_requires vs requirements files
======================================


install_requires
----------------

``install_requires`` is a :ref:`setuptools` :file:`setup.py` keyword that
should be used to specify what a project **minimally** needs to run correctly.
When the project is installed by :ref:`pip`, this is the specification that is
used to install its dependencies.

For example, if the project requires A and B, your ``install_requires`` would be
like so:

::

 install_requires=[
    'A',
    'B'
 ]

Additionally, it's best practice to indicate any known lower or upper bounds.

For example, it may be known, that your project requires at least v1 of 'A', and
v2 of 'B', so it would be like so:

::

 install_requires=[
    'A>=1',
    'B>=2'
 ]

It may also be known that project 'A' introduced a change in its v2
that breaks the compatibility of your project with v2 of 'A' and later,
so it makes sense to not allow v2:

::

 install_requires=[
    'A>=1,<2',
    'B>=2'
 ]

It is not considered best practice to use ``install_requires`` to pin
dependencies to specific versions, or to specify sub-dependencies
(i.e. dependencies of your dependencies).  This is overly-restrictive, and
prevents the user from gaining the benefit of dependency upgrades.

Lastly, it's important to understand that ``install_requires`` is a listing of
"Abstract" requirements, i.e just names and version restrictions that don't
determine where the dependencies will be fulfilled from (i.e. from what
index or source).  The where (i.e. how they are to be made "Concrete") is to
be determined at install time using :ref:`pip` options. [1]_


Requirements files
------------------

:ref:`Requirements Files <pip:Requirements Files>` described most simply, are
just a list of :ref:`pip:pip install` arguments placed into a file.

Whereas ``install_requires`` defines the dependencies for a single project,
:ref:`Requirements Files <pip:Requirements Files>` are often used to define
the requirements for a complete Python environment.

Whereas ``install_requires`` requirements are minimal, requirements files
often contain an exhaustive listing of pinned versions for the purpose of
achieving :ref:`repeatable installations <pip:Repeatability>` of a complete
environment.

Whereas ``install_requires`` requirements are "Abstract", i.e. not associated
with any particular index, requirements files often contain pip
options like ``--index-url`` or ``--find-links`` to make requirements
"Concrete", i.e. associated with a particular index or directory of
packages. [1]_

Whereas ``install_requires`` metadata is automatically analyzed by pip during an
install, requirements files are not, and only are used when a user specifically
installs them using ``python -m pip install -r``.

----

.. [1] For more on "Abstract" vs "Concrete" requirements, see
       https://caremad.io/posts/2013/07/setup-vs-requirement/.
