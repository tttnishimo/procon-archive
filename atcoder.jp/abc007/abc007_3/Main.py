from collections import deque
r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
s=[input() for _ in range(r)]

m=[[1,0],[-1,0],[0,1],[0,-1]]
a=[[-1 for _ in range(c)] for _ in range(r)]
a[sy-1][sx-1]=0
q=deque([[sy-1,sx-1]])
while len(q)>0:
  y,x=q.popleft()
  for i,j in m:
    if s[y+i][x+j]=='.' and a[y+i][x+j]==-1:
      q.append([y+i,x+j])
      a[y+i][x+j]=a[y][x]+1
print(a[gy-1][gx-1])