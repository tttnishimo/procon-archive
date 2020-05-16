n,k = map(int,input().split())
if k > n:
  k = n
a = list(map(int, input().split()))
dp = [0]*n
for i in range(1,n):
  if i <= k:
    dp[i] = abs(a[i]-a[0])
  else:
    dp[i] = min([abs(a[i]-a[i-j])+dp[i-j] for j in range(1,k+1)])
print(dp[-1])