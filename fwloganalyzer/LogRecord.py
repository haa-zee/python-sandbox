'''
Created on Jun 4, 2014

@author: haazee
'''
import re


class LogRecord(object):
    '''
    classdocs
    '''


    def __init__(self, logLine):
        '''
        Constructor
        '''
        self.parseLogLine(logLine)
        
    
    def parseLogLine(self):
        self.timestamp=