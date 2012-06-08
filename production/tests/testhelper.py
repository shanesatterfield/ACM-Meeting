import traceback
import sys
import os

def clear():
    name = os.name
    if not name == "nt" and not name == "posix":
        print "\n"*80
    else:
        if name == "nt":
            os.system("cls")
        if name == "posix":
            os.system("clear")

def comp(a, b):
    return a == b

def wtf(str = ""):
    raise Exception("TestFail: " + str)

def good(str):
    print "[PASS]: " + str
    print ""

def bad(str):
    print "[FAIL]: " + str


def do_test(func, good_message, bad_message = None):
    try:
        func()
        good(good_message)
    except Exception, ex:
        if bad_message == None:
            bad(good_message)
        else:
            bad(bad_message)

        print "===================="
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback, limit=130, file=sys.stdout)
        print ex
        print "==================="