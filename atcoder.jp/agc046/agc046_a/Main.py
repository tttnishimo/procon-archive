import math
n=int(input())
if 1 < math.gcd(360,n) < 360:
  print(360//math.gcd(360,n))
else:
  print(360)