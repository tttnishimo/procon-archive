import math
input()
A=list(map(int,input().split()))
ans=math.gcd(A[0],A[1])
for a in A:
  ans=math.gcd(ans,a)
print(ans)