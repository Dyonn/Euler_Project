import time
start=time.time()
matrix = [[0 for x in range(15)] for y in range(15)] 
lines=["75"
,"95 64"
,"17 47 82"
,"18 35 87 10"
,"20 04 82 47 65"
,"19 01 23 75 03 34"
,"88 02 77 73 07 63 67"
,"99 65 04 28 06 16 70 92"
,"41 41 26 56 83 40 80 70 33"
,"41 48 72 33 47 32 37 16 94 29"
,"53 71 44 65 25 43 91 52 97 51 14"
,"70 11 33 28 77 73 17 78 39 68 17 57"
,"91 71 52 38 17 14 91 43 58 50 27 29 48"
,"63 66 04 68 89 53 67 30 73 16 69 87 40 31"
,"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]
for n in range(15):
  line=lines[n]
  for m in range(n+1):
    matrix[n][m]=line[m*3:m*3+2]
high=0
for n in range(16384):
  binn="00000000000000"+bin(n)[2:]
  lenn=len(binn)
  total=75
  total+=int(matrix[1][int(binn[lenn-1])])
  total+=int(matrix[2][int(binn[lenn-1])+int(binn[lenn-2])])
  total+=int(matrix[3][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])])
  total+=int(matrix[4][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])])
  total+=int(matrix[5][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])])
  total+=int(matrix[6][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])])
  total+=int(matrix[7][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])+int(binn[lenn-7])])
  total+=int(matrix[8][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])+int(binn[lenn-7])+int(binn[lenn-8])])
  total+=int(matrix[9][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])+int(binn[lenn-7])+int(binn[lenn-8])+int(binn[lenn-9])])
  total+=int(matrix[10][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])+int(binn[lenn-7])+int(binn[lenn-8])+int(binn[lenn-9])+int(binn[lenn-10])])
  total+=int(matrix[11][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])+int(binn[lenn-7])+int(binn[lenn-8])+int(binn[lenn-9])+int(binn[lenn-10])+int(binn[lenn-11])])
  total+=int(matrix[12][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])+int(binn[lenn-7])+int(binn[lenn-8])+int(binn[lenn-9])+int(binn[lenn-10])+int(binn[lenn-11])+int(binn[lenn-12])])
  total+=int(matrix[13][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])+int(binn[lenn-7])+int(binn[lenn-8])+int(binn[lenn-9])+int(binn[lenn-10])+int(binn[lenn-11])+int(binn[lenn-12])+int(binn[lenn-13])])
  total+=int(matrix[14][int(binn[lenn-1])+int(binn[lenn-2])+int(binn[lenn-3])+int(binn[lenn-4])+int(binn[lenn-5])+int(binn[lenn-6])+int(binn[lenn-7])+int(binn[lenn-8])+int(binn[lenn-9])+int(binn[lenn-10])+int(binn[lenn-11])+int(binn[lenn-12])+int(binn[lenn-13])+int(binn[lenn-14])])
  if total>high:high=total  
print(high,time.time()-start," seconds")
