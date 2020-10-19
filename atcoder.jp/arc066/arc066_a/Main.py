n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=1
if n%2==1:
  if a[0]==0:
    a.insert(0,0)
  else:
    ans=0
for i in range(len(a)):
  if (i//2*2+(n+1)%2)!=a[i]:
    ans=0
print(ans*2**(n//2)%1000000007)