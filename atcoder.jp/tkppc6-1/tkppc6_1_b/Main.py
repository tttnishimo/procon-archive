import collections
N,M=map(int,input().split())
A=list(map(int,input().split()))
c=len(collections.Counter(A))
if c+M<=N:
  print(c+M)
else:
  print(N)