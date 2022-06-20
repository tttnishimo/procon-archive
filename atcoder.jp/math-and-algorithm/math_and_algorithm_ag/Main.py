x1,y1,r1=map(int,input().split())
x2,y2,r2=map(int,input().split())
d=((x1-x2)**2+(y1-y2)**2)**.5
if r1+r2<d:
  print(5)
elif r1+r2==d:
  print(4)
elif abs(r1-r2)>d:
  print(1)
elif abs(r1-r2)==d:
  print(2)
else:
  print(3)