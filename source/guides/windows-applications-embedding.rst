.. _`Windows applications`:

=================================================
Creating a Windows application that embeds Python
=================================================


Overview
========


Why embed Python?
-----------------

When writing an application on Windows, whether command line or GUI, it
integrates much better with the operating system if the application is delivered
as a native Windows executable. However, Python is not a natively compiled
language, and so does not create executables by default.

The normal way around this issue is to make your Python code into a library, and
declare one or more "script entry points" for the library. When the library is
installed, the installer will generate a native executable which invokes the
Python interpreter, calling your entry point function. This is a very effective
solution, and is used by many Python applications. It is supported by utilities
such as ``pipx`` and ``uv tool``, which make managing such entry points (and the
virtual environments needed to support them) easy.

There are, however, some downsides to this approach. The entry point wrapper
results in a chain of processes being created - the wrapper itself, the virtual
environment redirector, and finally the Python interpreter. Creating all these
processes isn't cheap, and particularly for a small command line utility, it
impacts application startup time noticeably. Furthermore, the entry point
wrapper is a standard executable with a zipfile attached - because of this, the
application cannot be signed in advance by the developer, and this is often seen
as "suspicious" by virus scanners. If a scan is triggered, this can make the
application even slower to start, as well as running the risk of "false
positives", where an innocent app is flagged as malicious.

In addition, you may not want to expose your users to the fact that you wrote
your code in Python. The implementation language should not be something your
users need to care about.

If any of these issues matter to you, you should consider writing your
application in Python, but then embedding it, and the Python interpreter, into a
native executable application that you can ship to your users. This does require
you to write a small amount of native code (typically in C), but the code is
mostly boilerplate and easy to maintain.


What will your application look like?
-------------------------------------

When embedding Python, it is not possible to create a "single file" application.
The Python interpreter itself is made up of multiple files, so you will need
those at a minimum. However, once you have decided to ship your application as
multiple files, it becomes very easy to structure your code.

There are basically three "parts" to an embedded application:

1. The main executable that the user runs.
2. The Python interpreter.
3. Your application code, written in Python.

You can, if you wish, dump all of those items into a single directory. However,
it is much easier to manage the application if you keep them separate.
Therefore, the recommended layout is::

    Application directory
        MyAwesomePythonApp.exe
        interp
            (embedded Python interpreter)
        lib
            (Python code implementing the application)

The remainder of this guide will assume this layout.


How to build your application
=============================

Writing the Python code
-----------------------

Your Python application should be runnable by invoking a single function in your
application code. Typically, this function will be called ``main`` and will be
located in the root package of your application, but that isn't a hard
requirement. If you prefer to locate the function somewhere else, all you will
need to do is make a small modification to the wrapper code.

Your code can use 3rd party dependencies freely. These will be installed along
with your application.

When you are ready to build your application, you can install the Python code
using::

    pip install --target "<Application directory>\lib" MyAwesomePythonApp

You can then run your application as follows::

    $env:PYTHONPATH="<Application directory>\lib"
    python -c "from MyAwesomePythonApp import main; main()"

Note that this uses your system Python interpreter. This will not be the case
for the final app, but it is useful to test that the Python code has been
installed correctly.

If that works, congratulations! You have successfully created the Python part of
your application.

The embedded interpreter
------------------------

You can download embeddable builds of Python from
https://www.python.org/downloads/windows/. You want the "Windows embeddable
package". There are usually 3 versions, for 64-bit, 32-bit and ARM64
architectures. Generally, you should use the 64-bit version unless you have a
specific need for one of the others (in which case, you will need to modify how
you compile the main application executable slightly, to match).

Simply unpack the downloaded zip file into the "interp" subdirectory of your
application layout.

In order for your embedded interpreter to be able to find your application code,
you should modify the ``python*._pth`` directory contained in the distribution. By
default it looks like this::

    python313.zip
    .

    # Uncomment to run site.main() automatically
    #import site

