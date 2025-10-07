.. _build-details:

==========================
:file:`build-details.json`
==========================

.. toctree::
   :hidden:

   v1.0 <v1.0>


The ``build-details.json`` file is a standardized file format that provides
build-specfic information of a Python installation, such as its version,
extension ABI details, and other information that is specific to that particular
build of Python.

Starting from Python 3.14, a ``build-details.json`` file is installed in the
platform-independent standard library directory (``stdlib``, e.g.
``/usr/lib/python3.14/build-details.json``).

Please refer to the :ref:`latest version <build-details-v1.0>` for its
specification.

..
   Update to point to the latest version!

.. literalinclude:: examples/build-details-v1.0.json
   :caption: Example
   :language: json
   :linenos:


Changelog
---------

..
   Order in decreasing order.

v1.0
~~~~

.. list-table::

    * - Specification
      - :ref:`build-details-v1.0`

    * - Schema
      - https://packaging.python.org/en/latest/specifications/schemas/build-details-v1.0.schema.json


- Initial version, introduced by :pep:`739`.
