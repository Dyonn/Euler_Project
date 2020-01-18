import time
start=time.time()
primes=0
counter=2
while primes < 10001:
  prime=1
  for p in range(2,int((counter+1)/2)):
    if (counter//p == counter/p):
      prime=0
      break
  if prime==1:
    primes+=1
  counter=counter+1
print(counter,time.time()-start," seconds")
