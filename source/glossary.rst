========
Glossary
========


.. glossary::


    Binary Distribution

        A specific kind of :term:`Built Distribution` that contains compiled
        extensions.


    Build Backend

        A library that takes a source tree or
        :term:`source distribution <Source Distribution (or "sdist")>`
        and builds a source distribution or :term:`wheel <Wheel>` from it.
        The build is delegated to the backend by a
        :term:`frontend <Build Frontend>`.
        All backends offer a standardized interface.

        Examples of build backends are
        :ref:`flit's flit-core <flit>`,
        :ref:`hatch's hatchling <hatch>`,
        :ref:`maturin`,
        :ref:`meson-python`,
        :ref:`scikit-build-core`,
        and :ref:`setuptools`.


    Build Frontend

        A tool that users might run
        that takes arbitrary source trees or
        :term:`source distributions <Source Distribution (or "sdist")>`
        and builds source distributions or :term:`wheels <Wheel>` from them.
        The actual building is delegated to each source tree's
        :term:`build backend <Build Backend>`.

        Examples of build frontends are :ref:`pip` and :ref:`build`.


    Built Distribution

        A :term:`Distribution <Distribution Package>` format containing files
        and metadata that only need to be moved to the correct location on the
        target system, to be installed. :term:`Wheel` is such a format, whereas
        distutil's :term:`Source Distribution <Source Distribution (or
        "sdist")>` is not, in that it requires a build step before it can be
        installed.  This format does not imply that Python files have to be
        precompiled (:term:`Wheel` intentionally does not include compiled
        Python files).


    Distribution Package

        A versioned archive file that contains Python :term:`packages <Import
        Package>`, :term:`modules <Module>`, and other resource files that are
        used to distribute a :term:`Release`. The archive file is what an
        end-user will download from the internet and install.

        A distribution package is more commonly referred to with the single
        words "package" or "distribution", but this guide may use the expanded
        term when more clarity is needed to prevent confusion with an
        :term:`Import Package` (which is also commonly called a "package") or
        another kind of distribution (e.g. a Linux distribution or the Python
        language distribution), which are often referred to with the single term
        "distribution". See :ref:`distribution-package-vs-import-package`
        for a breakdown of the differences.

    Egg

        A :term:`Built Distribution` format introduced by :ref:`setuptools`,
        which is being replaced by :term:`Wheel`.  For details, see
        :doc:`The Internal Structure of Python Eggs <setuptools:deprecated/python_eggs>` and
        `Python Eggs <http://peak.telecommunity.com/DevCenter/PythonEggs>`_

    Extension Module

        A :term:`Module` written in the low-level language of the Python implementation:
        C/C++ for Python, Java for Jython. Typically contained in a single
        dynamically loadable pre-compiled file, e.g.  a shared object (.so) file
        for Python extensions on Unix, a DLL (given the .pyd extension) for
        Python extensions on Windows, or a Java class file for Jython
        extensions.


    Known Good Set (KGS)

        A set of distributions at specified versions which are compatible with
        each other. Typically a test suite will be run which passes all tests
        before a specific set of packages is declared a known good set. This
        term is commonly used by frameworks and toolkits which are comprised of
        multiple individual distributions.


    Import Package

        A Python module which can contain other modules or recursively, other
        packages.

        An import package is more commonly referred to with the single word
        "package", but this guide will use the expanded term when more clarity
        is needed to prevent confusion with a :term:`Distribution Package` which
        is also commonly called a "package". See :ref:`distribution-package-vs-import-package`
        for a breakdown of the differences.

    Module

        The basic unit of code reusability in Python, existing in one of two
        types: :term:`Pure Module`, or :term:`Extension Module`.


    Package Index

        A repository of distributions with a web interface to automate
        :term:`package <Distribution Package>` discovery and consumption.


    Per Project Index

        A private or other non-canonical :term:`Package Index` indicated by
        a specific :term:`Project` as the index preferred or required to
        resolve dependencies of that project.


    Project

        A library, framework, script, plugin, application, or collection of data
        or other resources, or some combination thereof that is intended to be
        packaged into a :term:`Distribution <Distribution Package>`.

        Since most projects create :term:`Distributions <Distribution Package>`
        using either :pep:`518` ``build-system``, :ref:`distutils` or
        :ref:`setuptools`, another practical way to define projects currently
        is something that contains a :term:`pyproject.toml`, :term:`setup.py`,
        or :term:`setup.cfg` file at the root of the project source directory.

        Python projects must have unique names, which are registered on
        :term:`PyPI <Python Package Index (PyPI)>`. Each project will then
        contain one or more :term:`Releases <Release>`, and each release may
        comprise one or more :term:`distributions <Distribution Package>`.

        Note that there is a strong convention to name a project after the name
        of the package that is imported to run that project. However, this
        doesn't have to hold true. It's possible to install a distribution from
        the project 'foo' and have it provide a package importable only as
        'bar'.


    Pure Module

        A :term:`Module` written in Python and contained in a single ``.py`` file (and
        possibly associated ``.pyc`` and/or ``.pyo`` files).


    Python Packaging Authority (PyPA)

        PyPA is a working group that maintains many of the relevant
        projects in Python packaging. They maintain a site at
        :doc:`pypa.io <pypa:index>`, host projects on `GitHub
        <https://github.com/pypa>`_ and `Bitbucket
        <https://bitbucket.org/pypa>`_, and discuss issues on the
        `distutils-sig mailing list
        <https://mail.python.org/mailman3/lists/distutils-sig.python.org/>`_
	and `the Python Discourse forum <https://discuss.python.org/c/packaging>`__.


    Python Package Index (PyPI)

        `PyPI <https://pypi.org>`_ is the default :term:`Package
        Index` for the Python community. It is open to all Python developers to
        consume and distribute their distributions.

    pypi.org

        `pypi.org <https://pypi.org>`_ is the domain name for the
        :term:`Python Package Index (PyPI)`. It replaced the legacy index
        domain name, ``pypi.python.org``, in 2017. It is powered by
        :ref:`warehouse`.

    pyproject.toml

        The tool-agnostic :term:`Project` specification file.
        Defined in :pep:`518`.

    Release

        A snapshot of a :term:`Project` at a particular point in time, denoted
        by a version identifier.

        Making a release may entail the publishing of multiple
        :term:`Distributions <Distribution Package>`.  For example, if version
        1.0 of a project was released, it could be available in both a source
        distribution format and a Windows installer distribution format.


    Requirement

       A specification for a :term:`package <Distribution Package>` to be
       installed.  :ref:`pip`, the :term:`PYPA <Python Packaging Authority
       (PyPA)>` recommended installer, allows various forms of specification
       that can all be considered a "requirement". For more information, see the
       :ref:`pip:pip install` reference.


    Requirement Specifier

       A format used by :ref:`pip` to install packages from a :term:`Package
       Index`. For an EBNF diagram of the format, see :ref:`dependency-specifiers`.
       For example, "foo>=1.3" is a
       requirement specifier, where "foo" is the project name, and the ">=1.3"
       portion is the :term:`Version Specifier`

    Requirements File

       A file containing a list of :term:`Requirements <Requirement>` that can
       be installed using :ref:`pip`. For more information, see the :ref:`pip`
       docs on :ref:`pip:Requirements Files`.


    setup.py
    setup.cfg

        The project specification files for :ref:`distutils` and :ref:`setuptools`.
        See also :term:`pyproject.toml`.


    Source Archive

        An archive containing the raw source code for a :term:`Release`, prior
        to creation of a :term:`Source Distribution <Source Distribution (or
        "sdist")>` or :term:`Built Distribution`.


    Source Distribution (or "sdist")

        A :term:`distribution <Distribution Package>` format (usually generated
        using ``python -m build --sdist``) that provides metadata and the
        essential source files needed for installing by a tool like :ref:`pip`,
        or for generating a :term:`Built Distribution`.


    System Package

        A package provided in a format native to the operating system,
        e.g. an rpm or dpkg file.


    Version Specifier

       The version component of a :term:`Requirement Specifier`. For example,
       the ">=1.3" portion of "foo>=1.3".  Read the :ref:`Version specifier specification
       <version-specifiers>` for a full description of the
       specifiers that Python packaging currently supports.  Support for this
       specification was implemented in :ref:`setuptools` v8.0 and :ref:`pip` v6.0.

    Virtual Environment

        An isolated Python environment that allows packages to be installed for
        use by a particular application, rather than being installed system
        wide. For more information, see the section on :ref:`Creating and using
        Virtual Environments`.

    Wheel

        A :term:`Built Distribution` format introduced by an official
        :doc:`standard specification
        </specifications/binary-distribution-format/>`,
        which is intended to replace the :term:`Egg` format.  Wheel is currently
        supported by :ref:`pip`.

    Working Set

        A collection of :term:`distributions <Distribution Package>` available
        for importing. These are the distributions that are on the `sys.path`
        variable. At most, one :term:`Distribution <Distribution Package>` for a
        project is possible in a working set.
