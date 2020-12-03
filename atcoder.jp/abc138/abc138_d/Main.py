n,q=map(int,input().split())
a=[[] for _ in range(n)]
for _ in range(n-1):
  b,c=map(int,input().split())
  a[b-1].append(c-1)
  a[c-1].append(b-1)
ans=[0]*n
for _ in range(q):
  b,c=map(int,input().split())
  ans[b-1]+=c
u=[0]*n
q=[0]
while q:
  v=q.pop()
  u[v]=1
  for c in a[v]:
    if u[c]: continue
    ans[c]+=ans[v]
    q.append(c)
print(*ans)