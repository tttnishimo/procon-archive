n = int(input())
res = n // 10
i = 5
if n % 2 == 1:
  print(0)
else:
  n = n // 10
  while n // i != 0:
    res += n // i
    i *= 5
  print(res)