import time
import itertools
start=time.time()
checked=[]
amicables=0
for n in range(1,10001):
  checked.append(0)
for n in range(1,10000):
  if checked[n]==0:
    checked[n]=1
    factorsum=0
    for m in range(1,n):
      if n//m == n/m:
        factorsum+=m
    if factorsum>n:
      othersum=0
      for m in range(1,factorsum):
        if factorsum//m == factorsum/m:
          othersum+=m
      if othersum==n:
        checked[factorsum]=1
        amicables+=factorsum
        if othersum<10000:
          amicables+=othersum
print(amicables,time.time()-start," seconds")

