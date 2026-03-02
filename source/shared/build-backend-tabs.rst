.. (comment) This file is included in guides/writing-pyproject-toml.rst and tutorials/packaging-projects.rst.
.. The minimum versions here are the versions that introduced support for PEP 639.

.. tab:: Hatchling

    .. code-block:: toml

        [build-system]
        requires = ["hatchling >= 1.26"]
        build-backend = "hatchling.build"

.. tab:: setuptools

    .. code-block:: toml

        [build-system]
        requires = ["setuptools >= 77.0.3"]
        build-backend = "setuptools.build_meta"

.. tab:: Flit

    .. code-block:: toml

        [build-system]
        requires = ["flit_core >= 3.12.0, <4"]
        build-backend = "flit_core.buildapi"

.. tab:: PDM

    .. code-block:: toml

        [build-system]
        requires = ["pdm-backend >= 2.4.0"]
        build-backend = "pdm.backend"

.. tab:: uv-build

    .. code-block:: toml

        [build-system]
        requires = ["uv_build >= 0.10.0, <0.11.0"]
        build-backend = "uv_build"
