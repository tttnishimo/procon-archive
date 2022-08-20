mod=10**9+7
N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=0
for i in range(N):
  ans+=A[i]*pow(2,i,mod)
  ans%=mod
print(ans)