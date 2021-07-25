N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
for i in range(N):
  ans+=abs(A[i]-B[i])
if ans<=K and ans%2==K%2:
  print('Yes')
else:
  print('No')