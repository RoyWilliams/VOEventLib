# Copyright 2010 Roy D. Williams
"""
validate: Sample program for use with VOEvent library.
Reads a VOEvent file and checks it for compliance
See the VOEvent specification for details
http://www.ivoa.net/Documents/latest/VOEvent.html
"""

from VOEventLib.Vutil import *
import sys

schema = ""
if len(sys.argv) > 1:
    xmlString = open(sys.argv[1]).read()
else:
    print "Usage: python validate.py <filename> [<schemafile>]"
    sys.exit(1)

if len(sys.argv) > 2:
    schema = sys.argv[2]

if len(schema) == 0:
    (success, message) = validate(xmlString)
else:
    (success, message) = validate(xmlString, schema)

print success
print message
