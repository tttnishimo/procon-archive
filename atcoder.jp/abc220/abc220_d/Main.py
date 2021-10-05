N=int(input())
A=list(map(int,input().split()))
ans=[0]*10
ans[A[0]]=1
for i in range(1,N):
  t=[0]*10
  for j in range(10):
    t[(A[i]+j)%10]+=ans[j]
    t[(A[i]*j)%10]+=ans[j]
  for j in range(10):
    t[j]%=998244353
  ans=t
print(*ans,sep='\n')