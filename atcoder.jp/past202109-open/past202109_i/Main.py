import heapq
N=int(input())
A=list(map(int,input().split()))
M=0
for i in range(N):
  while A[i]%2==0:
    A[i]=A[i]//2
    M+=1
A.sort()
for _ in range(M):
  heapq.heappush(A,heapq.heappop(A)*3)
print(A[0])