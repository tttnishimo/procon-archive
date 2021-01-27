n,k=map(int,input().split())
ans=0
for i in range(k,n+2):
  ans+=(n+1)*n//2-(n-i+1)*(n-i)//2-i*(i-1)//2+1
  ans%=1000000007
print(ans)