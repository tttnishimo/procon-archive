l,x,y,s,d=map(int,input().split())
if s <= d:
  if x < y:
    print(min((d-s)/(x+y),(l-d+s)/(y-x)))
  else:
    print((d-s)/(x+y))
else:
  if x < y:
    print(min((l+d-s)/(x+y),(s-d)/(y-x)))
  else:
    print((l+d-s)/(x+y))