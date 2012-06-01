"""
ACM Meeting Script

Author: Shane Satterfield
Author: David Nuon
"""

#!/usr/bin/env python
import sys
sys.path.insert(0, './app/lib')
sys.path.insert(0, './app/')

import argparse
import am_config
import argparse

parser = argparse.ArgumentParser()

## Command List
parser.add_argument('--render', '-rn', help="Prints the HTML document from markdwn." )
parser_args = parser.parse_args()

print parser_args