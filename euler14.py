import time
start=time.time()
longest=0
which=0
for n in range(1,1000000):
  counter=0
  num=n
  while num>1:
    if num//2==num/2:
      num=num/2
    else:
      num=3*num+1
    counter=counter+1    
  if counter>longest:
    longest=counter
    which=n
print(which,time.time()-start," seconds")
