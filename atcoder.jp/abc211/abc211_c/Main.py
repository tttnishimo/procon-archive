s=input()
c='chokudai'
dp=[[1,0,0,0,0,0,0,0,0] for _ in range(len(s)+1)]
for i in range(len(s)):
  for j in range(8):
    if s[i]==c[j]:
      dp[i+1][j+1]=dp[i][j]+dp[i][j+1]
    else:
      dp[i+1][j+1]=dp[i][j+1]
print(dp[-1][-1]%1000000007)