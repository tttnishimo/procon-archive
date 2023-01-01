H,W,L=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(L)]
ans=[[0]*(W+1) for _ in range(H+1)]
for a in A:
  ans[a[0]-1][a[1]-1]+=1
  ans[a[0]-1][a[3]]-=1
  ans[a[2]][a[1]-1]-=1
  ans[a[2]][a[3]]+=1
for h in range(H):
  for w in range(1,W):
    ans[h][w]+=ans[h][w-1]
for w in range(W):
  for h in range(1,H):
    ans[h][w]+=ans[h-1][w]
for h in range(H):
  print(*ans[h][:-1])