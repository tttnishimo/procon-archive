import collections
N,M=map(int, input().split())
A=list(map(int, input().split()))
c=collections.Counter(A)
p=list(c.values())
p.sort()
if len(c)<M:
  print(0,p[-1])
else:
  print(p[0],p[-1])