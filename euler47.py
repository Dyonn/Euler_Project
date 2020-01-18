import time
from math import sqrt
start=time.time()

#first find the primes
primes=[]
primeslist=[]
maxprime=1000000000
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

answer=False
n=1
while answer==False:
  n+=1
  if n//100==n/100:print(n)
  answer=True
  for m in range(n,n+3):
    finished=False
    if answer==True:
      for p1 in primeslist:
        if (answer==True and finished==False) or p1>m:
          answer=False
          break
        if m//p1 == m/p1:
          sofar=m/p1
          for p2 in primeslist:
            if p2>p1:
              if (answer==True and finished==False) or p2>sofar:
                answer=False
                break
              if sofar//p2==sofar/p2:
                sofar=sofar/p2
                for p3 in primeslist:
                  if p3>p2:
                    if (answer==True and finished==False) or p3>sofar:
                      answer=False
                      break
                    if sofar//p3==sofar/p3:
                      sofar=sofar/p3
                      for p4 in primeslist:
                        if p4>p3:
                          if (answer==True and finished==False) or p4>sofar:
                            answer=False
                            break
                          if sofar//p4==sofar/p4:
                             finished=True
                             answer=True
                             break              
print(n,time.time()-start," seconds")
