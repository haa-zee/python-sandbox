# -*- coding: utf-8 -*-
'''
Created on Nov 5, 2014

@author: haazee
'''

import threading

class Szal2(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(Szal2,self).__init__()
        
    def run(self):
        print "Start ", threading.current_thread().getName()
        for i in xrange(5000000000): pass
        print "Finished ", threading.current_thread().getName()
        
        
if __name__ == "__main__":
        t1=Szal2()
        t2=Szal2()
        t1.start()
        t2.start()
        t2.join()
        t1.join()
        