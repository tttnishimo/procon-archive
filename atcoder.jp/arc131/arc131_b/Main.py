H,W=map(int,input().split())
S=[['6']*(W+2)]
for _ in range(H):
  S.append(['6']+list(input())+['6'])
S.append(['6']*(W+2))
for i in range(1,H+1):
  for j in range(1,W+1):
    a=['1','2','3','4','5','6']
    d=[[-1,0],[0,-1],[1,0],[0,1]]
    if S[i][j]=='.':
      for dx,dy in d:
        if S[i+dx][j+dy] in a:
          a.remove(S[i+dx][j+dy])
      S[i][j]=a[0]
for i in range(1,H+1):
  print(*S[i][1:-1],sep='')