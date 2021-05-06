import itertools
N,Q=map(int,input().split())
a=[0]*(N+1)
for i in range(Q):
  l,r=map(int,input().split())
  a[l-1]+=1
  a[r]-=1
a=list(itertools.accumulate(a))
print(*[i%2 for i in a[:-1]],sep='')