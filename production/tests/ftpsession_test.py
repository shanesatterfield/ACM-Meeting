"""
	Test for FTPSession class

	Author: David Nuon
	Author: Shane Satterfield
"""

#!/usr/bin/env python
from testhelper import *
import sys

clear()

sys.path.insert(0, '../app/lib')
sys.path.insert(0, '../app/')

test = None
dirhandler = None

def init_test():
    global test
    global dirhandler

    args = sys.argv[:-1]
    path = ""

    if len(args) == 0:
        wtf("Please enter a path for the local test directory")
    else:
        args[0] = path

    from ftpsession import FTPSession
    from dirhandler import DirHandler

    dirhandler = DirHandler(path)
    test = FTPSession("", "", "") #TODO : Write a valid constructor


def make_environment():
    global test
    test.mkdir("test")
    test.cd("test") # This folder should be empty

def spam_dir_test():
    global test
    dirlist = range(0, 10)

    for item in dirlist:
        test.mkdir(str(item))

    if not comp(test.dir(), dirlist):
        wtf("The created directories do not appear in the list")

    for item in dirlist:
        test.rmdir(str(item))

def spam_files_test():
    global test
    testfiles = ["test_file.txt"]    

    if not comp(test.ls(), []):
        wtf("The test directory is not empty")

    test.create_file(testfiles[0], "file_content")
    if not comp(test.ls(), testfiles):
        wtf("The test file created does not appeear in the list.")

    for n in xrange(0, 10):
        testfiles.append(str(n))
        test.create_file(str(n), "blah blah blah")

    if not comp(test.ls(), testfiles):
        wtf("The 10 new files created do not appear in the list.")

    for item in testfiles:
        test.rm(item)

    if not comp(test.ls(), []):
        wtf("The test directory is not empty")


def cleanup_test():
    global test
    if not test.current_dir() == "test":
        wtf("We should be in our test environment.")
    else:
        test.cd("..")
        test.rmdir("test")
    test.quit()

do_test(init_test, "Initialize")
do_test(make_environment, "Start our testing")
do_test(spam_dir_test, "Make lots of directories")
do_test(spam_files_test, "Make lots of files")
do_test(cleanup_test, "Cleanup")