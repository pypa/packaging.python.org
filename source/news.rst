News
====

.. note:: This document is not currently updated. Previously, the document
  highlighted changes in Python packaging.


September 2019
--------------
- Added a guide about publishing dists via GitHub Actions. (:pr:`PR #647 <647>`)

August 2019
-----------
- Updated to use :file:`python3 -m` when installing pipx. (:pr:`PR #631 <631>`)

July 2019
---------
- Marked all PEP numbers with the :pep: role. (:pr:`PR #629 <629>`)
- Upgraded Sphinx version and removed pypa.io intersphinx. (:pr:`PR #625 <625>`)
- Mentioned :file:`find_namespace_packages`. (:pr:`PR #622 <622>`)
- Updated directory layout examples for consistency. (:pr:`PR #611 <611>`)
- Updated Bandersnatch link to GitHub. (:pr:`PR #623 <623>`)

June 2019
---------
- Fixed some typos. (:pr:`PR #620 <620>`)

May 2019
--------
- Added :file:`python_requires` usage to packaging tutorial. (:pr:`PR #613 <613>`)
- Added a MANIFEST.in guide page. (:pr:`PR #609 <609>`)

April 2019
----------
- Added a mention for :file:`shiv` in the key projects section. (:pr:`PR #608 <608>`)
- Reduced emphasis on virtualenv. (:pr:`PR #606 <606>`)

March 2019
----------
- Moved single-sourcing guide version option to Python 3. (:pr:`PR #605 <605>`)
- Covered RTD details for contributing. (:pr:`PR #600 <600>`)

February 2019
-------------
- Elaborate upon the differences between the tutorial and the real packaging process. (:pr:`PR #602 <602>`)
- Added instructions to install Python CLI applications. (:pr:`PR #594 <594>`)

January 2019
------------
- Added :file:`--no-deps` to the packaging tutorial. (:pr:`PR #593 <593>`)
- Updated Sphinx and Nox. (:pr:`PR #591 <591>`)
- Referenced Twine from Python3. (:pr:`PR #581 <581>`)

December 2018
-------------
- No programmers in the office!

November 2018
-------------
- Removed landing page link to PyPI migration guide. (:pr:`PR #575 <575>`)
- Changed bumpversion to bump2version. (:pr:`PR #572 <572>`)
- Added single-sourcing package version example. (:pr:`PR #573 <573>`)
- Added a guide for creating documentation. (:pr:`PR #568 <568>`)

October 2018
------------
- Updated Nox package name. (:pr:`PR #566 <566>`)
- Mentioned Sphinx extensions in guides. (:pr:`PR #562 <562>`)

September 2018
--------------
- Added a section on checking RST markup. (:pr:`PR #554 <554>`)
- Updated user installs page. (:pr:`PR #558 <558>`)
- Updated Google BigQuery urls. (:pr:`PR #556 <556>`)
- Replaced tar command with working command. (:pr:`PR #552 <552>`)
- Changed to double quotes in the pip install SomeProject==1.4. (:pr:`PR #550 <550>`)

August 2018
-----------
- Removed the recommendation to store passwords in cleartext. (:pr:`PR #546 <546>`)
- Moved the Overview to a task based lead in along with the others. (:pr:`PR #540 <540>`)
- Updated Python version supported by virtualenv. (:pr:`PR #538 <538>`)
- Added outline/rough draft of new Overview page. (:pr:`PR #519 <519>`)

July 2018
---------

- Improved binary extension docs. (:pr:`PR #531 <531>`)
- Added scikit-build to key projects. (:pr:`PR #530 <530>`)

June 2018
---------

- Fixed categories of interop PEP for pypa.io. (:pr:`PR #527 <527>`)
- Updated Markdown descriptions explanation. (:pr:`PR #522 <522>`)

May 2018
--------

- Noted issues with Provides-Dist and Obsoletes-Dist. (:pr:`PR #513 <513>`)
- Removed outdated warning about Python version mixing with Pipenv. (:pr:`PR #501 <501>`)
- Simplified packaging tutorial. (:pr:`PR #498 <498>`)
- Updated Windows users instructions for clarity. (:pr:`PR #493 <493>`)
- Updated the license section description for completeness. (:pr:`PR #492 <492>`)
- Added specification-style document to contributing section. (:pr:`PR #489 <489>`)
- Added documentation types to contributing guide. (:pr:`PR #485 <485>`)

April 2018
----------

- Added README guide. (:pr:`PR #461 <461>`)
- Updated instructions and status for PyPI launch. (:pr:`PR #475 <475>`)
- Added instructions for Warehouse. (:pr:`PR #471 <471>`)
- Removed GPG references from publishing tutorial. (:pr:`PR #466 <466>`)
- Added 'What’s in which Python 3.4–3.6?'. (:pr:`PR #468 <468>`)
- Added a guide for phasing out Python versions. (:pr:`PR #459 <459>`)
- Made default Description-Content-Type variant GFM. (:pr:`PR #462 <462>`)

March 2018
----------

- Updated "installing scientific packages". (:pr:`PR #455 <455>`)
- Added :file:`long_description_content_type` to follow PEP 556. (:pr:`PR #457 <457>`)
- Clarified a long description classifier on pypi.org. (:pr:`PR #456 <456>`)
- Updated Core Metadata spec to follow PEP 556. (:pr:`PR #412 <412>`)

February 2018
-------------

