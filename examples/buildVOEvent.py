# Copyright 2010 Roy D. Williams
"""
buildVOEvent: Creates a complex VOEvent with tables
See the VOEvent specification for details
http://www.ivoa.net/Documents/latest/VOEvent.html
"""

from VOEventLib.VOEvent import *
from VOEventLib.Vutil import *
import sys, os

objid = '8df63j29dj8shj'

# Kings and Queens of England
tudors = [
{'start':'1485 Aug 22', 'end':'1509 Apr 21', 'death':'asthma & gout',            'name':'Henry VII'},
{'start':'1509 Apr 21', 'end':'1547',        'death':'syphilis & gluttony',      'name':'Henry VIII'},
{'start':'1547 Jan 28', 'end':'1553',        'death':'TB & congenital syphilis', 'name':'Edward VI'},
{'start':'1553 Jul 10', 'end':'1553 Jul 19', 'death':'dethroned; beheaded 1554', 'name':'Lady Jane Grey'},
{'start':'1553 Jul 6',  'end':'1558 Nov 17', 'death':'influenza',                'name':'Mary I'},
{'start':'1558 Nov 17', 'end':'1603 Mar 24', 'death':'cold, tonsilitis, illness','name':'Elizabeth I'}
]


############ VOEvent header ############################
v = VOEvent.VOEvent(version="2.0")
v.set_ivorn("ivo://silly/billy#%s" % objid)
v.set_role("test")
v.set_Description("Report of some irrelevant information")

############ Who ############################
w = Who()
a = Author()
a.add_contactName("Donald Duck and Goofy")
a.add_contactEmail("dduck@disney.com")
w.set_Author(a)
v.set_Who(w)

############ What ############################
w = What()

# params related to the event. None are in Groups.
p = Param(name="objid", ucd="meta.id", value="%s"% objid)
p.set_Description(["The object ID assigned by the Sillybilly survey"])
w.add_Param(p)

p = Param(name="magnitude", ucd="phot.mag", unit="mag", dataType="float",  value="13.34")
p.set_Description(["The magnitude (brightest V-band) of the moving object"])
w.add_Param(p)

# A Group of Params
g = Group(name="Animals")
p = Param(name="Tiger", dataType="float", value="1.234")
g.add_Param(p)
p = Param(name="Lion",  dataType="float", value="1.234")
g.add_Param(p)
w.add_Group(g)

# make the Kings and Queens table
t = Table(name="Tudor Monarchs", Description=["Accession and death for the Tudor monarchs"])
t.add_Param(Param(name="House", ucd="meta.text", value="Tudor"))
t.add_Field(Field(name="Name"))
t.add_Field(Field(name="Start Reign"))
t.add_Field(Field(name="End Reign"))
t.add_Field(Field(name="Cause of Death"))
ut = utilityTable(t)
ut.blankTable(len(tudors))
for i in range(len(tudors)):
    r = tudors[i]
    ut.setValue("Name",           i, r["name"])
    ut.setValue("Start Reign",    i, r["start"])
    ut.setValue("End Reign",      i, r["end"])
    ut.setValue("Cause of Death", i, r["death"])
t = ut.getTable()
w.add_Table(t)

v.set_What(w)

############ Wherewhen ############################
wwd = {'observatory':     'Keck',
       'coord_system':    'UTC-FK5-GEO',
       'time':            '2018-11-11T11:11:11',
       'timeError':       0.11,
       'longitude':       123.45,
       'latitude':        67.89,
       'positionalError': 0.01,
}

ww = makeWhereWhen(wwd)
if ww: v.set_WhereWhen(ww)

############ Citation ############################
c = Citations()
c.add_EventIVORN(EventIVORN(cite="followup", valueOf_="ivo:silly/billy#89474"))
c.add_EventIVORN(EventIVORN(cite="followup", valueOf_="ivo:silly/billy#89475"))
v.set_Citations(c)

############ output the event ############################
xml = stringVOEvent(v)
print xml
