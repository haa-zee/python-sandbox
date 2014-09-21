#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time

start=time.clock()
rex=re.compile('^(.{11})\s(\d\d:\d\d:\d\d)\s(\S+)\s(\w+\.\w+)\s(\w+):\s+(ACCEPT|REJECT|DROP)\s+(.*$)')

count=0
n1,n2=0,0
with open('/home/haazee/logteszt/kern.log.long','r') as log:

    for rec in log:
        w=rex.search(rec)
        if w:
            g=w.groups()
            n1+=1
        else:
            n2+=1
        
end=time.clock()
print(n1,n2)
print "Time: ",end-start
