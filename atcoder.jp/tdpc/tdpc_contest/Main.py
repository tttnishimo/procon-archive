n=int(input())
a=list(map(int,input().split()))
dp=[[0]*100001 for _ in range(n+1)]
for j in range(1,n+1):
  for i in range(1,100001):
    if i == a[j-1]:
      dp[j][i] = 1
    elif dp[j-1][i] == 1:
      dp[j][i] = 1
    elif dp[j-1][i-a[j-1]] == 1:
      dp[j][i] = 1
print(sum(dp[n])+1)