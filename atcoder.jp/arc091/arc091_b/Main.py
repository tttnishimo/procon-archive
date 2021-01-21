n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
  ans+=max(0,i-k)*(n//i)+max(0,n%i-max(1,k)+1)
print(ans)