from functools import lru_cache
MOD = 998244353
@lru_cache
def f(n):
  if n<=4:
    return n
  return f(n//2)*f(n-n//2)%998244353
X=int(input())
print(f(X))