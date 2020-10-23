.. _creating-documentation:

======================
Creating Documentation
======================

This section covers the basics of how to create documentation using `Sphinx`_ and host the documentation for free in `Read The Docs`_.

.. _Sphinx: http://sphinx-doc.org/
.. _Read The Docs: https://readthedocs.org/

Installing Sphinx
-----------------
Use ``pip`` to install Sphinx:

.. code-block:: bash

	pip install -U sphinx

For other installation methods, see this `installation guide`_ by Sphinx.

.. _installation guide: http://www.sphinx-doc.org/en/master/usage/installation.html

Getting Started With Sphinx
---------------------------

Create a ``docs`` directory inside your project to hold your documentation:

.. code-block:: bash

	cd /path/to/project
	mkdir docs

Run ``sphinx-quickstart`` inside the ``docs`` directory:

.. code-block:: bash

	cd docs
	sphinx-quickstart

This sets up a source directory, walks you through some basic configurations, and creates an ``index.rst`` file as well as a ``conf.py`` file.

You can add some information about your project in ``index.rst``, then build them:

.. code-block:: bash

	make html

For more details on the build process, see this `guide`_ by Read The Docs.

.. _guide: https://docs.readthedocs.io/en/latest/intro/import-guide.html

Other Sources
-------------

For a more detailed guide on how to use Sphinx and reStructuredText, please see this `documentation tutorial`_ on Hitchhiker's Guide to Python. 

.. _documentation tutorial: https://docs.python-guide.org/writing/documentation/




