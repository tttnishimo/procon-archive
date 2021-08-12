N,K=map(int,input().split())
A=[[] for _ in range(N)]
B=[[] for _ in range(N)]
for i in range(K):
  c,k=map(str,input().split())
  k=int(k)
  A[k-1].append(i)
  if c=='L':
    for j in range(k,N):
      B[j].append(i)
  else:
    for j in range(k-1):
      B[j].append(i)
ans=1
for i in range(N):
  if len(A[i])>1:
    ans*=0
  elif len(A[i])==0:
    ans*=len(B[i])
    ans%=998244353
print(ans)