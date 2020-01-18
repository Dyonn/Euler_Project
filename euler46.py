import time
from math import sqrt
start=time.time()

#first find the primes
primes=[]
primeslist=[]
maxprime=1000000
for n in range(maxprime):
  primes.append(1)
primes[1]=0
for n in range(2,int(sqrt(maxprime))):
  if primes[n] == 1:
    for m in range(n*2,maxprime):
      if primes[m] == 1:
        if m//n == m/n:
          primes[m]=0
for n in range(2,maxprime):
  if primes[n]==1:
    primeslist.append(n)

answer=True
n=34
while answer==True:
  answer=False
  n+=1
  while n in primeslist or n//2==n/2:
    n+=1
  print(n)
  for m in primeslist:
    if m>n or answer==True:break
    test=sqrt((n-m)/2)
    if int(test)==test:answer=True
print(n,time.time()-start," seconds")
