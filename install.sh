#!/usr/bin/env sh
# The best way to install (and uninstall) your Python CLI app is to use pip
# (pip3 for Python 3). In the root directory of the CLI source code, running
# pip3 install . will install this app using setup.py as “instructions”.
# Likewise, running pip3 uninstall pycli will remove the app.

# I decided to put this logic in a shell script so that I didn’t have to always
# manually type out these commands (which gets very tedious when you are
# actively developing a CLI app). So I dump it all in a shell script.

pip3 install -e .
