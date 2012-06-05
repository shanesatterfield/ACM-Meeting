"""
    Test for DirHandler class

    Author: David Nuon
"""

#!/usr/bin/env python
from testhelper import *
import sys

clear()

current_directory = sys.path[0]

sys.path.insert(0, '../app/lib')
sys.path.insert(0, '../app/')

import traceback
import am_config

test = None


def init_test():
    global test
    from dirhandler import DirHandler as dirhandler
    test = dirhandler(current_directory)

# Make a directory to do our test in
def testenv_test():
    global test

    # We make a directory to make our test in
    test.mkdir("test")
    test.cd("test")

# Make a bunch of files in our test directory
def makefiles_test():
    global test

    # Make some files
    for n in xrange(0, 10):
        test.create_file(str(n), "n")

    if not comp(test.ls(), map(lambda x : str(x), range(0, 10))):
        print test.ls()
        wtf()

    # And then delete them
    for n in xrange(0, 10):
        test.rm(str(n))

    print test.ls()
    if not comp(test.ls(), []):
        wtf()


def mkdir_test():
    global test
    for n in xrange(0, 10):
        test.mkdir(str(n))

    if not comp(test.dir(), map(lambda x : str(x), range(0, 10))):
        wtf()

def rmdir_test():
    global test
    for n in xrange(0, 10):
        test.rmdir(str(n))

    if not comp(test.dir(), []):
        wtf()

def create_file_test():
    global test
    test.create_file("test.md", "201212")

def rm_file_test():
    global test
    test.rm("test.md")    

def create_file_child_dir_test():
    global test
    test.mkdir("test_dir")
    test.create_file("test.md", "test", "test_dir")    

def rm_dir_with_files_test():
    global test
    test.rmdir("test_dir")

def cleantestenv():
    global test

    test.cd("..")
    test.rmdir("test")


do_test(init_test, "DirHandler was able to be initialized", "Intializatid")
do_test(testenv_test, "mkdir test/cd test")
do_test(makefiles_test, "Makefiles test")
do_test(mkdir_test, "make ten directories", "mkdir()")
do_test(rmdir_test,"remove the ten directories created", "rmdir()")
do_test(create_file_test, "create a file in root.", "create_file()")
do_test(create_file_child_dir_test, "create_file in a child director of root.", "create_file in child dir")
do_test(rm_dir_with_files_test, "rmdir() a directory with files in it", "rmdir() a directory with files in it")
do_test(rm_file_test, "deleting test.md in root")
do_test(cleantestenv, "cleaning up our mess")


print "Test done"