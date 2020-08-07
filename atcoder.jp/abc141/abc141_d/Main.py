import heapq
n,m=map(int,input().split())
a=list(map(lambda x:int(x)*(-1),input().split()))
heapq.heapify(a)
for _ in range(m):
  b=heapq.heappop(a)
  heapq.heappush(a,-(-b//2))
print(-sum(a))