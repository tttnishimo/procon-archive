N=int(input())
a=[list(map(int, input().split())) for _ in range(N)]
b=[False]*N
b[-1]=True
ans=0
for i in range(N-1,-1,-1):
  if b[i]:
    ans+=a[i][0]
    for j in range(a[i][1]):
      b[a[i][j+2]-1]=True
print(ans)