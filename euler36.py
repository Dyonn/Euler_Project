import time
import math
start=time.time()
tot=0
for n in range(1,1000000,2):
  str_n = str(n)
  back_n=""
  for m in range(len(str_n),0,-1):
    back_n+=str_n[m-1]
  if int(back_n)==n:
    bin_n = str(bin(n))[2:]
    back_bin=""
    for m in range(len(bin_n),0,-1):
      back_bin+=bin_n[m-1]
    if bin_n==back_bin:
      tot+=n
      print(tot,n,back_n,bin_n,back_bin)
print(tot,time.time()-start," seconds")
