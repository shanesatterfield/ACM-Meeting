"""
	Test for MarkdownFile class

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
	from markdownfile import MarkdownFile

	class TestClass(MarkdownFile):
		def reset(self):
			self._contents = ""
			self.level = ""

	test = TestClass()

def print_file():
	global test
	test.write("- This is a test.")
	test.write("- This is a test.")

	print test
	test.reset()

do_test(init_test, "Initialization")
do_test(print_file, "Print File")