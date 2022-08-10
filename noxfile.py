# Copyright 2017, PyPA
# The Python Packaging User Guide is licensed under a Creative Commons
# Attribution-ShareAlike license:
#   http://creativecommons.org/licenses/by-sa/3.0.

import shutil
import nox


nox.options.sessions = []


@nox.session()
def translation(session):
    """
    Build the gettext .pot files.
    """
    session.install("-r", "requirements.txt")
    target_dir = "locales"
    session.run(
        "sphinx-build", 
        "-b", "gettext",  # build gettext-style message catalogs (.pot file)
        "-d", ".nox/.doctrees/", # path to put the cache
        "source/",  # where the rst files are located
        target_dir, # where to put the .pot file
    )

@nox.session()
def build(session, autobuild=False):
    """
    Make the website.
    """
    session.install("-r", "requirements.txt")

    target_build_dir = "build"

    shutil.rmtree(target_build_dir, ignore_errors=True)

    if autobuild:
        command = "sphinx-autobuild"
        extra_args = "-H", "0.0.0.0"
    else:
        # NOTE: This branch adds options that are unsupported by autobuild
        command = "sphinx-build"
        extra_args = (
            "--color",  # colorize the output
            "--keep-going",  # don't interrupt the build on the first warning
        )

    session.run(
        command, *extra_args,
        "-j", "auto",  # parallelize the build
        "-b", "html",  # use HTML builder
        "-n",  # nitpicky warn about all missing references
        "-W",  # Treat warnings as errors.
        *session.posargs,
        "source",  # where the rst files are located
        target_build_dir,  # where to put the html output
    )


@nox.session()
def preview(session):
    """
    Make and preview the website.
    """
    session.install("sphinx-autobuild")
    build(session, autobuild=True)


@nox.session()
def linkcheck(session):
    """
    Check for broken links.
    """
    session.install("-r", "requirements.txt")
    session.run(
        "sphinx-build", 
        "-b", "linkcheck", # use linkcheck builder
        "--color",
        "-n", "-W", "--keep-going",  # be strict
        "source", # where the rst files are located
        "build", # where to put the check output
    )
