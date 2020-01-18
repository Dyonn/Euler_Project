import time
start=time.time()
abundants=[]
total=0
for n in range(12,28124):
  factorsum=0
  for m in range(1,n):
    if n%m==0:
      factorsum+=m
  if factorsum>n:
    abundants.append(n)
for n in range(1,28124):
  cando=0
  for m in abundants:
    if m>n//2:break
    if n-m in abundants:
      cando=1
      break
  if cando==0:
    total+=n
    print(n)
print(total,time.time()-start," seconds")
