import fractions
from functools import reduce
def gcd(*numbers):
  return reduce(fractions.gcd, numbers)

n,x=map(int,input().split())
a = list(map(int,input().split()))
a = [abs(a[i]-x) for i in range(n)]
ans = 0
print(gcd(*a))