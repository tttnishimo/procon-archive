import math
N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
ans=10**10
for i in range(N-1):
  for j in range(i+1,N):
    d=math.dist(A[i],A[j])
    ans=min(ans,d)
print(ans)