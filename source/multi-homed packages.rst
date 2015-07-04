.. _`Multi-homed Packages`:

Multi-homed Packages
====================

In the basic use case, a package is represented by a
single distribution in a single location. With the
introduction of namespace packages, this expectation
is no longer necessarily maintained. A package such
as ``zc.component`` shares the ``zc`` namespace with
``zc.interface``. Theoretically, those packages could
be installed in separate locations or together in a
single ``zc`` directory.

One consequence of the "flat" package installation used
by pip is that a given package is expected to be merged
into a single, canonical location. Pip provides no
mechanism to resolve a package from multiple locations.
This limitation leads to issues such as `Pip 3
<https://github.com/pypa/pip/issues/3>`_ and
`Setuptools 250
<https://bitbucket.org/pypa/setuptools/issue/250/>`_.

Python 3.3 via PEP 420 adds native support in Python
for multi-homed namespace packages. In this model,
pip could theoretically support multi-homed packages.

At the time of this writing, only known workaround is to
install packages using ``easy_install`` or force use of
eggs with ``pip install --egg``.
