import time
start=time.time()
start_day=2
months=0
for year in range(1901,2001):
  if (year//4==year/4 and year//100!=year/100) or year//400==year/400:
    if start_day==0:
      months+=3
    elif start_day in (1,3,4):
      months+=2
    else:
      months+=1
    start_day=(start_day+2)%7
  else:
    if start_day==4:
      months+=3
    elif start_day in (0,1,2):
      months+=2
    else:
      months+=1
    start_day=(start_day+1)%7
print(months,time.time()-start," seconds")


#non-leap 1st Jan:
#sun:2
#mon:2
#tue:2
#wed:1
#thu:3
#fri:1
#sat:1
#
#leap:
#sun:3
#mon:2
#tue:1
#wed:2
#thu:2
#fri:1
#sat:1
