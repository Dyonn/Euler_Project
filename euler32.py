import time
start=time.time()
products=[]
for n in range(1,100):
  for m in range(123,10000):
    ans=str(n*m)+str(n)+str(m)
    if len(ans)==9:
      pandigital=1
      for o in range(1,10):
        if ans.find(str(o))==-1:
          pandigital=0
          break
      if pandigital==1: products.append(n*m)
products=list(dict.fromkeys(products))
total=0
for n in products:
  total+=n
print(total,time.time()-start," seconds")

#can only be made from 2x3=5 or 1x4=4 digit products