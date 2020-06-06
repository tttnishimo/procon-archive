a,r,n=map(int,input().split())
if r==1:
  print(a)
else:
  for i in range(n-1):
    a*=r
    if a>10**9:
      break
  if a<=10**9:
    print(a)
  else:
    print('large')