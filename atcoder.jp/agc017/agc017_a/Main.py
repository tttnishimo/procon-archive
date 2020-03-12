import math

def comb(n, r):
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,p = map(int, input().split())
a = list(map(int, input().split()))
res = 0

for i in range(n):
  a[i] = a[i]%2

for i in range((a.count(1)+1)//2):
  res = res + comb(a.count(1), 2*i+1)
if res == 0 and p == 0:
  res = 1
res = res * 2**a.count(0)
print(res)