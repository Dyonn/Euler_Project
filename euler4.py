import time
start=time.time()
largest=0
for a in range(1,999):
  for b in range(1,999):
    c = a * b
    str_c = str(c)
    l = len(str_c)
    back_c = ""
    for n in range(l-1,-1,-1):
      back_c = back_c + str_c[n]
    if str_c == back_c and c > largest: largest = c
print(largest,time.time()-start," seconds")
