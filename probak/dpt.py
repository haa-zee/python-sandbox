#!/usr/bin/env python
import sys
import itertools
import operator
import collections


class protocol_counters(object):
    def __init__(self):
        self.protocol_array={'TCP':collections.Counter(),'UDP':collections.Counter(),'ICMP':collections.Counter(),'Unknown':collections.Counter()}
        
    def add(self,protocol, portnumber=None):
        self.protocol_array[protocol].update(portnumber)
    
    def getCounters(self):
        return self.protocol_array
    
    def __str__(self):
        return str(self.getCounters())
        
        
class host_data(object):
    
    def __init__(self):
        self.source_ips={}
        
    def add_packet_data(self,ipaddr,protocol=None,portnumber=None):
        if ipaddr not in self.source_ips:
            self.source_ips[ipaddr]=protocol_counters()
        self.source_ips[ipaddr].add(protocol,portnumber)
        
    def __iter__(self):
        return self.source_ips.iteritems()
    
    def __len__(self):
        return len(self.source_ips)
    
        


filename=sys.argv[1] if len(sys.argv)>1 else "/home/haazee/kern.log"


hh=host_data()



with open(filename,"r") if filename != "-" else sys.stdin as logfile:
    n=0
    for rec in itertools.ifilter(lambda a: "kernel: DROP IN=" in a, logfile):
        n+=1
        if n%10000==0:
                print n
                
        head=rec[:51]
        fields=rec[52:].split()
        print fields
        data=filter(lambda a: "PROTO=" in a or "DPT=" in a or "SRC=" in a,fields)
        src_ip=data[0].split("=")[1]
        proto=data[1].split("=")[1]
        port=data[2].split("=")[1] if proto in ('TCP','UDP') else None
        hh.add_packet_data(src_ip, proto, port)
        
                
print len(hh)
    
for i,p in hh:
    print i,p.getCounters()['UDP']
