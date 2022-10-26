H,W=map(int,input().split())
S=[input() for _ in range(H)]
ans=[]
for w in range(W):
  t=0
  for h in range(H):
    if S[h][w]=='#':
      t+=1
  ans.append(t)
print(*ans)