N,M=map(int,input().split())
A=list(map(int,input().split()))
a=[sum(A[:M])]
for i in range(M,N):
  a.append(a[-1]+A[i]-A[i-M])
t=sum(A[i]*(i+1) for i in range(M))
ans=t
for i in range(N-M):
  t+=M*A[i+M]-a[i]
  ans=max(ans,t)
print(ans)