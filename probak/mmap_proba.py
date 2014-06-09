#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, mmap

class Counter(object):
	def __init__(self):
		self.zero()

	def inc(self):
		self.count += 1
		return self.count

	def zero(self):
		self.count = 0

	def get(self):
		return self.count


def measure(callable,*args,**kwargs):
	def timerfunc(*args,**kwargs):
		t1=time.time()
		callable(*args)
		t2=time.time()
		print "Runtime of %s was %f seconds.\n"%(callable.__name__,t2-t1)
	print "--- measure ---"
	return timerfunc

@measure
def teszt_fileio(filename):
	
	c=Counter()
	with open(filename, "r") as f:
		for l in f:
			c.inc()
	print "(file) Read lines:%u"%c.get()

	
@measure
def teszt_mmap(filename):
	c=Counter()
	with open(filename,"r") as f:
		fnum=f.fileno()
		mm=mmap.mmap(fnum,0,mmap.MAP_PRIVATE,mmap.PROT_READ)
		l=mm.readline()
		while l:
			c.inc()
			l=mm.readline()
	print "(mmap) Read lines: %u"%c.get()
	



for i in xrange(10):
	teszt_fileio("kernel.log")
	teszt_mmap("kernel.log")

