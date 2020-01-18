import time
start=time.time()
found=0
for a in range(1,998):
  for b in range(a+1,997):
    c=1000-a-b
    if c>b and a+b+c==1000 and (a**2)+(b**2)==c**2:
      found=1
      break
    if found==1:break
  if found==1:break
if found==1:
  print(a*b*c,time.time()-start," seconds")
else:
  print ("not found")