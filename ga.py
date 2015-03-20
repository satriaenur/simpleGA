import random

def fitness(f):
	return 1/(f+0.1)

def fungsi(x):
	return 3*x[0]**2+2*x[1]**2-4*x[0]+x[1]/2

def encode(x,y):
	binx = bin(x)[2:].zfill(4)
	biny = bin(y)[2:].zfill(4)
	return list(binx+biny)

def decode(x):
	intx = int(x[:4],2)
	inty = int(x[4:],2)
	return [intx,inty]

def populasi():
	return [encode(random.randint(0,10),random.randint(0,10)) for x in xrange(10)]

a = populasi()
fit = [fitness(fungsi(decode("".join(x)))) for x in a]

print a
print ""
print fit

print decode("".join(a[fit.index(min(fit))]))