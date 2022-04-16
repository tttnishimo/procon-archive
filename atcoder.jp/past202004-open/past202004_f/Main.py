import heapq
N=int(input())
A=[list(map(int, input().split())) for _ in range(N)]
L=[[] for _ in range(N)]
q=[]
ans=0
for a,b in A:
  L[a-1].append(b)
for i in L:
  for j in i:
    heapq.heappush(q,-j)
  ans-=heapq.heappop(q)
  print(ans)