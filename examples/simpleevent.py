# Copyright 2010 Roy D. Williams
"""
simpleVOEvent: Sample program for use with VOEvent library.
Builds a simple VOEvent packet from nothing
See the VOEvent specification for details
http://www.ivoa.net/Documents/latest/VOEvent.html
"""

import sys
from VOEventLib.VOEvent import *
from VOEventLib.Vutil import *

v = VOEvent.VOEvent(role='test', ivorn='ivo://testing#111')
v.set_version('2.0')
v.set_role('test')

author = Author(contactName=['Donald Duck'])
v.set_Who(Who(Author=author))

what = What()
what.add_Param(Param(name='apple', value='123'))
what.add_Param(Param(name='orange', value='124'))
v.set_What(what)

# print the XML
#sys.stdout.write('<?xml version="1.0" ?>\n')
#v.export(sys.stdout, 0, namespace_='voe:')
#sys.stdout.write('\n')

schemaURL = "http://www.cacr.caltech.edu/~roy/VOEvent/VOEvent2-110220.xsd"

s = stringVOEvent(v, schemaURL)
print s
