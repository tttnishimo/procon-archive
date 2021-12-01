N,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
A.sort(reverse=True)
ans=0
for a,b in A:
  w=min(W,b)
  ans+=a*w
  W-=w
print(ans)