import time
from fractions import Fraction
start=time.time()
tot=1
for n in range(11,100):
  if n%10>0:
    for m in range(n+1,100):
      if m%10>0:
        if n%10==m%10 and (n//10)/(m//10)==n/m:
          tot*=((n//10)/(m//10))
          print (n,m)
        elif n//10==m//10 and (n%10)/(m%10)==n/m:
          tot*=((n%10)/(m%10))
          print (n,m)
        elif n//10==m%10 and (n%10)/(m//10)==n/m:
          tot*=((n%10)/(m//10))
          print (n,m)
        elif n%10==m//10 and (n//10)/(m%10)==n/m:
          tot*=((n//10)/(m%10))
          print (n,m)
print(tot,time.time()-start," seconds")
