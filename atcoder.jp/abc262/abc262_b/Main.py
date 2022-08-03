N,M=map(int,input().split())
A=[[False]*N for _ in range(N)]
for _ in range(M):
  u,v=map(int,input().split())
  A[u-1][v-1]=True
  A[v-1][u-1]=True
ans=0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if A[i][j] and A[i][k] and A[j][k]:
        ans+=1
print(ans)