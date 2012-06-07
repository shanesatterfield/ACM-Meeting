"""
	Test for OfficerRoll class

	Author: David Nuon
"""

#!/usr/bin/env python
from testhelper import *
import sys

clear()

sys.path.insert(0, "../app/model/")
sys.path.insert(0, "../app/lib/")

def init_test():
	from officerroll import OfficerRoll

do_test(init_test, "Initialize")