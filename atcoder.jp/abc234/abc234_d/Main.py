import heapq
N,K=map(int,input().split())
A=list(map(int,input().split()))
q=A[:K]
print(min(q))
heapq.heapify(q)
for i in range(K,N):
  b=heapq.heappop(q)
  b=max(b,A[i])
  heapq.heappush(q,b)
  ans=heapq.heappop(q)
  print(ans)
  heapq.heappush(q,ans)