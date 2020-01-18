import time
start=time.time()
bigsum=0
for n in range(11,230000):
  stri=str(n)
  tot=0
  for m in range(len(str(n))):
    tot+=int(stri[m])**5
  if tot==n:bigsum+=n
print(bigsum,time.time()-start," seconds")
