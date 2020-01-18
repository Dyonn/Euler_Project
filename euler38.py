import time
import math
start=time.time()
biggest=0
for n in range(1,9999):
  tot=""
  for m in range(1,9):
    tot+=str(n*m)
    if len(tot)>=9:break
  if len(tot)==9:
    found=1
    for m in range(1,9):
      if tot.find(str(m))==-1:
        found=0
        break
    if found==1:
      if int(tot)>biggest:biggest=int(tot)
print(biggest,time.time()-start," seconds")
