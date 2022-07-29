N=int(input())
S=[input()*3 for _ in range(N)]
S=S*3
ans=0
d=((1,1),(1,0),(0,1),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1))
for i in range(N,2*N):
  for j in range(N,2*N):
    for dx,dy in d:
      sx,sy=i,j
      s=S[sx][sy]
      for _ in range(N-1):
        sx+=dx
        sy+=dy
        s+=S[sx][sy]
      ans=max(ans,int(s))
print(ans)