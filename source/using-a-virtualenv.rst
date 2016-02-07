==========================
Using virtual environments
==========================

By default, when we use ``pip`` to install packages, it will install
them in a default location where all other packages are installed. This
default behaviour may however not be desirable. The solution is to use
a tool called `virtualenv
<https://virtualenv.readthedocs.org/en/latest/>`__. It allows us to
create isolated *virtual environments* in which we can install our
packages. You can think of isolated environments as individual sandboxes. By
having a separate virtual environment for each of your projects, you
will keep the packages installed in each separate from one another.

Installation
------------

If you are using Python 2 or Python 3 (upto and including Python 3.2),
install virtualenv using ``pip install virtualenv`` or ``pip3 install
virtualenv`` respectively. You will then be able to create and work
with virtual environments via the ``virtualenv`` command.

If you are using Python 3.3 or a more recent version, support for
creating virtual environments should already be installed and
accessible via the ``pyvenv`` command.

For the rest of the guide, I will be using ``pyvenv`` as the command
name assuming that you are using Python 3.3 or greater. However, for
other Python versions, ``virtualenv`` should work the same.


Creating a virtual environment
------------------------------

The first step is to create a virtual environment which creates a new
sub-directory at your specified location. It may be a good idea to
have all your virtual environments under one sub-directory. Let's
assume that I want the new virtual environment ``tabulate`` to be
created in the sub-directory ``$HOME/work/virtualenvs`` where
``$HOME`` refers to the user's home directory on Linux and Mac
OS X. The following command will carry out this operation:

.. code::

   $ pyvenv ~/work/virtualenvs/tabulate

If you are on Windows, assuming that we want the new virtualenv to be
created under ``C:\work\virtualenvs``, the equivalent command would
be:

.. code::

   > python -m venv C:\work\virtualenvs\tabulate

A new virtual environment ``tabulate`` has now been created for us. To
be able to install packages in it, we need to *activate* it.

Activating a virtual environment and installing packages
--------------------------------------------------------

On Linux/Mac OS X we can activate our virtual environment,
``tabulate`` via the following command:

.. code::

   $ source ~/work/virtualenvs/tabulate/bin/activate

On Windows, the command to activate the virtual environment is:

.. code::

   > \work\virtualenvs\tabulate\Scripts\activate

Now, we are in the virtual environment. To see the packages currently
installed in our virtual enviroment, we can use the ``pip list`` command:

.. code::

   (tabulate) $ pip3 list
   pip (7.1.0)
   setuptools (18.0.1)

You can see that we have only two packages installed in our virtual
environment. We can install our desired packages using `pip` now. As
an example of a package, we will install and use the `tabulate
<https://bitbucket.org/astanin/python-tabulate>`__ package. It is an easy way
to display tabular data without having to do a lot of tedious work
ourselves.

.. code ::

   (tabulate) $ pip install tabulate
   Collecting tabulate
   Using cached tabulate-0.7.5.tar.gz
   Installing collected packages: tabulate
   Running setup.py install for tabulate
   Successfully installed tabulate-0.7.5

Our package is now installed, let's run a simple example to see how it works.

Using the package
-----------------

The program below will print a table consisting of the numbers in a
list and how many times each appears as a table: 

.. code::

   from collections import Counter
   from tabulate import tabulate

   def frequency_table(numbers):
       table = Counter(numbers)
       rows = []
       for number in table.most_common():
            rows.append([number[0], number[1]])
       print(tabulate(rows, headers=['Number', 'Frequency']))

   if __name__=='__main__':
       scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
       frequency_table(scores)


Save the above program to a file and run it while within the virtual
environment. On Linux/Mac OS X, this will be just using the
``python`` or ``python3`` command and passing the file name you saved
the file to:

.. code::

   $ python <file.py>

You should see the following output when run:

.. code::

   Number    Frequency
   --------  -----------
       9            5
       6            3
       1            2
       5            2
       7            2
       8            2
      10            2
       2            1
       4            1


Feel free to explore the ``tabulate`` package more to see the
different types of table you can create with it.

Deactivating a virtual environment
----------------------------------

Once we are done working in our virtual environment, the
``deactivate`` command will deactivate the virtual environment for us:

.. code::

   (tabulate) $ deactivate

The same command will work on Windows as well.

Deleting a virtual environment
------------------------------

Over time, the number of virtual environments can increase and you may
want to just remove the ones you don't need anymore. To do so, simply
delete the directory for the new virtual enviroment. For example, for
the ``tabulate`` virtual environment we created above, delete the
`tabulate` directory from ``$HOME/work/virtualenvs`` on Linux/Mac OS X
or ``C:\work\virtualenvs`` on Windows.

Key steps
---------

To summarize, here are the steps when working with virtual environments:

- Create a virtual environment using ``pyvenv`` or ``virtualenv``
- Activate it using the activate script
- Work
- Deactivate using ``deactivate``
