import bisect
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(n-2):
  for j in range(i+1,n-1):
    ans+=bisect.bisect_left(a,a[i]+a[j])-j-1
print(ans)