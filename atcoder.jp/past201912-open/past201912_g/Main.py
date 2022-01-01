N=int(input())
A=[list(map(int,input().split())) for _ in range(N-1)]
ans=-10**9
def base3(v):
  if v//3:
    return base3(v//3)+str(v%3)
  return str(v%3)
for i in range(3**N):
  t=0
  S=base3(i)
  S='0'*(N-len(S))+S
  for j in range(N-1):
    for k in range(j+1,N):
      if S[j]==S[k]:
        t+=A[j][k-j-1]
  ans=max(ans,t)
print(ans)