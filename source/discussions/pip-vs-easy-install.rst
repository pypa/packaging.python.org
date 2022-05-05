
.. _`pip vs easy_install`:

===================
pip vs easy_install
===================


:ref:`easy_install <easy_install>`, now `deprecated`_, was released in 2004 as part of :ref:`setuptools`.
It was notable at the time for installing :term:`packages <Distribution Package>` from
:term:`PyPI <Python Package Index (PyPI)>` using requirement specifiers, and
automatically installing dependencies.

:ref:`pip` came later in 2008, as alternative to :ref:`easy_install <easy_install>`, although still
largely built on top of :ref:`setuptools` components.  It was notable at the
time for *not* installing packages as :term:`Eggs <Egg>` or from :term:`Eggs <Egg>` (but
rather simply as 'flat' packages from :term:`sdists <Source Distribution (or
"sdist")>`), and introducing the idea of :ref:`Requirements Files
<pip:Requirements Files>`, which gave users the power to easily replicate
environments.

Here's a breakdown of the important differences between pip and the deprecated easy_install:

+------------------------------+--------------------------------------+-------------------------------+
|                              | **pip**                              | **easy_install**              |
+------------------------------+--------------------------------------+-------------------------------+
|Installs from :term:`Wheels   |Yes                                   |No                             |
|<Wheel>`                      |                                      |                               |
+------------------------------+--------------------------------------+-------------------------------+
|Uninstall Packages            |Yes (``python -m pip uninstall``)     |No                             |
+------------------------------+--------------------------------------+-------------------------------+
|Dependency Overrides          |Yes (:ref:`Requirements Files         |No                             |
|                              |<pip:Requirements Files>`)            |                               |
+------------------------------+--------------------------------------+-------------------------------+
|List Installed Packages       |Yes (``python -m pip list`` and       |No                             |
|                              |``python -m pip freeze``)             |                               |
+------------------------------+--------------------------------------+-------------------------------+
|:pep:`438`                    |Yes                                   |No                             |
|Support                       |                                      |                               |
+------------------------------+--------------------------------------+-------------------------------+
|Installation format           |'Flat' packages with :file:`egg-info` | Encapsulated Egg format       |
|                              |metadata.                             |                               |
+------------------------------+--------------------------------------+-------------------------------+
|sys.path modification         |No                                    |Yes                            |
|                              |                                      |                               |
|                              |                                      |                               |
+------------------------------+--------------------------------------+-------------------------------+
|Installs from :term:`Eggs     |No                                    |Yes                            |
|<Egg>`                        |                                      |                               |
+------------------------------+--------------------------------------+-------------------------------+
|`pylauncher support`_         |No                                    |Yes [1]_                       |
|                              |                                      |                               |
+------------------------------+--------------------------------------+-------------------------------+
|:ref:`Multi-version Installs` |No                                    |Yes                            |
|                              |                                      |                               |
+------------------------------+--------------------------------------+-------------------------------+
|Exclude scripts during install|No                                    |Yes                            |
|                              |                                      |                               |
+------------------------------+--------------------------------------+-------------------------------+
|per project index             |Only in virtualenv                    |Yes, via setup.cfg             |
|                              |                                      |                               |
+------------------------------+--------------------------------------+-------------------------------+

----

.. _deprecated: https://setuptools.readthedocs.io/en/latest/history.html#v42-0-0

.. [1] https://setuptools.readthedocs.io/en/latest/deprecated/easy_install.html#natural-script-launcher


.. _pylauncher support: https://bitbucket.org/vinay.sajip/pylauncher
