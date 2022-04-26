N,K=map(int,input().split())
S=[[0]*26 for _ in range(N)]
al='abcdefghijklmnopqrstuvwxyz'
for i in range(N):
  s=input()
  for j in s:
    S[i][al.index(j)]=1
ans=0
for i in range(2**N):
  A=[0]*26
  for j in range(N):
    if i>>j&1:
      A=[A[k]+S[j][k] for k in range(26)]
  ans=max(ans,A.count(K))
print(ans)