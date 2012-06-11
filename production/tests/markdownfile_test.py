"""
	Test for MarkdownFile class

	Author: David Nuon
"""

#!/usr/bin/env python
from testhelper import *
import sys
sys.path.insert(0, '../')

clear()

import traceback

test = None

def init_test():
	global test
	from acm.util.markdownfile import MarkdownFile

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