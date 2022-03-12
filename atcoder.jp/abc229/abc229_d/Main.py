S=input()
K=int(input())
N=len(S)
cnt=[0]*(N+1)
for i in range(N):
  cnt[i+1]=cnt[i]
  if S[i]=='.':
    cnt[i+1]+=1
ans=0
r=0
for i in range(N):
  while r<N and cnt[r+1]<=cnt[i]+K:
    r+=1
  ans=max(ans,r-i)
print(ans)