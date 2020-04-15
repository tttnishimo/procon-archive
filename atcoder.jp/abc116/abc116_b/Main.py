n = int(input())
a = [n]
i = 1
flg = 0
while flg == 0:
  if n % 2 == 0:
    n = n // 2
  else:
    n = 3 * n + 1
  if n in a:
    flg = 1
  else:
    a.append(n)
  i += 1
print(i)