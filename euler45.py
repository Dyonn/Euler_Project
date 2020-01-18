#Pn=1.5n^2-0.5n-x
#Hn=2n^2-n-x
#Tn=0.5n^2+0.5n-x


import time
from math import sqrt
start=time.time()
answer=False
n=285
while answer==False:
  n+=1
  tri=n*(n+1)/2
  pent=(0.5+sqrt(0.25+6*tri))/3
  if int(pent)==pent:
    hexa=(1+sqrt(1+8*tri))/4
    if int(hexa)==hexa:
      answer=True
print(tri,time.time()-start," seconds")

