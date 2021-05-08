from collections import *
def main():
  H,W=map(int,input().split())
  q=deque()
  d=((1,0),(-1,0),(0,1),(0,-1))
  s=[[True]*(W+2)]
  for i in range(H):
    t=list(input())
    for j in range(W):
      if t[j]=='#':
        q.append((i+1,j+1,0))
        t[j]=True
      else:
        t[j]=False
    s+=[[True]+t+[True]]
  s+=[[True]*(W+2)]
  while q:
    y,x,ans=q.popleft()
    for dy,dx in d:
      if s[y+dy][x+dx]==False:
        s[y+dy][x+dx]=True
        q.append((y+dy,x+dx,ans+1))
  print(ans)
main()