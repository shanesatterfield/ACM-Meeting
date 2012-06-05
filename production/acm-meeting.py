"""
ACM Meeting Script

Author: Shane Satterfield
Author: David Nuon
"""

#!/usr/bin/env python
import sys
sys.path.insert(0, './app/lib')
sys.path.insert(0, './app/')

import argparse
import datetime

import am_config
from dirhandler import DirHandler

parser = argparse.ArgumentParser()
dirhandler = DirHandler(am_config.MINUTES_DIRECTORY)

## Command List
parser.add_argument('--make', '-m', help="Makes a new directory for minutes")
parser.add_argument('--start', '-s', help="Copies agenda.md to minutes.md")
parser.add_argument('--upload', '-u', help="Upload the current directory to the server")
parser.add_argument('--sync', '-x', help="Compare files of a minutes directory with remote, get newer files.")

pargs = parser.parse_args()

if pargs.make:
    now = datetime.datetime.now()
    folder_name = pargs.make

    if pargs.make == 'current':
        folder_name = now.strftime("%Y-%m-%d")

    try:
        dirhandler.mkdir(folder_name)
        dirhandler.cd(folder_name)
        dirhandler.create_file("agenda.md", "") # TODO: Add content here
    except IOError:
        print "The directory %s already exists" % folder_name

elif pargs.start:
    if pargs.start == 'current':
        print "You are copying over agenda.md to minutes.md"
    else:
        pass

elif pargs.upload:
    if pargs.upload == 'upload':
        print "You are going to upload the documents to the server"
    else:
        pass

elif pargs.sync:
    if pargs.upload == 'sync':
        print "You are going to sync and pull down newer documents from the server"
    else:
        pass