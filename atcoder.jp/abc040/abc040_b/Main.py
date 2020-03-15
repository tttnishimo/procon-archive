n = int(input())
m = int(pow(n,0.5))
res = 1000000
if n >= 10000:
  for i in range(n//10000,m+1):
    j = 1
    while i * j <= n:
      tmp = i * j
      amari = n - tmp
      res = min(res,amari + abs(i - j))
      j += 1
  print(res)

else:
  for i in range(1,m+1):
    j = 1
    while i * j <= n:
      tmp = i * j
      amari = n - tmp
      res = min(res,amari + abs(i - j))
      j += 1
  print(res)