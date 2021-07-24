import math
A,B,C=map(int,input().split())
n=math.gcd(math.gcd(A,B),C)
ans=A//n+B//n+C//n-3
print(ans)