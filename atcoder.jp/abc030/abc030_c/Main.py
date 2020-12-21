import bisect
n,m=map(int,input().split())
x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
t=0
ans=0
while t<=a[-1]:
  t=a[bisect.bisect_left(a,t)]+x
  if t<=b[-1]:
    t=b[bisect.bisect_left(b,t)]+y
    ans+=1
  else:
    break
print(ans)