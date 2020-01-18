import time
start=time.time()
powers=[]
for a in range(2,101):
  for b in range(2,101):
    powers.append(a**b)
leng=len(list(set(powers)))
print(leng,time.time()-start," seconds")
