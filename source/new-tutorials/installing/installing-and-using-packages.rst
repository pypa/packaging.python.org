Installing and using packages
=============================

This tutorial will show you how to install a Python package and use it. Before
you read this tutorial make sure you have all the packaging tools by reading
:doc:`installing-packaging-tools`.

Creating a virtualenv
---------------------

As mentioned in the previous tutorial, :ref:`virtualenv` allows you to manage
separate package installations for different projects. It essentially allows
you to create a "virtual" isolated Python installation and install packages
into that virtual installation. When you switch projects, you can simply
create a new virtual environment and not have to worry about breaking the
packages installed in the other environments. It is always recommended to use
a virtualenv while developing Python applications.

To create a virtual environment, go to your project's directory (you can
just create an empty directory somewhere for this tutorial) and run
virtualenv:

.. code-block:: bash 

    virtualenv env

.. Note:: If you have Python 2 and 3 installed, you will probably need to
    specify the Python version you want using
    ``virtualenv --python python3 env``.

The second argument is the location to create the virtualenv. Generally, you
can just create this in your project and call it ``env``.

.. Note:: You should exclude your virtualenv directory from your version
    control system using ``.gitignore`` or similar.

virtualenv will create a virtual Python installation in the ``env`` folder.


Activating a virtualenv
-----------------------

Before you can start installing or using packages in your virtualenv you'll
need to *activate* it. 

On macOS and Linux:

.. code-block:: bash

    source env/bin/activate

On Windows::

    .\env\Scripts\activate

You can confirm you're in the virtualenv by checking the location of your
Python interpreter, it should point to the ``env`` directory.

On macOS and Linux:

.. code-block:: bash

    which python
    .../env/bin/python

On Windows:

.. code-block:: bash

    where python
    .../env/bin/python.exe


Installing packages
-------------------

Now that you're in your virtualenv you can install packages. Let's install
the excellent `Requests`_ library from the :term:`Python Package Index (PyPI)`:

.. code-block:: bash

    pip install requests

pip should download requests and all of its dependencies and install them:

.. code-block:: text

    Collecting requests
      Using cached requests-2.18.4-py2.py3-none-any.whl
    Collecting chardet<3.1.0,>=3.0.2 (from requests)
      Using cached chardet-3.0.4-py2.py3-none-any.whl
    Collecting urllib3<1.23,>=1.21.1 (from requests)
      Using cached urllib3-1.22-py2.py3-none-any.whl
    Collecting certifi>=2017.4.17 (from requests)
      Using cached certifi-2017.7.27.1-py2.py3-none-any.whl
    Collecting idna<2.7,>=2.5 (from requests)
      Using cached idna-2.6-py2.py3-none-any.whl
    Installing collected packages: chardet, urllib3, certifi, idna, requests
    Successfully installed certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

.. _Requests: http://docs.python-requests.org/


Using installed packages
------------------------

Now that requests is installed you can create a simple ``main.py`` file to
use it:

.. code-block:: python

    import requests

    response = requests.get('https://httpbin.org/ip')

    print('Your IP is {}'.format(response.text))

As long as you're in your virtualenv you'll be able to import and use your
installed packages.


Leaving the virtualenv
----------------------

If you want to switch projects or otherwise leave your virtualenv, simply run:

.. code-block:: bash

    deactivate

If you want to re-enter the virtualenv just follow the same instructions above
about activating a virtualenv. There's no need to re-create the virtualenv.


Next steps
----------

You now know how to install and use Python packages! :) However, there is
still some other useful things to learn that can be helpful.

.. TODO:: Link to tutorials on using requirements.txt, guides on using different install sources and methods, etc.
