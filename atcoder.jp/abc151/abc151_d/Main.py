from collections import deque
h,w=map(int,input().split())
m=[[1,0],[-1,0],[0,1],[0,-1]]
l=['#'*(w+2)]
for _ in range(h):
  l.append('#'+input()+'#')
l.append('#'*(w+2))

def bfs(a,b):
  s=[[-1 for _ in range(w+2)] for _ in range(h+2)]
  s[a][b]=0
  q=deque([[a,b]])
  while len(q)>0:
    x,y=q.popleft()
    for i,j in m:
      if l[x+i][y+j]=='.' and s[x+i][y+j]==-1:
        q.append([x+i,y+j])
        s[x+i][y+j]=s[x][y]+1
        dis=s[x+i][y+j]
  return dis

ans=[]
for i in range(h+2):
  for j in range(w+2):
    if l[i][j]=='.':
      ans.append(bfs(i,j))
print(max(ans))