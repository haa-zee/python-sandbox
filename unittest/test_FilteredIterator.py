# -*- coding: utf-8 -*-
'''
Created on Jun 22, 2014

@author: haazee
'''

import unittest

class ListWithReadline(object):
    def __init__(self, listobject):
        self.__listobject=listobject
        
    def readline(self):
        if len(self.__listobject)>0:
            returnedObject=self.__listobject.pop(0)
        else:
            returnedObject=None
        return returnedObject
    
    
class Test(unittest.TestCase):

    
    def testLogIterator(self):
        import fwloganalyzer.FilteredStream
        testStrings=ListWithReadline([u"... kernel: DROP... - ezt nem szabad megtalálnia",'kernel: DROP ...', 'filler', 
                                      'text text text kernel: ACCEPT text text', 'DROP', 'ACCEPT',u"2014-05-12 14:33:55 localhost warning.kernel: DROP IN="])
        self.assertEqual(3, len([i for i in fwloganalyzer.FilteredStream(testStrings)]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogIterator']
    unittest.main()