n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=10**20
for i in range(n-k+1):
  l,r=a[i],a[i+k-1]
  if l*r<0:
    ans=min(ans,min(abs(l),abs(r))*2+max(abs(l),abs(r)))
  else:
    ans=min(ans,max(abs(l),abs(r)))
print(ans)