N,M,K=map(int,input().split())
mod=998244353
dp=[1]*(K+1)
for _ in range(N):
  for i in range(K-M+1)[::-1]:
    dp[i+M]-=dp[i]
    dp[i+M]%=mod
  for i in range(K):
    dp[i+1]+=dp[i]
    dp[i+1]%=mod
print(dp[K-N])