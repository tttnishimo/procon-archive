N,K=map(int,input().split())
A=list(map(int,input().split()))
l,r=0,10**9
while r>l+1:
  ans=0
  m=l+(r-l)//2
  for a in A:
    ans+=m//a
  if ans>=K:
    r=m
  else:
    l=m
print(r)