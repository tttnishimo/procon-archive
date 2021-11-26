N,Q=map(int,input().split())
a=[['N']*N for _ in range(N)]
for _ in range(Q):
  b=list(map(int,input().split()))
  if b[0]==1:
    a[b[1]-1][b[2]-1]='Y'
  elif b[0]==2:
    for i in range(N):
      if a[i][b[1]-1]=='Y':
        a[b[1]-1][i]='Y'
  else:
    c=list(a[b[1]-1])
    for i in range(N):
      if c[i]=='Y':
        for j in range(N):
          if b[1]-1==j:
            continue
          if a[i][j]=='Y':
            a[b[1]-1][j]='Y'
for i in a:
  print(*i,sep='')