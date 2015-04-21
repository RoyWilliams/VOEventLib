# Copyright 2010 Roy D. Williams

import sys
from VOEventLib.VOEvent import *
from VOEventLib.Vutil import *

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print "Usage: python modify.py <filename>"
    sys.exit(1)

# parse the event from the file name
v = parse(filename)

tables = v.get_What().get_Table()
for t in tables:
    print "TABLE %s" % t.get_name()
    utable = utilityTable(t)

# get all the table entries
    colList = utable.getByCols()
    for (name, vect) in colList.items():
        print 'column', name, '=', vect
