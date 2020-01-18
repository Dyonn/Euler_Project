import time
start=time.time()
this=[]
for n in range(21):
  this.append(0)
  this[n]=1
this[0]=1
for n in range(20):
  for m in range(20):
    this[m]=this[m]+this[m-1]
print(this[19],time.time()-start," seconds")
