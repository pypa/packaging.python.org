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

.. code-block:: python

	pip install -U sphinx

For other installation methods, see this `installation guide`_ by Sphinx.

.. _installation guide: http://www.sphinx-doc.org/en/master/usage/installation.html

Getting Started With Sphinx
---------------------------

Create a ``doc`` directory inside your project to hold your documentation:

.. code-block:: python

	cd /path/to/project
	mkdir docs

Run ``spinx-quickstart`` inside the ``docs`` directory:

.. code-block:: python

	cd docs
	sphinx-quickstart

This sets up a source directory, walks you through some basic configurations, and creates an ``index.rst`` file as well as a ``conf.py`` file.

You can add some information about your project in ``index.rst``, then build them:

.. code-block:: python

	make html

For more details on the build process, see this `guide`_ by Read The Docs.

.. _guide: https://docs.readthedocs.io/en/latest/intro/import-guide.html