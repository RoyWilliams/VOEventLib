# Copyright 2010 Roy D. Williams
"""
modify: Sample program for use with VOEvent library.
Reads a VOEvent file and does some modifications, then output.
See the VOEvent specification for details
http://www.ivoa.net/Documents/latest/VOEvent.html
"""

from VOEventLib.VOEvent import *
from VOEventLib.Vutil import *
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print>>sys.stderr, "Usage: python modify.py <filename>"
    sys.exit(1)

# parse the event from the file name
v = parse(filename)

# set the ivorn to something else
v.set_ivorn('ivo://silly/billy#iuw6e7F72ufh')

# set the author
v.get_Who().get_Author().set_contactName(['Mickey Mouse'])

# look for a specific param in the event
param = findParam(v, '', 'magnitude')
if param:
    val = paramValue(param)
    print>>sys.stderr, "Old val is %s" % val
# change the value of the param
    param.set_value("16.45")
    val = paramValue(param)
    print>>sys.stderr, "New val is %s" % val

xml = stringVOEvent(v)
print xml


