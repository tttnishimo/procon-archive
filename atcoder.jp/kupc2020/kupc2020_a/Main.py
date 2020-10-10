n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n-1):
  ans+=abs(a[i][0]-a[i+1][0])+abs(a[i][1]-a[i+1][1])
print(ans)