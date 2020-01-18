import time
start=time.time()
thenum=600851475143
for fac in range(3,thenum):
  f = thenum/fac
  if (int(f) == f):
    print(f)
    f=int(f)
    prime=1
    for p in range(2,f):
      if (f//p == f/p):
        prime=0
        break
    if (prime==1):
      break
print(time.time()-start," seconds")
