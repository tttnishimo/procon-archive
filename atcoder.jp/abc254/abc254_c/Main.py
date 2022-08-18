N,K=map(int,input().split())
A=list(map(int,input().split()))
for i in range(K):
  A[i::K]=sorted(A[i::K])
if A==sorted(A):
  print('Yes')
else:
  print('No')