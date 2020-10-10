h,w=map(int,input().split())
a=[input() for _ in range(h)]
ans=0
for i in range(h):
  for j in range(w-1):
    if a[i][j]=='.' and a[i][j+1]=='.':
      ans+=1
for i in range(h-1):
  for j in range(w):
    if a[i][j]=='.' and a[i+1][j]=='.':
      ans+=1
print(ans)