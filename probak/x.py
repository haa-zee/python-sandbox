# teszt
import time,sys

	

def avg2(lista):
	return reduce(lambda a,b: a+b, lista)/float(len(lista))

def avg1(lista):
	return sum(lista)/float(len(lista))


avg=avg1

if(len(sys.argv)>1):
	if(sys.argv[1]!='1'):
		avg=avg2
s=time.time()
n=0
with open("kern.log","r") as f:
	l=[ len(r) for r in f ]
	n=len(l)
	#for r in f:
	#	l.append(len(r))
	#	n+=1
print "start computing"
print n,avg(l)
print "finished"
e=time.time()
print e-s
