import time
start=time.time()
fib=[]
fib.append(0)
fib.append(1)
fib.append(1)
leng=2
while len(str(fib[leng]))<1000:
  leng+=1
  nxt=fib[leng-2]+fib[leng-1]
  fib.append(nxt)
print(leng,time.time()-start," seconds")
