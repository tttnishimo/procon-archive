N,W=map(int,input().split())
dp=[[0]*(W+1) for _ in range(N+1)]
A=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
  for j in range(W+1):
    if A[i][0]<=j:
      dp[i+1][j]=max(dp[i][j],max(0,dp[i][j-A[i][0]])+A[i][1])
    else:
      dp[i+1][j]=dp[i][j]
print(dp[-1][-1])