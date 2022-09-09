def eq(x):
  return a*(x**5)+b*x+c
a,b,c=map(int,input().split())
l=1.0
r=2.0
while r-l>0.0000000001:
  mid=(r+l)/2
  if eq(mid)>=0:
    r=mid
  else:
    l=mid
print(r)