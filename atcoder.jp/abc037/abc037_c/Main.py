n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n):
  if k>n//2:
    ans+=a[i]*min(n-i,i+1,n-k+1)
  else:
    ans+=a[i]*min(n-i,i+1,k)
print(ans)