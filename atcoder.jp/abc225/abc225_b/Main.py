N=int(input())
A=[0]*(N+1)
for _ in range(N-1):
  a,b=map(int,input().split())
  A[a]+=1
  A[b]+=1
if N-1 in A:
  print('Yes')
else:
  print('No')