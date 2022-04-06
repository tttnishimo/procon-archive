N,K,X=map(int,input().split())
A=list(map(int,input().split()))
for i in range(N):
  x=A[i]//X
  if x<=K:
    K-=x
    A[i]-=x*X
  else:
    while A[i]>=X and K>0:
      A[i]-=X
      K-=1
A.sort(reverse=True)
print(sum(A)-sum(A[:min(K,N)]))