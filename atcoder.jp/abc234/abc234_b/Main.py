N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
ans=0
for i in range(N-1):
  for j in range(i+1,N):
    ans=max(ans,((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2)**.5)
print(ans)