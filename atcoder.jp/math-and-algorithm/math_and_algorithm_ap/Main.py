mod=10**9+7
def fib(n):
  a=1
  b=0
  for _ in range(n):
    a,b=(a+b)%mod,a
  return b
ans=fib(int(input()))
print(ans)