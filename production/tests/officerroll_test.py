"""
	Test for OfficerRoll class

	Author: David Nuon
"""

#!/usr/bin/env python
from testhelper import *
import sys
sys.path.insert(0, '../')

clear()

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
global test_business

def init_test():
	global test
	global test_business


	from acm.model.officerroll import OfficerRoll, OfficerBusiness

	test = OfficerRoll(testdata)
	test_business = OfficerBusiness(testdata)


def render_roll():
	global test
	print test.markdown()

def render_business():
	global test_business
	print test_business.markdown()	

do_test(init_test, "Initialize")
do_test(render_business, "Render Businesss")
do_test(render_roll, "Render Roll")