.. (comment) This file is included in guides/writing-pyproject-toml.rst and tutorials/packaging-projects.rst.

.. tab:: Hatchling

    .. code-block:: toml

        [build-system]
        requires = ["hatchling"]
        build-backend = "hatchling.build"

.. tab:: setuptools

    .. code-block:: toml

        [build-system]
        requires = ["setuptools >= 61.0"]
        build-backend = "setuptools.build_meta"

.. tab:: Flit

    .. code-block:: toml

        [build-system]
        requires = ["flit_core >= 3.4"]
        build-backend = "flit_core.buildapi"

.. tab:: PDM

    .. code-block:: toml

        [build-system]
        requires = ["pdm-backend"]
        build-backend = "pdm.backend"
