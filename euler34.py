import time
import math
start=time.time()
bigtot=0
for n in range(3,2540161):
  str_n=str(n)
  tot=0
  for m in range(len(str_n)):
    tot+=math.factorial(int(str_n[m]))
  if n==tot:bigtot+=n
print(bigtot,time.time()-start," seconds")
