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

def init_test():
	from ftpsession import FTPSession
	test = FTPSession("", "", "") #TODO : Write a valid constructor

def ls_test():
    pass

def create_file_test():
    pass

def rm_test():
    pass

def file_exists_test():
    pass

def dir_test():
    pass

def mkdir_test():
    pass

def rmdir_test():
    pass

def dir_exists_test():
    pass

def upload_test():
    pass

def downlaod_test():
    pass

do_test(init_test, "Create Object")
do_test(ls_test, "List Remote Files")
do_test(create_file_test, "Create Files")
do_test(rm_test, "Delete Files")
do_test(file_exists_test, "Check for file")
do_test(dir_test, "List Directories")
do_test(mkdir_test, "Make Directory")
do_test(rmdir_test, "Delete Directory")
do_test(dir_exists_test, "Check if Directory exists")
do_test(upload_test, "Upload")
do_test(downlaod_test, "Donwload")
