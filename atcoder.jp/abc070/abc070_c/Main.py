import math
n=int(input())
ans=1
for i in range(n):
  a=int(input())
  ans=a*ans//math.gcd(a,ans)
print(ans)