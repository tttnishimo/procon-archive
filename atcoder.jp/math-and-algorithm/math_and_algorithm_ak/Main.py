N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=[int(input()) for _ in range(M)]
ans=[0]*(N+1)
for i in range(1,M):
  a,b=B[i-1],B[i]
  if B[i-1]>B[i]:
    a,b=b,a
  ans[a]+=1
  ans[b]-=1
for i in range(1,N+1):
  ans[i]+=ans[i-1]
ans.pop(0)
ans.pop(-1)
print(sum(A[i]*ans[i] for i in range(N-1)))