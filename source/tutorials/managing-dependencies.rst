.. _managing-dependencies:

Managing Application Dependencies
=================================

The :ref:`package installation tutorial <installing-packages>`
covered the basics of getting set up to install and update Python packages.

However, running these commands interactively can get tedious even for your
own personal projects, and things get even more difficult when trying to set up
development environments automatically for projects with multiple contributors.

This tutorial walks you through the use of :ref:`Pipenv` to manage dependencies
for an application. It will show you how to install and use the necessary tools
and make strong recommendations on best practices.

Keep in mind that Python is used for a great many different purposes, and
precisely how you want to manage your dependencies may change based on how you
decide to publish your software. The guidance presented here is most directly
applicable to the development and deployment of network services (including
web applications), but is also very well suited to managing development and
testing environments for any kind of project.

.. Note:: This guide is written for Python 3, however, these instructions
    should also work on Python 2.7.

Installing Pipenv
-----------------

:ref:`Pipenv` is a dependency manager for Python projects. If you're familiar
with Node.js' `npm`_ or Ruby's `bundler`_, it is similar in spirit to those
tools. While :ref:`pip` alone is often sufficient for personal use, Pipenv is
recommended for collaborative projects as it's a higher-level tool that
simplifies dependency management for common use cases.

Use ``pip`` to install Pipenv:

.. code-block:: python

    pip install --user pipenv

.. _pipenv-user-base:

.. Note:: This does a `user installation`_ to prevent breaking any system-wide
    packages. If ``pipenv`` isn't available in your shell after installation,
    you'll need to add the `user base`_'s binary directory to your ``PATH``.

    On Linux and macOS you can find the user base binary directory by running
    ``python -m site --user-base`` and adding ``bin`` to the end. For example,
    this will typically print ``~/.local`` (with ``~`` expanded to the
    absolute path to your home directory) so you'll need to add
    ``~/.local/bin`` to your ``PATH``. You can set your ``PATH`` permanently by
    `modifying ~/.profile`_.

    On Windows you can find the user base binary directory by running
    ``py -m site --user-site`` and replacing ``site-packages`` with
    ``Scripts``. For example, this could return
    ``C:\Users\Username\AppData\Roaming\Python36\site-packages`` so you would
    need to set your ``PATH`` to include
    ``C:\Users\Username\AppData\Roaming\Python36\Scripts``. You can set your
    user ``PATH`` permanently in the `Control Panel`_. You may need to log
    out for the ``PATH`` changes to take effect.

.. _npm: https://www.npmjs.com/
.. _bundler: http://bundler.io/
.. _user base: https://docs.python.org/3/library/site.html#site.USER_BASE
.. _user installation: https://pip.pypa.io/en/stable/user_guide/#user-installs
.. _modifying ~/.profile: https://stackoverflow.com/a/14638025
.. _Control Panel: https://msdn.microsoft.com/en-us/library/windows/desktop/bb776899(v=vs.85).aspx

Installing packages for your project
------------------------------------

Pipenv manages dependencies on a per-project basis. To install packages,
change into your project's directory (or just an empty directory for this
tutorial) and run:

.. code-block:: bash

    cd myproject
    pipenv install requests

Pipenv will install the `Requests`_ library and create a ``Pipfile``
for you in your project's directory. The :ref:`Pipfile` is used to track which
dependencies your project needs in case you need to re-install them, such as
when you share your project with others. You should get output similar to this
(although the exact paths shown will vary):

.. code-block:: text

    Creating a Pipfile for this project...
    Creating a virtualenv for this project...
    Using base prefix '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6'
    New python executable in ~/.local/share/virtualenvs/tmp-agwWamBd/bin/python3.6
    Also creating executable in ~/.local/share/virtualenvs/tmp-agwWamBd/bin/python
    Installing setuptools, pip, wheel...done.

    Virtualenv location: ~/.local/share/virtualenvs/tmp-agwWamBd
    Installing requests...
    Collecting requests
      Using cached requests-2.18.4-py2.py3-none-any.whl
    Collecting idna<2.7,>=2.5 (from requests)
      Using cached idna-2.6-py2.py3-none-any.whl
    Collecting urllib3<1.23,>=1.21.1 (from requests)
      Using cached urllib3-1.22-py2.py3-none-any.whl
    Collecting chardet<3.1.0,>=3.0.2 (from requests)
      Using cached chardet-3.0.4-py2.py3-none-any.whl
    Collecting certifi>=2017.4.17 (from requests)
      Using cached certifi-2017.7.27.1-py2.py3-none-any.whl
    Installing collected packages: idna, urllib3, chardet, certifi, requests
    Successfully installed certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

    Adding requests to Pipfile's [packages]...

.. _Requests: https://python-requests.org
.. _pipenv-tox: https://docs.pipenv.org/advanced/#tox-automation-project


Using installed packages
------------------------

Now that Requests is installed you can create a simple :file:`main.py` file
to use it:

.. code-block:: python

    import requests

    response = requests.get('https://httpbin.org/ip')

    print('Your IP is {0}'.format(response.json()['origin']))

Then you can run this script using ``pipenv run``:

.. code-block:: bash

    pipenv run python main.py

You should get output similar to this:

.. code-block:: text

    Your IP is 8.8.8.8

Using ``pipenv run`` ensures that your installed packages are available to
your script. It's also possible to spawn a new shell that ensures all commands
have access to your installed packages with ``pipenv shell``.


Next steps
----------

Congratulations, you now know how to effectively manage dependencies and
development environments on a collaborative Python project! ✨ 🍰 ✨

If you're interested in creating and distributing your own Python packages, see
the :ref:`tutorial on packaging and distributing packages <distributing-packages>`.

Note that when your application includes definitions of Python source packages,
they (and their dependencies) can be added to your ``pipenv`` environment with
``pipenv install -e <relative-path-to-source-directory>`` (e.g.
``pipenv install -e .`` or ``pipenv install -e src``).

If you find this particular approach to managing application dependencies isn't
working well for you or your use case, you may want to explore these other tools
and techniques to see if one of them is a better fit:

* `pip-tools <https://github.com/jazzband/pip-tools>`_ to build your own
  custom workflow from lower level pieces like ``pip-compile`` and ``pip-sync``
* `hatch <https://github.com/ofek/hatch>`_ for opinionated coverage of even
  more steps in the project management workflow (such as incrementing versions,
  tagging releases, and creating new skeleton projects from project templates)
* `poetry <https://github.com/sdispater/poetry>`_ for Python developer focused
  components that are designed primarily for publication to a Python package index
  (``pipenv`` deliberately avoids making the assumption that the application
  being worked on will support distribution as a ``pip``-installable Python package,
  while ``poetry`` based applications rely explicitly on their Python packaging
  metadata to describe their application structure and dependencies)
