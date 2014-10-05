
========
Glossary
========

:Page Status: Complete
:Last Reviewed: 2014-05-10


.. glossary::


    Binary Distribution

        A specific kind of :term:`Built Distribution` that contains compiled
        extensions.


    Built Distribution

        A :term:`distribution-package <distribution package>` format
        containing files and metadata that only
        need to be moved to the correct location on the target system, to be
        installed. :term:`Wheel` is such a format, whereas distutil's
        :term:`Source Distribution <Source Distribution (or "sdist")>` is not,
        in that it requires a build step before it can be installed.  This
        format does not imply that python files have to be precompiled
        (:term:`Wheel` intentionally does not include compiled python files).


    distribution package

        A distribution package is a versioned archive file containing Python
        :term:`packages <import package>`, :term:`modules <module>`, and
        other resource files used to distribute a :term:`Release`. The
        distribution package is the file an end-user can download from the
        internet and install.

        Despite ":term:`package`" having a :term:`second meaning
        <import package>`, it is common in Python simply to say "package"
        to refer to distribution packages. For example, the name of the
        Python installation tool :ref:`pip` is an acronym for "pip installs
        packages," which refers to distribution packages.


    Egg

        A :term:`Built Distribution` format introduced by :ref:`setuptools`,
        which is being replaced by :term:`Wheel`.  For details, see `The
        Internal Structure of Python Eggs
        <http://pythonhosted.org/setuptools/formats.html>`_ and `Python Eggs
        <http://peak.telecommunity.com/DevCenter/PythonEggs>`_

    Extension Module

        A :term:`module` written in the low-level language of the Python implementation:
        C/C++ for Python, Java for Jython. Typically contained in a single
        dynamically loadable pre-compiled file, e.g.  a shared object (.so) file
        for Python extensions on Unix, a DLL (given the .pyd extension) for
        Python extensions on Windows, or a Java class file for Jython
        extensions.

    import package

        An import package is a directory containing an ``__init__.py`` file (ex.
        ``mypackage/__init__.py``), and also usually containing modules
        (possibly along with other packages).

        Despite ":term:`package`" having a :term:`second meaning
        <distribution package>`, it is common in Python simply to say
        "package" to refer to import packages (e.g. instructing one to
        import a package by typing ``import mypackage``).


    Known Good Set (KGS)

        A set of :term:`distribution packages <distribution package>`
        at specified versions which are compatible with
        each other. Typically a test suite will be run which passes all tests
        before a specific set is declared a known good set. This
        term is commonly used by frameworks and toolkits which are comprised of
        multiple individual distribution packages.


    Module

        The basic unit of code reusability in Python, existing in one of two
        types: :term:`Pure Module`, or :term:`Extension Module`.


    package

        This ubiquitous Python word in fact has two meanings:
        ":term:`distribution package`" for the versioned archive file that
        contains a project :term:`release`, and ":term:`import package`"
        for a directory of Python modules that can be imported. See the
        entries for these two terms for more complete definitions.

        The :term:`Python Packaging User Guide (PyPUG)` sometimes uses these
        more complete terms instead of "package" for emphasis, or when the
        context is not enough to tell which meaning is intended. Usually,
        however, context is enough.


    Package Index

        A repository of :term:`distribution packages <distribution package>`
        with a web interface to automate :term:`distribution package` discovery and consumption.


    Project

        A library, framework, script, plugin, application, or collection of data
        or other resources, or some combination thereof that is intended to be
        packaged into a :term:`distribution package`.

        Since most projects create :term:`distribution packages <distribution package>` using
        :ref:`distutils` or :ref:`setuptools`, another practical way to define
        projects currently is something that contains a :term:`setup.py` at the
        root of the project src directory, where "setup.py" is the project
        specification filename used by :ref:`distutils` and :ref:`setuptools`.

        Python projects must have unique names, which are registered on
        :term:`PyPI <Python Package Index (PyPI)>`. Each project will then
        contain one or more :term:`Releases <Release>`, and each release may
        comprise one or more :term:`distribution packages <distribution package>`.

        Note that there is a strong convention to name a project after the name
        of the package that is imported to run that project. However, this
        doesn't have to hold true. It's possible to install a distribution from
        the project 'spam' and have it provide a package importable only as
        'eggs'.


    Pure Module

        A :term:`module` written in Python and contained in a single .py file (and
        possibly associated .pyc and/or .pyo files).


    Python Packaging Authority (PyPA)

        PyPA is a working group that maintains many of the relevant projects in
        Python packaging. They host projects on `github
        <https://github.com/pypa>`_ and `bitbucket
        <https://bitbucket.org/pypa>`_, and discuss issues on the `pypa-dev
        mailing list <https://groups.google.com/forum/#!forum/pypa-dev>`_.


    Python Packaging User Guide (PyPUG)

        The guide you are reading.


    Python Package Index (PyPI)

        `PyPI <https://pypi.python.org/pypi>`_ is the default :term:`Package
        Index` for the Python community. It is open to all Python developers to
        consume and distribute their distributions.

    Release

        A snapshot of a :term:`Project` at a particular point in time, denoted
        by a version identifier.

        Making a release may entail the publishing of multiple
        :term:`distribution packages <distribution package>`.  For example, if version 1.0 of a
        project was released, it could be available in both a source
        distribution format and a Windows installer distribution format.


    Requirement

       A specification for a :term:`package <distribution package>` to be
       installed.  :ref:`pip`, the :term:`PYPA <Python Packaging Authority
       (PyPA)>` recommended installer, allows various forms of specification
       that can all be considered a "requirement". For more information, see the
       :ref:`pip:pip install` reference.


    Requirements File

       A file containing a list of :term:`Requirements <Requirement>` that can
       be installed using :ref:`pip`. For more information, see the :ref:`pip`
       docs on :ref:`pip:Requirements Files`.


    setup.py

        The project specification file for :ref:`distutils` and :ref:`setuptools`.


    Source Archive

        An archive containing the raw source code for a :term:`Release`, prior
        to creation of an :term:`Source Distribution <Source Distribution (or
        "sdist")>` or :term:`Built Distribution`.


    Source Distribution (or "sdist")

        A :term:`distribution-package <distribution package>` format (usually
        generated using
        ``python setup.py sdist``) that provides metadata and the essential
        source files needed for installing by a tool like :ref:`pip`, or for
        generating a :term:`Built Distribution`.


    System Package

        A package provided in a format native to the operating system,
        e.g. an rpm or dpkg file.


    Virtual Environment

        An isolated Python environment that allows packages to be installed for
        use by a particular application, rather than being installed system
        wide. For more information, see the tutorial section on :ref:`Creating
        and using Virtual Environments`.

    Wheel

        A :term:`Built Distribution` format introduced by :ref:`PEP427s`, which
        is intended to replace the :term:`Egg` format.  Wheel is currently
        supported by :ref:`pip`.

    Working Set

        A collection of :term:`distribution packages <distribution package>` available for
        importing. These are the distributions that are on the `sys.path`
        variable. At most, one :term:`distribution package` for a project is possible in
        a working set.

