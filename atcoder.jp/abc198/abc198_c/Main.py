r,x,y=map(int,input().split())
if x*x+y*y<r*r:
  print(2)
else:
  print(int(-(-((x*x+y*y)**0.5)//r)))