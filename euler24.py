import time
from itertools import permutations 
start=time.time()
l = list(permutations(range(10))) 
print(l[999999],time.time()-start," seconds")
