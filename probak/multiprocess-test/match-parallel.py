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
        
    def __str__(self):
        cmd_to_str=["*INVALID*","CMD_DATA","CMD_STOP"]
        return cmd_to_str[self.command]+","+str(self.data)
        
            
class Reader(mp.Process):
    
    def __init__(self, queue_object, file_name="kern.log", *args, **kwargs):
        self.input_file=file_name
        self.queue_object=queue_object
        super(Reader,self).__init__(*args,**kwargs)
        
    def run(self):
        BUFFER_SIZE=2000000
        n=0
        print self.name," started..."
        with open(self.input_file,"r") as infile:
            next_block=infile.readlines(BUFFER_SIZE)
            while(len(next_block)>0):
                n+=1
                self.queue_object.put(Message(data=next_block))
                next_block=infile.readlines(BUFFER_SIZE)
        
                 
        print "lines: %u"%(n)
        
        
class Processor(mp.Process):
    def __init__(self, queue_object, result_queue, *args, **kwargs):
        self.queue_object=queue_object
        self.result_queue=result_queue
        self.matching_object=re.compile(r'^(.*)(user\.warning) (kernel:) (DROP|REJECT|ACCEPT) (IN=\w+) .*$')
        self.n=0
        super(Processor,self).__init__(*args,**kwargs)
        
    def run(self):
        print self.name," started..."
        try:
            next_object=self.queue_object.get()
            while next_object.command != Message.CMD_STOP:
                for i in next_object.data:
                    if self.matching_object.match(i):
                        self.n+=1
                next_object=self.queue_object.get()
        except Exception as e:
            print "Queue - get - error - (finished?)", mp.current_process().name
            print e
            print "-"*80
            self.result_queue.put(Message(data=(self.name,self.ident, self.n)))
            return
        
        print "Processor finished normally", self.name, "(%u)"%(self.n)
        self.result_queue.put(Message(data=(self.name,self.ident, self.n)))
        return
    
#--------------------------------------------------------------------            

if __name__ == '__main__':
    start=time.time()
    
    q=mp.Queue(40)
    result_queue=mp.Queue()
    
    r=Reader(q,"kern.log")
    plist=[Processor(q,result_queue) for i in xrange(3)]
    r.start()
    for p in plist:
        p.start()
        
        
    r.join()
    for p in plist:
        q.put(Message(Message.CMD_STOP))
    
    for p in plist:
        p.join()

    while not result_queue.empty():
        print result_queue.get()
        
        
    end=time.time()
    print "Elapsed time: %f secs"%((end-start))
    print "konyec"