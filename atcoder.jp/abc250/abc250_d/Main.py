import numpy as np
import bisect

def sieve(n):
  p = np.ones((int(n**.34) + 1))
  p[0:2] = 0
  for i in range(2, int(n**.34 + 1)):
    if p[i]:
      p[i*i::i] = 0
  primes = np.where(p==1)[0]
  return list(primes)

N = int(input())
ans = 0
primes = sieve(N)
n = len(primes)
for i in range(n-1):
  m = bisect.bisect(primes, int((N/primes[i])**.33333))
  s = 0
  for j in range(max(i+1, 0, m-100), min(n, m+100)):
    if primes[i]*primes[j]**3 <= N:
      s = j - i
  ans += s
print(ans)