N,M,T=map(int,input().split())
A=list(map(int,input().split()))
ans=A[0]-M
for i in range(1,N):
  ans+=max(0,A[i]-A[i-1]-2*M)
ans+=max(0,T-A[-1]-M)
print(ans)