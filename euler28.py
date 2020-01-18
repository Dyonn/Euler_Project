import time
start=time.time()
matrix = [[0 for x in range(1002)] for y in range(1002)] 
matrix[500][500]=1
x=501
y=500
for n in range(2,1002002):
  matrix[x][y]=n
  if matrix[x-1][y]>0 and matrix[x][y-1]==0:
    y=y-1
  elif matrix[x][y+1]>0 and matrix[x-1][y]==0:
    x=x-1
  elif matrix[x+1][y]>0 and matrix[x][y+1]==0:
    y=y+1
  else:
    x=x+1
tot=0
for n in range(1001):
  tot+=matrix[n][n]+matrix[1000-n][n]
tot-=matrix[500][500]
print(tot,time.time()-start," seconds")
