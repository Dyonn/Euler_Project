tot=0
a=1
b=1
c=2
while c<4000000:
  c=a+b
  if(c//2 == c/2) : tot=tot+c
  a=b
  b=c
print(tot)