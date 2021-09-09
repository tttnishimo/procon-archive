import bisect
N,M=map(int,input().split())
l=[[] for _ in range(N)]
for _ in range(M):
  a,b=map(int,input().split())
  l[a-1].append(b-1)
  l[b-1].append(a-1)
ans=0
for i in range(N):
  l[i].sort()
  if bisect.bisect(l[i],i)==1:
    ans+=1
print(ans)