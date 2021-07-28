N=int(input())
S=input()
ans=0
for i in range(N+1):
  flg=0
  for j in range(N):
    if (j<=i and S[j]=='K') or (j>i and S[j]=='D'):
      flg=1
  if flg==0:
    ans+=1
print(ans)