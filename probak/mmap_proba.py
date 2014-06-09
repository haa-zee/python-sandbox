#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Ez a program csak azért született, mert valahol olvastam az mmap-ről és elsősorban kíváncsi voltam a
működésére, másodsorban azt is olvastam, hogy gyorsabb, mint a file I/O és ezt is tesztelni akartam.
Na ez utóbbi nem nyert, nálam következetesen hosszabb időket fut mmap-pel, mintha hagyományos I/O-t 
használtam volna.

'''
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

class AverageTimes(object):
	runtimes={}
	@classmethod
	def add(cls,name,time):
		if(cls.runtimes.has_key(name)):
			cls.runtimes[name].append(time)
		else:
			cls.runtimes[name]=[time]


class Measure(object):
	'''
	Ennek az osztálynak a kódját - legalábbis az ötletét - a django.hu-ról "loptam, bár az valamivel kulturáltabb :)"
	http://django.hu/2010/8/19/dekoracio#extended
	'''
	def __init__(self, functionName):
		self.function=functionName
		self.reset()

	def reset(self):
		self.lengthOfTheLastRun=0

	def getLength(self):
		return self.lengthOfTheLastRun

	def __call__(self, *args):
		return self.decorFunction(*args)

	def decorFunction(self, *args):
		starttime=time.time()
		returnValue=self.function(*args)
		endtime=time.time()
		self.lengthOfTheLastRun=endtime-starttime
		AverageTimes.add(self.function.__name__,self.lengthOfTheLastRun)
		return returnValue



@Measure
def teszt_fileio(filename):
	
	c=Counter()
	with open(filename, "r") as f:
		for l in f:
			c.inc()
	print "(file) Read lines:%u"%c.get()

	
@Measure
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


print "\n\n"
for i in AverageTimes.runtimes:
	print "\t",i,sum(AverageTimes.runtimes[i])/len(AverageTimes.runtimes[i])
