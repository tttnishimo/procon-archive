x1,y1,r=map(int,input().split())
x2,y2,x3,y3=map(int,input().split())
if x1+r>max(x2,x3) or y1+r>max(y2,y3) or x1-r<min(x2,x3) or y1-r<min(y2,y3):
  print('YES')
else:
  print('NO')
if x2==x3 and y2==y3:
  print('NO')
elif (x1-max(x2,x3))**2+(y1-max(y2,y3))**2>r**2 or (x1-max(x2,x3))**2+(y1-min(y2,y3))**2>r**2 or (x1-min(x2,x3))**2+(y1-max(y2,y3))**2>r**2 or (x1-min(x2,x3))**2+(y1-min(y2,y3))**2>r**2:
  print('YES')
else:
  print('NO')