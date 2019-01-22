# Copyright 2017, PyPA
# The Python Packaging User Guide is licensed under a Creative Commons
# Attribution-ShareAlike license:
#   http://creativecommons.org/licenses/by-sa/3.0.

import shutil
import nox


@nox.session(py="3")
def build(session, autobuild=False):
    session.install("-r", "requirements.txt")
    # Treat warnings as errors.
    session.env["SPHINXOPTS"] = "-W"

    shutil.rmtree("build", ignore_errors=True)

    if autobuild:
        command = "sphinx-autobuild"
    else:
        command = "sphinx-build"

    session.run(command, "-W", "-b", "html", "source", "build")


@nox.session(py="3")
def preview(session):
    session.install("sphinx-autobuild")
    build(session, autobuild=True)
