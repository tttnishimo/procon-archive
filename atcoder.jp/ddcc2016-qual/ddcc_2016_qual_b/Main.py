r,n,m=map(int,input().split())
ans=0
for i in range(1,n+m):
  ans+=(r**2-(2*r/n*min(abs(i-n/2),abs(i-m-n/2)))**2)**0.5
print(2*ans)