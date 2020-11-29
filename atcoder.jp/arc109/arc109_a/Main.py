a,b,x,y=map(int,input().split())
if a==b:
  print(x)
elif b>a:
  print(min(3*x,x+y)+(b-a-1)*min(2*x,y))
else:
  print(x+(a-b-1)*min(2*x,y))