H,W=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(H)]
r=[sum(i) for i in a]
c=[sum([a[i][j] for i in range(H)]) for j in range(W)]
b=[[r[i]+c[j]-a[i][j] for j in range(W)] for i in range(H)]
for i in range(H):
  print(*b[i])