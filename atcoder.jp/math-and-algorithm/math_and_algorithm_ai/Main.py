import itertools
N,Q=map(int,input().split())
A=list(map(int,input().split()))
a=list(itertools.accumulate(A))
a.insert(0,0)
for _ in range(Q):
  l,r=map(int,input().split())
  print(a[r]-a[l-1])