N,M=map(int,input().split())
S=[input() for _ in range(N)]
ans=0
for i in range(N-1):
  for j in range(i+1,N):
    f=1
    for k in range(M):
      if S[i][k]=='x' and S[j][k]=='x':
        f=0
    ans+=f
print(ans)