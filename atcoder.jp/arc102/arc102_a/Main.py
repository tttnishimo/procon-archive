n,k=map(int,input().split())
if k%2==0:
  print((n//(k//2)-n//k)**3+(n//k)**3)
else:
  print((n//k)**3)