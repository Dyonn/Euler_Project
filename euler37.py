import time
import math
start=time.time()

#first find the primes
primes=[]
primeslist=[]
maxprime=1000000
for n in range(maxprime):
  primes.append(1)
primes[1]=0
for n in range(2,int(math.sqrt(maxprime))):
  if primes[n] == 1:
    for m in range(n*2,maxprime):
      if primes[m] == 1:
        if m//n == m/n:
          primes[m]=0
for n in range(2,maxprime):
  if primes[n]==1:
    primeslist.append(n)

tot=0
answers=0
for n in primeslist:
  if n>10:
    str_n=str(n)
    allprimes=1
    for m in range(len(str_n)-1):
      str_n=str_n[1:]
      if int(str_n) not in primeslist:
        allprimes=0
        break
    if allprimes==1:
      str_n=str(n)
      for m in range(len(str_n)-1):
        str_n=str_n[:-1]
        if int(str_n) not in primeslist:
          allprimes=0
          break
    if allprimes==1:
      answers+=1
      tot+=n
      if answers==11:
        break
print(tot,time.time()-start," seconds")
