import time
start=time.time()

#first find the primes
primes=[1]
primeslist=[]
lowprimes=[]
for n in range(1,2000000):
  primes.append(0)
  primes[n]=1
primes[1]=0
for n in range(2,1415):
  if primes[n] == 1:
    for m in range(n*2,2000000):
      if primes[m] == 1:
        if m//n == m/n:
          primes[m]=0
for n in range(1,2000000):
  if primes[n]==1:
    primeslist.append(n)
  if n<1000:
    lowprimes.append(n)

maxprimes=0
n=0
for a in range(-999,1000):
  print(a)
  for b in lowprimes:
    if b>=n:
      prim=0
      while n*n+a*n+b in primeslist:
        n+=1
      if n>maxprimes:
        maxprimes=n
        which_a=a
        which_b=b
        print (a,b,n)
print(which_a*which_b,maxprimes,time.time()-start," seconds")
  
