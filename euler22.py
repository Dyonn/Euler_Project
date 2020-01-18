import time
import csv
start=time.time()
with open('p022_names.txt', 'r') as f:
  reader = csv.reader(f)
  matrix = list(reader)
matrix = matrix[0]
matrix=list(matrix)
matrix.sort()
total=0
for n in range(len(matrix)):
  score=0
  for m in range(len(matrix[n])):
    name=matrix[n]
    score+=ord(name[m])-64
  score*=(n+1)
  total+=score
print(total,time.time()-start," seconds")

#A=65