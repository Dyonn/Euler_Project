import time
import math
start=time.time()
most=0
for n in range(1,1000):
  solutions=0
  for a in range(1,n-1):
    for b in range(1,n-a-1):
      if a+b+math.sqrt((a**2)+(b**2))==n:solutions+=1
  if solutions>most:
    most=solutions
    which=n
print(which,time.time()-start," seconds")
