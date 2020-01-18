import time
start=time.time()
sum100=0
sumsq=0
for n in range(1,101):
  sum100=sum100+n
  sumsq=sumsq+n**2
  print(sumsq)
answer=sum100**2-sumsq
print(answer,time.time()-start," seconds")
