import time
import math
start=time.time()

#first find the primes
primes=[1]
primeslist=[1]
maxprime=1000000
for n in range(2,maxprime):
  primes.append(0)
  primes[n]=1
primes[1]=0
for n in range(2,int(math.sqrt(maxprime))):
  if primes[n] == 1:
    for m in range(n*2,maxprime):
      if primes[m] == 1:
        if m//n == m/n:
          primes[m]=0
for n in range(1,maxprime):
  if primes[n]==1:
    primeslist.append(n)

circulars=0
for n in primeslist:
  allprimes=1
  newstr=str(n)
  for o in range(1,len(newstr)):
    str_n=newstr
    newstr=""
    for m in range(1,len(str_n)):
      newstr+=str_n[m]
    newstr+=str_n[0]
    if int(newstr) not in primeslist:allprimes=0
  if allprimes==1:
    circulars+=1
    print(n)
print(circulars,time.time()-start," seconds")
