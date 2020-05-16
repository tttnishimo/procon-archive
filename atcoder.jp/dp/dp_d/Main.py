n,m=map(int,input().split())
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
  w,v=map(int,input().split())
  for j in range(m+1):
    if j < w:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j-w]+v,dp[i-1][j])
print(dp[n][m])