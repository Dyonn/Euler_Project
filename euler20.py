import time
import math
start=time.time()
ans=str(math.factorial(100))
tot=0
for n in range(len(ans)):
  tot+=int(ans[n])
print(tot,time.time()-start," seconds")

