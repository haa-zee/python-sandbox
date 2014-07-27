#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 26, 2014

@author: haazee
'''

class C(object):
    c=1

    @classmethod
    def s(cls,v):
        cls.c=v
    
        
        
C.s(2)
print C.c

C.s(33)
print C.c
