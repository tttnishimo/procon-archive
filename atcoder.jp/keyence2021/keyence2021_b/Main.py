from collections import Counter
n,k=map(int,input().split())
a=Counter(list(map(int,input().split())))
ans=0
t=k
for i in range(n):
  t=min(t,a[i])
  ans+=t
print(ans)