You need to add a single line, ``../lib``, after the line with the dot. The
resulting file will look like this::

    python313.zip
    .
    ../lib

    # Uncomment to run site.main() automatically
    #import site

If you have put your application Python code somewhere else, this is the only
thing you need to change. The file contains a list of directories (relative to
the interpreter directory) which will be added to Python's ``sys.path`` when
starting the interpreter.

The driver application
----------------------

This is the only part of your application that has to be written in C. The
application code should look like the following::

    /* Include the Python headers */
    #include <Python.h>

    /* Finding the Python interpreter */
    #include <windows.h>
    #include <pathcch.h>

    /* Tell the Visual Studio linker what libraries we need */
    #pragma comment(lib, "delayimp")
    #pragma comment(lib, "pathcch")

    int dll_dir(wchar_t *path) {
        wchar_t interp_dir[PATHCCH_MAX_CCH];
        if (GetModuleFileNameW(NULL, interp_dir, PATHCCH_MAX_CCH) &&
            SUCCEEDED(PathCchRemoveFileSpec(interp_dir, PATHCCH_MAX_CCH)) &&
            SUCCEEDED(PathCchCombineEx(interp_dir, PATHCCH_MAX_CCH, interp_dir, path, PATHCCH_ALLOW_LONG_PATHS)) &&
            SetDefaultDllDirectories(LOAD_LIBRARY_SEARCH_DEFAULT_DIRS) &&
            AddDllDirectory(interp_dir) != 0) {
                    return 1;
        }
        return 0;
    }

    /* Your application main program */
    int wmain(int argc, wchar_t **argv)
    {
        PyStatus status;
        PyConfig config;

        /* Tell the loader where to find the Python interpreter.
         * This is the name, relative to the directory containing
         * the application executable, of the directory where you
         * placed the embeddable Python distribution.
         *
         * This MUST be called before any functions from the Python
         * runtime are called.
         */
        if (!dll_dir(L"interp"))
            return -1;

        /* Initialise the Python configuration */
        PyConfig_InitIsolatedConfig(&config);
        /* Pass the C argv array to ``sys.argv`` */
        PyConfig_SetArgv(&config, argc, argv);
        /* Install the standard Python KeyboardInterrupt handler */
        config.install_signal_handlers = 1;
        /* Initialise the runtime */
        status = Py_InitializeFromConfig(&config);
        /* Deal with any errors */
        if (PyStatus_Exception(status)) {
            PyConfig_Clear(&config);
            if (PyStatus_IsExit(status)) {
                return status.exitcode;
            }
            Py_ExitStatusException(status);
            return -1;
        }

        /* CPython is now initialised.
         * Now load and run your application code.
         */

        int exitCode = -1;
        PyObject *module = PyImport_ImportModule("MyAwesomePythonApp");
        if (module) {
            // Pass any more arguments here
            PyObject *result = PyObject_CallMethod(module, "main", NULL);
            if (result) {
                exitCode = 0;
                Py_DECREF(result);
            }
            Py_DECREF(module);
        }
        if (exitCode != 0) {
            PyErr_Print();
        }
        Py_Finalize();
        return exitCode;
    }


Almost all of this is boilerplate that you can copy unchanged into your
application, if you wish.

You should change the name of the module that gets imported, and if you chose a
different name for your main function, you should change that as well.
Everything else can be left unaltered.

If you want to customise the way the interpreter is run, or set up the
environment in a specific way, you can do so by modifying this code. However,
such modifications are out of scope for this guide. If you want to make such
changes, you should be familiar with the relevant parts of the Python C API
documentation and the Windows API.

Building the driver application
-------------------------------

To build the driver application, you will need a copy of Visual Studio, and a
full installation of the same version of Python as you are using for the
embedded interpreter. The reason for the full Python installation is that the
embedded version does not include the necessary C headers and library files to
build code using the Python C API.

It may be possible to use a C compiler other than Visual Studio, but if you wish
to do this, you will need to work out how to do the build, including the
necessary delay loading, yourself.

