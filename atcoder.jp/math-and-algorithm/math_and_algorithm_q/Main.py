import math
input()
A=list(map(int,input().split()))
ans=1
for a in A:
  t=math.gcd(ans,a)
  ans*=a//t
print(ans)