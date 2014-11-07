#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Nov 7, 2014

@author: haazee
'''
import re
import multiprocessing as mp
import time

class Message(object):
    CMD_DATA    =   1
    CMD_STOP    =   2
    
    def __init__(self, command=CMD_DATA, data=None):
        self.command=command
        self.data=data
        
            
class Reader(mp.Process):
    
    def __init__(self, queue_object, file_name="kern.log", *args, **kwargs):
        self.input_file=file_name
        self.queue_object=queue_object
        super(Reader,self).__init__(*args,**kwargs)
        
    def run(self):
        BUFFER_SIZE=5000000
        n=0
        print mp.current_process().name
        with open(self.input_file,"r") as infile:
            next_block=infile.readlines(BUFFER_SIZE)
            while(len(next_block)>0):
                n+=1
                self.queue_object.put(Message(data=next_block))
                next_block=infile.readlines(BUFFER_SIZE)
        print "lines: %u"%(n)
        
        
class Processor(mp.Process):
    def __init__(self, queue_object, *args, **kwargs):
        self.queue_object=queue_object
        self.matching_object=re.compile(r'^(.*)(user\.warning) (kernel:) (DROP|REJECT|ACCEPT) (IN=\w+) .*$')
        super(Processor,self).__init__(*args,**kwargs)
        
    def run(self):
        n=0
        try:
            next_object=self.queue_object.get()
            while next_object.command != Message.CMD_STOP:
                for i in next_object.data:
                    if self.matching_object.match(i):
                        n+=1
                next_object=self.queue_object.get()
        except Exception as e:
            print "Queue - get - error - (finished?)", mp.current_process().name
            print e
            print "-"*80
            return
        
        print "Processor finished normally", mp.current_process().name, " line count:",n
            
            
#--------------------------------------------------------------------            

if __name__ == '__main__':
    start=time.time()
    
    q=mp.Queue(4)
    
    r=Reader(q,"kern.log")
    plist=[Processor(q),Processor(q),Processor(q),]
    r.start()
    for p in plist:
        p.start()
    r.join()
    for p in plist:
        q.put(Message(Message.CMD_STOP))
        
    for p in plist:
        p.join()
        
    end=time.time()
    print "Elapsed time: %f secs"%((end-start))
    print "konyec"