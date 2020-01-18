import time
import math
start=time.time()

for d1 in range(9,-1,-1):
  s2=9
  e2=0
  if d1==0:
    s2=8
    e2=-1
  for d2 in range(s2,e2,-1):
    if d1==0 or d2!=d1:
      print(d1,d2)
      s3=9
      e3=0
      if d1==0:s3=8
      if d2==0:
        s3=7
        e3=-1
      for d3 in range(s3,e3,-1):
        if (d1==0 and d2==0) or (d3!=d2 and d3!=d1):
          s4=9
          e4=0
          if d1==0:s4=8
          if d2==0:s4=7
          if d3==0:
            s4=6
            e4=-1
          for d4 in range(s4,e4,-1):
            if (d1==0 and d2==0 and d3==0) or (d4!=d3 and d4!=d2 and d4!=d1):
              s5=9
              e5=0
              if d1==0:s5=8
              if d2==0:s5=7
              if d3==0:s5=6
              if d4==0:
                s5=5
                e5=-1
              for d5 in range(s5,e5,-1):
                if (d1==0 and d2==0 and d3==0 and d4==0) or (d5!=d4 and d5!=d3 and d5!=d2 and d5!=d1):
                  s6=9
                  e6=0
                  if d1==0:s6=8
                  if d2==0:s6=7
                  if d3==0:s6=6
                  if d4==0:s6=5
                  if d5==0:
                    s6=4
                    e6=-1
                  for d6 in range(s6,e6,-1):
                    if (d1==0 and d2==0 and d3==0 and d4==0 and d5==0) or (d6!=d5 and d6!=d4 and d6!=d3 and d6!=d2 and d6!=d1):
                      s7=9
                      e7=0
                      if d1==0:s7=8
                      if d2==0:s7=7
                      if d3==0:s7=6
                      if d4==0:s7=5
                      if d5==0:s7=4
                      if d6==0:
                        s7=3
                        e7=-1
                      for d7 in range(s7,e7,-1):
                        if (d1==0 and d2==0 and d3==0 and d4==0 and d5==0 and d6==0) or (d7!=d6 and d7!=d5 and d7!=d4 and d7!=d3 and d7!=d2 and d7!=d1):
                          s8=9
                          e8=0
                          if d1==0:s8=8
                          if d2==0:s8=7
                          if d3==0:s8=6
                          if d4==0:s8=5
                          if d5==0:s8=4
                          if d6==0:s8=3
                          if d7==0:
                            s8=2
                            e8=-1
                          for d8 in range(s8,e8,-1):
                            if (d1==0 and d2==0 and d3==0 and d4==0 and d5==0 and d6==0 and d7==0) or (d8!=d7 and d8!=d6 and d8!=d5 and d8!=d4 and d8!=d3 and d8!=d2 and d8!=d1):
                              s9=9
                              e9=0
                              if d1==0:s9=8
                              if d2==0:s9=7
                              if d3==0:s9=6
                              if d4==0:s9=5
                              if d5==0:s9=4
                              if d6==0:s9=3
                              if d7==0:s9=2
                              if d8==0:
                                s9=1
                                e9=-1
                              for d9 in range(s9,e9,-1):
                                if (d1==0 and d2==0 and d3==0 and d4==0 and d5==0 and d6==0 and d7==0 and d8==0) or (d9!=d8 and d9!=d7 and d9!=d6 and d9!=d5 and d9!=d4 and d9!=d3 and d9!=d2 and d9!=d1):
                                  rng=int(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9))
                                  prime=1
                                  for m in range(2,int(math.sqrt(rng))):
                                    if rng==2143:print("m",m)
                                    if rng%m == 0:
                                      prime=0
                                      break
                                  if prime==1:
                                    break
                              if prime==1:break
                          if prime==1:break
                      if prime==1:break
                  if prime==1:break
              if prime==1:break
          if prime==1:break
      if prime==1:break
  if prime==1:break
print(rng,time.time()-start," seconds")
