News
====

November 2017
-------------

- Introduced a new dependency management tutorial based on Pipenv. (:pr:`402`)
- Updated the *Single Sourcing Package Version* tutorial to reflect pip's current
  strategy. (:pr:`400`)
- Added documentation about the ``py_modules`` argument to ``setup``. (:pr:`398`)
- Simplified the wording for the :file:`manifest.in` section. (:pr:`395`)

October 2017
------------

- Added a specification for the :file:`entry_points.txt` file. (:pr:`398`)
- Created a new guide for managing packages using ``pip`` and ``virtualenv``. (:pr:`385`)
- Split the specifications page into multiple pages. (:pr:`386`)

September 2017
--------------

- Encouraged using ``readme_renderer`` to validate :file:`README.rst`.
  (:pr:`379`)
- Recommended using the `--user-base` option. (:pr:`374`)

August 2017
-----------

- Added a new, experimental tutorial on installing packages using ``Pipenv``. (:pr:`369`)
- Added a new guide on how to use ``TestPyPI``. (:pr:`366`)
- Added :file:`pypi.org` as a term. (:pr:`365`)

July 2017
---------

- Added ``flit`` to the key projects list. (:pr:`358`)
- Added ``enscons`` to the list of key projects. (:pr:`357`)
- Updated this guide's ``readme`` with instructions on how to build the guide locally. (:pr:`356`)
- Made the new ``TestPyPI`` URL more visible, adding note to homepage about pypi.org. (:pr:`354`)
- Added a note about the removal of the explicit registration API. (:pr:`347`)

June 2017
---------

- Added a document on migrating uploads to :file:`PyPI.org`. (:pr:`339`)
- Added documentation for ``python_requires``. (:pr:`338`)
- Added a note about PyPI migration in the *Tool Recommendations* tutorial. (:pr:`335`)
- Added a note that :file:`manifest.in` does not affect wheels. (:pr:`332`)
- Added a license section to the distributing guide. (:pr:`331`)
- Expanded the section on the ``name`` argument. (:pr:`329`)
- Adjusted the landing page. (:pr:`327`, :pr:`326`, :pr:`324`)
- Updated to Sphinx 1.6.2. (:pr:`323`)
- Switched to the PyPA theme. (:pr:`305`)
- Re-organized the documentation into the new structure. (:pr:`318`)

May 2017
--------

- Added documentation for the ``Description-Content-Type`` field. (:pr:`258`)
- Added contributor and style guide. (:pr:`307`)
- Documented ``pip`` and ``easy_install``'s differences for per-project indexes. (:pr:`233`)

April 2017
----------

- Added travis configuration for testing pull requests. (:pr:`300`)
- Mentioned the requirement of the ``wheel`` package for creating wheels (:pr:`299`)
- Removed the ``twine register`` reference in the *Distributing Packages* tutorial. (:pr:`271`)
- Added a topic on plugin discovery. (:pr:`294`, :pr:`296`)
- Added a topic on namespace packages. (:pr:`290`)
- Added documentation explaining prominently how to install ``pip`` in ``/usr/local``. (:pr:`230`)
- Updated development mode documentation to mention that order of local packages matters. (:pr:`208`)
- Convert readthedocs link for their ``.org`` -> ``.io`` migration for hosted projects (:pr:`239`)
- Swaped order of :file:`setup.py` arguments for the upload command, as order
  is significant. (:pr:`260`)
- Explained how to install from unsupported sources using a helper application. (:pr:`289`)


March 2017
----------

- Covered ``manylinux1`` in *Platform Wheels*. (:pr:`283`)

February 2017
-------------

- Added :pep:`518`. (:pr:`281`)
