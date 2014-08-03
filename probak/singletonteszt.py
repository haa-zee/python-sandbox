#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 27, 2014

@author: haazee

Innen: http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
'''
class Singleton(type):
    _instances = {}

    # A köv. sor végére kell a #@NoSelf, hogy az eclipse ne pofázzon az első helyen álló cls argumentum miatt
    def __call__(cls, *args, **kwargs):  #@NoSelf
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Python2
#class MyClass(BaseClass):
#    __metaclass__ = Singleton

#Python3
#class MyClass(BaseClass, metaclass=Singleton):
#    pass

class SingSingSingleton(object):
    __metaclass__=Singleton
    
        
class XSingSingSingleton(SingSingSingleton):
    pass

a=SingSingSingleton()
b=SingSingSingleton()
c=XSingSingSingleton()
print a,b
print c
