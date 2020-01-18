tot=0
for n in range(1,1000):
  if (n//3 == n/3) or (n//5 == n/5) : tot = tot + n
print (tot)