#!/usr/bin/env python

## @defgroup Setup
# @brief The setup module, which is used to install the python-typeutils library 
from distutils.core import setup
from pkg_resources import require
from pkg_resources import DistributionNotFound
from pkg_resources import VersionConflict
import sys

#we need python version 2.6 or greater
try:
    require('python>=2.6')
except DistributionNotFound as distrErr:
    #handle not found errors and version conflicts.
    print "Failed to find required package:", distrErr.args[0]
    print "Please download and install missing dependencies.\nInstall failed."
    sys.exit(-1)
except VersionConflict as verConfictErr:
    print "Version conflict: Required version(s):", verConfictErr.args[1], " found version:", \
    verConfictErr.args[0]
    print "Please download and install the required version.\nInstall failed."
    sys.exit(-1)

#install the python-typeutils library
setup(
      name = 'python-typeutils',
      version = '0.2',
      description = 'Utilities that are useful in multiple projects, and defy description.',
      author = 'Siddhu Warrier',
      author_email = 'siddhuwarrier@gmail.com',
      url = 'http://siddhuwarrier.homelinux.org/projects/utils',
      package_dir = {'typeutils':'src'},
      packages = ['typeutils'],
      #data files are relative to sys prefix or install exec prefix. So by default this
      #shoulld go into /usr/share/docs/pyxkb/
      data_files = [
                    ('share/docs/python-typeutils/',['doxygen-docs/latex/refman.pdf', 'COPYING', 
                                               'README', 'NEWS', 'AUTHORS'])
                    ]
      )
