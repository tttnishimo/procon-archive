n=int(input())
a=list(map(int,input().split()))
ans=10**10
for i in range(2**n-1):
  tmp=a[0]
  tmp2=0
  for j in range(1,n):
    if (i>>j&1)==(i>>(j-1)&1):
      tmp|=a[j]
    else:
      tmp2^=tmp
      tmp=a[j]
  tmp2^=tmp
  ans=min(ans,tmp2)
print(ans)