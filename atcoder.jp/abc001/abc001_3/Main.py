from decimal import Decimal,ROUND_HALF_UP
a,b=map(int,input().split())
deg=['NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','N']
deg=deg[int((a-112.5)//225)]
b=float(Decimal(b/6).quantize(Decimal('0'),rounding=ROUND_HALF_UP))/10
if b<=0.2:
  print('C',0)
elif b<=1.5:
  print(deg,1)
elif b<=3.3:
  print(deg,2)
elif b<=5.4:
  print(deg,3)
elif b<=7.9:
  print(deg,4)
elif b<=10.7:
  print(deg,5)
elif b<=13.8:
  print(deg,6)
elif b<=17.1:
  print(deg,7)
elif b<=20.7:
  print(deg,8)
elif b<=24.4:
  print(deg,9)
elif b<=28.4:
  print(deg,10)
elif b<=32.6:
  print(deg,11)
else:
  print(deg,12)