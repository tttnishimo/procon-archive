N,T=map(int,input().split())
A=list(map(int,input().split()))
a=0
t=0
ans=0
for i in range(N-1):
  a+=A[i]
  t=-(-a//T)
  ans+=t
  a-=t*T
print(ans)