To compile the code, you need to know the location of the Python headers and
library files. You can get these locations from the interpreter as follows::

    import sysconfig

    print("Include files:", sysconfig.get_path("include"))
    print("Library files:", sysconfig.get_config_var("LIBDIR"))

To build your application, you can then simply use the following commands::

    cl /c /Fo:main.obj main.c /I<Include File Location>
    link main.obj /OUT:MyAwesomePythonApp.exe /DELAYLOAD:python313.dll /LIBPATH:<Lib File Location>

You should use the correct Python version in the ``/DELAYLOAD`` argument, based
on the name of the DLL in your embedded distribution. For a production build,
you might want additional options, such as optimisation (although the wrapper
exe is small enough that optimisation might not make a significant difference).

If you place the resulting ``exe`` file in your application target directory, and
run it, your application should run, exactly the same as it did when you invoked
it using Python directly.

Why do we delay load Python?
----------------------------

In order to run the application, it needs to be able to find the Python
interpreter. This is handled by the linker, as with any other referenced DLL.
However, by default your embedded Python interpreter will not be on the standard
search path for DLLs, and as a result your application will fail, or will pick
up the wrong Python installation. By delay loading Python, we allow our code to
change the search path *before* loading the interpreter. This is handled by the
``dll_dir`` function in the application code.

It *is* possible to create an application without using delay loading, but this
requires that the Python distribution is unpacked in the root of your
application directory. The recommended approach achieves a cleaner separation of
the various parts of the application.


Taking things further
=====================

Distributing your application
-----------------------------

Now that you have your application, you will want to distribute it. There are
many ways of doing this, from simply publishing a zip of the application
directory and asking your users to unpack it somewhere appropriate, to
full-scale installers. This guide doesn't cover installers, as they are a
complex subject of their own. However, the requirements of a Python application
built this way are fairly trivial (unpack the application directory and provide
a way for the user to run the exe), so most of the complexity is unneeded (but
it's there if you have special requirements).

Sharing code
------------

Until now, we've assumed that you have one application, with its own Python code
and its own interpreter. This is the simplest case, but you may have a suite of
applications, and not want to have the overhead of an interpreter for each. Or
you may have a lot of common Python code, with many different entry points.

This is fine - it's easy to modify the layout to cover these cases. You can have
as many executable files in the application directory as you want.  These can
all call their own entry point - they can even use completely independent
libraries of Python code, although in that case you'd need to add some code to
manipulate ``sys.path``.

The point is that the basic structure can be as flexible as you want it to be -
but it's better to start simple and add features as you need them, so that you
don't have to maintain code that handles cases you don't care about.


Potential Issues
================

Using tkinter
-------------

The embedded Python distribution does not include tkinter. If your application
needs a GUI, the simplest option is likely to be to use one of the other GUI
frameworks available from PyPI, such as PyQt or wxPython.

If your only option is tkinter, you will need to add a copy to the embedded
distribution, or use a different distribution. Both of these options are outside
the scope of this guide, however.

Subprocesses and ``sys.executable``
-----------------------------------

A common pattern in Python code is to run a Python subprocess using
``subprocess.run([sys.executable, ...])``. This will not work for an embedded
application, as ``sys.executable`` is your application, not the Python
interpreter.

The embedded distribution does contain a Python interpreter, which can be used
in cases like this, but you will need to locate it yourself::

    python_executable = Path(sys.executable).parent / ("interp/python.exe")

If you are using the ``multiprocessing`` module, it has a specific method you
must use to configure it to work correctly in an embedded environment,
documented `in the Library reference
<https://docs.python.org/3.13/library/multiprocessing.html#multiprocessing.set_executable>`_.


What about other operating systems?
===================================

This guide only applies to Windows. On other operating systems, there is no
"embeddable" build of Python (at least, not at the time of writing). On the
positive side, though, operating systems other than Windows have less need for
this, as support for interpreted code as applications is generally better. In
particular, on Unix a Python file with a "shebang" line is treated as a
first-class application, and there is no benefit to making a native
appliocation.

So while this discussion is specific to Windows, the problem it is solving is
*also* unique to Windows.
