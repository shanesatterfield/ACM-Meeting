"""
	Test for FTPSession class

	Author: David Nuon
	Author: Shane Satterfield
"""

#!/usr/bin/env python
from testhelper import *
import sys
import argparse

parser = argparse.ArgumentParser()

## Command List
parser.add_argument('--host', '-host', help="Host Name")
parser.add_argument('--username', '-u', help="Username")
parser.add_argument('--password', '-p', default=None, help="Password")

clear()

sys.path.insert(0, '../')

sys.path.insert(0, '../')

# We're testing the FTP module
test = None
running = True


def init_test():
    global test
    global running

    from acm.util.ftpsession import FTPSession

    pargs = parser.parse_args()

    if pargs.host and pargs.username:
        host = pargs.host
        user = pargs.username
        if pargs.password == None:
            passwd = ""
        else:
            passwd = pargs.password
    
        test = FTPSession(host, user, passwd) 
    else:
        running = False
        raise Exception

def make_environment():
    global test
    test.mkdir("test")
    test.cd("test") # This folder should be empty

def spam_dir_test():
    global test
    dirlist = map(lambda x: str(x), range(0, 10))

    for item in dirlist:
        test.mkdir(item)

    if not comp(test.dir(), dirlist):
        wtf("The created directories do not appear in the list")

    for item in dirlist:
        test.rmdir(item)


def cleanup_test():
    global test

    if not test.current_dir() == "test":
        wtf("We should be in our test environment.")
    else:
        test.cd("..")
        test.rmdir_all("test")
    test.quit()

do_test(init_test, "Initialize")

if running:
    do_test(make_environment, "Start our testing")
    do_test(spam_dir_test, "Make lots of directories")
    do_test(cleanup_test, "Cleanup")
else:
    raise Exception("Not enough arguments")
