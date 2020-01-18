import time
start=time.time()
tot=0
for d1 in range(10):
  for d2 in range(10):
    if d2!=d1:
      for d3 in range(10):
        if d3!=d1 and d3!=d2:
          for d4 in range(10):
            if d4!=d1 and d4!=d2 and d4!=d3:
              if d4%2==0:
                for d5 in range(10):
                  if d5!=d1 and d5!=d2 and d5!=d3 and d5!=d4:
                    if (d3+d4+d5)%3==0:
                      for d6 in range(10):
                        if d6!=d1 and d6!=d2 and d6!=d3 and d6!=d4 and d6!=d5:
                          if d6%5==0:
                            for d7 in range(10):
                              if d7!=d1 and d7!=d2 and d7!=d3 and d7!=d4 and d7!=d5 and d7!=d6:
                                if (d5*100+d6*10+d7)%7==0:
                                  for d8 in range(10):
                                    if d8!=d1 and d8!=d2 and d8!=d3 and d8!=d4 and d8!=d5 and d8!=d6 and d8!=d7:
                                      if (d6*100+d7*10+d8)%11==0:
                                        for d9 in range(10):
                                          if d9!=d1 and d9!=d2 and d9!=d3 and d9!=d4 and d9!=d5 and d9!=d6 and d9!=d7 and d9!=d8:
                                            if (d7*100+d8*10+d9)%13==0:
                                              for d10 in range(10):
                                                if d10!=d1 and d10!=d2 and d10!=d3 and d10!=d4 and d10!=d5 and d10!=d6 and d10!=d7 and d10!=d8 and d10!=d9:
                                                  if (d8*100+d9*10+d10)%17==0:
                                                    tot+=d1*1000000000+d2*100000000+d3*10000000+d4*1000000+d5*100000+d6*10000+d7*1000+d8*100+d9*10+d10
print(tot,time.time()-start," seconds")
