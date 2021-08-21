N,L=map(int,input().split())
dp=[1 for i in range(N)]
for i in range(L-1,N):
  dp[i]=dp[i-1]+dp[i-L]
  dp[i]%=1000000007
print(dp[-1])