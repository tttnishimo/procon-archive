n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
ans=n
for i in range(n):
  for j in range(i+1,n):
    t=n
    dx=a[j][0]-a[i][0]
    dy=a[j][1]-a[i][1]
    for k in range(n):
      for l in range(n):
        if a[l][0]-a[k][0]==dx and a[l][1]-a[k][1]==dy:
          t-=1
    ans=min(ans,t)
print(ans)