
# -*- coding: utf-8 -*-

def foo(a, b, c, *extra):
    return len(extra)

def bar(a, b, c, **args):
    return args.get("magicnumber", None) == 7

# test code
if foo(1,2,3,4) == 1:
    print "Good."
if foo(1,2,3,4,5) == 2:
    print "Better."
if bar(1,2,3,magicnumber = 6) == False:
    print "Great."
if bar(1,2,3,magicnumber = 7) == True:
    print "Awesome!"
