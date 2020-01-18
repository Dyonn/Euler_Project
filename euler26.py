import time
import decimal
start=time.time()
with decimal.localcontext() as ctx:
  ctx.prec = 4000
  longest=0
  which=0
  for n in range(2,1000):
    teststr=str(decimal.Decimal(1)/decimal.Decimal(n))
    for m in range(1,2000):
      if len(teststr)>=10+m+m:
        if teststr[10:10+m]==teststr[10+m:10+m+m]:
          if m>longest:
            longest=m
            which=n
          break
  print(longest,which,time.time()-start," seconds")
  
