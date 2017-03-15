"""Utilities to install a package by name into the current Python environment.
"""

import os
from subprocess import run, PIPE
import sys

def in_conda():
    """Return True if this Python is in conda, False otherwise.
    """
    # TODO: better way of checking this?
    return 'Continuum' in sys.version

def conda_environment_path():
    """Return the path of the conda environment containing this Python.
    
    Before calling this, use in_conda() to check if we're in a conda environment.
    """
    return os.path.dirname(os.path.dirname(sys.executable))

# TODO: show output as it arrives, rather than all at the end
def _reprint_output(res):
    if res.stdout:
        print(res.stdout.decode('utf-8', 'ignore'), file=sys.stdout)
    if res.stderr:
        print(res.stderr.decode('utf-8', 'ignore'), file=sys.stderr)

def conda_install(pkgname):
    """Install a package using conda.
    """
    prefix = conda_environment_path()
    res = run(['conda', 'install', '--prefix', prefix, '--yes', pkgname],
                stdout=PIPE, stderr=PIPE)
    _reprint_output(res)
    return res.returncode

def pip_install(pkgname):
    """Install a package using pip.
    """
    # TODO add --user if appropriate
    res = run([sys.executable, '-m', 'pip', 'install', pkgname])
    _reprint_output(res)
    return res.returncode

def install(pkgname):
    """Install a package using pip or conda.
    """
    if in_conda():
        if conda_install(pkgname) == 0:
            print("Installed {} using conda".format(pkgname))
            return
        print("Installing {} using conda failed, trying pip".format(pkgname))
    
    if pip_install(pkgname) == 0:
        print("Installed {} using pip".format(pkgname))
    else:
        print("ERROR: Failed to install {}".format(pkgname))
