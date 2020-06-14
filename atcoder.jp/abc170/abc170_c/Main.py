x,n=map(int,input().split())
if n==0:
  print(x)
else:
  a=list(map(int,input().split()))
  tmp=1000
  for i in reversed(range(-1,102)):
    if i not in a:
      if tmp >= abs(i-x):
        tmp=abs(i-x)
        ans=i
  print(ans)