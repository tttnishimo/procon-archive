n,k=map(int,input().split())
if k>int(str(k)[::-1]) or n<k:
  print(0)
else:
  ans=0
  i=0
  while k*10**i<=n:
    ans+=1
    i+=1
  i=0
  while int(str(k)[::-1])*10**i<=n:
    ans+=1
    i+=1
  if k==int(str(k)[::-1]):
    ans//=2
  print(ans)