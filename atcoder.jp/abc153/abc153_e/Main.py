h,n=map(int,input().split())
ab_input=[list(map(int,input().split())) for _ in range(n)]
max_a=max(a for a,b in ab_input)
dp=[0]*(h+max_a)
for i in range(1,h+max_a):
  dp[i]=min(dp[i-a]+b for a,b in ab_input)
print(dp[h])