import math
N=int(input())
for i in range(2,2*10**6):
  N//=math.gcd(N,i)
  if N==1:
    print(i)
    exit()
print(N)