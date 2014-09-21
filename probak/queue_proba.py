#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Aug 23, 2014

@author: haazee
'''
import Queue,threading
import time

class Szal(threading.Thread):
    _lockObject=threading.RLock()
    
    def __init__(self, queue=None):
        self.queue=queue
        super(Szal, self).__init__()
    
    def safeprint(self,string_to_print):
        self.__class__._lockObject.acquire()
        print string_to_print
        self.__class__._lockObject.release()
        
        
    def run(self):
        self.safeprint(self.getName()+"  started")
        
        data=self.queue.get()
        while( data[1] != "stop" ):
            self.safeprint(self.getName() + " ==> " + str(data[0])+"/"+data[1])
            time.sleep(0.5)
            self.queue.task_done()
            data=self.queue.get()
        
        self.safeprint(self.getName()+"  stopped")
        self.queue.task_done()
        
        
        
l=[]
q=Queue.PriorityQueue()

for i in xrange(5):
    l.append(Szal(q))
    
for t in l:
    t.start()

with open("kern.log","r") as kernlog:
    for r in kernlog.readline().split():
        q.put((10,r))

for i in xrange(threading.active_count()-1):
    q.put((9999,"stop"))

    
while(threading.active_count()>1):
    time.sleep(1)
print "Main thread: join"
print "Active tasks: %u\n"%q.unfinished_tasks
q.join()


print "Main thread finished"

    