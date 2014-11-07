#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Nov 7, 2014

@author: haazee
'''
import re
import time


def count_matching_lines():
    n=0
    netfilter_expression=re.compile(r'^(.*)(user\.warning) (kernel:) (DROP|REJECT|ACCEPT) (IN=\w+) .*$')
    with open("kern.log","r") as logfile:
        for next_line in logfile:
            if netfilter_expression.match(next_line):
                n+=1
    return n
            
if __name__ == '__main__':
    start=time.time()
    print count_matching_lines()
    end=time.time()
    print "Elapsed time: %f secs"%(end-start)