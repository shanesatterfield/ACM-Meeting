"""
	Test for IndentedFile class

	Author: David Nuon
"""

#!/usr/bin/env python
from testhelper import *
import sys

clear()

sys.path.insert(0, '../app/lib')
sys.path.insert(0, '../app/')

test = None

def init_test():
	global test
	from indentedfile import IndentedFile

	class TestClass(IndentedFile):
		def reset(self):
			self._level    = 0
			self._contents = ""

	test = TestClass()

def indent_test():
	global test

	# the default tab is \t
	test_string = "\t2222\n"
	test.tab()
	test.write("2222")

	if not comp(test_string, test.get_contents()):
		wtf()
	
	test.reset()

def indent_with_space_test():
	from indentedfile import IndentedFile

	tab = "   "*3 # Tab with three spaces
	space_test = IndentedFile(tab)

	test_string = tab + "Hello World!\n"
	space_test.tab()
	space_test.write("Hello World!")

	if not comp(test_string, space_test.get_contents()):
		wtf()

	del space_test

def multi_indent():
	global test
	test_string = "\t\t\tLevel 3!\n"

	test.tab()
	test.tab()
	test.tab()
	test.write("Level 3!")

	if not comp(test_string, test.get_contents()):
		wtf()

	test.reset()

def multi_line_test():
	global test

	test_string =  "Level 0\n"
	for n in xrange(1, 4):
		tabs = "\t" * n
		test_string += tabs + "Level %s\n" % n

	test.write("Level " + str(0))
	for n in xrange(1, 4):
		test.tab()
		test.write("Level " + str(n))

	if not comp(test_string, test.get_contents()):
		wtf()

	test.reset()

def tab_and_untab_test():
	global test
	ts = ""
	tab = "\t"
	level = 0

	ts += tab*level + "Foo\n"	
	level += 1
	ts += tab*level + "Bar\n"
	level -= 1
	ts += tab*level + "Hello World!\n"

	test.write("Foo")
	test.tab()
	test.write("Bar")
	test.untab()
	test.write("Hello World!")

	if not comp(ts, test.get_contents()):
		wtf()

	test.reset()

do_test(init_test, "Intialization")
do_test(indent_test, "Indent Test")
do_test(indent_with_space_test, "Indenting with spaces")
do_test(multi_indent, "Multiple indents")
do_test(multi_line_test, "Multiline Indent")
do_test(tab_and_untab_test, "Tab and Untab Test")

print "Test Done"
