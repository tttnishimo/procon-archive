N,D=map(int,input().split())
S=[input() for _ in range(D)]
ans=0
for i in range(D-1):
  a=[0]*N
  for ii in range(N):
    if S[i][ii]=='o':
      a[ii]=1
  for j in range(i+1,D):
    b=list(a)
    for jj in range(N):
      if S[j][jj]=='o':
        b[jj]=1
    ans=max(ans,sum(b))
print(ans)