import time
start=time.time()
counter=0 
triangle=[0]
factors=1
while factors <= 500:
  factors=1
  counter+=1
  triangle.append(0)
  triangle[counter] = triangle[counter-1] + counter
  if triangle[counter]>70000000:
    for f in range(2,50):
      if triangle[counter]//f == triangle[counter]/f:factors = factors + 1
    if factors>=5:
      for f in range(50,5000):
        if triangle[counter]//f == triangle[counter]/f:factors = factors + 1
      if factors>=100:
        for f in range(5000,triangle[counter]//2):
          if triangle[counter]//f == triangle[counter]/f:factors = factors + 1
    print (triangle[counter],":",factors)
print(triangle[counter],time.time()-start," seconds")
