import sys
sys.setrecursionlimit(1000000)
H,W=map(int,input().split())
c=[list(input()) for i in range(H)]
def dfs(h,w):
  if not(0<=h<H) or not(0<=w<W) or c[h][w]=="#":return
  if c[h][w]=="g":
    print("Yes")
    sys.exit()
  c[h][w]="#"
  dfs(h-1,w)
  dfs(h+1,w)
  dfs(h,w-1)
  dfs(h,w+1)

for i in range(H):
  for j in range(W):
    if c[i][j]=="s":
      sh,sw=i,j
      break
dfs(sh,sw)
print("No")