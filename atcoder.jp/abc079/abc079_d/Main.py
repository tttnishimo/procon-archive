h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(10)]
b=[list(map(int,input().split())) for _ in range(h)]
c=[a[i][1] for i in range(10)]
ans=0
for _ in range(10):
  for i in range(10):
    for j in range(10):
      if c[i]>c[j]+a[i][j]:
        c[i]=c[j]+a[i][j]
for i in b:
  for j in i:
    if j!=-1:
      ans+=c[j]
print(ans)