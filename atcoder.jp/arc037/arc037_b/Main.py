from collections import deque
n,m=map(int,input().split())
g=[[] for _ in range(n)]
for _ in range(m):
  a,b=map(int,input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)
v=[0 for _ in range(n)]
ans=0
def dfs(i,j):
  v[i]=1
  for x in g[i]:
    if x==j:
      continue
    if v[x]==1:
      v.append(1)
      continue
    dfs(x,i)
for i in range(n):
  if v[i]==0:
    dfs(i,-1)
    if len(v)==n:
      ans+=1
    else:
      n=len(v)
print(ans)