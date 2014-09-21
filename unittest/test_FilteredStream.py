# -*- coding: utf-8 -*-
'''
Created on Jun 22, 2014

@author: haazee
'''

import unittest
import re
import fwloganalyzer.FilteredStream

class ListWithReadline(list):

    def readline(self):
        if len(self)>0:
            return self.pop(0)
        return None
    
    
class TestFilteredStream(unittest.TestCase):

    def setUp(self):
        self.compiledRegex=re.compile(r"^.*kernel: (DROP|ACCEPT) ")
        self.logfileName="kernel.log"
        self.testStrings=ListWithReadline([u"... kernel: DROP... - ezt nem szabad megtalálnia",'kernel: DROP ...', 'filler', 
                                      'text text text kernel: ACCEPT text text', 'DROP', 'ACCEPT',u"2014-05-12 14:33:55 localhost warning.kernel: DROP IN="])
        
    def testFilteredStreamWithAMockObject(self):
        self.assertEqual(len(self.testStrings), len([i for i in fwloganalyzer.FilteredStream(self.testStrings)]))

    def testFilteredLogStreamWithAMockObject_filtered(self):
        self.assertEqual(3, len([i for i in fwloganalyzer.FilteredStream(self.testStrings,self.compiledRegex)]))
    
    def testFilteredStreamWithAFile(self):
        with open(self.logfileName,"r") as k:
            self.assertEqual(523631, len([i for i in fwloganalyzer.FilteredStream(k)]))
    
    def testFilteredStreamWithAFile_filtered(self):
        with open(self.logfileName,"r") as k:
            self.assertEqual(521479, len([i for i in fwloganalyzer.FilteredStream(k,self.compiledRegex)]))
            
    
    def testLogIteratorWithNoMatchingRegex(self):
        with open(self.logfileName,"r") as k:
            self.assertEqual(0, len([i for i in fwloganalyzer.FilteredStream(k, re.compile(r"^krixkrax-biztosan-nincs-talalat.*$"))]))
      
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogIterator']
    unittest.main()