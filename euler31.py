import time
start=time.time()
counter=0
for c200 in range(0,2):
  for c100 in range(0,3):
    if c200*200+c100*100<=200:
      for c50 in range(0,5):
        if c200*200+c100*100+c50*50<=200:
          for c20 in range(0,11):
            if c200*200+c100*100+c50*50+c20*20<=200:
              for c10 in range(0,21):
                if c200*200+c100*100+c50*50+c20*20+c10*10<=200:
                  for c5 in range(0,41):
                    if c200*200+c100*100+c50*50+c20*20+c10*10+c5*5<=200:
                      for c2 in range(0,101):
                       if c200*200+c100*100+c50*50+c20*20+c10*10+c5*5+c2*2<=200:
                         counter+=1
print(counter,time.time()-start," seconds")
