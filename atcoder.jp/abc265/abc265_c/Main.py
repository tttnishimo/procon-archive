H,W=map(int,input().split())
S=[list(input()) for _ in range(H)]
h,w=0,0
while True:
  t=S[h][w]
  S[h][w]=0
  if t=='U':
    h-=1
    if h<0:
      print(1,w+1)
      exit()
  elif t=='D':
    h+=1
    if h>H-1:
      print(H,w+1)
      exit()
  elif t=='R':
    w+=1
    if w>W-1:
      print(h+1,W)
      exit()
  else:
    w-=1
    if w<0:
      print(h+1,1)
      exit()
  if S[h][w]==0:
    print(-1)
    exit()