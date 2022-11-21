N,K=map(int,input().split())
A=list(map(int,input().split()))
if K>=N:
  A=[0]*N
else:
  A=A[K:]+[0]*K
print(*A)