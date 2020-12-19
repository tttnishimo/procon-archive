import math
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=a[0]
for i in a:
  b=math.gcd(b,i)
  if k==i:
    print('POSSIBLE')
    exit()
if k%b==0 and k<=max(a):
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')