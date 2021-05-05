import itertools
N=int(input())
a=[0]
b=[0]
for _ in range(N):
  c,p=map(int,input().split())
  if c==1:
    a.append(p)
    b.append(0)
  else:
    a.append(0)
    b.append(p)
a=list(itertools.accumulate(a))
b=list(itertools.accumulate(b))
for _ in range(int(input())):
  l,r=map(int,input().split())
  print(a[r]-a[l-1],b[r]-b[l-1])