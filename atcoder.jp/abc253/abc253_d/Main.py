import math
N,A,B=map(int,input().split())
C=A*B//math.gcd(A,B)
ans=N*(N+1)//2
a=N//A
b=N//B
c=N//C
ans+=c*(c+1)//2*C-a*(a+1)//2*A-b*(b+1)//2*B
print(ans)