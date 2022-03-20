import math
L,R=map(int,input().split())
ans=0
for i in range(min(100,R-L)):
  for j in range(min(100,R-L)):
    if R-i>L+j and math.gcd(R-i,L+j)==1:
      ans=max(ans,R-i-L-j)
print(ans)