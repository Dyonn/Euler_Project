import time
start=time.time()
array=[1]
for n in range(1,2000000):
  array.append(n)
  array[n]=1
total=0
array[1]=0
for n in range(2,1415):
  if array[n] == 1:
    for m in range(n+1,2000000):
      if array[m] == 1:
        if m//n == m/n:
          array[m]=0
for n in range(1,2000000):
  if array[n]==1:total=total+n
print(total,time.time()-start," seconds")
