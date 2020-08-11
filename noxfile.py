# Copyright 2017, PyPA
# The Python Packaging User Guide is licensed under a Creative Commons
# Attribution-ShareAlike license:
#   http://creativecommons.org/licenses/by-sa/3.0.

import shutil
import nox


@nox.session(py="3")
def build(session, autobuild=False):
    session.install("-r", "requirements.txt")

    target_build_dir = "build"

    shutil.rmtree(target_build_dir, ignore_errors=True)

    if autobuild:
        command = "sphinx-autobuild"
        extra_args = "-H", "0.0.0.0"
    else:
        command = "sphinx-build"
        extra_args = (
            "--color",  # colorize the output, unsupported by autobuild
        )

    session.run(
        command, *extra_args,
        # FIXME: uncomment once the theme is fixed
        # Ref: https://github.com/pypa/pypa-docs-theme/issues/17
        # "-j", "auto",  # parallelize the build
        "-b", "html",  # use HTML builder
        "-n",  # nitpicky warn about all missing references
        "-W",  # Treat warnings as errors.
        "source",  # where the rst files are located
        target_build_dir,  # where to put the html output
    )


@nox.session(py="3")
def preview(session):
    session.install("sphinx-autobuild")
    build(session, autobuild=True)
