import itertools
n=int(input())
a=list(map(int,input().split()))
b=list(itertools.accumulate(a))
b.insert(0,0)
ans=0
for i in range(n):
  ans+=(n-1)*a[i]*a[i]-2*a[i]*b[i]
print(ans)