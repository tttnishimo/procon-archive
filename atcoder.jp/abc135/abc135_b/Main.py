n = int(input())
a = list(map(int, input().split()))
flg = 0
for i in range(n):
  if a[i] == i + 1:
    pass
  else:
    flg += 1
if flg == 0 or flg == 2:
  print('YES')
else:
  print('NO')