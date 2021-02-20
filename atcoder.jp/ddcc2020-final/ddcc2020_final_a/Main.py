n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  j=2
  tmp=0
  while a[i]!=1:
    while a[i]%j==0:
      a[i]//=j
      tmp+=1
    j+=1
  if i==0:
    b=tmp
  else:
    b^=tmp
if b:
  print('Yes')
else:
  print('No')