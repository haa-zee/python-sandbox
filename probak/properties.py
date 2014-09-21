#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 30, 2014

@author: haazee
'''

class Oszt(object):
    '''Oszt akkó' mi van? :) '''
    
    @property
    def timestamp(self):
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, a):
        print '---- {} ----'.format(a)
        self._timestamp=a
        
    @timestamp.deleter
    def timestamp(self):
        del(self._timestamp)
        
        
o=Oszt()
o.timestamp=88
print o.timestamp
del(o.timestamp)