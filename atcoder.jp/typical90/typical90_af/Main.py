import itertools
N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
M=int(input())
B=set(input() for _ in range(M))
ans=10**9
for p in itertools.permutations(range(N)):
  t=0
  f=True
  for i in range(N-1):
    if (str(p[i]+1)+' '+str(p[i+1]+1)) in B or (str(p[i+1]+1)+' '+str(p[i]+1)) in B:
      f=False
  for i in range(N):
    t+=A[p[i]][i]
  if f:
    ans=min(ans,t)
if ans==10**9:
  print(-1)
else:
  print(ans)