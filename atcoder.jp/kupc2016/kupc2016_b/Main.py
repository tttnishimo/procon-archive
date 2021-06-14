N,K=map(int,input().split())
P=[input() for _ in range(N)]
a=[0]*26
ans=0
al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in P:
  a[al.index(s[0])]+=1
for i in range(N//K+1):
  a.sort(reverse=True)
  for j in range(K):
    a[j]-=1
  if a[j]<0:
    break
  ans+=1
print(ans)