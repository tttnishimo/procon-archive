n=int(input())
ans=0
k=999
while n>k:
  ans+=n-k
  k=k*1000+999
print(ans)