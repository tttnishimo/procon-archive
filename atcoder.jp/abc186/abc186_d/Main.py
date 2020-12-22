import itertools
n=int(input())
a=list(map(int,input().split()))
a.sort()
c=list(itertools.accumulate(a))
ans=0
for i in range(-1,-n,-1):
  ans+=a[i]*(i+n)-c[i-1]
print(ans)