n,k = map(int, input().split())
if n == 0 or k == 1:
  print(0)
elif n < (k + 1)//2:
  print(n)
elif n < k:
  print(k - n)
elif n == k or n % k == 0:
  print(0)
else:
  print((k * (n//k + 1)) % n)