- Added python3-venv and python3-pip to Debian installation instructions. (:pr:`PR #445 <445>`)
- Updated PyPI migration info. (:pr:`PR #439 <439>`)
- Added a warning about managing multiple versions with pipenv. (:pr:`PR #430 <430>`)
- Added example of multiple emails to Core Metadata. (:pr:`PR #429 <429>`)
- Added explanation of "legacy" in test.pypi.org/legacy. (:pr:`PR #426 <426>`)

January 2018
------------

- Added a link to PyPI's list of classifiers. (:pr:`PR #425 <425>`)
- Updated README.rst explanation. (:pr:`PR #419 <419>`)

December 2017
-------------

- Replaced :file:`~` with :file:`$HOME` in guides and tutorials.  (:pr:`PR #418 <418>`)
- Noted which fields can be used with environment markers. (:pr:`PR #416 <416>`)
- Updated Requires-Python section. (:pr:`PR #414 <414>`)
- Added news page. (:pr:`PR #404 <404>`)

November 2017
-------------

- Introduced a new dependency management tutorial based on Pipenv. (:pr:`PR #402 <402>`)
- Updated the *Single Sourcing Package Version* tutorial to reflect pip's current
  strategy. (:pr:`PR #400 <400>`)
- Added documentation about the ``py_modules`` argument to ``setup``. (:pr:`PR #398 <398>`)
- Simplified the wording for the :file:`manifest.in` section. (:pr:`PR #395 <395>`)

October 2017
------------

- Added a specification for the :file:`entry_points.txt` file. (:pr:`PR #398 <398>`)
- Created a new guide for managing packages using ``pip`` and ``virtualenv``. (:pr:`PR #385 <385>`)
- Split the specifications page into multiple pages. (:pr:`PR #386 <386>`)

September 2017
--------------

- Encouraged using ``readme_renderer`` to validate :file:`README.rst`.
  (:pr:`PR #379 <379>`)
- Recommended using the ``--user-base`` option. (:pr:`PR #374 <374>`)

August 2017
-----------

- Added a new, experimental tutorial on installing packages using ``Pipenv``. (:pr:`PR #369 <369>`)
- Added a new guide on how to use ``TestPyPI``. (:pr:`PR #366 <366>`)
- Added :file:`pypi.org` as a term. (:pr:`PR #365 <365>`)

July 2017
---------

- Added ``flit`` to the key projects list. (:pr:`PR #358 <358>`)
- Added ``enscons`` to the list of key projects. (:pr:`PR #357 <357>`)
- Updated this guide's ``readme`` with instructions on how to build the guide locally. (:pr:`PR #356 <356>`)
- Made the new ``TestPyPI`` URL more visible, adding note to homepage about pypi.org. (:pr:`PR #354 <354>`)
- Added a note about the removal of the explicit registration API. (:pr:`PR #347 <347>`)

June 2017
---------

- Added a document on migrating uploads to :file:`PyPI.org`. (:pr:`PR #339 <339>`)
- Added documentation for ``python_requires``. (:pr:`PR #338 <338>`)
- Added a note about PyPI migration in the *Tool Recommendations* tutorial. (:pr:`PR #335 <335>`)
- Added a note that :file:`manifest.in` does not affect wheels. (:pr:`PR #332 <332>`)
- Added a license section to the distributing guide. (:pr:`PR #331 <331>`)
- Expanded the section on the ``name`` argument. (:pr:`PR #329 <329>`)
- Adjusted the landing page. (:pr:`PR #327 <327>`, :pr:`PR #326 <326>`, :pr:`PR #324 <324>`)
- Updated to Sphinx 1.6.2. (:pr:`PR #323 <323>`)
- Switched to the PyPA theme. (:pr:`PR #305 <305>`)
- Re-organized the documentation into the new structure. (:pr:`PR #318 <318>`)

May 2017
--------

- Added documentation for the ``Description-Content-Type`` field. (:pr:`PR #258 <258>`)
- Added contributor and style guide. (:pr:`PR #307 <307>`)
- Documented ``pip`` and ``easy_install``'s differences for per-project indexes. (:pr:`PR #233 <233>`)

April 2017
----------

- Added travis configuration for testing pull requests. (:pr:`PR #300 <300>`)
- Mentioned the requirement of the ``wheel`` package for creating wheels (:pr:`PR #299 <299>`)
- Removed the ``twine register`` reference in the *Distributing Packages* tutorial. (:pr:`PR #271 <271>`)
- Added a topic on plugin discovery. (:pr:`PR #294 <294>`, :pr:`PR #296 <296>`)
- Added a topic on namespace packages. (:pr:`PR #290 <290>`)
- Added documentation explaining prominently how to install ``pip`` in ``/usr/local``. (:pr:`PR #230 <230>`)
- Updated development mode documentation to mention that order of local packages matters. (:pr:`PR #208 <208>`)
- Convert readthedocs link for their ``.org`` -> ``.io`` migration for hosted projects (:pr:`PR #239 <239>`)
- Swapped order of :file:`setup.py` arguments for the upload command, as order
  is significant. (:pr:`PR #260 <260>`)
- Explained how to install from unsupported sources using a helper application. (:pr:`PR #289 <289>`)


March 2017
----------

- Covered ``manylinux1`` in *Platform Wheels*. (:pr:`PR #283 <283>`)

February 2017
-------------

- Added :pep:`518`. (:pr:`PR #281 <281>`)
