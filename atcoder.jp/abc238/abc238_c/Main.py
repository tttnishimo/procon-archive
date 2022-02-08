N=int(input())
l=len(str(N))-1
ans=0
for i in range(l):
  n=10**(i+1)-10**i
  ans+=n*(n+1)//2
m=N-10**l+1
ans+=m*(m+1)//2
ans%=998244353
print(ans)