import numpy as np
N,W=map(int,input().split())
knap=[]
for i in range(N):
  knap.append(tuple(map(int,input().split())))
total_value=sum([v for w,v in knap])
INF=float("inf")
dp=np.full(total_value+1,INF)
dp[0]=0
for i,(w,v) in enumerate(knap):
  dp[v:]=np.minimum(dp[v:],dp[:-v]+w)  
print(max([i for i in range(total_value+1) if dp[i]<=W]))