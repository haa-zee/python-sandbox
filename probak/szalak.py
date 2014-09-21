#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Aug 2, 2014

@author: haazee
'''

import threading
import time

class Proba(object):
    
    def __init__(self, lockObject):
        self.lock=lockObject
        self.szam=0
        
    def run(self):
        self.lock.acquire()
        print threading.current_thread().getName(), " started"
        self.lock.release()
        for i in xrange(120):
            w=self.szam
            time.sleep(0.01)
            x=self.szam
            if w==x and threading.active_count()>1:
                self.szam+=1
            else:
                self.lock.acquire()
                print threading.current_thread().getName(), "finished.  ",w,x,self.szam, " ",threading.active_count()
                self.lock.release()
                return
            
            
locker=threading.RLock()
p=Proba(locker)

for i in xrange(150):
    t=threading.Thread(target=p.run)
    t.start()
