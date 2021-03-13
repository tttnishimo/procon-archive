n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
ans=1000000000
for i in range(n):
  if a[i][0]<a[i][2]:
    ans=min(ans,a[i][1])
if ans==1000000000:
  print(-1)
else:
  print(ans)