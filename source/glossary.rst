========
Glossary
========


.. glossary::


    Binary Distribution

        A specific kind of :term:`Built Distribution` that contains compiled
        extensions.


    Build Frontend

        A tool that users interact with directly to trigger a build of
        a :term:`Project`, which in turn invokes the project's
        :term:`Build Backend` in a suitable environment
        to generate a :term:`Built Distribution` (i.e. a :term:`Wheel`),
        from a :term:`Source Tree` or :term:`Source Distribution`.
        Examples include :ref:`build`, as well as :ref:`pip`
        (when running a command such as ``pip wheel some-directory/``).
        Compare to :term:`Integration Frontend`.
        For more details,
        see the :ref:`build-frontend-backend-interface` specification.


    Build Backend

        A tool directly responsible for transforming a
        :term:`Source Tree` or :term:`Source Distribution`
        into a :term:`Built Distribution` (i.e. a :term:`Wheel`).
        Typically invoked by a :term:`Build Frontend` rather than directly.
        Examples include :ref:`flit`, :ref:`hatch` and :ref:`setuptools`.
        For more details,
        see the :ref:`build-frontend-backend-interface` specification.


    Built Distribution

        A :term:`Distribution` format containing files and metadata
        that only need to be moved to the correct location
        on the target system to be installed.
        :term:`Wheel` is such a format, whereas a :term:`Sdist` is not,
        in that it requires processing by the :term:`Project`'s
        :term:`Build Backend` before it can be installed.
        This format does not imply that Python files have to be precompiled
        (:term:`Wheel` intentionally does not include compiled Python files).


    Distribution Package
    Distribution
    Package

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
        "distribution".


    Editable Installation
    Editable Mode

        An installation mode implying that the :term:`Source Tree` of the
        :term:`project` being installed is available in a local directory,
        in which users expect that changes to its *Python* code
        become effective without the need of a new installation step.

        When a project is installed in "editable mode",
        users expect it to behave as identically as practical
        to a non-editable installation
        (though some minor differences might be visible).
        In particular, the code must be importable by other code,
        and metadata must be available by standard mechanisms
        such as ``importlib.metadata``.

        Formally specified in :pep:`660` and now defined in the
        :ref:`build-frontend-backend-interface` specification.


    Egg

        A :term:`Built Distribution` format introduced by :ref:`setuptools`,
        which is being replaced by :term:`Wheel`.  For details, see `
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
        is also commonly called a "package".


    Integration Frontend

        A tool that users run directly
        that takes a set of :term:`Requirement`\s,
        such as from a :term:`Project`'s :ref:`core-metadata`,
        a :term:`Requirements File` or specified manually,
        and attempts to update a working environment to satisfy them.
        This may require locating, building and installing
        a combination of :term:`Built Distribution`\s
        and :term:`Source Distribution`\s,
        including acting as a :term:`Build Frontend` in the latter case.
        In a command like ``pip install lxml==2.4.0``,
        :ref:`pip` is acting as an integration frontend.


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

        A library, framework, script, plugin, application,
        collection of data or other resources, or some combination thereof
        that is intended to be packaged into a :term:`Distribution`.

        Since most projects create :term:`Distribution`\s
        using a :term:`Build Backend` :ref:`declared <declaring-build-system>`
        within a :ref:`pyproject.toml file <pyproject-toml-config-file>`,
        (or else implicitly use :ref:`setuptools`),
        another practical way to define a project
        is something that contains a :term:`pyproject.toml`
        (or :term:`setup.py`/:term:`setup.cfg`) file
        at the root of the project :term:`Source Tree`.

        Python projects must have unique :ref:`names <core-metadata-name>`,
        which are registered on a :term:`Package Index`
        such as :term:`PyPI <Python Package Index (PyPI)>`.
        Each project will contain one or more :term:`Releases <Release>`,
        and each release may comprise one or more :term:`Distribution`\s.

        Note that there is a strong convention to name a project after the name
        of the package that is imported to use that project.
        However, this doesn't have to hold true.
        It's possible to install a distribution from the project ``foo``
        and have it provide a package importable only as ``bar``.


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

        The tool-agnostic :term:`Project` configuration file.
        Originally introduced in :pep:`518` and now defined in the
        :ref:`pyproject-toml-config-file` specification.


    Release

        A snapshot of a :term:`Project` at a particular point in time, denoted
        by a version identifier.

        Making a release may entail the publishing of multiple
        :term:`Distributions <Distribution Package>`.  For example, if version
        1.0 of a project was released, it could be available in both a source
        distribution format and a Windows installer distribution format.


    Requirement

       A specification for a :term:`Package`
       to be installed by an :term:`Integration Frontend`.
       :ref:`pip`, the :term:`PyPA <Python Packaging Authority (PyPA)>`
       recommended installer,
       allows various forms of specification
       that can all be considered a "requirement".
       For more information, see the :ref:`pip:pip install` reference.


    Requirement Specifier

       A syntax used to declare the name and version of a :term:`Package`
       that an :term:`Integration Frontend` such as :ref:`pip`
       should install from a :term:`Package Index`.
       For example, ``foo>=1.3`` is a requirement specifier,
       where ``foo`` is the :ref:`project name <core-metadata-name>`
       and ``>=1.3`` is the :term:`Version Specifier`.
       The format was initially specified in :pep:`508`,
       and is now defined in the :ref:`dependency-specifiers` specification.


    Requirements File

       A file containing a list of :term:`Requirement`\s that can
       be installed using an :term:`Integration Frontend`, such as :ref:`pip`.
       For more information,
       see the :ref:`pip` docs on :ref:`pip:Requirements Files`.


    setup.py
    setup.cfg

        The project specification files for :ref:`distutils` and :ref:`setuptools`.
        See also :term:`pyproject.toml`.


    Source Archive

        An archive containing the :term:`Source Tree` for a :term:`Release`,
        prior to creation of a
        :term:`Source Distribution` or :term:`Built Distribution`.


    Source Distribution
    Sdist

        A :term:`Distribution` format
        (generated using, e.g., ``python -m build --sdist``)
        that provides metadata and the essential source files needed
        by a :term:`Build Backend` to generate a :term:`Built Distribution`
        for installation by an installer like :ref:`pip`.


    Source Tree

        A collection of files and directories (typically from a VCS checkout)
        containing the raw source code of a :term:`project`
        that is used for development.
        Can be stored in a :term:`Source Archive`
        and is used by a :term:`Build Backend` to generate a
        :term:`Source Distribution`
        and in turn a :term:`Built Distribution`,
        as well as directly in an :term:`Editable Installation`.
        Typically contains a :ref:`pyproject-toml-config-file` at its root.


    System Package

        A package provided in a format native to the operating system,
        e.g. an rpm or dpkg file.


    Version Specifier

       The version component of a :term:`Requirement Specifier`. For example,
       the ">=1.3" portion of "foo>=1.3".  :pep:`440` contains
       a :pep:`full specification
       <440#version-specifiers>` of the
       specifiers that Python packaging currently supports.  Support for PEP440
       was implemented in :ref:`setuptools` v8.0 and :ref:`pip` v6.0.

    Virtual Environment

        An isolated Python environment that allows packages to be installed for
        use by a particular application, rather than being installed system
        wide. For more information, see the section on :ref:`Creating and using
        Virtual Environments`.


    Wheel

        A :term:`Built Distribution` format, introduced by :pep:`427`
        and now defined in the :ref:`binary-distribution-format` specification,
        which replaces the legacy :term:`Egg` format.
        Wheel is supported by :ref:`pip` and other installation tools,
        and is the primary output of :term:`Build Backend`\s.


    Working Set

        A collection of :term:`distributions <Distribution Package>` available
        for importing. These are the distributions that are on the `sys.path`
        variable. At most, one :term:`Distribution <Distribution Package>` for a
        project is possible in a working set.
