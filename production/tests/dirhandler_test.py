"""
    Test for DirHandler class

    Author: David Nuon
"""

#!/usr/bin/env python
from testhelper import *
import sys

clear()

sys.path.insert(0, '../app/lib')
sys.path.insert(0, '../app/')

import traceback
import am_config

test = None

def init_test():
    global test
    from dirhandler import DirHandler as dirhandler
    test = dirhandler(am_config.MINUTES_DIRECTORY)

def mkdir_test():
    global test
    for n in xrange(0, 10):
        test.mkdir("testdir_" + str(n))

def rmdir_test():
    global test
    for n in xrange(0, 10):
        test.rmdir("testdir_" + str(n))

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

do_test(init_test, "DirHandler was able to be initialized", "Intializatid")
do_test(mkdir_test, "make ten directories", "mkdir()")
do_test(rmdir_test,"remove the ten directories created", "rmdir()")
do_test(create_file_test, "create a file in root.", "create_file()")
do_test(create_file_child_dir_test, "create_file in a child director of root.", "create_file in child dir")
do_test(rm_dir_with_files_test, "rmdir() a directory with files in it", "rmdir() a directory with files in it")
do_test(rm_file_test, "deleting test.md in root")

print "Test done"