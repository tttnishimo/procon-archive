from collections import *
h,w=map(int,input().split())
s=[['#']*(w+2)]+[['#']+list(input())+['#'] for _ in range(h)]+[['#']*(w+2)]
s[1][1]=1
q=deque([[1,1]])
d=[[1,0],[-1,0],[0,1],[0,-1]]
while q:
  y,x=q.popleft()
  for dy,dx in d:
    if s[y+dy][x+dx]=='.':
      s[y+dy][x+dx]=s[y][x]+1
      q.append([y+dy,x+dx])
if s[h][w]=='.':
  print(-1)
else:
  print((h+2)*(w+2)-sum([t.count('#') for t in s])-s[h][w])