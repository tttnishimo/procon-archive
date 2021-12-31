import itertools
N,K=map(int,input().split())
A=list(map(int,input().split()))
A=list(itertools.accumulate(A,initial=0))
ans=0
d={}
for i in A:
  if i-K in d:
    ans+=d[i-K]
  if i in d:
    d[i]+=1
  else:
    d[i]=1
print(ans)