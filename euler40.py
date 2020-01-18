import time
start=time.time()
leng=0
n=1
target=1
answer=1
while leng<1000000:
  if leng<target and leng+len(str(n))>=target:
    answer*=int(str(n)[target-leng-1])
    target*=10
  leng+=len(str(n))
  n+=1
print(answer,time.time()-start," seconds")
