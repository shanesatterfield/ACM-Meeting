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
import am_config

parser = argparse.ArgumentParser()

## Command List
parser.add_argument('--make', '-m', help="Makes a new directory for minutes")
parser.add_argument('--start', '-s', help="Copies agenda.md to minutes.md")
parser.add_argument('--upload', '-u', help="Upload the current directory to the server")
parser.add_argument('--sync', '-x', help="Compare files of a minutes directory with remote, get newer files.")

pargs = parser.parse_args()

if pargs.make:
	if pargs.make == 'current':
		print "You are making a new minutes directory current."
elif pargs.start:
	if pargs.start == 'current':
		print "You are copying over agenda.md to minutes.md"
elif pargs.upload:
	if pargs.upload == 'upload':
		print "You are going to upload the documents to the server"
elif pargs.sync:
	if pargs.upload == 'sync':
		print "You are going to sync and pull down newer documents from the server"