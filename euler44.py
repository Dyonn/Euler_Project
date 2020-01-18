import time
import math
start=time.time()

pentagon = lambda n : n*((3*n)-1)/2

#pentagons=[]
#for n in range(1,1000000):
#  pentagons.append((n*(3*n)-1)/2)

answer=0
for n in range(1,10000):
  print(n)
  for m in range(n,10000):
    if (math.sqrt(24*(pentagon(n)+pentagon(m))+1)+1)/6==(math.sqrt(24*(pentagon(n)+pentagon(m))+1)+1)//6:
      if (math.sqrt(24*(pentagon(m)-pentagon(n))+1)+1)/6==(math.sqrt(24*(pentagon(m)-pentagon(n))+1)+1)//6:
        answer=pentagon(m)-pentagon(n)
        break
  if answer>0:break    
print(answer,time.time()-start," seconds")
