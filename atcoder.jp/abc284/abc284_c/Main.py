def dfs(n):
  vi[n]=True
  for m in A[n]:
    if vi[m]:
      continue
    dfs(m)
N,M=map(int,input().split())
A=[[] for _ in range(N+1)]
vi=[False]*(N+1)
ans=0
for _ in range(M):
  u,v=map(int,input().split())
  A[u].append(v)
  A[v].append(u)
for i in range(1,N+1):
  if vi[i]==False:
    ans+=1
    dfs(i)
print(ans)