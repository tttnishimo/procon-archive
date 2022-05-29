n,r=map(int,input().split())
a=1
for i in range(n,n-r,-1):
  a*=i
for i in range(1,r+1):
  a//=i
print(a)