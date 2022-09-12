import math
N=int(input())
A=list(map(int, input().split()))
f=0
for i in range(N-1):
  f=math.gcd(f,abs(A[i]-A[i+1]))
if f==1:
  print(2)
else:
  print(1)