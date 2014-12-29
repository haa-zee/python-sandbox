#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 7, 2014

@author: haazee
'''
import hashlib
import pprint

def generator(start=0, count=10000000, step=1):
    return [ (hashlib.sha256(str(i)).hexdigest(),i) for i in xrange(start, start+count, step)]

def compare(s1,s2):
    reply=""
    for i in zip(s1,s2):
        reply+='*' if i[0]==i[1] else '-'
    return reply
        

if __name__ == '__main__':
    n=generator(start=100000000, count=20000000)
    print u"lista kész"
    n.sort()
    print u"rendezés kész"
    maxeq=[0,0]
    for i in xrange(len(n)-1):
        d=compare(n[i][0],n[i+1][0])
        e=d.count('*')
        if(i%100000 == 0):
            print i
        if maxeq[0]<e:
            maxeq[0]=e
            maxeq[1]=i
            
    print maxeq
    first=n[maxeq[1]]
    last=n[maxeq[1]+1]
    
    print "f:",first[0]
    print "l:",last[0]
    print "c:",compare(first[0],last[0])


    
    #pprint.pprint(n[0:1000])
