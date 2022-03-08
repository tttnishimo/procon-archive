N=int(input())
a,b,c,d,e=1,1,1,1,1
k=998244353
for _ in range(1,N):
  v,w,x,y,z=a,b,c,d,e
  v=(a+b)%k
  w=(a+b+c)%k
  x=(b+c+d)%k
  y=(c+d+e)%k
  z=(d*2+e)%k
  a,b,c,d,e=v,w,x,y,z
print(((a+b+c+d)*2+e)%k)