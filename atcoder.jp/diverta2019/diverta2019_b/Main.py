r,g,b,n = map(int, input().split())
res = 0
for i in range(int(n/r) + 1):
  for j in range(int((n - i * r) / g) + 1):
    if (n - i * r - j * g) % b == 0 or n - i * r - j * g == 0:
      res = res + 1
print(res)