import sys
sys.setrecursionlimit(10000)

N,M=map(int,input().split())
c=[[] for i in range(N)]
for i in range(M):
  a,b=map(int,input().split())
  c[a-1].append(b-1)
ans=0

def dfs(x):
  if seen[x]:
    return
  seen[x]=True
  for xx in c[x]:
    dfs(xx)

for i in range(N):
  seen=[False]*N
  dfs(i)
  ans+=sum(seen)
print(ans)