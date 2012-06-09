"""
	Test for Agenda class

	Author: David Nuon
"""

#!/usr/bin/env python
from testhelper import *
import sys

clear()

sys.path.insert(0, "../app/model/")
sys.path.insert(0, "../app/lib/")

# A CSV File

testdata = """name,position,email,exec
David Nuon,President,chair@csulb.acm.org,1
Ian Goegebuer,Vice President,vicechair@csulb.acm.org,1
Christopher Gomez,Treasurer,treasurer@csulb.acm.org,1
Shane Satterfield,Secretary,secretary@csulb.acm.org,1
Victoria Hatfield,AESB Representative,aesbrep@csulb.acm.org,
Anthony Gialcalone,Librarian,librarian@csulb.acm.org,
Leo Tronolone,Publicity and Recruitment Chair,publicity@csulb.acm.org,
James Coolidge,Market Manager,vendor@csulb.acm.org,
Orion Sakorn,Historian,historian@csulb.acm.org,
Diana Ignacio,Event Coordinator,events@csulb.acm.org,
John-Jimi Kathleen Som,Webmaster,webmaster@csulb.acm.org,
Johnny Patterson,Office Technician,tech@csulb.acm.org,"""

global test

def init_test():
	global test

	from agenda import Agenda
	test = Agenda(testdata)

def render_test():
	global test
	print test.markdown()


do_test(init_test, "Initialize")
do_test(render_test, "Render Businesss")
