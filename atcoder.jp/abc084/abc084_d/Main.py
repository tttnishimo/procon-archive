import itertools
def eratosthenes_sieve(n):
  is_prime=[True]*(n+1)
  is_prime[0]=is_prime[1]=False
  for p in range(2,n+1):
    if is_prime[p]:
      for q in range(2*p,n+1,p):
        is_prime[q]=False
  return is_prime

is_prime=eratosthenes_sieve(10**5)
a=[0]*10**5
a[3]=1
for i in range(5,10**5,4):
  if is_prime[i] and is_prime[(i+1)//2]:
    a[i]=1
a=list(itertools.accumulate(a))
for _ in range(int(input())):
  l,r=map(int,input().split())
  print(a[r]-a[l-1])