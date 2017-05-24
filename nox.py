# Copyright 2017, PyPA
# The Python Packaging User Guide is licensed under a Creative Commons
# Attribution-ShareAlike license:
#   http://creativecommons.org/licenses/by-sa/3.0.

import os

import nox


@nox.session
def build(session):
    session.interpreter = 'python3.6'
    session.install('-r', 'requirements.txt')
    # Treat warnings as errors.
    session.env['SPHINXOPTS'] = '-W'
    session.run('make', 'clean', 'html')


def linkmonitor(session, command):
    if not os.path.exists(os.path.join('build', 'html')):
        session.error('HTML output not available, run nox -s build first.')
    session.interpreter = 'python3.6'
    session.install('-r', 'scripts/linkmonitor/requirements.txt')
    session.run(
        'python', 'scripts/linkmonitor/linkmonitor.py', command)


@nox.session
def checklinks(session):
    linkmonitor(session, 'check')


@nox.session
def updatelinks(session):
    linkmonitor(session, 'update')
