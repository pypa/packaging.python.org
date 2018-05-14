# Copyright 2017, PyPA
# The Python Packaging User Guide is licensed under a Creative Commons
# Attribution-ShareAlike license:
#   http://creativecommons.org/licenses/by-sa/3.0.

import shutil
import nox


@nox.session
def build(session):
    session.interpreter = 'python3.6'
    session.install('-r', 'requirements.txt')
    # Treat warnings as errors.
    session.env['SPHINXOPTS'] = '-W'
    session.run(shutil.rmtree, 'build', ignore_errors=True)
    session.run('sphinx-build', '-W', '-b', 'html', 'source', 'build')


@nox.session
def preview(session):
    session.reuse_existing_virtualenv = True
    build(session)
    session.chdir('build/html')
    session.run('python', '-m', 'http.server')
