# -*- coding: utf-8 -*-
'''
Created on Jun 22, 2014

@author: haazee
'''

import unittest

import fwloganalyzer.FilteredStream

class ListWithReadline(list):

    def readline(self):
        if len(self)>0:
            return self.pop(0)
        return None
    
    
class Test(unittest.TestCase):

    
    def testLogIteratorWithAMockObject(self):
        testStrings=ListWithReadline([u"... kernel: DROP... - ezt nem szabad megtalálnia",'kernel: DROP ...', 'filler', 
                                      'text text text kernel: ACCEPT text text', 'DROP', 'ACCEPT',u"2014-05-12 14:33:55 localhost warning.kernel: DROP IN="])
        self.assertEqual(3, len([i for i in fwloganalyzer.FilteredStream(testStrings)]))
    
    def testLogIteratorWithAFile(self):
        with open("kernel.log","r") as k:
            self.assertEqual(521479, len([i for i in fwloganalyzer.FilteredStream(k)]))
            
    
    def testLogIteratorWithNoMatchingRegex(self):
        import re
        with open("kernel.log","r") as k:
            self.assertEqual(0, len([i for i in fwloganalyzer.FilteredStream(k, re.compile(r"^krixkrax-biztosan-nincs-talalat.*$"))]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogIterator']
    unittest.main()