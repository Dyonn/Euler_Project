import time
import csv
start=time.time()
with open('p042_words.txt', 'r') as f:
  reader = csv.reader(f)
  words_list=list(reader)
words=words_list[0]

triangles=[]
for n in range(1,50):
  triangles.append(n*(n+1)/2)

counter=0
for n in words:
  tot=0
  for m in range(len(n)):
    tot+=ord(n[m])-64
  if tot in triangles:counter+=1
 
print(counter,time.time()-start," seconds")
