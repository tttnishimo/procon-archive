import math
a,b,c=map(int,input().split())
if a+b-c>=0 and a-b-c<=0:
  if a+c<b:
    print((a+b+c)**2*math.pi-abs(a-b+c)**2*math.pi)
  else:
    print((a+b+c)**2*math.pi)
else:
  print((a+b+c)**2*math.pi-min(abs(a-b-c),abs(a-b+c),abs(a+b-c))**2*math.pi)