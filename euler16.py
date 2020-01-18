import time
start=time.time()
full=str(2**1000)
ans=0
for n in range(len(full)):
  ans+=int(full[n])
print(ans,time.time()-start," seconds")
