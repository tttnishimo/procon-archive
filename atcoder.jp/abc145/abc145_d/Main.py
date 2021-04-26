def cmb(n,r,mod):
  if (r<0 or r>n):
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod

mod=10**9+7
N=10**6
g1=[1,1]
g2=[1,1]
inverse=[0,1]
for i in range(2,N+1):
  g1.append((g1[-1]*i)%mod)
  inverse.append((-inverse[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inverse[-1])%mod)

x,y=map(int,input().split())
if x>y:
  x,y=y,x
a=y-x
b=(x-a)//3
ans=cmb(a+b*2,b,mod)
if (x+y)%3!=0:
  ans=0
print(ans)